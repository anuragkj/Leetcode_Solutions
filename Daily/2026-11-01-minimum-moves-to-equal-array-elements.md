# [453] Minimum Moves to Equal Array Elements

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-11-01 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/)

**Topics:** Array, Math

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

Example 1:

Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

Example 2:

Input: nums = [1,1,1]
Output: 0

Constraints:

- n == nums.length

- 1 <= nums.length <= 10^5

- -10^9 <= nums[i] <= 10^9

- The answer is guaranteed to fit in a 32-bit integer.

**Examples / sample tests:**

```
[1,2,3]
[1,1,1]
```

---

## Problem Summary
Given an array of integers, find the minimum number of moves required to make all elements equal. In one move, you can increment `n-1` elements of the array by 1.

## Intuition
This problem seems tricky because the operation "increment `n-1` elements" is not straightforward to track. Let's try to reframe it.

Consider the effect of one move:
- We have `n` elements.
- We pick `n-1` elements and add `1` to each.
- The *one* element not picked remains unchanged.

This operation is mathematically equivalent to **decrementing the single remaining element by 1**.
Let's verify this with an example:
- Original array: `[a, b, c]`
- **Operation 1 (original problem):** Increment `a` and `b`. The array becomes `[a+1, b+1, c]`.
- **Operation 2 (transformed idea):** Decrement `c`. The array becomes `[a, b, c-1]`.

Now, let's look at the *differences* between elements, which is what matters for them to become equal:
- For `[a+1, b+1, c]`: Differences are `(a+1)-c`, `(b+1)-c`, `(b+1)-(a+1) = b-a`.
- For `[a, b, c-1]`: Differences are `a-(c-1)`, `b-(c-1)`, `b-a`.
Notice that `a-(c-1) = a-c+1 = (a+1)-c`. Similarly for `b`. The relative differences between elements are preserved!

So, the problem can be rephrased as: **"What is the minimum number of moves to make all array elements equal, where in one move you can decrement any single element by 1?"**

If we can only decrement elements, and we want them all to be equal, what's the target value? We cannot decrement any element below the **minimum element** in the original array. Therefore, the final equal value must be `min(nums)`.
For each element `num_i` in the array, we need to decrement it `num_i - min(nums)` times to reach `min(nums)`. The total number of moves will simply be the sum of these individual decrements.

## Approach
1.  **Find the minimum element**: Iterate through the `nums` array to find its smallest value. Store this in a variable, say `min_val`.
2.  **Calculate total moves**: Initialize a `moves` counter to `0`.
3.  **Sum differences**: Iterate through the `nums` array again. For each `num` in `nums`, calculate the difference `(num - min_val)` and add this value to `moves`.
4.  **Return result**: The final value of `moves` is the minimum number of operations required.

## Visualization

Let's visualize `nums = [1, 2, 3]` with `min_val = 1`.
Our goal is to make all elements equal to `1` by "decrementing" them.

```
Original Array: [1, 2, 3]
Minimum Value:   ^
                 1

Target for all elements: 1

Element 1:  1  ->  1   (Needs 1 - 1 = 0 decrements)
Element 2:  2  ->  1   (Needs 2 - 1 = 1 decrement)
Element 3:  3  ->  1   (Needs 3 - 1 = 2 decrements)
             ^      ^
             |      |
             |      Total decrements for this element
             Original value

Total Moves = (1-1) + (2-1) + (3-1) = 0 + 1 + 2 = 3
```

## Dry Run

Let's trace Example 1: `nums = [1, 2, 3]`

| Step | `nums` | `min_val` | `num` | `num - min_val` | `moves` | Notes                               |
| :--- | :----- | :-------- | :---- | :-------------- | :------ | :---------------------------------- |
| 1    | `[1,2,3]`| -         | -     | -               | `0`     | Initialize `moves`                  |
| 2    | `[1,2,3]`| `1`       | -     | -               | `0`     | Find `min_val = min([1,2,3])`       |
| 3    | `[1,2,3]`| `1`       | `1`   | `1 - 1 = 0`     | `0`     | First element: `moves += 0`         |
| 4    | `[1,2,3]`| `1`       | `2`   | `2 - 1 = 1`     | `1`     | Second element: `moves += 1`        |
| 5    | `[1,2,3]`| `1`       | `3`   | `3 - 1 = 2`     | `3`     | Third element: `moves += 2`         |
| 6    | -        | -         | -     | -               | `3`     | All elements processed. Return `moves`. |

Final Result: `3`

## Complexity

*   **Time Complexity**: **O(N)**.
    We iterate through the array once to find the minimum element (Python's `min()` takes O(N) time) and then iterate through it again to sum the differences (another O(N) pass). Thus, the total time complexity is linear with respect to the number of elements `N` in the array.
*   **Space Complexity**: **O(1)**.
    We only use a few constant extra variables to store `min_val` and `moves`, regardless of the input array size.

## Edge Cases

*   **`n = 1` (single element array)**: `nums = [5]`. `min_val = 5`. `moves = (5 - 5) = 0`. This is correct, as no moves are needed if there's only one element.
*   **All elements are already equal**: `nums = [1, 1, 1]`. `min_val = 1`. `moves = (1-1) + (1-1) + (1-1) = 0`. This is correct, as no moves are needed if all elements are already equal.
*   **Large numbers / large `n`**: The constraints state `n` up to `10^5` and `nums[i]` up to `10^9`. The sum `sum(num_i - min_val)` can potentially be large. For example, if `nums = [1, 2, ..., 10^5]`, `min_val = 1`, and `moves = sum(i-1 for i in range(1, 10^5+1))` which is approximately `5 * 10^9`. While this would exceed a 32-bit signed integer, Python's integers handle arbitrary size, so overflow is not an issue in Python. The problem guarantees the answer fits in a 32-bit integer, implying test cases will not produce results exceeding this limit.

## Solution

```python
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # Step 1: Find the minimum element in the array.
        # This value will be the target for all elements in our transformed problem
        # (where we "decrement" elements).
        min_val = min(nums)
        
        # Step 2: Initialize a counter for the total number of moves.
        moves = 0
        
        # Step 3: Iterate through each element in the array.
        # For each element, calculate the difference between it and the minimum value.
        # This difference represents the number of "decrements" needed for that element,
        # which directly corresponds to the number of "moves" in the original problem.
        for num in nums:
            moves += (num - min_val)
            
        # Step 4: Return the total calculated moves.
        return moves

```

## Why This Works

The solution is correct because of a fundamental equivalence: **incrementing `n-1` elements by 1 is exactly the same as decrementing 1 element by 1, relative to the other elements.** This transformation simplifies the problem significantly. If we can only decrement elements, and our goal is to make them all equal, the only possible target value is the initial minimum element of the array. Any other target value (either lower or higher) would either be impossible to reach (if lower than `min(nums)`) or would require more total "decrements" (if higher than `min(nums)`), thus more moves. By summing `(num - min_val)` for each element, we calculate the exact total number of "decrements" needed, which directly translates to the minimum number of moves in the original problem.

---
<sub>Generated 2026-11-01 06:42 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
