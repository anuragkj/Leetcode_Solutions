# [3644] Maximum K to Sort a Permutation

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-10-23 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximum-k-to-sort-a-permutation/)

**Topics:** Array, Bit Manipulation

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [0..n - 1].

You may swap elements at indices i and j only if nums[i] AND nums[j] == k, where AND denotes the bitwise AND operation and k is a non-negative integer.

Return the maximum value of k such that the array can be sorted in non-decreasing order using any number of such swaps. If nums is already sorted, return 0.

Example 1:

Input: nums = [0,3,2,1]

Output: 1

Explanation:

Choose k = 1. Swapping nums[1] = 3 and nums[3] = 1 is allowed since nums[1] AND nums[3] == 1, resulting in a sorted permutation: [0, 1, 2, 3].

Example 2:

Input: nums = [0,1,3,2]

Output: 2

Explanation:

Choose k = 2. Swapping nums[2] = 3 and nums[3] = 2 is allowed since nums[2] AND nums[3] == 2, resulting in a sorted permutation: [0, 1, 2, 3].

Example 3:

Input: nums = [3,2,1,0]

Output: 0

Explanation:

Only k = 0 allows sorting since no greater k allows the required swaps where nums[i] AND nums[j] == k.

Constraints:

- 1 <= n == nums.length <= 10^5

- 0 <= nums[i] <= n - 1

- nums is a permutation of integers from 0 to n - 1.

**Examples / sample tests:**

```
[0,3,2,1]
[0,1,3,2]
[3,2,1,0]
```

---

## Problem Summary
Given a permutation `nums` of `[0, n-1]`, find the largest non-negative integer `k` such that the array can be sorted. Swaps are allowed between `nums[i]` and `nums[j]` if and only if `nums[i] AND nums[j] == k`. If the array is already sorted, return 0.

## Intuition
The core idea for sorting a permutation using swaps is that for every element `nums[i]` that is not in its correct sorted position `i` (i.e., `nums[i] != i`), the value `nums[i]` and the value `i` must belong to the same "swap group" or connected component. A swap group is formed by values that can be reached from each other through a series of allowed swaps.

1.  **Condition for `k`:** If two values `u` and `v` can be swapped (i.e., `u AND v == k`), then both `u` and `v` must have all the bits of `k` set. This means `u AND k == k` and `v AND k == k`. By transitivity, any value `x` that is part of a swap group for a given `k` must satisfy `x AND k == k`.
2.  **Required connections:** For the array to be sortable, for every index `i` where `nums[i] != i`, the value `nums[i]` (currently at index `i`) must be able to reach its correct position `nums[i]`, and the value `i` (which is currently at `nums[j]=i` for some `j`) must be able to reach its correct position `i`. This means that for every `i` such that `nums[i] != i`, the value `i` and the value `nums[i]` must be in the same connected component.
3.  **Maximum `k`:** Combining these: for any `k` to allow sorting, for every `i` where `nums[i] != i`, both `i` and `nums[i]` must satisfy `x AND k == k`. This implies that `k` must be a submask of `i` and `nums[i]` for all such `i`. Therefore, `k` must be a submask of the bitwise AND of *all* values `x` that are either `i` or `nums[i]` for some `i` where `nums[i] != i`. Let this combined bitwise AND be `K_max`. Any valid `k` must be a submask of `K_max`. Thus, `K_max` is the largest possible candidate for `k`.
4.  **Verification:** We calculate `K_max`. Then, we need to verify if this `K_max` actually allows all necessary swaps. This involves building a graph where nodes are values `0` to `n-1`, and an edge exists between `u` and `v` if `u AND v == K_max`. We then check if all required pairs `(i, nums[i])` (where `nums[i] != i`) are in the same connected component.

The hint "Take the bitwise AND of all elements that are not in their correct position" directly points to calculating `K_max`. "Elements that are not in their correct position" refers to both the value `nums[i]` and the value `i` itself (since `i` is not at index `i`).

## Approach
1.  **Handle Already Sorted Case:** First, check if the input array `nums` is already sorted. If `nums[i] == i`

---
<sub>Generated 2026-10-23 05:15 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
