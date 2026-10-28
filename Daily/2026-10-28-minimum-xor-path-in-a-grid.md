# [3882] Minimum XOR Path in a Grid

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-10-28 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-xor-path-in-a-grid/)

**Topics:** Array, Dynamic Programming, Bit Manipulation, Matrix

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 2D integer array grid of size m * n.

You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).

At each step, you may move either right or down.

The cost of a path is defined as the bitwise XOR of all the values in the cells along that path, including the start and end cells.

Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).

Example 1:

Input: grid = [[1,2],[3,4]]

Output: 6

Explanation:

There are two valid paths:

- (0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7

- (0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6

The minimum XOR value among all valid paths is 6.

Example 2:

Input: grid = [[6,7],[5,8]]

Output: 9

Explanation:

There are two valid paths:

- (0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9

- (0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11

The minimum XOR value among all valid paths is 9.

Example 3:

Input: grid = [[2,7,5]]

Output: 0

Explanation:

There is only one valid path:

- (0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0

The XOR value of this path is 0, which is the minimum possible.

Constraints:

- 1 <= m == grid.length <= 1000

- 1 <= n == grid[i].length <= 1000

- m * n <= 1000

- 0 <= grid[i][j] <= 1023​

**Examples / sample tests:**

```
[[1,2],[3,4]]
[[6,7],[5,8]]
[[2,7,5]]
```

---

## Problem Summary
You are given a grid of numbers and need to find a path from the top-left cell to the bottom-right cell. You can only move right or down. The "cost" of a path is the bitwise XOR sum of all numbers in the cells along that path. The goal is to find the **minimum possible XOR sum** among all such valid paths.

## Intuition
This problem asks for a minimum value over paths in a grid, which often suggests **Dynamic Programming (DP)**. A standard DP approach for path problems is `dp[i][j]` representing the minimum cost to reach cell `(i, j)`. However, here the "cost" is an XOR sum, which doesn't combine in a simple additive way for minimization (e.g., `min(XOR_A, XOR_B)` doesn't directly relate to `min(XOR_A ^ C, XOR_B ^ C)`).

The key observation is that the maximum value in any cell is `1023`, which is `2^10 - 1`. This means all numbers, and consequently all possible XOR sums, will fit within 10 bits (i.e., values from 0 to 1023). This small range of possible XOR values is crucial. Instead of storing *just* the minimum XOR sum at `dp[i][j]`, we can store **all possible XOR sums** that can lead to cell `(i, j)`.

So, our intuition leads to a DP state where `dp[i][j]` is a **set** of all unique XOR sums encountered on paths from `(0,0)` to `(i,j)`.

## Approach
1.  **Initialize DP Table:** Create a 2D DP table, `dp`, of the same dimensions as the `grid`. Each cell `dp[i][j]` will store a `set` of integers. These sets will hold all unique XOR sums possible to reach `(i, j)` from `(0, 0)`.

2.  **Base Case:** For the starting cell `(0, 0)`, the only path is just the cell itself. So, `dp[0][0]` will contain a set with a single element: `grid[0][0]`.

3.  **Iterate and Fill DP Table:** Iterate through the grid from `(0, 0)` to `(m-1, n-1)` (row by row, then column by column). For each cell `(i, j)`:
    *   Retrieve the `current_cell_value = grid[i][j]`.
    *   If `(i, j)` is `(0, 0)`, skip it as its base case is already handled.
    *   **From Above:** If `i > 0` (meaning `(i, j)` has a cell directly above it, `(i-1, j)`), iterate through every `prev_xor_sum` in `dp[i-1][j]`. For each `prev_xor_sum`, calculate a new XOR sum: `new_xor_sum = prev_xor_sum ^ current_cell_value`. Add this `new_xor_sum` to `dp[i][j]`.
    *   **From Left:** If `j > 0` (meaning `(i, j)` has a cell directly to its left, `(i, j-1)`), iterate through every `prev_xor_sum` in `dp[i][j-1]`. For each `prev_xor_sum`, calculate `new_xor_sum = prev_xor_sum ^ current_cell_value`. Add this `new_xor_sum` to `dp[i][j]`.

4.  **Final Result:** After filling the entire `dp` table, the set `dp[m-1][n-1]` will contain all possible XOR sums to reach the bottom-right cell. The minimum among these is our answer. Return `min(dp[m-1][n-1])`.

## Visualization

Let's visualize the DP table for `grid = [[1,2],[3,4]]`:

```
Grid:
+---+---+
| 1 | 2 |
+---+---+
| 3 | 4 |
+---+---+

DP Table (sets of XOR sums):

Initial:
dp = [ [ {}, {} ],
       [ {}, {} ] ]

1. Base Case: dp[0][0] = {1}
dp = [ [ {1}, {} ],
       [ {}, {} ] ]

2. Process (0,1) with value 2:
   Comes from dp[0][0] = {1}
   New XOR: 1 ^ 2 = 3
dp = [ [ {1}, {3} ],
       [ {}, {} ] ]

3. Process (1,0) with value 3:
   Comes from dp[0][0] = {1}
   New XOR: 1 ^ 3 = 2
dp = [ [ {1}, {3} ],
       [ {2}, {} ] ]

4. Process (1,1) with value 4:
   a. From dp[0][1] = {3} (above)
      New XOR: 3 ^ 4 = 7
      dp[1][1] = {7}
   b. From dp[1][0] = {2} (left)
      New XOR: 2 ^ 4 = 6
      dp[1][1] = {7, 6} (set union)

dp = [ [ {1}, {3} ],
       [ {2}, {7, 6} ] ]

Final Result: min(dp[1][1]) = min({7, 6}) = 6
```

## Dry Run
Let's walk through **Example 1: `grid = [[1,2],[3,4]]`**

`m = 2`, `n = 2`
Initialize `dp = [[set(), set()], [set(), set()]]`

1.  **Base Case:**
    `dp[0][0].add(grid[0][0])` -> `dp[0][0] = {1}`

2.  **Iterate `i` from 0 to 1, `j` from 0 to 1:**

    *   **`i = 0, j = 0`**: `current_cell_value = 1`. This is the starting cell, `continue`.
        `dp` state: `[[{1}, set()], [set(), set()]]`

    *   **`i = 0, j = 1`**: `current_cell_value = 2`.
        *   `i > 0` is `False`.
        *   `j > 0` is `True`. From `dp[0][0] = {1}`:
            *   `prev_xor_sum = 1`. `new_xor_sum = 1 ^ 2 = 3`.
            *   `dp[0][1].add(3)`
        `dp` state: `[[{1}, {3}], [set(), set()]]`

    *   **`i = 1, j = 0`**: `current_cell_value = 3`.
        *   `i > 0` is `True`. From `dp[0][0] = {1}`:
            *   `prev_xor_sum = 1`. `new_xor_sum = 1 ^ 3 = 2`.
            *   `dp[1][0].add(2)`
        *   `j > 0` is `False`.
        `dp` state: `[[{1}, {3}], [{2}, set()]]`

    *   **`i = 1, j = 1`**: `current_cell_value = 4`.
        *   `i > 0` is `True`. From `dp[0][1] = {3}`:
            *   `prev_xor_sum = 3`. `new_xor_sum = 3 ^ 4 = 7`.
            *   `dp[1][1].add(7)`
        *   `j > 0` is `True`. From `dp[1][0] = {2}`:
            *   `prev_xor_sum = 2`. `new_xor_sum = 2 ^ 4 = 6`.
            *   `dp[1][1].add(6)`
        `dp` state: `[[{1}, {3}], [{2}, {7, 6}]]`

3.  **Final Result:**
    The loop finishes. We return `min(dp[m-1][n-1])`, which is `min(dp[1][1])`.
    `min({7, 6}) = 6`.

The minimum possible XOR value is **6**.

## Complexity
*   **Time Complexity:** `O(m * n * MAX_XOR_VAL)`.
    *   We iterate through each of the `m * n` cells in the grid.
    *   For each cell `(i, j)`, we might iterate through the sets `dp[i-1][j]` and `dp[i][j-1]`.
    *   Since `grid[i][j] <= 1023`, the maximum possible XOR value is `1023`. Thus, each set `dp[i][j]` can contain at most `1024` distinct XOR values.
    *   Adding an element to a Python `set` takes `O(1)` on average.
    *   Therefore, processing each cell takes roughly `O(MAX_XOR_VAL)` time.
    *   Total time: `m * n * 1024`. Given `m * n <= 1000`, this is `1000 * 1024 = 1,024,000` operations, which is efficient enough.

*   **Space Complexity:** `O(m * n * MAX_XOR_VAL)`.
    *   The `dp` table stores `m * n` sets.
    *   Each set can store up to `MAX_XOR_VAL` integers.
    *   Total space: `m * n * 1024` integers. Given `m * n <= 1000`, this is `1000 * 1024` integers. If an integer takes 4 bytes, this is about `4MB`, which is well within typical memory limits.

## Edge Cases
*   **`m = 1, n = 1` (single cell grid):** The path is just the cell itself. The solution correctly initializes `dp[0][0]` with `grid[0][0]` and returns `min(dp[0][0])`, which is `grid[0][0]`.
*   **`m = 1` (single row grid):** The path only moves right. The `i > 0` condition will always be false, so only paths from the left (`j > 0`) are considered, correctly calculating the XOR sum across the row.
*   **`n = 1` (single column grid):** The path only moves down. The `j > 0` condition will always be false, so only paths from above (`i > 0`) are considered, correctly calculating the XOR sum down the column.
*   **`grid` contains `0`s:** XORing with `0` does not change the value (`X ^ 0 = X`). The logic handles this naturally, as `0` is just another integer value.
*   **All `grid` values are identical:** The XOR sums will still be correctly tracked. For example, `[[5,5],[5,5]]` will yield `5^5^5 = 5` and `5^5^5 = 5`, resulting in `5`.

## Solution

```python
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j] will store a set of all possible XOR sums to reach cell (i, j).
        # The maximum possible XOR value is 1023 (since grid[i][j] <= 1023),
        # so each set will contain at most 1024 distinct values.
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        # Base case: The XOR sum to reach the starting cell (0, 0) is just its value.
        dp[0][0].add(grid[0][0])
        
        # Fill the DP table
        for i in range(m):
            for j in range(n):
                current_cell_value = grid[i][j]
                
                # Skip the starting cell as its base case is already handled.
                if i == 0 and j == 0:
                    continue
                
                # If we can come from the cell directly above (i-1, j)
                if i > 0:
                    # For each XOR sum that reached (i-1, j),
                    # calculate a new XOR sum by including current_cell_value.
                    for prev_xor_sum in dp[i-1][j]:
                        dp[i][j].add(prev_xor_sum ^ current_cell_value)
                
                # If we can come from the cell directly to the left (i, j-1)
                if j > 0:
                    # For each XOR sum that reached (i, j-1),
                    # calculate a new XOR sum by including current_cell_value.
                    for prev_xor_sum in dp[i][j-1]:
                        dp[i][j].add(prev_xor_sum ^ current_cell_value)
                        
        # The minimum XOR value to reach the bottom-right cell (m-1, n-1)
        # is the minimum value in its set of possible XOR sums.
        return min(dp[m-1][n-1])

```

## Why This Works
This dynamic programming approach works because it systematically explores **all possible valid paths** from the start to every cell in the grid. By storing a **set of all unique XOR sums** at each cell `(i, j)`, we ensure that when we compute the possible XOR sums for `(i, j)`, we consider every valid path leading to `(i, j)` from `(0, 0)`. Since movement is restricted to only right or down, there are no cycles, and the state of `dp[i][j]` only depends on previously computed states `dp[i-1][j]` and `dp[i][j-1]`. The bitwise XOR operation is associative, meaning the order of operations does not affect the final result, so simply XORing the current cell's value with previous path sums correctly extends the path. Finally, by taking the minimum value from the set at the destination cell `(m-1, n-1)`, we guarantee that we find the overall minimum XOR sum among all valid paths.

---
<sub>Generated 2026-10-28 06:10 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
