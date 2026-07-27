# [1464] Maximum Product of Two Elements in an Array

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-07-27 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/)

**Topics:** Array, Sorting, Heap (Priority Queue)

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example 1:

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

Example 3:

Input: nums = [3,7]
Output: 12

Constraints:

- 2 <= nums.length <= 500

- 1 <= nums[i] <= 10^3

**Examples / sample tests:**

```
[3,4,5,2]
[1,5,4,5]
[3,7]
```

---

## Problem Summary
Given an array of integers, we need to select two distinct numbers. Our goal is to maximize the product of these two numbers after subtracting 1 from each of them.

## Intuition
We want to maximize the expression `(nums[i]-1) * (nums[j]-1)`. Since all `nums[k]` are at least 1, `nums[k]-1` will always be non-negative (greater than or equal to 0). To maximize the product of two non-negative numbers, we should choose the **largest possible factors**. This means we should pick the **two largest numbers** from the `nums` array.

## Approach
The most efficient way to find the two largest numbers in an array is to iterate through it once, keeping track of the largest and second largest numbers seen so far.

1.  **Initialize `max1` and `max2`**: Set two variables, `max1` and `max2`, to 0. `max1` will store the largest number found, and `max2` will store the second largest. We can initialize them to 0 because all numbers in `nums` are at least 1, so any `nums[i]` will be greater than 0.
2.  **Iterate through `nums`**: For each `num` in the input array `nums`:
    *   **If `num` is greater than `max1`**: This means we've found a new largest number. The old `max1` now becomes the new `max2`, and `num` becomes the new `max1`.
        *   `max2 = max1`
        *   `max1 = num`
    *   **Else if `num` is greater than `max2` (but not `max1`)**: This means `num` is not the largest, but it's larger than our current second largest.
        *   `max2 = num`
3.  **Calculate Result**: After iterating through all numbers, `max1` will hold the largest number in the array, and `max2` will hold the second largest. Return `(max1 - 1) * (max2 - 1)`.

## Visualization

Let's trace the process with `nums = [3, 4, 5, 2]`:

```
nums: [3, 4, 5, 2]
       ^
       |
       Current num

Initial: max1 = 0, max2 = 0

Iteration 1 (num = 3):
  Is 3 > max1 (0)? Yes.
  max2 becomes 0 (old max1)
  max1 becomes 3 (current num)
  State: max1 = 3, max2 = 0

Iteration 2 (num = 4):
  Is 4 > max1 (3)? Yes.
  max2 becomes 3 (old max1)
  max1 becomes 4 (current num)
  State: max1 = 4, max2 = 3

Iteration 3 (num = 5):
  Is 5 > max1 (4)? Yes.
  max2 becomes 4 (old max1)
  max1 becomes 5 (current num)
  State: max1 = 5, max2 = 4

Iteration 4 (num = 2):
  Is 2 > max1 (5)? No.
  Is 2 > max2 (4)? No.
  State: max1 = 5, max2 = 4

End of loop.
Final max1 = 5, max2 = 4.
Result: (5 - 1) * (4 - 1) = 4 * 3 = 12
```

## Dry Run

Let's walk through Example 1: `nums = [3, 4, 5, 2]`

| Step | `num` | `max1` (before) | `max2` (before) | Condition (`num > max1`?) | Condition (`num > max2`?) | `max1` (after) | `max2` (after) |
| :--- | :---- | :-------------- | :-------------- | :------------------------ | :------------------------ | :------------- | :------------- |
| Init | -     | 0               | 0               | -                         | -                         | 0              | 0              |
| 1    | 3     | 0               | 0               | `3 > 0` (True)            | -                         | 3              | 0              |
| 2    | 4     | 3               | 0               | `4 > 3` (True)            | -                         | 4              | 3              |
| 3    | 5     | 4               | 3               | `5 > 4` (True)            | -                         | 5              | 4              |
| 4    | 2     | 5               | 4               | `2 > 5` (False)           | `2 > 4` (False)           | 5              | 4              |

**Final Result**: After the loop, `max1 = 5` and `max2 = 4`. The maximum product is `(max1 - 1) * (max2 - 1) = (5 - 1) * (4 - 1) = 4 * 3 = 12`.

## Complexity

*   **Time Complexity**: O(N) because we iterate through the `nums` array exactly once, where N is the number of elements in `nums`.
*   **Space Complexity**: O(1) because we only use a constant amount of extra space for variables like `max1` and `max2`, regardless of the input array size.

## Edge Cases

*   **Smallest array size (`nums.length = 2`)**: E.g., `nums = [3, 7]`.
    *   `max1=0, max2=0`
    *   `num=3`: `max1=3, max2=0`
    *   `num=7`: `max1=7, max2=3`
    *   Result: `(7-1)*(3-1) = 6*2 = 12`. The solution correctly identifies the two elements and calculates the product.
*   **Duplicate largest numbers**: E.g., `nums = [1, 5, 4, 5]`.
    *   `max1=0, max2=0`
    *   `num=1`: `max1=1, max2=0`
    *   `num=5`: `max1=5, max2=1`
    *   `num=4`: `max1=5, max2=4` (since `4 > 1`)
    *   `num=5`: `5` is not `> max1` (5). But `5` *is* `> max2` (4). So `max2=5`.
    *   Result: `(5-1)*(5-1) = 4*4 = 16`. This correctly handles duplicates, as the problem asks for two *different indices*, not necessarily different values.
*   **All numbers are 1**: E.g., `nums = [1, 1, 1]`.
    *   `max1=0, max2=0`
    *   `num=1`: `max1=1, max2=0`
    *   `num=1`: `max1=1, max2=1` (since `1 > 0`)
    *   `num=1`: No change.
    *   Result: `(1-1)*(1-1) = 0*0 = 0`. This is correct.

## Solution

```python
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize max1 and max2 to keep track of the two largest numbers.
        # Since nums[i] >= 1, initializing to 0 is safe as any num will be greater.
        max1 = 0  # Stores the largest number found so far
        max2 = 0  # Stores the second largest number found so far

        for num in nums:
            if num > max1:
                # If current num is greater than the current largest (max1),
                # then max1 becomes the new second largest (max2),
                # and num becomes the new largest (max1).
                max2 = max1
                max1 = num
            elif num > max2:
                # If current num is not greater than max1, but is greater than max2,
                # then num becomes the new second largest (max2).
                max2 = num
        
        # After iterating through all numbers, max1 and max2 hold the two largest.
        # Calculate and return the product (max1 - 1) * (max2 - 1).
        return (max1 - 1) * (max2 - 1)

```

## Why This Works

This approach works because the problem asks us to maximize `(nums[i]-1) * (nums[j]-1)`. Since all `nums[k] >= 1`, it means `nums[k]-1 >= 0`. When multiplying two non-negative numbers, their product is maximized when both factors are as large as possible. Therefore, we need to find the two largest numbers in the array. The single-pass algorithm efficiently identifies these two largest numbers (`max1` and `max2`) by comparing each element against the current largest and second largest, ensuring that `max1` always holds the absolute largest and `max2` holds the second largest (or a duplicate of `max1` if there are multiple occurrences of the largest value).

---
<sub>Generated 2026-07-27 04:24 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
