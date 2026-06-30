# Daily LeetCode Explainer

Every morning this repo generates a deep study note for the LeetCode **Question of the Day** —
problem, intuition, a diagram, a step-by-step dry run, complexity, edge cases, and a
**paste-ready Python solution** — and commits it to [`Daily/`](../Daily).

It **never submits** anything to LeetCode (zero ban risk). You read the note and paste the
solution yourself.

## How it works

```
.github/workflows/daily_explainer.yml   # cron: 00:30 UTC (06:00 IST) + manual trigger
scripts/daily_leetcode.py               # fetch daily Q (public API) -> Gemini -> Markdown
Daily/<date>-<slug>.md                   # one note per day
Daily/README.md                          # index of all notes
```

- The question is fetched from LeetCode's **public** GraphQL API — **no token, ever**
  (this is what replaces the session/CSRF token you had to refresh constantly).
- The explanation + solution are written by **Google Gemini** using a free API key.

## One-time setup

1. **Get a free Gemini API key** at <https://aistudio.google.com/app/apikey>.
2. In this repo: **Settings → Secrets and variables → Actions → New repository secret**
   - Name: `GEMINI_API_KEY`
   - Value: *your key*
3. (Optional) To pin a model, add a repo **Variable** `GEMINI_MODEL`
   (e.g. `gemini-2.0-flash`). Default tries `gemini-2.5-flash` then `gemini-2.0-flash`.
4. Go to the **Actions** tab → **Daily LeetCode Explainer** → **Run workflow** to test it now.

That's the only manual step, and the Gemini key does **not** expire every few weeks like the
LeetCode session token did.

## Run it locally (optional)

```bash
export GEMINI_API_KEY=your_key_here
python scripts/daily_leetcode.py        # set FORCE=1 to overwrite today's note
```
