# [2091] Removing Minimum and Maximum From Array

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-08-30 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/)

**Topics:** Array, Greedy

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 0-indexed array of distinct integers nums.

There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.

A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.

Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.

Example 1:

Input: nums = [2,10,7,5,4,1,8,6]
Output: 5
Explanation:
The minimum element in the array is nums[5], which is 1.
The maximum element in the array is nums[1], which is 10.
We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
This results in 2 + 3 = 5 deletions, which is the minimum number possible.

Example 2:

Input: nums = [0,-4,19,1,8,-2,-3,5]
Output: 3
Explanation:
The minimum element in the array is nums[1], which is -4.
The maximum element in the array is nums[2], which is 19.
We can remove both the minimum and maximum by removing 3 elements from the front.
This results in only 3 deletions, which is the minimum number possible.

Example 3:

Input: nums = [101]
Output: 1
Explanation:
There is only one element in the array, which makes it both the minimum and maximum element.
We can remove it with 1 deletion.

Constraints:

- 1 <= nums.length <= 10^5

- -10^5 <= nums[i] <= 10^5

- The integers in nums are distinct.

**Examples / sample tests:**

```
[2,10,7,5,4,1,8,6]
[0,-4,19,1,8,-2,-3,5]
[101]
```

---

## Problem Summary
You are given an array of distinct integers. Your goal is to remove both the minimum and maximum elements from this array. You can only perform deletions from either the front or the back of the array. The task is to find the **minimum total number of deletions** required to achieve this.

## Intuition
The core idea revolves around the fact that we need to remove two specific elements: the minimum and the maximum. Since deletions can only happen from the ends of the array, we have a limited set of strategies. To remove an element at a certain index `i`, we must remove all elements between that end and `i`.

Consider the positions of the minimum and maximum elements. Let's say the array has `N` elements.
*   To remove an element at index `idx` from the **front**, we must delete `idx + 1` elements (indices `0` through `idx`).
*   To remove an element at index `idx` from the **back**, we must delete `N - idx` elements (indices `idx` through `N-1`).

Since we need to remove *both* the minimum and maximum, there are only three fundamental ways to do this:
1.  **Remove both from the front**: Delete elements from the front until both the minimum and maximum are gone.
2.  **Remove both from the back**: Delete elements from the back until both the minimum and maximum are gone.
3.  **Remove one from the front and the other from the back**: Delete the element closer to the front from the front, and the element closer to the back from the back.

Our strategy will be to calculate the number of deletions for each of these three scenarios and then pick the smallest one.

## Approach
1.  **Find Minimum and Maximum Indices**: First, iterate through the `nums` array to find the actual minimum value, maximum value, and their respective 0-indexed positions (`min_idx` and `max_idx`).

2.  **Calculate Deletions for Scenario 1 (Both from Front)**:
    *   To remove both elements by only deleting from the front, we must delete all elements up to and including the one that is **further from the front**.
    *   The number of deletions will be `max(min_idx, max_idx) + 1`.

