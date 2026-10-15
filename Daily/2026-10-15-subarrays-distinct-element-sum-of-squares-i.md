# [2913] Subarrays Distinct Element Sum of Squares I

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-10-15 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/)

**Topics:** Array, Hash Table, Binary Indexed Tree, Segment Tree

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

- Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].

Return the sum of the squares of distinct counts of all subarrays of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 1^2 + 1^2 + 1^2 + 2^2 + 2^2 + 2^2 = 15.

Example 2:

Input: nums = [1,1]
Output: 3
Explanation: Three possible subarrays are:
[1]: 1 distinct value
[1]: 1 distinct value
[1,1]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 1^2 + 1^2 + 1^2 = 3.

Constraints:

- 1 <= nums.length <= 100

- 1 <= nums[i] <= 100

**Examples / sample tests:**

```
[1,2,1]
[1,1]
```

---

## Problem Summary
The task is to calculate the total sum of squares of distinct element counts for all possible contiguous subarrays within a given integer array `nums`. For each subarray, we find how many unique numbers it contains, square that count, and add it to a running total.

## Intuition
The problem asks us to consider *every single possible subarray*. Whenever we need to process all subarrays, a common and straightforward approach involves **nested loops**: one loop to pick the **starting point** (`i`) of a subarray, and another inner loop to pick its **ending point** (`j`).

For each subarray `nums[i...j]` identified by these loops, we then need to find its **distinct count**. A `set` data structure is perfectly suited for this, as it only stores unique elements. As we extend the subarray from `nums[i...i]` to `nums[i...j]`, we can incrementally add elements to a `set` and its size will always give us the distinct count for the current subarray.

Given the small constraint `nums.length <= 100`, an `O(N^2)` approach (where `N` is the length of `nums`) will be efficient enough.

## Approach
We will use a nested loop structure to iterate through all possible subarrays and a `set` to efficiently track distinct elements for each subarray.

1.  Initialize a variable `total_sum_of_squares` to `0`. This will store our final result.
2.  Start an **outer loop** that iterates with an index `i` from `0` to `len(nums) - 1`. This `i` represents the **starting index** of a subarray.
3.  Inside the outer loop, for each `i`, initialize an empty `set` called `current_distinct_elements`. This set will keep track of distinct elements for the subarray starting at `i` and ending at the current `j`.
4.  Start an **inner loop** that iterates with an index `j` from `i` to `len(nums) - 1`. This `j` represents the **ending index** of the current subarray `nums[i...j]`.
5.  Inside the inner loop, for each `j`:
    *   Add the element `nums[j]` to the `current_distinct_elements` set. Since it's a set, duplicate additions have no effect on its size.
    *   Calculate the `distinct_count` for the current subarray `nums[i...j]` by getting the size of the `current_distinct_elements` set (i.e., `len(current_distinct_elements)`).
    *   Add the square of this `distinct_count` (`distinct_count ** 2`) to `total_sum_of_squares`.
6.  After both loops complete, `total_sum_of_squares` will hold the sum of squares of distinct counts for all subarrays. Return this value.

## Visualization

Let's trace `nums = [1, 2, 1]` with the nested loops and the `current_distinct_elements` set.

```
nums = [1, 2, 1]
total_sum_of_squares = 0

Outer loop (i):
  i = 0 (Subarrays starting at index 0):
    current_distinct_elements = {}

    Inner loop (j):
      j = 0:
        Add nums[0] (1) to set.
        current_distinct_elements = {1}
        Distinct count = 1
        total_sum_of_squares += 1^2  (total = 1)
        Subarray: [1]
        
      j = 1:
        Add nums[1] (2) to set.
        current_distinct_elements = {1, 2}
        Distinct count = 2
        total_sum_of_squares += 2^2  (total = 1 + 4 = 5)
        Subarray: [1, 2]

      j = 2:
        Add nums[2] (1) to set. (Set remains {1, 2} as 1 is already present)
        current_distinct_elements = {1, 2}
        Distinct count = 2
        total_sum_of_squares += 2^2  (total = 5 + 4 = 9)
        Subarray: [1, 2, 1]

  i = 1 (Subarrays starting at index 1):
    current_distinct_elements = {}  (reset for new 'i')

    Inner loop (j):
      j = 1:
        Add nums[1] (2) to set.
        current_distinct_elements = {2}
        Distinct count = 1
        total_sum_of_squares += 1^2  (total = 9 + 1 = 10)
        Subarray: [2]

      j = 2:
        Add nums[2] (1) to set.
        current_distinct_elements = {2, 1}
        Distinct count = 2
        total_sum_of_squares += 2^2  (total = 10 + 4 = 14)
        Subarray: [2, 1]

  i = 2 (Subarrays starting at index 2):
    current_distinct_elements = {}  (reset for new 'i')

    Inner loop (j):
      j = 2:
        Add nums[2] (1) to set.
        current_distinct_elements = {1}
        Distinct count = 1
        total_sum_of_squares += 1^2  (total = 14 + 1 = 15)
        Subarray: [1]

Final total_sum_of_squares = 15
```

