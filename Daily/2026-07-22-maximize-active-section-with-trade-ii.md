# [3501] Maximize Active Section with Trade II

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-07-22 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximize-active-section-with-trade-ii/)

**Topics:** Array, String, Binary Search, Segment Tree

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a binary string s of length n, where:

- '1' represents an active section.

- '0' represents an inactive section.

You can perform at most one trade to maximize the number of active sections in s. In a trade, you:

- Convert a contiguous block of '1's that is surrounded by '0's to all '0's.

- Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.

Additionally, you are given a 2D array queries, where queries[i] = [l_i, r_i] represents a substring s[l_i...r_i].

For each query, determine the maximum possible number of active sections in s after making the optimal trade on the substring s[l_i...r_i].

Return an array answer, where answer[i] is the result for queries[i].

Note

- For each query, treat s[l_i...r_i] as if it is augmented with a '1' at both ends, forming t = '1' + s[l_i...r_i] + '1'. The augmented '1's do not contribute to the final count.

- The queries are independent of each other.

Example 1:

Input: s = "01", queries = [[0,1]]

Output: [1]

Explanation:

Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

Example 2:

Input: s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]]

Output: [4,3,1,1]

Explanation:

-
	Query [0, 3] → Substring "0100" → Augmented to "101001"

	Choose "0100", convert "0100" → "0000" → "1111".

	The final string without augmentation is "1111". The maximum number of active sections is 4.

-
	Query [0, 2] → Substring "010" → Augmented to "10101"

	Choose "010", convert "010" → "000" → "111".

	The final string without augmentation is "1110". The maximum number of active sections is 3.

-
	Query [1, 3] → Substring "100" → Augmented to "11001"

	Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

-
	Query [2, 3] → Substring "00" → Augmented to "1001"

	Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

Example 3:

Input: s = "1000100", queries = [[1,5],[0,6],[0,4]]

Output: [6,7,2]

Explanation:

	Query [1, 5] → Substring "00010" → Augmented to "1000101"
	Choose "00010", convert "00010" → "00000" → "11111".

	The final string without augmentation is "1111110". The maximum number of active sections is 6.

	Query [0, 6] → Substring "1000100" → Augmented to "110001001"
	Choose "000100", convert "000100" → "000000" → "111111".

	The final string without augmentation is "1111111". The maximum number of active sections is 7.

	Query [0, 4] → Substring "10001" → Augmented to "1100011"
	Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.

Example 4:

Input: s = "01010", queries = [[0,3],[1,4],[1,3]]

Output: [4,4,2]

Explanation:

-
	Query [0, 3] → Substring "0101" → Augmented to "101011"

	Choose "010", convert "010" → "000" → "111".

	The final string without augmentation is "11110". The maximum number of active sections is 4.

-
	Query [1, 4] → Substring "1010" → Augmented to "110101"

	Choose "010", convert "010" → "000" → "111".

	The final string without augmentation is "01111". The maximum number of active sections is 4.

-
	Query [1, 3] → Substring "101" → Augmented to "11011"

	Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.

Constraints:

- 1 <= n == s.length <= 10^5

- 1 <= queries.length <= 10^5

- s[i] is either '0' or '1'.

- queries[i] = [l_i, r_i]

- 0 <= l_i <= r_i < n

**Examples / sample tests:**

```
"01"
[[0,1]]
"0100"
[[0,3],[0,2],[1,3],[2,3]]
"1000100"
[[1,5],[0,6],[0,4]]
"01010"
[[0,3],[1,4],[1,3]]
```

---

This problem asks us to maximize the number of '1's in a given substring `s[l...r]` by performing at most one special "trade" operation. The trade involves converting a block of '1's surrounded by '0's to '0's, and then converting a resulting block of '0's surrounded by '1's to '1's. A crucial detail is that for each query `s[l...r]`, it's conceptually augmented with '1's at both ends, forming `t = '1' + s[l...r] + '1'`, but these augmented '1's do not contribute to the final count.

## Problem Summary
For each query `[l, r]` on a binary string `s`, find the maximum number of '1's in `s[l...r]` after at most one trade. A trade converts a `0...01...10...0` pattern into all `1`s, provided this block is surrounded by '1's (which can be augmented '1's at the substring boundaries).

## Intuition
Let's analyze the "trade" operation. It consists of two steps:
1.  Convert a contiguous block of '1's (let's call it `O`) that is surrounded by '0's to all '0's. This means we find a pattern `0 O 0`.
2.  After this conversion, we now have a larger block of '0's. If this new, larger block of '0's is surrounded by '1's, we convert it to all '1's. This means we are looking for `1 (new_0_block) 1`.

Combining these steps, the trade effectively identifies a pattern `1 (0...0) (1...1) (0...0) 1` and converts the entire `(0...0) (1...1) (0...0)` part into all '1's. Let `Z_L` be the left block of '0's, `O` be the '1's block, and `Z_R` be the right block of '0's. The trade converts `Z_L O Z_R` into `1...1`. The number of '1's obtained from this trade is `len(Z_L) + len(O) + len(Z_R)`.

For a given query `s[l...r]`, the augmented string `t = '1' + s[l...r] + '1'` means that any block of '0's within `s[l...r]` that extends to `l` or `r` is effectively surrounded by '1's. This leads to two main scenarios for maximizing '1's:

1.  **No trade or suboptimal trade:** The answer is simply the count of '1's in `s[l...r]`.
2.  **Trade of a `Z_L O Z_R` pattern fully contained within `s[l...r]`:** We find a `0...01...10...0` pattern in `s[l...r]` where the entire pattern is surrounded by '1's (either from `s` or the augmented '1's). The maximum '1's would be `len(Z_L) + len(O) + len(Z_R)`.
3.  **Trade that converts the entire `s[l...r]` to '1's:** This is possible if `s[l...r]` contains a `010` pattern (i.e., a '0', then a '1',

---
<sub>Generated 2026-07-22 04:00 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
