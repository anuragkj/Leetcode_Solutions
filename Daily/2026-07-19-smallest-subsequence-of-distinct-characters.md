# [1081] Smallest Subsequence of Distinct Characters

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-07-19 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)

**Topics:** String, Stack, Greedy, Monotonic Stack

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

Constraints:

- 1 <= s.length <= 1000

- s consists of lowercase English letters.

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/

**Examples / sample tests:**

```
"bcabc"
"cbacdcbc"
```

---

The `stack` data structure is perfect for problems requiring us to build a sequence greedily while maintaining certain properties (like lexicographical order) by potentially removing "bad" elements from the end.

## Problem Summary

Given a string `s`, we need to find the lexicographically smallest subsequence that contains all the unique characters of `s` exactly once. This means the resulting string must be sorted as much as possible, using each distinct character only a single time.

## Intuition

To get the **lexicographically smallest** subsequence, we want to place **smaller characters as early as possible**.
Consider building our result character by character. When we encounter a character `c` from the input string `s`:

1.  If `c` is **already in our current result**, we can simply **skip it**. We only need distinct characters once, and we've already included `c` at an earlier (and thus potentially better) position.

2.  If `c` is **not in our current result**, we **must include it** at some point. Where should we put it?
    *   We want `c` to be as early as possible.
    *   What if `c` is **smaller** than the last character `last_char` we added to our result?
        *   If `last_char` will **appear again later** in the string `s`, then we can **remove `last_char`** from our current result. By doing this, we make space for `c` to be placed earlier. Since `last_char` will reappear, we can pick it up later to satisfy the "all distinct characters" requirement. This greedy choice helps make the subsequence lexicographically smaller.
        *   If `last_char` **does NOT appear again later** in `s`, then we **MUST keep `last_char`**. It's our last chance to include it, and removing it would prevent us from having all distinct characters.
    *   If `c` is **larger** than `last_char`, we simply append `c`.

This "remove if smaller and can be found later" logic is a classic pattern for problems solvable with a **monotonic stack**. We'll use a stack to build our result, popping elements that are "worse" (larger) if we have a chance to replace them with a "better" (smaller) character later.

To implement this, we need two auxiliary data structures:
*   A `stack` (Python list) to build our result.
*   A `seen` set to quickly check if a character is already in our `stack` (and thus in our current result).
*   A `last_occurrence` dictionary/array to store the last index of each character in `s`. This helps us determine if a character `last_char` can be found later in `s`.

## Approach

1.  **Precompute Last Occurrences**: Iterate through the input string `s` once to build a dictionary (or an array for fixed alphabet size) called `last_occurrence`. This dictionary will map each character to its **last index** in `s`. For example, if `s = "cbacdcbc"`, `last_occurrence['c']` would be 7, `last_occurrence['b']` would be 6, etc.

2.  **Initialize Data Structures**:
    *   Create an empty list, `stack`, which will store the characters of our resulting subsequence.
    *   Create an empty set, `seen`, to keep track of characters currently present in the `stack`. This helps ensure distinctness.

3.  **Iterate and Build Subsequence**: Iterate through the input string `s` character by character, along with its index `i`:

---
<sub>Generated 2026-07-19 04:05 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