## Dry Run
Let's trace Example 1: `nums = [1,2,1]`

| `i` | `j` | `nums[j]` | `current_distinct_elements` | `distinct_count` | `distinct_count^2` | `total_sum_of_squares` |
| :-- | :-- | :-------- | :-------------------------- | :--------------- | :----------------- | :--------------------- |
|     |     |           |                             |                  |                    | **0**                  |
| **0** |     |           |                             |                  |                    |                        |
|     | 0   | 1         | `{1}`                       | 1                | 1                  | 0 + 1 = **1**          |
|     | 1   | 2         | `{1, 2}`                    | 2                | 4                  | 1 + 4 = **5**          |
|     | 2   | 1         | `{1, 2}`                    | 2                | 4                  | 5 + 4 = **9**          |
| **1** |     |           |                             |                  |                    |                        |
|     | 1   | 2         | `{2}`                       | 1                | 1                  | 9 + 1 = **10**         |
|     | 2   | 1         | `{2, 1}`                    | 2                | 4                  | 10 + 4 = **14**        |
| **2** |     |           |                             |                  |                    |                        |
|     | 2   | 1         | `{1}`                       | 1                | 1                  | 14 + 1 = **15**        |

The final `total_sum_of_squares` is **15**, which matches the example output.

## Complexity
*   **Time Complexity**: `O(N^2)`. The outer loop runs `N` times, and the inner loop runs up to `N` times. Inside the inner loop, adding an element to a hash set (`set.add()`) and getting its length (`len(set)`) are both `O(1)` operations on average. Thus, the total time complexity is `N * N * O(1) = O(N^2)`. Given `N <= 100`, `N^2 = 100^2 = 10,000` operations, which is very fast.
*   **Space Complexity**: `O(N)`. In the worst case, the `current_distinct_elements` set might store all `N` elements if they are all distinct.

## Edge Cases
*   **`nums.length = 1`**: E.g., `nums = [5]`. The loops will correctly identify one subarray `[5]`, its distinct count is 1, `1^2 = 1`. The total sum will be 1. The solution handles this correctly.
*   **All elements are the same**: E.g., `nums = [1,1,1]`. For any subarray `[1]`, `[1,1]`, or `[1,1,1]`, the distinct count will always be 1. The sum will be `1^2` for each of the `N*(N+1)/2` subarrays. The solution correctly calculates this.
*   **All elements are distinct**: E.g., `nums = [1,2,3]`. The distinct count for `nums[i...j]` will be `j - i + 1`. The solution correctly calculates this by adding each new unique element to the set.

## Solution

```python
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum_of_squares = 0
        n = len(nums)

        # The outer loop iterates through all possible starting indices 'i'
        # for a subarray.
        for i in range(n):
            # For each starting index 'i', we need a fresh set to track
            # distinct elements for subarrays that begin at 'i'.
            current_distinct_elements = set()
            
            # The inner loop iterates through all possible ending indices 'j'
            # for a subarray, where 'j' is always greater than or equal to 'i'.
            for j in range(i, n):
                # Add the current element nums[j] to our set.
                # Sets automatically handle uniqueness; adding an existing element
                # has no effect on the set's size.
                current_distinct_elements.add(nums[j])
                
                # The distinct count for the subarray nums[i...j] is simply
                # the number of elements in our set.
                distinct_count = len(current_distinct_elements)
                
                # Add the square of this distinct count to our running total.
                total_sum_of_squares += distinct_count ** 2
                
        return total_sum_of_squares

```

## Why This Works
This approach works because it systematically generates and processes **every single possible contiguous subarray** of the input array `nums`. The nested loops (`i` for start, `j` for end) guarantee that no subarray is missed. For each subarray `nums[i...j]`, the `set` data structure efficiently maintains an accurate count of its unique elements. Since `set` operations (add, check size) are very fast on average, and the array length `N` is small (`<= 100`), this `O(N^2)` method is both correct and highly efficient enough to pass within typical time limits.

---
<sub>Generated 2026-10-15 05:04 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
