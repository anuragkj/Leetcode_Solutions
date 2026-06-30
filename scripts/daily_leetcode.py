#!/usr/bin/env python3
"""
Daily LeetCode Explainer
========================
Fetches the LeetCode "Question of Today" via the public (token-free) GraphQL API,
asks Gemini to write a deep, commute-readable study note (intuition, diagram,
dry run, complexity, edge cases, and a paste-ready Python solution), and writes
it as a Markdown file plus an index entry.

It does NOT submit anything to LeetCode. You read the note and paste the
solution yourself.

Env vars:
  GEMINI_API_KEY  (required)  - your free Google AI Studio key
  GEMINI_MODEL    (optional)  - override model; default tries a sensible list
  FORCE           (optional)  - "1" to regenerate even if today's file exists
"""

import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

LEETCODE_GRAPHQL = "https://leetcode.com/graphql"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
DEFAULT_MODELS = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-flash-latest"]

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DAILY_DIR = os.path.join(ROOT, "Daily")
INDEX_FILE = os.path.join(DAILY_DIR, "README.md")


# --------------------------------------------------------------------------- #
# HTTP helpers
# --------------------------------------------------------------------------- #
def _post_json(url, payload, headers=None, timeout=120):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "Mozilla/5.0 (DailyLeetCodeExplainer)")
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def set_output(**kv):
    """Expose values to later workflow steps via $GITHUB_OUTPUT (no-op locally)."""
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as f:
        for k, v in kv.items():
            f.write(f"{k}={v}\n")


def graphql(query, variables=None):
    payload = {"query": query, "variables": variables or {}}
    out = _post_json(LEETCODE_GRAPHQL, payload, headers={"Referer": "https://leetcode.com"})
    if "errors" in out:
        raise RuntimeError(f"LeetCode GraphQL error: {out['errors']}")
    return out["data"]


# --------------------------------------------------------------------------- #
# LeetCode fetching
# --------------------------------------------------------------------------- #
def fetch_daily():
    q = """
    query questionOfToday {
      activeDailyCodingChallengeQuestion {
        date
        link
        question { questionFrontendId title titleSlug difficulty }
      }
    }"""
    d = graphql(q)["activeDailyCodingChallengeQuestion"]
    qq = d["question"]
    return {
        "date": d["date"],
        "link": "https://leetcode.com" + d["link"],
        "id": qq["questionFrontendId"],
        "title": qq["title"],
        "slug": qq["titleSlug"],
        "difficulty": qq["difficulty"],
    }


def fetch_question(slug):
    q = """
    query q($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        content
        difficulty
        exampleTestcases
        topicTags { name }
        hints
        codeSnippets { langSlug code }
      }
    }"""
    return graphql(q, {"titleSlug": slug})["question"]


# --------------------------------------------------------------------------- #
# HTML -> readable text
# --------------------------------------------------------------------------- #
def html_to_text(raw):
    if not raw:
        return ""
    t = raw
    # superscripts like 10<sup>5</sup> -> 10^5
    t = re.sub(r"<sup>(.*?)</sup>", r"^\1", t, flags=re.S)
    t = re.sub(r"<sub>(.*?)</sub>", r"_\1", t, flags=re.S)
    # block-ish tags -> newlines
    t = re.sub(r"</(p|div|pre|ul|ol|h[1-6])>", "\n", t, flags=re.I)
    t = re.sub(r"<br\s*/?>", "\n", t, flags=re.I)
    t = re.sub(r"<li>", "\n- ", t, flags=re.I)
    # drop all remaining tags
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    # tidy whitespace
    t = t.replace(" ", " ")
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


# --------------------------------------------------------------------------- #
# Gemini
# --------------------------------------------------------------------------- #
def _extract_text(resp):
    cands = resp.get("candidates") or []
    if not cands:
        return ""
    parts = (cands[0].get("content") or {}).get("parts") or []
    return "".join(p.get("text", "") for p in parts).strip()


def call_gemini(prompt, api_key):
    models = [os.environ["GEMINI_MODEL"]] if os.environ.get("GEMINI_MODEL") else list(DEFAULT_MODELS)
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.3, "maxOutputTokens": 20000, "topP": 0.95},
    }
    last_err = None
    for model in models:
        url = GEMINI_URL.format(model=model, key=api_key)
        for attempt in range(3):
            try:
                resp = _post_json(url, payload, timeout=180)
                text = _extract_text(resp)
                if text:
                    print(f"  Gemini OK via {model} (attempt {attempt + 1})", flush=True)
                    return text
                last_err = f"empty response from {model}: {json.dumps(resp)[:300]}"
            except urllib.error.HTTPError as e:
                body = e.read().decode("utf-8", "replace")[:300]
                last_err = f"{model} HTTP {e.code}: {body}"
                # 429/500/503 -> worth retrying / falling back
            except Exception as e:  # noqa: BLE001
                last_err = f"{model}: {e}"
            time.sleep(2 * (attempt + 1))
        print(f"  Gemini model {model} failed: {last_err}", flush=True)
    raise RuntimeError(f"All Gemini attempts failed. Last error: {last_err}")


