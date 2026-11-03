# [3736] Minimum Moves to Equal Array Elements III

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-11-03 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/)

**Topics:** Array, Math

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums.

In one move, you may increase the value of any single element nums[i] by 1.

Return the minimum total number of moves required so that all elements in nums become equal.

Example 1:

Input: nums = [2,1,3]

Output: 3

Explanation:

To make all elements equal:

- Increase nums[0] = 2 by 1 to make it 3.

- Increase nums[1] = 1 by 1 to make it 2.

- Increase nums[1] = 2 by 1 to make it 3.

Now, all elements of nums are equal to 3. The minimum total moves is 3.

Example 2:

Input: nums = [4,4,5]

Output: 2

Explanation:

To make all elements equal:

- Increase nums[0] = 4 by 1 to make it 5.

- Increase nums[1] = 4 by 1 to make it 5.

Now, all elements of nums are equal to 5. The minimum total moves is 2.

Constraints:

- 1 <= nums.length <= 100

- 1 <= nums[i] <= 100

**Examples / sample tests:**

```
[2,1,3]
[4,4,5]
```

---

## Problem Summary
You are given an array of integers. In one move, you can increase any single element by 1. The goal is to find the minimum total number of moves required to make all elements in the array equal.

## Intuition
We can only **increase** elements. This is a crucial constraint. If we want all elements to become equal to some target value `T`, then for each `nums[i]`, we must perform `T - nums[i]` moves. Since we can only increase elements, `T` must be greater than or equal to every `nums[i]`. This means `T` must be at least the **maximum value** currently present in the array.

To minimize the total number of moves, `sum(T - nums[i])`, we need to choose the smallest possible `T`. The smallest possible `T` that satisfies `T >= max(nums)` is exactly `max(nums)`. Therefore, the optimal strategy is to bring all elements up to the current maximum value in the array.

## Approach
1. **Find the maximum value:** Iterate through the `nums` array to find its maximum element. Let's call this `max_val`.
2. **Calculate total moves:** Initialize a `total_moves` counter to 0.
3. **Sum differences:** Iterate through `nums` again. For each `num` in the array, calculate the difference `max_val - num`. This difference represents the number of moves needed to bring that specific `num` up to `max_val`. Add this difference to `total_moves`.
4. **Return result:** After iterating through all elements, `total_moves` will hold the minimum total moves required.

## Visualization
Let's visualize the process with `nums = [2, 1, 3]`.
The maximum value in the array is `3`. Our goal is to make all elements `3`.

```
Original Array:
[2] [1] [3]
 ^   ^   ^
 |   |   |
 |   |   +-- Already 3 (0 moves)
 |   +------ Needs 3 - 1 = 2 moves
 +---------- Needs 3 - 2 = 1 move

Moves for each element:
nums[0] = 2  ->  3 (1 move)
nums[1] = 1  ->  3 (2 moves)
nums[2] = 3  ->  3 (0 moves)

Total Moves = 1 + 2 + 0 = 3
```

## Dry Run
Let's walk through Example 1: `nums = [2,1,3]`

| Step | `nums` | `max_val` (found) | `num` (current) | `moves_for_num` (`max_val - num`) | `total_moves` |
| :--- | :----- | :---------------- | :-------------- | :-------------------------------- | :------------ |
| 1.   | `[2,1,3]` | `3`               | -               | -                                 | `0`           |
| 2.   | -      | `3`               | `2`             | `3 - 2 = 1`                       | `0 + 1 = 1`   |
| 3.   | -      | `3`               | `1`             | `3 - 1 = 2`                       | `1 + 2 = 3`   |
| 4.   | -      | `3`               | `3`             | `3 - 3 = 0`                       | `3 + 0 = 3`   |
| **Final** | -      | -                 | -               | -                                 | `3`           |

The final result is `3`, which matches the example output.

## Complexity
*   **Time Complexity:** O(N)
    *   Finding the maximum element takes O(N) time.
    *   Iterating through the array to sum the differences also takes O(N) time.
    *   Overall, the time complexity is dominated by these two linear passes.
*   **Space Complexity:** O(1)
    *   We only use a few extra variables (`max_val`, `total_moves`) regardless of the input array size.

## Edge Cases
*   **Single element array:** `nums = [5]`. `max_val = 5`. `total_moves = (5 - 5) = 0`. Correct, no moves needed.
*   **All elements already equal:** `nums = [7,7,7]`. `max_val = 7`. `total_moves = (7-7) + (7-7) + (7-7) = 0`. Correct, no moves needed.
*   **Smallest possible values:** `nums = [1,1,2]`. `max_val = 2`. `total_moves = (2-1) + (2-1) + (2-2) = 1 + 1 + 0 = 2`. Correct.
*   **Largest possible values:** `nums = [100, 99, 100]`. `max_val = 100`. `total_moves = (100-100) + (100-99) + (100-100) = 0 + 1 + 0 = 1`. Correct.

## Solution

```python
from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Step 1: Find the maximum element in the array.
        # This will be our target value, as we can only increase elements.
        # All other elements must be increased to match this maximum.
        max_val = max(nums)
        
        total_moves = 0
        
        # Step 2 & 3: Iterate through each number in the array
        # and sum the moves needed for each.
        for num in nums:
            # The number of moves needed for this specific element 'num'
            # is the difference between the target (max_val) and its current value.
            total_moves += (max_val - num)
            
        # Step 4: Return the accumulated total moves.
        return total_moves

```

## Why This Works
The core reason this approach works is that we are only allowed to **increase** elements. This means the final common value `T` that all elements become equal to *must* be greater than or equal to every initial `nums[i]`. Consequently, `T` must be at least `max(nums)`. To minimize the total moves, which is `sum(T - nums[i])`, we need to choose the smallest possible `T`. The smallest possible `T` is `max(nums)` itself. Any `T` larger than `max(nums)` would require `(T - max(nums))` additional moves for *every* element, thus increasing the total sum unnecessarily.

---
<sub>Generated 2026-11-03 07:09 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
