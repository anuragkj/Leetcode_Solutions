# [1658] Minimum Operations to Reduce X to Zero

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-09-23 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/)

**Topics:** Array, Hash Table, Binary Search, Sliding Window, Prefix Sum

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

Constraints:

- 1 <= nums.length <= 10^5

- 1 <= nums[i] <= 10^4

- 1 <= x <= 10^9

**Examples / sample tests:**

```
[1,1,4,2,3]
5
[5,6,7,8,9]
4
[3,2,20,1,1,3]
10
```

---

## Problem Summary
The goal is to find the **minimum number of operations** to make an integer `x` exactly 0. An operation consists of removing either the leftmost or rightmost element from the `nums` array and subtracting its value from `x`.

## Intuition
The problem asks for the minimum number of elements to remove from *both ends* of the array `nums` such that their sum equals `x`. This means the elements we *remove* form a prefix and a suffix of the original array.

Thinking in reverse often simplifies such problems. If we remove a prefix and a suffix, the elements that **remain** in the middle form a **contiguous subarray**.
Let `total_sum` be the sum of all elements in `nums`. If the removed elements sum to `x`, then the remaining elements must sum to `total_sum - x`.

So, the problem transforms into: **Find the longest contiguous subarray whose sum is `total_sum - x`**. Once we find this longest subarray, the number of elements *not* in it will be `len(nums) - (length of this subarray)`, which directly gives us the minimum operations. This is because minimizing removed elements is equivalent to maximizing remaining elements.

## Approach
1.  **Calculate Total Sum**: First, compute the `total_sum` of all elements in the `nums` array.
2.  **Determine Target Sum**: The target sum for the *middle subarray* is `target_sum = total_sum - x`.
3.  **Handle Edge Cases for Target Sum**:
    *   If `target_sum < 0`: It's impossible to reach `x=0` by removing positive numbers if `x` is already greater than the `total_sum` of the array. Return -1.
    *   If `target_sum == 0`: This means we need to remove *all* elements. The longest subarray with sum 0 would be an empty subarray, but we are looking for the *remaining* part. If `target_sum` is 0, it means the sum of all elements is `x`. So we need to remove all `len(nums)` elements. This is a special case where `max_len` should be 0, and the result is `len(nums)`.
4.  **Sliding Window**: Use a **two-pointer sliding window** to find the longest subarray with `target_sum`.
    *   Initialize `left = 0` (start of the window), `current_sum = 0`, and `max_len = -1` (to indicate no such subarray found yet).
    *   Iterate `right` from `0` to `len(nums) - 1`:
        *   Add `nums[right]` to `current_sum`. This expands the window to the right.
        *   While `current_sum > target_sum` and `left <= right`:
            *   Subtract `nums[left]` from `current_sum`. This shrinks the window from the left.
            *   Increment `left`.
        *   If `current_sum == target_sum`:
            *   A subarray with the `target_sum` has been found. Update `max_len = max(max_len, right - left + 1)`. We want the *longest* such subarray.
5.  **Return Result**:
    *   After iterating through all possible `right` pointers, if `max_len` is still `-1`, it means no subarray with `target_sum` was found. Return `-1`.
    *   Otherwise, return `len(nums) - max_len`. This is the minimum number of operations (elements removed from ends).

---
<sub>Generated 2026-09-23 05:04 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