def build_prompt(meta, statement, examples, hints, py_snippet):
    tags = ", ".join(meta["tags"]) or "n/a"
    hints_txt = "\n".join(f"- {h}" for h in hints) if hints else "(none provided)"
    return f"""You are an expert competitive-programming tutor and Python engineer.
Write a complete, beginner-friendly but rigorous study note for the LeetCode problem below.
The reader will READ this on a phone during a commute, then paste your solution into LeetCode.
Be clear, visual, and CORRECT.

PROBLEM
- Title: {meta['title']}
- Number: {meta['id']}
- Difficulty: {meta['difficulty']}
- Topics: {tags}

STATEMENT (cleaned):
{statement}

EXAMPLES / SAMPLE TEST CASES:
{examples}

OFFICIAL HINTS:
{hints_txt}

REQUIRED PYTHON SIGNATURE — fill this EXACTLY (keep the class name, method name, and argument types):
{py_snippet}

Write GitHub-flavored Markdown with these sections, in this order, each as a `##` heading:
## Problem Summary
2-3 lines, plain English.
## Intuition
How to *think* about it from scratch — what observation cracks it open.
## Approach
The optimal algorithm as a numbered list of concrete steps.
## Visualization
An ASCII diagram OR a ```mermaid fenced diagram illustrating the core idea
(sliding window / two pointers / tree / DP table — whatever fits). Make it genuinely illustrative.
## Dry Run
Walk through Example 1 step by step in a Markdown table showing how the key state
(pointers, counts, dp, etc.) changes each iteration, then state the final result.
## Complexity
Time and Space, each with a one-line justification.
## Edge Cases
Bullet list of tricky inputs and how the solution handles them.
## Solution
The final Python code in a ```python block, matching the required signature EXACTLY,
clean and lightly commented. It must be optimal and submission-ready.
## Why This Works
One short paragraph: the invariant / proof sketch.

RULES:
- Output ONLY the Markdown body, starting exactly at "## Problem Summary".
- Do NOT add a top-level `#` title, do NOT wrap the whole answer in code fences, and add no commentary before or after.
- The solution must be the most efficient standard approach and pass all stated constraints.
- Keep it skimmable; bold key terms.
"""


# --------------------------------------------------------------------------- #
# Assembly
# --------------------------------------------------------------------------- #
def assemble_markdown(meta, statement, examples, body):
    tags = ", ".join(meta["tags"]) or "—"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    header = (
        f"# [{meta['id']}] {meta['title']}\n\n"
        f"**Difficulty:** {meta['difficulty']} &nbsp;·&nbsp; "
        f"**Daily Challenge:** {meta['date']} &nbsp;·&nbsp; "
        f"[Open on LeetCode]({meta['link']})\n\n"
        f"**Topics:** {tags}\n\n"
        f"> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution "
        f"yourself** on LeetCode. Nothing here is auto-submitted.\n\n"
        f"---\n\n"
        f"## Original Problem\n\n"
        f"{statement}\n\n"
        f"**Examples / sample tests:**\n\n```\n{examples}\n```\n\n"
        f"---\n\n"
    )
    footer = (
        f"\n\n---\n<sub>Generated {now} by the Daily LeetCode Explainer "
        f"(Gemini) • language: Python • not submitted automatically.</sub>\n"
    )
    return header + body.strip() + footer


def update_index(meta, rel_path):
    os.makedirs(DAILY_DIR, exist_ok=True)
    row = (
        f"| {meta['date']} | {meta['id']} | "
        f"[{meta['title']}]({os.path.basename(rel_path)}) | "
        f"{meta['difficulty']} | {', '.join(meta['tags']) or '—'} |"
    )
    head = (
        "# 📅 Daily LeetCode Study Notes\n\n"
        "Auto-generated, paste-ready solutions + deep explanations for the LeetCode "
        "**Question of the Day**. Newest first.\n\n"
        "| Date | # | Problem | Difficulty | Topics |\n"
        "|------|---|---------|------------|--------|\n"
    )
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, encoding="utf-8") as f:
            content = f.read()
    else:
        content = head

    if f"]({os.path.basename(rel_path)})" in content:
        # already indexed (e.g. FORCE re-run) — leave the table untouched
        return

    lines = content.splitlines()
    # insert right after the table separator row
    for i, ln in enumerate(lines):
        if set(ln.strip()) <= set("|-: ") and "-" in ln and ln.strip().startswith("|"):
            lines.insert(i + 1, row)
            break
    else:
        lines = head.rstrip("\n").splitlines() + [row]
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY is not set.", file=sys.stderr)
        return 1

    print("Fetching today's LeetCode daily question…", flush=True)
    daily = fetch_daily()
    print(f"  -> [{daily['id']}] {daily['title']} ({daily['difficulty']}) — {daily['date']}", flush=True)

    os.makedirs(DAILY_DIR, exist_ok=True)
    rel_path = f"{daily['date']}-{daily['slug']}.md"
    out_path = os.path.join(DAILY_DIR, rel_path)
    common = dict(id=daily["id"], title=daily["title"], difficulty=daily["difficulty"],
                  date=daily["date"], link=daily["link"], note_file=rel_path)
    if os.path.exists(out_path) and os.environ.get("FORCE") != "1":
        print(f"  Already exists: Daily/{rel_path} (set FORCE=1 to regenerate). Nothing to do.", flush=True)
        set_output(status="skipped", **common)
        return 0

    q = fetch_question(daily["slug"])
    statement = html_to_text(q.get("content"))
    examples = (q.get("exampleTestcases") or "").strip() or "(see statement)"
    tags = [t["name"] for t in (q.get("topicTags") or [])]
    hints = q.get("hints") or []
    snippets = {s["langSlug"]: s["code"] for s in (q.get("codeSnippets") or [])}
    py_snippet = snippets.get("python3") or snippets.get("python") or "class Solution:\n    pass"

    meta = {**daily, "tags": tags}
    prompt = build_prompt(meta, statement, examples, hints, py_snippet)

    print("Generating explanation with Gemini…", flush=True)
    body = call_gemini(prompt, api_key)

    md = assemble_markdown(meta, statement, examples, body)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)
    update_index(meta, rel_path)
    print(f"Wrote Daily/{rel_path} ({len(md)} chars) and updated index.", flush=True)
    set_output(status="generated", **common)
    return 0


if __name__ == "__main__":
    sys.exit(main())
