# [628] Maximum Product of Three Numbers

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-07-26 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximum-product-of-three-numbers/)

**Topics:** Array, Math, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:

Input: nums = [1,2,3]
Output: 6

Example 2:

Input: nums = [1,2,3,4]
Output: 24

Example 3:

Input: nums = [-1,-2,-3]
Output: -6

Constraints:

- 3 <= nums.length <= 10^4

- -1000 <= nums[i] <= 1000

**Examples / sample tests:**

```
[1,2,3]
[1,2,3,4]
[-1,-2,-3]
```

---

## Problem Summary
Given an array of integers, the goal is to find any three numbers within the array whose product is the largest possible, and then return that maximum product.

## Intuition
To maximize a product of three numbers, we generally want to pick the largest possible numbers. If all numbers are positive, this means picking the three largest numbers. However, negative numbers introduce a twist: the product of two negative numbers is positive. This means two very small (i.e., very negative) numbers, when multiplied together, can create a large positive value. If we then multiply this by the single largest positive number in the array, it might yield a product greater than that of just the three largest numbers.

Therefore, the maximum product must come from one of two scenarios:
1.  The product of the **three largest numbers** in the array.
2.  The product of the **two smallest (most negative) numbers** and the **single largest number** in the array.

To easily find these "largest" and "smallest" numbers, **sorting** the array is a very effective first step.

## Approach
1.  **Sort the Array**: First, sort the input array `nums` in **ascending order**. This arranges the numbers from smallest to largest.
2.  **Identify Candidates**: After sorting, let `n` be the length of the array.
    *   The three largest numbers will be `nums[n-1]`, `nums[n-2]`, and `nums[n-3]`. Calculate their product: `product_of_three_largest = nums[n-1] * nums[n-2] * nums[n-3]`.
    *   The two smallest numbers will be `nums[0]` and `nums[1]`. The single largest number is `nums[n-1]`. Calculate their product: `product_of_two_smallest_and_one_largest = nums[0] * nums[1] * nums[n-1]`.
3.  **Return Maximum**: The final answer is the maximum of these two candidate products.

## Visualization

Let's visualize a sorted array `nums` and the indices involved in our two candidate products:

```
Sorted Array:
[ nums[0], nums[1], ..., nums[n-3], nums[n-2], nums[n-1] ]
  ▲        ▲              ▲           ▲           ▲
  |        |              |           |           |
  |        |              |           |           +-- Largest number
  |        |              |           +-------------- 2nd Largest number
  |        |              +-------------------------- 3rd Largest number
  |        +----------------------------------------- 2nd Smallest number
  +-------------------------------------------------- Smallest number

Candidate Product 1:
nums[n-3] * nums[n-2] * nums[n-1]
(Product of the three largest numbers)

Candidate Product 2:
nums[0] * nums[1] * nums[n-1]
(Product of the two smallest numbers and the largest number)
```

We compare these two products and pick the greater one.

## Dry Run
Let's walk through Example 2: `nums = [1,2,3,4]`

1.  **Sort the Array**:
    `nums` becomes `[1,2,3,4]` (it was already sorted).
    The length `n = 4`.

2.  **Identify Candidates**:
    *   **Product of three largest numbers**:
        These are `nums[n-1]`, `nums[n-2]`, `nums[n-3]`.
        Which are `nums[3]`, `nums[2]`, `nums[1]`.
        Values: `4`, `3`, `2`.
        `product_of_three_largest = 4 * 3 * 2 = 24`.

    *   **Product of two smallest and one largest number**:
        These are `nums[0]`, `nums[1]`, `nums[n-1]`.
        Which are `nums[0]`, `nums[1]`, `nums[3]`.
        Values: `1`, `2`, `4`.
        `product_of_two_smallest_and_one_largest = 1 * 2 * 4 = 8`.

3.  **Return Maximum**:
    `max(24, 8) = 24`.

The final result is `24`.

## Complexity
*   **Time Complexity**: `O(N log N)`
    *   This is dominated by the **sorting** step. Python's `list.sort()` uses Timsort, which has an average and worst-case time complexity of `O(N log N)`.
