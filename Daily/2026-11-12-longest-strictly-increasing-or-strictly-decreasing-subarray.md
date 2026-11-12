# [3105] Longest Strictly Increasing or Strictly Decreasing Subarray

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-11-12 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/)

**Topics:** Array

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

Example 1:

Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.

Example 2:

Input: nums = [3,3,3,3]

Output: 1

Explanation:

The strictly increasing subarrays of nums are [3], [3], [3], and [3].

The strictly decreasing subarrays of nums are [3], [3], [3], and [3].

Hence, we return 1.

Example 3:

Input: nums = [3,2,1]

Output: 3

Explanation:

The strictly increasing subarrays of nums are [3], [2], and [1].

The strictly decreasing subarrays of nums are [3], [2], [1], [3,2], [2,1], and [3,2,1].

Hence, we return 3.

Constraints:

- 1 <= nums.length <= 50

- 1 <= nums[i] <= 50

**Examples / sample tests:**

```
[1,4,3,3,2]
[3,3,3,3]
[3,2,1]
```

---

## Problem Summary
Given an array of integers, find the longest contiguous subarray that is either **strictly increasing** (each element is greater than the previous) or **strictly decreasing** (each element is less than the previous). A single element is considered both strictly increasing and strictly decreasing.

## Intuition
When looking for the "longest contiguous subarray" with a certain property, a common and efficient approach is to use a **single pass** through the array. We can maintain counters for the current length of strictly increasing and strictly decreasing subarrays as we iterate. If the pattern breaks, we reset the relevant counter. We continuously update a global maximum length with the longest sequence found so far.

## Approach
We will iterate through the array once, keeping track of the lengths of the current strictly increasing and strictly decreasing subarrays.

1.  **Initialization**:
    *   Initialize `max_length` to 1, as any single element forms a valid subarray of length 1.
    *   Initialize `current_increasing_length` to 1.
    *   Initialize `current_decreasing_length` to 1.
    *   If the array has 0 or 1 element, `max_length` will correctly be 0 or 1, respectively. (Given constraints, `nums.length >= 1`, so `max_length` will always be at least 1).

2.  **Iteration**:
    *   Iterate from the second element of the array (`i = 1`) up to the end.
    *   For each `nums[i]`, compare it with the previous element `nums[i-1]`:
        *   **If `nums[i] > nums[i-1]`**: The strictly increasing sequence continues. Increment `current_increasing_length`. The strictly decreasing sequence is broken, so reset `current_decreasing_length` to 1 (for the current element `nums[i]` itself).
        *   **If `nums[i] < nums[i-1]`**: The strictly decreasing sequence continues. Increment `current_decreasing_length`. The strictly increasing sequence is broken, so reset `current_increasing_length` to 1.
        *   **If `nums[i] == nums[i-1]`**: Both strictly increasing and strictly decreasing sequences are broken because strict monotonicity requires elements to be *different*. Reset both `current_increasing_length` and `current_decreasing_length` to 1.

3.  **Update Maximum**:
    *   After each comparison and counter update, update `max_length` by taking the maximum of its current value, `current_increasing_length`, and `current_decreasing_length`.

4.  **Return**:
    *   After the loop finishes, `max_length` will hold the length of the longest strictly increasing or strictly decreasing subarray. Return `max_length`.

## Visualization
Let's trace the process with `nums = [1,4,3,3,2]`.

```
Array: [1, 4, 3, 3, 2]
Index:  0  1  2  3  4

Initial:
max_length = 1
current_increasing_length = 1
current_decreasing_length = 1

Iteration 1: i = 1, nums[1] = 4, nums[0] = 1
  nums[1] (4) > nums[0] (1)
  -> current_increasing_length becomes 1 + 1 = 2
  -> current_decreasing_length resets to 1
  max_length = max(1, 2, 1) = 2

Iteration 2: i = 2, nums[2] = 3, nums[1] = 4
  nums[2] (3) < nums[1] (4)
  -> current_decreasing_length becomes 1 + 1 = 2
  -> current_increasing_length resets to 1
  max_length = max(2, 1, 2) = 2

Iteration 3: i = 3, nums[3] = 3, nums[2] = 3
  nums[3] (3) == nums[2] (3)
  -> current_increasing_length resets to 1
  -> current_decreasing_length resets to 1
  max_length = max(2, 1, 1) = 2

Iteration 4: i = 4, nums[4] = 2, nums[3] = 3
  nums[4] (2) < nums[3] (3)
  -> current_decreasing_length becomes 1 + 1 = 2
  -> current_increasing_length resets to 1
  max_length = max(2, 1, 2) = 2

End of loop.
Final max_length = 2
```

