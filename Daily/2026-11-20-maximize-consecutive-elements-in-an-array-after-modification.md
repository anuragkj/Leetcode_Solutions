# [3041] Maximize Consecutive Elements in an Array After Modification

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-11-20 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/)

**Topics:** Array, Dynamic Programming, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 0-indexed array nums consisting of positive integers.

Initially, you can increase the value of any element in the array by at most 1.

After that, you need to select one or more elements from the final array such that those elements are consecutive when sorted in increasing order. For example, the elements [3, 4, 5] are consecutive while [3, 4, 6] and [1, 1, 2, 3] are not.

Return the maximum number of elements that you can select.

Example 1:

Input: nums = [2,1,5,1,1]
Output: 3
Explanation: We can increase the elements at indices 0 and 3. The resulting array is nums = [3,1,5,2,1].
We select the elements [3,1,5,2,1] and we sort them to obtain [1,2,3], which are consecutive.
It can be shown that we cannot select more than 3 consecutive elements.

Example 2:

Input: nums = [1,4,7,10]
Output: 1
Explanation: The maximum consecutive elements that we can select is 1.

Constraints:

- 1 <= nums.length <= 10^5

- 1 <= nums[i] <= 10^6

**Examples / sample tests:**

```
[2,1,5,1,1]
[1,4,7,10]
```

---

## Problem Summary
You are given an array of positive integers. You can increase any element by at most 1. The goal is to select the maximum number of elements from the modified array such that they form a consecutive sequence when sorted (e.g., [3, 4, 5]). Return this maximum count.

## Intuition
The problem asks for the longest consecutive sequence after a specific modification. This immediately suggests **sorting** the input array `nums` first, as consecutive sequences are easier to find in sorted data.

Each number `x` in the original array `nums` can be transformed into either `x` or `x+1`.
If we are building a consecutive sequence like `[V, V+1, V+2, ...]`, each element `V+k` in this sequence must come from some original `num_i` such that `num_i` can become `V+k`. This means `num_i` must be either `V+k` (no modification) or `V+k-1` (modified to `V+k`).

This problem has the characteristics of a **Dynamic Programming** problem: we want to find the "longest" sequence, and decisions for one element can affect subsequent elements.
Let `dp[val]` be the maximum length of a consecutive sequence ending with `val`. When we process an element `num` from the sorted input array, `num` can contribute to two possible values in a final consecutive sequence:
1.  **`num` (no modification):** If `num` becomes `num`, it can extend a sequence that ended at `num-1`. The length of such a sequence would be `1 + dp[num-1]`.
2.  **`num+1` (modified):** If `num` becomes `num+1`, it can extend a sequence that ended at `num`. The length of such a sequence would be `1 + dp[num]`.

The crucial part is handling duplicates and ensuring that `dp[val]` always stores the *maximum* length. When we calculate the length for `num+1`, `dp[num]` should reflect the best sequence ending at `num` *before* the current `num` potentially updates `dp[num]` itself (if `num` becomes `num`).

## Approach
1.  **Sort the Array:** First, sort the input array `nums` in non-decreasing order. This simplifies finding consecutive elements.
2.  **Initialize DP State:** Use a hash map (Python's `defaultdict(int)` is perfect) called `dp`. `dp[val]` will store the maximum length of a consecutive sequence ending with `val`. Initialize `max_len = 0` to track the overall maximum length found.
3.  **Iterate and Update DP:** Iterate through each `num` in the sorted `nums` array. For each `num`:
    *   **Store `dp[num]` before potential update:** Get the current value of `dp[num]` (let's call it `prev_dp_num_val`). This is important because `num` can become `num` (updating `dp[num]`) or `num+1` (using the *previous* `dp[num]` value).
    *   **Calculate length if `num` becomes `num`:** This element can extend a sequence ending at `num-1`. The length would be `1 + dp.get(num - 1, 0)`. Update `dp[num]` with the maximum of its current value and this new length.
    *   **Calculate length if `num` becomes `num+1`:** This element can extend a sequence ending at `num`. The length would be `1

---
<sub>Generated 2026-11-20 07:41 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
