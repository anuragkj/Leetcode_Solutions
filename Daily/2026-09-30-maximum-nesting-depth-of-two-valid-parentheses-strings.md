# [1111] Maximum Nesting Depth of Two Valid Parentheses Strings

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-09-30 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/)

**Topics:** String, Stack, Bracket Sequences

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

A string is a valid parentheses string (denoted VPS) if and only if it consists of "(" and ")" characters only, and:

- It is the empty string, or

- It can be written as AB (A concatenated with B), where A and B are VPS's, or

- It can be written as (A), where A is a VPS.

We can similarly define the nesting depth depth(S) of any VPS S as follows:

- depth("") = 0

- depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's

- depth("(" + A + ")") = 1 + depth(A), where A is a VPS.

For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS's (and A.length + B.length = seq.length). The subsequences may not necessarily be contiguous.

For example, for the sequence 123456789, one possible split is:

	A = {1, 3, 5, 7, 9},

	B = {2, 4, 6, 8}.

This corresponds to the output [0, 1, 0, 1, 0, 1, 0, 1, 0]  where 0 indicates membership in A and 1 indicates membership in B.

Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.

Return an answer array (of length seq.length) that encodes such a choice of A and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that even though multiple answers may exist, you may return any of them.

Example 1:

Input: seq = "(()())"
Output: [0,1,1,1,1,0]

Example 2:

Input: seq = "()(())()"
Output: [0,0,0,1,1,0,1,1]

Constraints:

- 1 <= seq.size <= 10000

**Examples / sample tests:**

```
"(()())"
"()(())()"
```

---

## Problem Summary
Given a **Valid Parentheses String (VPS)** `seq`, the task is to split its characters into two disjoint subsequences, `A` and `B`, such that both `A` and `B` are also VPSs. The goal is to minimize the maximum nesting depth between `A` and `B`, i.e., `min(max(depth(A), depth(B)))`. We need to return an array where `answer[i] = 0` if `seq[i]` belongs to `A`, and `1` if it belongs to `B`.

## Intuition
The problem asks us to divide the parentheses into two groups such that the maximum nesting depth in either group is minimized. A key observation for VPS problems is the **nesting depth** of each parenthesis. When we encounter an opening parenthesis `(`, the nesting depth increases. When we encounter a closing parenthesis `)`, the nesting depth decreases. Each `(` and its matching `)` exist at the same nesting level.

To minimize the maximum depth, we want to distribute the parentheses as evenly as possible across the two groups. A common strategy for such problems is to assign items based on the **parity (even or odd)** of their associated "level" or "depth". If we assign parentheses at odd nesting depths to one group and those at even nesting depths to the other, we effectively "flatten" the overall structure. This ensures that the maximum depth in either resulting string `A` or `B` will be approximately half of the original string's maximum depth.

For example, if the original string has a maximum depth of `D`, by alternating assignments based on depth parity, we can achieve a maximum depth of `floor(D/2)` in both `A` and `B`. This is the theoretical minimum possible.

## Approach
We can solve this problem by iterating through the input string `seq` once, maintaining a counter for the current nesting depth.

1.  **Initialize `answer` array:** Create an array `ans` of the same length as `seq`, initialized with zeros. This will store our assignments.
2.  **Initialize `current_depth`:** Set a counter `current_depth` to `0`. This counter will track the current nesting level.
3.  **Iterate through `seq`:** For each character `seq[i]` in the input string:
    *   **If `seq[i]` is an opening parenthesis `(`:**
        *   Assign `seq[i]` to a group based on the **current `current_depth`'s parity**. Specifically, `ans[i] = current_depth % 2`.
        *   Then, increment `current_depth` because we've entered a deeper nesting level.
    *   **If `seq[i]` is a closing parenthesis `)`:**
        *   First, decrement `current_depth` because we are exiting a nesting level.
        *   Assign `seq[i]` to a group based on the **new `current_depth`'s parity**. Specifically, `ans[i] = current_depth % 2`.

This strategy ensures that:
*   Every matching pair of parentheses `( ... )` (which are at the same nesting level) will be assigned to the same group. This is crucial for `A` and `B` to remain valid parentheses strings.
*   The nesting levels are distributed such that the maximum depth in `A` and `B` is minimized.

## Visualization
Let's visualize the process for `seq = "(()())"`:

```mermaid
graph TD
    A[Start] --> B{Initialize: ans = [?, ?, ?, ?, ?, ?], current_depth = 0}
    B --> C(Loop

---
<sub>Generated 2026-09-30 05:53 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
