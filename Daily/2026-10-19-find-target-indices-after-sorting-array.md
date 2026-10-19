# [2089] Find Target Indices After Sorting Array

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-10-19 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/find-target-indices-after-sorting-array/)

**Topics:** Array, Binary Search, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.

Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.

Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.

Constraints:

- 1 <= nums.length <= 100

- 1 <= nums[i], target <= 100

**Examples / sample tests:**

```
[1,2,5,2,3]
2
[1,2,5,2,3]
3
[1,2,5,2,3]
5
```

---

## Problem Summary
Given an array of integers `nums` and a `target` integer, the goal is to find all indices where the `target` element appears *after* `nums` has been sorted in non-decreasing order. The returned list of indices must also be sorted in increasing order.

## Intuition
The problem statement itself gives us the biggest hint: "Return a list of the target indices of nums **after sorting nums** in non-decreasing order." This directly tells us the first and most crucial step. Once the array is sorted, all occurrences of the `target` value will be grouped together. Finding their indices then becomes a straightforward scan.

## Approach
The most direct and efficient approach for this problem involves two main steps:

1.  **Sort the Array**: First, sort the input array `nums` in non-decreasing (ascending) order. This rearranges the elements so that all identical values, including our `target`, are placed next to each other.
2.  **Scan for Target Indices**: After sorting, iterate through the now-sorted array from the beginning to the end. For each element, check if it equals the `target`. If `nums[i] == target`, then `i` is a target index, and we add it to our result list. Since we iterate from left to right (index 0, then 1, then 2, etc.), the indices will naturally be added to our result list in increasing order.

Here are the concrete steps:

1.  Initialize an empty list called `target_indices` to store the results.
2.  Sort the input array `nums` in-place.
3.  Iterate through the sorted `nums` array using a `for` loop with an index `i` from `0` to `len(nums) - 1`.
4.  Inside the loop, if `nums[i]` is equal to `target`, append the current index `i` to the `target_indices` list.
5.  After the loop finishes, return the `target_indices` list.

## Visualization
Let's trace Example 1: `nums = [1,2,5,2,3]`, `target = 2`.

```mermaid
graph TD
    A[Original nums: [1, 2, 5, 2, 3]] --> B{Sort nums};
    B --> C[Sorted nums: [1, 2, 2, 3, 5]];
    C --> D{Iterate and find target = 2};

    subgraph Scan
        D --> E[i = 0, nums[0] = 1 != 2];
        E --> F[i = 1, nums[1] = 2 == 2 --> Add 1 to result];
        F --> G[i = 2, nums[2] = 2 == 2 --> Add 2 to result];
        G --> H[i = 3, nums[3] = 3 != 2];
        H --> I[i = 4, nums[4] = 5 != 2];
    end

    I --> J[End of array];
    J --> K[Result: [1, 2]];
```

## Dry Run
Let's use Example 1: `nums = [1,2,5,2,3]`, `target = 2`.

| Step | Action                               | Sorted `nums`     | Current `i` | `nums[i]` | `target` | `target_indices` |
| :--- | :----------------------------------- | :---------------- | :---------- | :-------- | :------- | :--------------- |
| 1    | Initial `nums`                       | `[1,2,5,2,3]`     | -           | -         | `2`      | `[]`             |
| 2    | Sort `nums`                          | `[1,2,2,3,5]`     | -           | -         | `2`      | `[]`             |
| 3    | Start iteration: `i = 0`             | `[1,2,2,3,5]`     | `0`         | `1`       | `2`      | `[]`             |
| 4    | `nums[0]` (`1`) != `target` (`2`)    | `[1,2,2,3,5]`     | `0`         | `1`       | `2`      | `[]`             |
| 5    | `i = 1`                              | `[1,2,2,3,5]`     | `1`         | `2`       | `2`      | `[]`             |
| 6    | `nums[1]` (`2`) == `target` (`2`)    | `[1,2,2,3,5]`     | `1`         | `2`       | `2`      | `[1]`            |
| 7    | `i = 2`                              | `[1,2,2,3,5]`     | `2`         | `2`       | `2`      | `[1]`            |
| 8    | `nums[2]` (`2`) == `target` (`2`)    | `[1,2,2,3,5]`     | `2`         | `2`       | `2`      | `[1, 2]`         |
| 9    | `i = 3`                              | `[1,2,2,3,5]`     | `3`         | `3`       | `2`      | `[1, 2]`         |
| 10   | `nums[3]` (`3`) != `target` (`2`)    | `[1,2,2,3,5]`     | `3`         | `3`       | `2`      | `[1, 2]`         |
| 11   | `i = 4`                              | `[1,2,2,3,5]`     | `4`         | `5`       | `2`      | `[1, 2]`         |
| 12   | `nums[4]` (`5`) != `target` (`2`)    | `[1,2,2,3,5]`     | `4`         | `5`       | `2`      | `[1, 2]`         |
| 13   | End of loop                          | `[1,2,2,3,5]`     | -           | -         | `2`      | `[1, 2]`         |
| 14   | Return `target_indices`              | `[1,2,2,3,5]`     | -           | -         | `2`      | `[1, 2]`         |

Final Result: `[1, 2]`

## Complexity
*   **Time Complexity**: O(N log N). The dominant operation is sorting the `nums` array, which typically takes O(N log N) time (e.g., Python's Timsort). The subsequent linear scan to find target indices takes O(N) time. Since O(N log N) is greater than O(N), the overall time complexity is O(N log N).
*   **Space Complexity**: O(N). Python's `list.sort()` (Timsort) can use up to O(N) auxiliary space in the worst case. Additionally, the `target_indices` list can store up to N indices if all elements in `nums` are equal to `target`.

## Edge Cases
*   **Target not present**: If `target` is not in `nums`, the `target_indices` list will remain empty throughout the iteration, and an empty list `[]` will be correctly returned.
*   **All elements are target**: If all elements in `nums` are equal to `target`, then all indices from `0` to `len(nums) - 1` will be added to `target_indices`, which is the correct behavior.
*   **`nums` has one element**: The sorting and scanning logic works correctly for single-element arrays.
*   **`nums` is already sorted**: Sorting an already sorted array still takes O(N log N) time but doesn't change its order, and the subsequent scan works as expected.

## Solution

```python
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # Step 1: Sort the array in non-decreasing order.
        # This ensures all occurrences of 'target' will be contiguous.
        nums.sort()
        
        # Step 2: Initialize an empty list to store the target indices.
        target_indices = []
        
        # Step 3: Iterate through the sorted array to find target elements.
        # We use enumerate or range(len(nums)) to get both index and value.
        for i in range(len(nums)):
            # Step 4: If the current element is equal to the target,
            # add its index to our result list.
            if nums[i] == target:
                target_indices.append(i)
                
        # Step 5: Return the list of target indices.
        # Since we iterated from 0 to len(nums)-1, the indices are naturally sorted.
        return target_indices

```

## Why This Works
This approach works because **sorting the array is the key operation** that simplifies the problem. Once `nums` is sorted in non-decreasing order, all instances of the `target` value will be grouped together. By iterating through this sorted array from index `0` to `len(nums) - 1`, we naturally find all occurrences of `target` and collect their indices in increasing order, fulfilling all requirements of the problem statement.

---
<sub>Generated 2026-10-19 05:10 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