## Dry Run
Let's walk through Example 1: `nums = [1,4,3,3,2]`

| `i` | `nums[i]` | `nums[i-1]` | Comparison | `current_inc` | `current_dec` | `max_length` | Notes                                    |
| :-- | :-------- | :---------- | :--------- | :------------ | :------------ | :----------- | :--------------------------------------- |
| -   | -         | -           | -          | 1             | 1             | 1            | Initial state (for `nums[0]`)            |
| 1   | 4         | 1           | `4 > 1`    | 2             | 1             | 2            | `[1,4]` is increasing. `max(1,2,1)=2`    |
| 2   | 3         | 4           | `3 < 4`    | 1             | 2             | 2            | `[4,3]` is decreasing. `max(2,1,2)=2`    |
| 3   | 3         | 3           | `3 == 3`   | 1             | 1             | 2            | `[3,3]` breaks both. `max(2,1,1)=2`      |
| 4   | 2         | 3           | `2 < 3`    | 1             | 2             | 2            | `[3,2]` is decreasing. `max(2,1,2)=2`    |

Final Result: `max_length = 2`.

## Complexity
*   **Time Complexity**: O(N) because we iterate through the array exactly once, performing constant-time operations in each step.
*   **Space Complexity**: O(1) because we only use a few constant extra variables to store lengths and the maximum.

## Edge Cases
*   **`nums.length = 1`**: E.g., `nums = [5]`.
    *   `max_length` is initialized to 1. The loop `range(1, 1)` does not run. The function correctly returns 1.
*   **All elements are the same**: E.g., `nums = [3,3,3,3]`.
    *   `current_increasing_length` and `current_decreasing_length` will continuously reset to 1. `max_length` will remain 1. Correct.
*   **Strictly increasing array**: E.g., `nums = [1,2,3,4,5]`.
    *   `current_increasing_length` will increment up to `n`, while `current_decreasing_length` will always be 1. `max_length` will correctly become `n`.
*   **Strictly decreasing array**: E.g., `nums = [5,4,3,2,1]`.
    *   `current_decreasing_length` will increment up to `n`, while `current_increasing_length` will always be 1. `max_length` will correctly become `n`.

## Solution
```python
from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # If the array has 0 or 1 element, the longest subarray is the array itself.
        # Constraints state 1 <= nums.length, so n will always be at least 1.
        if n <= 1:
            return n

        # Initialize max_length to 1, as any single element is a valid subarray.
        max_length = 1
        
        # current_increasing_length tracks the length of the current strictly increasing subarray.
        current_increasing_length = 1
        # current_decreasing_length tracks the length of the current strictly decreasing subarray.
        current_decreasing_length = 1

        # Iterate from the second element to compare with the previous one.
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                # If current element is greater, the increasing sequence continues.
                current_increasing_length += 1
                # The decreasing sequence is broken, so reset its length to 1 (for current element).
                current_decreasing_length = 1
            elif nums[i] < nums[i-1]:
                # If current element is smaller, the decreasing sequence continues.
                current_decreasing_length += 1
                # The increasing sequence is broken, so reset its length to 1.
                current_increasing_length = 1
            else: # nums[i] == nums[i-1]
                # If current element is equal, both strictly increasing and strictly decreasing
                # sequences are broken. Reset both lengths to 1.
                current_increasing_length = 1
                current_decreasing_length = 1
            
            # Update the overall maximum length found so far.
            # We take the max of the current max_length and the lengths of the two current sequences.
            max_length = max(max_length, current_increasing_length, current_decreasing_length)
            
        return max_length

```

## Why This Works
This approach works because it correctly identifies and tracks the lengths of all possible strictly increasing and strictly decreasing subarrays in a single pass. By iterating through the array and comparing each element with its predecessor, we can determine if the current element extends an existing monotonic sequence or starts a new one. The `max_length` variable acts as an accumulator, always storing the maximum length encountered across both types of sequences up to the current point. Since every element is considered and its contribution to potential monotonic subarrays is evaluated, the final `max_length` is guaranteed to be the global maximum.

---
<sub>Generated 2026-11-12 07:36 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
