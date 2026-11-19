# [2567] Minimum Score by Changing Two Elements

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-11-19 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-score-by-changing-two-elements/)

**Topics:** Array, Greedy, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums.

- The low score of nums is the minimum absolute difference between any two integers.

- The high score of nums is the maximum absolute difference between any two integers.

- The score of nums is the sum of the high and low scores.

Return the minimum score after changing two elements of nums.

Example 1:

Input: nums = [1,4,7,8,5]

Output: 3

Explanation:

- Change nums[0] and nums[1] to be 6 so that nums becomes [6,6,7,8,5].

- The low score is the minimum absolute difference: |6 - 6| = 0.

- The high score is the maximum absolute difference: |8 - 5| = 3.

- The sum of high and low score is 3.

Example 2:

Input: nums = [1,4,3]

Output: 0

Explanation:

- Change nums[1] and nums[2] to 1 so that nums becomes [1,1,1].

- The sum of maximum absolute difference and minimum absolute difference is 0.

Constraints:

- 3 <= nums.length <= 10^5

- 1 <= nums[i] <= 10^9

**Examples / sample tests:**

```
[1,4,7,8,5]
[1,4,3]
```

---

## Problem Summary
The goal is to find the minimum possible "score" of an array after changing any two of its elements. The score is defined as the sum of the array's high score (maximum absolute difference between any two elements) and low score (minimum absolute difference between any two elements).

## Intuition
Let's break down the score: `Score = (High Score) + (Low Score)`.
*   **Low Score**: The minimum absolute difference between any two integers in the array.
*   **High Score**: The maximum absolute difference between any two integers in the array.

We are allowed to change *two* elements.
1.  **Minimizing the Low Score**: If we change two elements, say `nums[i]` and `nums[j]`, we can make them equal to any value `X`. For instance, we can change `nums[i]` and `nums[j]` to `nums[k]` (an existing element) or even a new value. If we make `nums[i] = nums[j] = X`, then the absolute difference `|nums[i] - nums[j]|` becomes `|X - X| = 0`. Since we *must* change two elements, we can always achieve a low score of `0`. This is the absolute minimum possible for the low score.
2.  **Minimizing the High Score**: Since we can always make the low score `0`, our entire problem simplifies to minimizing only the **high score** (`max_val - min_val`) after changing two elements.
3.  **Strategy to minimize `max_val - min_val`**: To make the range `max_val - min_val` as small as possible, we should target the extreme values of the array. We have two changes we can make.
    *   To increase the effective minimum, we should change the smallest element(s).
    *   To decrease the effective maximum, we should change the largest element(s).
    *   First, **sort the array**. This makes it easy to identify the smallest elements (`nums[0], nums[1], ...`) and largest elements (`nums[N-1], nums[N-2], ...`).
    *   With two changes, there are three primary ways to affect the overall minimum and maximum of the array to shrink the range:
        *   **Change the two smallest elements**: This effectively "removes" `nums[0]` and `nums[1]` from consideration for being the minimum. The new minimum would be `nums[2]`.
        *   **Change the two largest elements**: This effectively "removes" `nums[N-1]` and `nums[N-2]` from consideration for being the maximum. The new maximum would be `nums[N-3]`.
        *   **Change the smallest and the largest elements**: This effectively "removes" `nums[0]` and `nums[N-1]`. The new minimum would be `nums[1]`, and the new maximum would be `nums[N-2]`.
    *   Any other combination of changes (e.g., changing `nums[0]` and `nums[5]`) would result in a range that is either worse or equal to one of these three scenarios. For example, changing `nums[0]` and `nums[5]` would make `nums[1]` the new minimum and `nums[N-1]` the new maximum, leading to `nums[N-1] - nums[1]`. This range is larger than `nums[N-1] - nums[2]` (Scenario 1) if `nums[1] < nums[2]`. The optimal strategy is always to remove elements from the extremes.
    *   Therefore, we calculate the range (`max_val - min_val`) for these three scenarios and take the minimum among them.

