# [1520] Maximum Number of Non-Overlapping Substrings

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-09-18 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/)

**Topics:** Hash Table, String, Greedy, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

- The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.

- A substring that contains a certain character c must also contain all occurrences of c.

Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.

Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.

Constraints:

- 1 <= s.length <= 10^5

- s contains only lowercase English letters.

**Examples / sample tests:**

```
"adefaddaccc"
"abbaccd"
```

---

This study note provides a complete, beginner-friendly, and rigorous explanation for LeetCode problem 1520: "Maximum Number of Non-Overlapping Substrings".

## Problem Summary
Given a string `s`, find the maximum number of non-overlapping substrings. Each chosen substring must contain all occurrences of every character it includes. If multiple solutions yield the same maximum number of substrings, return the one with the minimum total length.

## Intuition
The core challenge lies in the condition: "A substring that contains a certain character `c` must also contain all occurrences of `c`." This is a powerful constraint. If we pick a substring `s[i..j]` that includes character `c`, then `s[i..j]` must span at least from `first[c]` (the first index of `c` in `s`) to `last[c]` (its last index). More precisely, for `s[i..j]` to be a valid substring, for *every* character `c` present within `s[i..j]`, its entire range `[first[c], last[c]]` must be contained within `[i, j]`. This implies that `i` must be less than or equal to `first[c]` and `j` must be greater than or equal to `last[c]` for all `c` in `s[i..j]`.

This leads to the idea of "minimal valid substrings": a substring `s[start..end]` is minimal if `start` is the smallest `first[c]` and `end` is the largest `last[c]` for all characters `c` within `s[start..end]`, and crucially, for every character `c'` within `s[start..end]`, `first[c'] >= start`. We can generate all such minimal valid substrings.

A key observation (also hinted by the problem) is that if any two such minimal valid substrings overlap, one must completely contain the other. This simplifies the problem significantly. If `[x,y]` is contained within `[i,j]`, and we want to maximize the count of non-overlapping substrings while minimizing total length, we should prefer `[x,y]` over `[i,j]` if both are options. This is because `[x,y]` is shorter and leaves more "space" for other non-overlapping substrings. This structure allows us to use a standard **greedy algorithm** similar to the Activity Selection Problem.

## Approach
The optimal algorithm involves three main steps:

1.  **Precompute Character Ranges:**
    *   For each character 'a' through 'z', find its `first` occurrence index and `last` occurrence index in the string `s`. Store these in two arrays, `first[char_idx]` and `last[char_idx]`.

2.  **Generate Minimal Valid Substrings:**
    *   Iterate through the string `s` with an index `i` from `0` to `len(s) - 1`.
    *   For each `i`, consider it as a potential **start** of a minimal valid substring. We only need to check `i` if it's the *first occurrence* of `s[i]` (i.e., `i == first[s[i]]`). If `s[i]` has appeared before, any valid substring containing it must have started earlier.
    *   Initialize `current_end = last[s[i]]` and `possible_start = i`.
    *   Iterate with a pointer `j` from `i` up to `current_end` (note: `current_end` can expand during this loop):
        *   For each character `s[j]`:
            *   **Check Condition 1:** If `first[s[j]] < possible_start`, it means `s[j]` appears *before* our current `possible_start`. This violates the condition that all occurrences of `s[j]` must be within `s[possible_start..current_end]`. Therefore, `s[possible_start..current_end]` cannot be a valid substring starting at `possible_start`. Mark it as invalid and break the inner loop.
            *   **Check Condition 2:** Update `current_end = max(current_end, last[s[j]])`. This ensures that `current_end` always covers the last occurrence of any character encountered so far within `s[possible_start..current_end]`.
    *   If the inner loop completes without `is_valid_candidate` becoming `False`, then `(possible_start, current_end)` represents a minimal valid substring. Add this `(start, end)` pair to a list of `candidates`.

3.  **Greedy Selection for Maximum Non-Overlapping Substrings:**
    *   Sort the `candidates` list. The standard greedy strategy for maximizing non-overlapping intervals is to sort by their **end index** (ascending). If end indices are equal, sort by **start index** (ascending).
    *   Initialize an empty `result` list and `last_taken_end = -1` (or any value smaller than any possible start index).
    *   Iterate through the sorted `candidates`: For each `(start, end)` pair:
        *   If `start > last_taken_end`, it means this substring does not overlap with the previously chosen one. Select it: add `s[start : end + 1]` to `result` and update `last_taken_end = end`.
        *   If `start <= last_taken_end`, it means this substring overlaps with or is contained within the previously chosen one. Skip it. The sorting by end index naturally ensures that if a smaller interval is contained within a larger one, the smaller one is considered first, leading to the minimum total length among solutions with maximum count.

4.  **Return `result`.**

## Visualization

Let's visualize the `first`, `last` arrays and the candidate generation for `s = "adefaddaccc"`:

**1. Precompute `first` and `last`:**

```
s: a d e f a d d a c c c
idx:0 1 2 3 4 5 6 7 8 9 10

first:
a: 0
d: 1
e: 2
f: 3
c: 8

last:
a: 7
d: 6
e: 2
f: 3
c: 10
```
*(Correction: `last['a']` should be 7, not 6. My dry run used 6, but the string is `adef

---
<sub>Generated 2026-09-18 05:06 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
