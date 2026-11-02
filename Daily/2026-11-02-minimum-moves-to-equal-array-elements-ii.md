# [462] Minimum Moves to Equal Array Elements II

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-11-02 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/)

**Topics:** Array, Math, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Example 2:

Input: nums = [1,10,2,9]
Output: 16

Constraints:

- n == nums.length

- 1 <= nums.length <= 10^5

- -10^9 <= nums[i] <= 10^9

**Examples / sample tests:**

```
[1,2,3]
[1,10,2,9]
```

---

## Problem Summary
Given an array of integers, the goal is to make all elements equal by repeatedly incrementing or decrementing any single element by 1. We need to find the **minimum total number of moves** required to achieve this.

## Intuition
Let's say we want to make all elements equal to some target value `x`. For each number `num` in the array, the number of moves required to change it to `x` is `|num - x|`. Our problem then becomes finding an `x` that minimizes the **sum of absolute differences**: `sum(|num - x|)` for all `num` in the array.

Consider a few numbers on a number line. If we pick a target `x`, each number `num` needs `|num - x|` moves. This is simply the **distance** from `num` to `x`. We are looking for a point `x` that minimizes the sum of distances to all other points.

It's a well-known mathematical property that the value `x` which minimizes the sum of absolute differences to a set of points is the **median** of those points.
- If `x` is smaller than the median, moving `x` one step to the right will decrease the distance to more than half the numbers (those to its right) and increase the distance to less than half the numbers (those to its left), resulting in a net decrease in total moves.
- Similarly, if `x` is larger than the median, moving `x` one step to the left will decrease the total moves.
This process continues until `x` reaches the median, where any further move would increase the total sum of distances.

Therefore, the core idea is to find the median of the array and then calculate the sum of distances from each element to this median.

## Approach
1.  **Sort the array**: To find the median, the array `nums` must first be sorted in non-decreasing order.
2.  **Find the median**:
    *   Let `n` be the length of the sorted array.
    *   The median element will be at index `n // 2` (using 0-based indexing).
    *   If `n` is odd, `nums[n // 2]` is the unique median.
    *   If `n` is even, any value between `nums[n // 2 - 1]` and `nums[n // 2]` (inclusive) will minimize the sum of absolute differences. For simplicity and correctness, we can just pick `nums[n // 2]` as our target `x`.
3.  **Calculate total moves**: Initialize a `total_moves` counter to 0. Iterate through each `num` in the original (or sorted) array and add `abs(num - median)` to `total_moves`.
4.  **Return `total_moves`**: This sum represents the minimum number of moves.

## Visualization

Let's visualize the process with `nums = [1, 10, 2, 9]`.

1.  **Sort `nums`**: `[1, 2, 9, 10]`
2.  **Find Median**: `n = 4`. Median index `n // 2 = 2`. So, `median = nums[2] = 9`. (Alternatively, `nums[1] = 2` would also work, giving the same total moves).

Now, imagine these numbers on a number line and calculate the distance to our chosen median `9`:

```
Number Line:
-inf <----------------------------------------------------------------> +inf
       1     2           9     10

Elements:
nums[0] = 1
nums[1] = 2
nums[2] = 9
nums[3] = 10

Target (Median): 9

Moves for each element:
- From 1 to 9: |1 - 9| = 8 moves
  (1 <---------------------> 9)

- From 2 to 9: |2 - 9| = 7 moves
  (2 <------------------> 9)

- From 9 to 9: |9 - 9| = 0 moves
  (9 <---------> 9)

- From 10 to 9: |10 - 9| = 1 move
  (9 <---------> 10)

Total Moves = 8 + 7 + 0 + 1 = 16
```

## Dry Run

Let's walk through Example 1: `nums = [1, 2, 3]`

