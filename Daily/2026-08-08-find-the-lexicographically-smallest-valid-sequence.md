# [3302] Find the Lexicographically Smallest Valid Sequence

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-08-08 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/)

**Topics:** Two Pointers, String, Dynamic Programming, Greedy

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given two strings word1 and word2.

A string x is called almost equal to y if you can change at most one character in x to make it identical to y.

A sequence of indices seq is called valid if:

- The indices are sorted in ascending order.

- Concatenating the characters at these indices in word1 in the same order results in a string that is almost equal to word2.

Return an array of size word2.length representing the lexicographically smallest valid sequence of indices. If no such sequence of indices exists, return an empty array.

Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices.

Example 1:

Input: word1 = "vbcca", word2 = "abc"

Output: [0,1,2]

Explanation:

The lexicographically smallest valid sequence of indices is [0, 1, 2]:

- Change word1[0] to 'a'.

- word1[1] is already 'b'.

- word1[2] is already 'c'.

Example 2:

Input: word1 = "bacdc", word2 = "abc"

Output: [1,2,4]

Explanation:

The lexicographically smallest valid sequence of indices is [1, 2, 4]:

- word1[1] is already 'a'.

- Change word1[2] to 'b'.

- word1[4] is already 'c'.

Example 3:

Input: word1 = "aaaaaa", word2 = "aaabc"

Output: []

Explanation:

There is no valid sequence of indices.

Example 4:

Input: word1 = "abc", word2 = "ab"

Output: [0,1]

Constraints:

- 1 <= word2.length < word1.length <= 3 * 10^5

- word1 and word2 consist only of lowercase English letters.

**Examples / sample tests:**

```
"vbcca"
"abc"
"bacdc"
"abc"
"aaaaaa"
"aaabc"
"abc"
"ab"
```

---

## Problem Summary
You are given two strings, `word1` and `word2`. The goal is to find the **lexicographically smallest sequence of indices** from `word1` such that concatenating `word1`'s characters at these indices forms a string "almost equal" to `word2`. "Almost equal" means at most one character difference. If no such sequence exists, return an empty array.

## Intuition
This problem asks for the **lexicographically smallest sequence of indices**. This is a strong hint for a **greedy approach**: at each step, when deciding which index `k` from `word1` to use for `word2[i]`, we should always try to pick the *smallest possible `k`*.

The "at most one character difference" condition is the main challenge. This means we can either:
1.  Match `word2[i]` perfectly with `word1[k]`.
2.  Use `word1[k]` as a mismatch for `word2[i]`, consuming our single allowed mismatch.

To make an informed greedy decision, we need to know if picking a certain `word1[k]` allows the *rest* of `word2` (i.e., `word2[i+1:]`) to be matched perfectly from `word1[k+1:]`. This suggests a **Dynamic Programming (DP) precomputation** to quickly check suffix matchability.

## Approach
The optimal solution combines DP precomputation with a greedy selection strategy, optimized using precomputed next-occurrence arrays.

1.  **Precompute `dp` array (Suffix Perfect Match Length):**
    *   Create an array `dp` of size `len(word1) + 1`.
    *   `dp[i]` will store the **length of the longest suffix of `word2` that can be formed as a *perfect subsequence* using characters from `word1[i:]`**.
    *   Initialize `dp[len(word1)] = 0` (an empty suffix of `word1` can perfectly match an empty suffix of `word2`).
    *   Iterate `i` from `len(word1) - 1` down to `0`:
        *   By default, `dp[i] = dp[i+1]` (meaning we skip `word1[i]`).
        *   Calculate `target_char_idx_in_word2 = len(word2) - dp[i+1] - 1`. This is the index in `word2` of the character we would need to match *next* if we were extending a perfect suffix match from `word1[i+1:]`.
        *   If `target_char_idx_in_word2` is a valid index (i.e., `>= 0`) AND `word1[i]` matches `word2[target_char_idx_in_word2]`:
            *   Then `word1[i]` can extend the perfect match. Set `dp[i] = dp[i+1] + 1`.
    *   This `dp` array is **non-increasing**.

2.  **Precompute `next_char_idx` array (Next Character Occurrence):**
    *   Create a 2D array `next_char_idx` of size `26 x (len(word1) + 1)`.
    *   `next_char_idx[char_code][i]` will store the **smallest index `j >= i` such that `word1[j]` is the character corresponding to `char_code`**.
    *   Initialize all entries with `len(word1)` (

---
<sub>Generated 2026-08-08 02:30 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