*   **Space Complexity**: `O(N)`
    *   Python's `list.sort()` can use `O(N)` auxiliary space in the worst case (though often `O(log N)` for Timsort). If an in-place sort with `O(1)` space was used (like Heapsort), it would be `O(1)` space, but Python's built-in sort is not guaranteed to be `O(1)` space.

## Edge Cases
*   **All positive numbers**: `[1,2,3,4]`. The three largest (`2,3,4`) will yield the max product (`24`). The two smallest and one largest (`1,2,4`) will yield `8`. Our solution correctly picks `24`.
*   **All negative numbers**: `[-1,-2,-3]`. Sorted: `[-3,-2,-1]`.
    *   Three largest: `(-1 * -2 * -3) = -6`.
    *   Two smallest and one largest: `(-3 * -2 * -1) = -6`.
    *   Our solution correctly picks `-6`. In this case, the "three largest" are actually the three numbers closest to zero.
*   **Mixed positive and negative, with large negative numbers**: `[-100, -2, -1, 1, 2, 3]`. Sorted: `[-100, -2, -1, 1, 2, 3]`.
    *   Three largest: `(1 * 2 * 3) = 6`.
    *   Two smallest and one largest: `(-100 * -2 * 3) = 600`.
    *   Our solution correctly picks `600`. This is the key case our two-candidate approach handles.
*   **Array length is minimum (3)**: `[1,2,3]` or `[-1,-2,-3]`. In this scenario, `n-1`, `n-2`, `n-3` are `2, 1, 0`. And `0, 1, n-1` are `0, 1, 2`. Both product calculations use the same three numbers, so the logic holds.
*   **Presence of zeros**: `[-5, -4, 0, 1, 2]`. Sorted: `[-5, -4, 0, 1, 2]`.
    *   Three largest: `(0 * 1 * 2) = 0`.
    *   Two smallest and one largest: `(-5 * -4 * 2) = 40`.
    *   Our solution correctly picks `40`.

## Solution

```python
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Step 1: Sort the array to easily access the smallest and largest elements.
        # Sorting in ascending order places smallest elements at the beginning
        # and largest elements at the end.
        nums.sort()
        
        n = len(nums)
        
        # Step 2: Calculate the two candidate products.

        # Candidate 1: Product of the three largest numbers.
        # These are nums[n-1], nums[n-2], nums[n-3] after sorting.
        # This covers cases where all numbers are positive, or all are negative
        # (e.g., [-1,-2,-3] -> -1 * -2 * -3 = -6, which is the max product here).
        product1 = nums[n-1] * nums[n-2] * nums[n-3]
        
        # Candidate 2: Product of the two smallest (most negative) numbers and the largest number.
        # These are nums[0], nums[1], nums[n-1] after sorting.
        # This is crucial for cases like [-100, -2, -1, 1, 2, 3] where
        # (-100 * -2 * 3 = 600) is greater than (1 * 2 * 3 = 6).
        product2 = nums[0] * nums[1] * nums[n-1]
        
        # Step 3: Return the maximum of the two candidate products.
        return max(product1, product2)

```

## Why This Works
This approach works because the maximum product of three numbers can only arise from one of two fundamental scenarios:
1.  All three numbers are positive. In this case, to maximize the product, we must choose the three largest positive numbers available.
2.  Two numbers are negative, and one is positive. The product of two negative numbers is positive. To maximize this positive product, we should choose the two most negative (smallest) numbers to make their product as large positive as possible, and then multiply by the single largest positive number available.

Any other combination (e.g., one negative, two positive; three negative; one positive, two negative) will either be covered by these two cases or yield a smaller product. For instance, if there's only one negative number, it's always better to pick three positives (if available) or two positives and a zero. If there are no positive numbers, the three largest (closest to zero) negative numbers will yield the maximum product (e.g., `[-5, -4, -3]` -> `-6`). Sorting the array allows us to easily access these critical "extreme" values (smallest and largest) and compare the only two possible candidates for the maximum product.

---
<sub>Generated 2026-07-26 04:08 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