3.  **Calculate Deletions for Scenario 2 (Both from Back)**:
    *   To remove both elements by only deleting from the back, we must delete all elements from the back up to and including the one that is **further from the back**.
    *   The element further from the back is the one with the **smaller index** (`min(min_idx, max_idx)`).
    *   The number of deletions will be `N - min(min_idx, max_idx)`. (If we remove elements from `min(min_idx, max_idx)` to `N-1`, that's `N - min(min_idx, max_idx)` elements).

4.  **Calculate Deletions for Scenario 3 (One from Front, One from Back)**:
    *   In this scenario, we remove the element that is **closer to the front** by deleting from the front.
    *   We remove the element that is **closer to the back** by deleting from the back.
    *   The element closer to the front is at index `min(min_idx, max_idx)`. Deletions from front: `min(min_idx, max_idx) + 1`.
    *   The element closer to the back is at index `max(min_idx, max_idx)`. Deletions from back: `N - max(min_idx, max_idx)`.
    *   The total deletions for this scenario will be `(min(min_idx, max_idx) + 1) + (N - max(min_idx, max_idx))`.

5.  **Return Minimum**: The final answer is the minimum of the three calculated deletion counts.

## Visualization

Let `N` be the length of the array.
Let `min_idx` be the index of the minimum element.
Let `max_idx` be the index of the maximum element.

```
Array: [ E0, E1, E2, ..., E_min, ..., E_max, ..., E_(N-1) ]
Indices:  0   1   2   ... min_idx ... max_idx ... (N-1)
```

**Scenario 1: Both from Front**
```
                    <------------------- Deletions from Front
Array: [ E0, E1, ..., E_min, ..., E_max, ..., E_(N-1) ]
Indices:  0   1   ... min_idx ... max_idx ... (N-1)
Goal: Remove all elements up to max(min_idx, max_idx).
Deletions = max(min_idx, max_idx) + 1
```

**Scenario 2: Both from Back**
```
Deletions from Back ------------------->
Array: [ E0, E1, ..., E_min, ..., E_max, ..., E_(N-1) ]
Indices:  0   1   ... min_idx ... max_idx ... (N-1)
Goal: Remove all elements from min(min_idx, max_idx) to N-1.
Deletions = N - min(min_idx, max_idx)
```

**Scenario 3: One from Front, One from Back**
```
                    <--- Deletions from Front (to remove element closer to front)
Array: [ E0, E1, ..., E_min, ..., E_max, ..., E_(N-1) ]
Indices:  0   1   ... min_idx ... max_idx ... (N-1)
                                       Deletions from Back ---> (to remove element closer to back)
Goal: Remove min(min_idx, max_idx) from front, and max(min_idx, max_idx) from back.
Deletions = (min(min_idx, max_idx) + 1) + (N - max(min_idx, max_idx))
```

## Dry Run
Let's walk through **Example 1**: `nums = [2,10,7,5,4,1,8,6]`

1.  **Initialization**:
    *   `N = 8`
    *   `min_val = infinity`, `max_val = -infinity`
    *   `min_idx = -1`, `max_idx = -1`

2.  **Find Min/Max and Indices**:
    | `i` | `nums[i]` | `min_val` | `min_idx` | `max_val` | `max_idx` |
    | :-- | :-------- | :-------- | :-------- | :-------- | :-------- |
    | 0   | 2         | 2         | 0         | 2         | 0         |
    | 1   | 10        | 2         | 0         | 10        | 1         |
    | 2   | 7         | 2         | 0         | 10        | 1         |
    | 3   | 5         | 2         | 0         | 10        | 1         |
    | 4   | 4         | 2         | 0         | 10        | 1         |
    | 5   | 1         | 1         | 5         | 10        | 1         |
    | 6   | 8         | 1         | 5         | 10        | 1         |
    | 7   | 6         | 1         | 5         | 10        | 1         |

    After loop: `min_idx = 5`, `max_idx = 1`.

3.  **Calculate Deletions**:
    *   `idx_closer_to_front = min(min_idx, max_idx) = min(5, 1) = 1`
    *   `idx_closer_to_back = max(min_idx, max_idx) = max(5, 1) = 5`

    *   **Scenario 1: Both from Front**
        `deletions_front_only = idx_closer_to_back + 1 = 5 + 1 = 6`

    *   **Scenario 2: Both from Back**
        `deletions_back_only = N - idx_closer_to_front = 8 - 1 = 7`

    *   **Scenario 3: One from Front, One from Back**
        `deletions_both_ends = (idx_closer_to_front + 1) + (N - idx_closer_to_back)`
        `deletions_both_ends = (1 + 1) + (8 - 5) = 2 + 3 = 5`

4.  **Final Result**:
    `min(deletions_front_only, deletions_back_only, deletions_both_ends)`
    `min(6, 7, 5) = 5`

The minimum number of deletions is **5**.

## Complexity
*   **Time Complexity**: O(N)
    *   We iterate through the array once to find the minimum and maximum elements and their indices. All subsequent calculations are constant time operations.
*   **Space Complexity**: O(1)
    *   We only use a few variables to store the array length, min/max values, their indices, and the results of the three scenarios. This is constant extra space.

## Edge Cases
*   **`nums.length = 1`**: `nums = [101]`
    *   `N = 1`. `min_idx = 0`, `max_idx = 0`.
    *   `deletions_front_only = max(0,0) + 1 = 1`.
    *   `deletions_back_only = 1 - min(0,0) = 1`.
    *   `deletions_both_ends = (min(0,0)+1) + (1-max(0,0)) = (0+1) + (1-0) = 1 + 1 = 2`.
    *   `min(1, 1, 2) = 1`. Correct. The solution handles this correctly, even though an explicit `if n == 1: return 1` check can be added for clarity.

*   **Min and Max at opposite ends**: `nums = [1, 5, 3, 2, 10]`
    *   `N = 5`. `min_idx = 0`, `max_idx = 4`.
    *   `deletions_front_only = max(0,4) + 1 = 5`.
    *   `deletions_back_only = 5 - min(0,4) = 5 - 0 = 5`.
    *   `deletions_both_ends = (min(0,4)+1) + (5-max(0,4)) = (0+1) + (5-4) = 1 + 1 = 2`.
    *   `min(5, 5, 2) = 2`. Correct (remove 1 from front, 10 from back).

*   **Min and Max adjacent**: `nums = [10, 1, 5, 3, 2]`
    *   `N = 5`. `min_idx = 1`, `max_idx = 0`.
    *   `deletions_front_only = max(1,0) + 1 = 2`.
    *   `deletions_back_only = 5 - min(1,0) = 5 - 0 = 5`.
    *   `deletions_both_ends = (min(1,0)+1) + (5-max(1,0)) = (0+1) + (5-1) = 1 + 4 = 5`.
    *   `min(2, 5, 5) = 2`. Correct (remove 10, then 1 from front).

## Solution
```python
from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        # Handle the trivial case where there's only one element
        # It's both min and max, and takes 1 deletion.
        if n == 1:
            return 1

        # Step 1: Find the minimum and maximum values and their 0-indexed positions.
        # Initialize with extreme values to ensure first element updates them.
        min_val = float('inf')
        max_val = float('-inf')
        min_idx = -1
        max_idx = -1

        for i in range(n):
            if nums[i] < min_val:
                min_val = nums[i]
                min_idx = i
            if nums[i] > max_val:
                max_val = nums[i]
                max_idx = i

        # For easier calculation, let's define the indices of the two elements
        # that are closer to the front and closer to the back.
        # 'idx_closer_to_front' is the smaller of min_idx and max_idx.
        # 'idx_closer_to_back' is the larger of min_idx and max_idx.
        idx_closer_to_front = min(min_idx, max_idx)
        idx_closer_to_back = max(min_idx, max_idx)

        # Scenario 1: Remove both elements by deleting only from the front.
        # We need to remove all elements up to and including the one further from the front.
        # This is (index of element further from front) + 1.
        deletions_front_only = idx_closer_to_back + 1

        # Scenario 2: Remove both elements by deleting only from the back.
        # We need to remove all elements from the back up to and including the one further from the back.
        # The element further from the back is the one closer to the front (smaller index).
        # This is N - (index of element closer to front).
        deletions_back_only = n - idx_closer_to_front

        # Scenario 3: Remove one element from the front and the other from the back.
        # Remove the element closer to the front from the front: (idx_closer_to_front + 1) deletions.
        # Remove the element closer to the back from the back: (N - idx_closer_to_back) deletions.
        deletions_both_ends = (idx_closer_to_front + 1) + (n - idx_closer_to_back)

        # The minimum deletions is the best of these three scenarios.
        return min(deletions_front_only, deletions_back_only, deletions_both_ends)

```

## Why This Works
This approach works because the three scenarios cover all possible optimal ways to remove two elements from the ends of an array. Any strategy that removes both the minimum and maximum elements must involve either:
1.  Removing a contiguous block from the front that includes both.
2.  Removing a contiguous block from the back that includes both.
3.  Removing a block from the front to get one element, and a block from the back to get the other.
There are no other configurations of deletions that could achieve the goal with fewer moves, as each deletion removes an element from an end, and we are always aiming to remove the minimum necessary elements to reach our targets. By calculating the cost for each of these exhaustive possibilities and taking the minimum, we guarantee finding the optimal solution.

---
<sub>Generated 2026-08-30 05:42 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