## Approach
1.  **Sort the array**: Sort `nums` in non-decreasing order. This allows us to easily access the smallest elements at the beginning and the largest elements at the end. Let `N` be the length of `nums`.
2.  **Simplify the problem**: Recognize that by changing two elements, we can always make the low score `0` (by making the two changed elements equal). Thus, the problem reduces to minimizing only the **high score** (`max_val - min_val`) after making two changes.
3.  **Consider three scenarios for changes**:
    *   **Scenario 1: Change the two smallest elements.**
        *   We change `nums[0]` and `nums[1]`.
        *   The new effective minimum of the array becomes `nums[2]`.
        *   The maximum element remains `nums[N-1]`.
        *   The range for this scenario is `nums[N-1] - nums[2]`.
    *   **Scenario 2: Change the two largest elements.**
        *   We change `nums[N-1]` and `nums[N-2]`.
        *   The new effective maximum of the array becomes `nums[N-3]`.
        *   The minimum element remains `nums[0]`.
        *   The range for this scenario is `nums[N-3] - nums[0]`.
    *   **Scenario 3: Change the smallest and the largest elements.**
        *   We change `nums[0]` and `nums[N-1]`.
        *   The new effective minimum of the array becomes `nums[1]`.
        *   The new effective maximum of the array becomes `nums[N-2]`.
        *   The range for this scenario is `nums[N-2] - nums[1]`.
4.  **Return the minimum**: The final answer is the minimum value among the three ranges calculated in step 3.

## Visualization

Let's visualize the sorted array `nums` and how the effective minimum and maximum elements shift for each scenario. `N` is the length of the array.

```
Original Sorted Array:
Indices:   0    1    2    ...   N-3   N-2   N-1
Values:  [n0,  n1,  n2,  ...   n(N-3), n(N-2), n(N-1)]
           ^min                                 ^max
           
Scenario 1: Change n0 and n1 (two smallest)
           [n0,  n1,  n2,  ...   n(N-3), n(N-2), n(N-1)]
            ^changed^  ^new_min                     ^max
           Effective range: n(N-1) - n2

Scenario 2: Change n(N-1) and n(N-2) (two largest)
           [n0,  n1,  n2,  ...   n(N-3), n(N-2), n(N-1)]
            ^min                     ^new_max  ^changed^
           Effective range: n(N-3) - n0

Scenario 3: Change n0 and n(N-1) (smallest and largest)
           [n0,  n1,  n2,  ...   n(N-3), n(N-2), n(N-1)]
            ^changed   ^new_min   ^new_max   ^changed
           Effective range: n(N-2) - n1
```

## Dry Run
Let's use Example 1: `nums = [1,4,7,8,5]`

1.  **Sort the array**:
    `nums` becomes `[1, 4, 5, 7, 8]`
    `N = 5`

2.  **Calculate ranges for the three scenarios**:

    *   **Scenario 1: Change `nums[0]` and `nums[1]` (1 and 4).**
        *   New effective minimum: `nums[2]` which is `5`.
        *   Maximum: `nums[N-1]` (`nums[4]`) which is `8`.
        *   Range: `8 - 5 = 3`.

    *   **Scenario 2: Change `nums[N-1]` and `nums[N-2]` (8 and 7).**
        *   Minimum: `nums[0]` which is `1`.
        *   New effective maximum: `nums[N-3]` (`nums[2]`) which is `5`.
        *   Range: `5 - 1 = 4`.

    *   **Scenario 3: Change `nums[0]` and `nums[N-1]` (1 and 8).**
        *   New effective minimum: `nums[1]` which is `4`.
        *   New effective maximum: `nums[N-2]` (`nums[3]`) which is `7`.
        *   Range: `7 - 4 = 3`.

3.  **Find the minimum of these ranges**:
    `min(3, 4, 3) = 3`.

The final result is `3`.