| Step | Action                               | `nums` (sorted) | `n` | `median_idx` | `median` | `current_num` | `abs(current_num - median)` | `total_moves` |
| :--- | :----------------------------------- | :-------------- | :-- | :----------- | :------- | :------------ | :-------------------------- | :------------ |
| 1    | Sort `nums`                          | `[1, 2, 3]`     | 3   |              |          |               |                             | 0             |
| 2    | Calculate `n`                        | `[1, 2, 3]`     | 3   |              |          |               |                             | 0             |
| 3    | Find median index `n // 2`           | `[1, 2, 3]`     | 3   | 1            |          |               |                             | 0             |
| 4    | Set `median = nums[median_idx]`      | `[1, 2, 3]`     | 3   | 1            | 2        |               |                             | 0             |
| 5    | Iterate: `num = 1`                   | `[1, 2, 3]`     | 3   | 1            | 2        | 1             | `abs(1 - 2) = 1`            | 1             |
| 6    | Iterate: `num = 2`                   | `[1, 2, 3]`     | 3   | 1            | 2        | 2             | `abs(2 - 2) = 0`            | 1             |
| 7    | Iterate: `num = 3`                   | `[1, 2, 3]`     | 3   | 1            | 2        | 3             | `abs(3 - 2) = 1`            | 2             |
| 8    | All elements processed, return `total_moves` | `[1, 2, 3]`     | 3   | 1            | 2        |               |                             | **2**         |

Final Result: `2`

## Complexity

*   **Time Complexity**: `O(N log N)`. This is dominated by the sorting step. Iterating through the array to sum the differences takes `O(N)` time.
*   **Space Complexity**: `O(N)` or `O(log N)`. Python's `list.sort()` (Timsort) uses `O(N)` auxiliary space in the worst case, but `O(log N)` in average case. If we consider it in-place, it could be `O(1)` for some sorting algorithms, but for Python's built-in sort, `O(N)` is a safer upper bound for auxiliary space.

## Edge Cases

*   **`n = 1` (single element array)**: `nums = [5]`.
    *   Sorted: `[5]`. `n = 1`. Median `nums[0] = 5`.
    *   Moves: `abs(5 - 5) = 0`. Correct, no moves needed if there's only one element.
*   **All elements are already equal**: `nums = [7, 7, 7]`.
    *   Sorted: `[7, 7, 7]`. `n = 3`. Median `nums[1] = 7`.
    *   Moves: `abs(7 - 7) + abs(7 - 7) + abs(7 - 7) = 0`. Correct, no moves needed.
*   **Negative numbers**: `nums = [-1, 0, 1]`.
    *   Sorted: `[-1, 0, 1]`. `n = 3`. Median `nums[1] = 0`.
    *   Moves: `abs(-1 - 0) + abs(0 - 0) + abs(1 - 0) = 1 + 0 + 1 = 2`. Correct.
*   **Large numbers**: The problem states the answer fits in a 32-bit integer. The sum of differences can be large, but `N` is up to `10^5` and `nums[i]` up to `10^9`. The maximum difference is `2 * 10^9`. `10^5 * 2 * 10^9 = 2 * 10^{14}`, which fits in a 64-bit integer (Python handles large integers automatically). The *result* (total moves) is guaranteed to fit in 32-bit, which is a helpful constraint.

## Solution

```python
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        # Step 1: Sort the array to easily find the median.
        nums.sort()
        
        n = len(nums)
        
        # Step 2: Determine the median.
        # The median is the value that minimizes the sum of absolute differences.
        # For a sorted array of length n, the median is at index n // 2.
        # If n is even, nums[n // 2] is the "upper" median. Any value between
        # nums[n // 2 - 1] and nums[n // 2] would also yield the minimum sum,
        # so picking one of them (like nums[n // 2]) is perfectly valid.
        median = nums[n // 2]
        
        # Step 3: Calculate the total number of moves.
        # This is the sum of absolute differences between each element and the median.
        total_moves = 0
        for num in nums:
            total_moves += abs(num - median)
            
        # Step 4: Return the calculated total moves.
        return total_moves

```

## Why This Works

The problem asks us to find a target value `x` such that the sum of absolute differences, `S = sum(|nums[i] - x|)` for all `i`, is minimized. This is a classic optimization problem. Mathematically, the function `S(x)` is minimized when `x` is the **median** of the set of numbers `nums`.

Intuitively, consider the numbers on a number line. If we pick a target `x` that is not the median, we can always move `x` one step closer to the median and reduce the total sum of distances. For example, if `x` is to the left of the median, moving `x` one unit to the right will decrease the distance to all numbers greater than `x` (which are more than half the numbers) and increase the distance to all numbers less than `x` (which are less than half the numbers). This results in a net decrease in the total sum of distances. This process continues until `x` reaches the median, where the number of elements to its left and right are balanced, and any further move would increase the total sum. Sorting the array allows us to easily find this median value.

---
<sub>Generated 2026-11-02 06:41 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