## Complexity
*   **Time Complexity**: `O(N log N)`
    *   This is dominated by the `nums.sort()` operation, where `N` is the length of the `nums` array. The subsequent calculations are constant time `O(1)`.
*   **Space Complexity**: `O(N)` or `O(log N)`
    *   Python's `list.sort()` (Timsort) typically uses `O(N)` auxiliary space in the worst case, but `O(log N)` in the average case for its merge operations. If the sort is done in-place without significant auxiliary space, it could be considered `O(1)` auxiliary space. For competitive programming, `O(N)` is a safe assumption for Python's sort.

## Edge Cases
*   **`nums.length = 3`**: The minimum allowed length.
    *   Example: `nums = [1, 4, 3]`
    *   Sorted: `[1, 3, 4]` (`N=3`)
    *   Scenario 1: `nums[2] - nums[2] = 4 - 4 = 0`
    *   Scenario 2: `nums[0] - nums[0] = 1 - 1 = 0`
    *   Scenario 3: `nums[1] - nums[1] = 3 - 3 = 0`
    *   Result: `min(0, 0, 0) = 0`. This is correct, as we can change two elements (e.g., 1 and 4 to 3) to make all elements equal, resulting in a score of 0. The solution handles this naturally.
*   **All elements are the same**: `nums = [5, 5, 5, 5]`
    *   Sorted: `[5, 5, 5, 5]` (`N=4`)
    *   Scenario 1: `nums[3] - nums[2] = 5 - 5 = 0`
    *   Scenario 2: `nums[1] - nums[0] = 5 - 5 = 0`
    *   Scenario 3: `nums[2] - nums[1] = 5 - 5 = 0`
    *   Result: `min(0, 0, 0) = 0`. Correct, as the score is already 0.
*   **Large values**: `nums[i]` up to `10^9`.
    *   The differences can also be large, but Python's integers handle arbitrary size, so no overflow issues. The logic remains sound.

## Solution

```python
from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Sort the array to easily access the smallest and largest elements.
        # This is crucial for identifying the effective min/max after changes.
        nums.sort()

        # The problem asks to minimize (high_score + low_score).
        # We can always make the low_score 0 by changing two elements to be equal.
        # For example, change nums[i] and nums[j] to nums[k]. Then |nums[k]-nums[k]| = 0.
        # So, the problem simplifies to minimizing only the high_score (max_val - min_val)
        # after making two changes.

        # There are three optimal ways to use two changes to minimize the range (max - min):

        # Option 1: Change the two smallest elements (nums[0] and nums[1]).
        # The new effective minimum of the array becomes nums[2].
        # The maximum element remains nums[n-1].
        # The range is (nums[n-1] - nums[2]).
        range_option1 = nums[n-1] - nums[2]

        # Option 2: Change the two largest elements (nums[n-1] and nums[n-2]).
        # The new effective maximum of the array becomes nums[n-3].
        # The minimum element remains nums[0].
        # The range is (nums[n-3] - nums[0]).
        range_option2 = nums[n-3] - nums[0]

        # Option 3: Change the smallest (nums[0]) and the largest (nums[n-1]) elements.
        # The new effective minimum of the array becomes nums[1].
        # The new effective maximum of the array becomes nums[n-2].
        # The range is (nums[n-2] - nums[1]).
        range_option3 = nums[n-2] - nums[1]

        # The minimum score will be the minimum of these three calculated ranges.
        return min(range_option1, range_option2, range_option3)

```

## Why This Works
This approach works because we can always make the "low score" zero by changing two elements to be the same value. This simplifies the problem to minimizing only the "high score" (the range `max_val - min_val`) using two changes. By sorting the array, we can efficiently identify the current smallest and largest elements. The three scenarios cover all optimal ways to use two changes to shrink the array's range: removing the two smallest, removing the two largest, or removing one smallest and one largest. Any other combination of changes would either result in a larger range or be equivalent to one of these three cases. Taking the minimum of these three ranges guarantees the overall minimum possible high score.

---
<sub>Generated 2026-11-19 07:49 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
