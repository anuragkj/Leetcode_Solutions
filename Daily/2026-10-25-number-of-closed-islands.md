# [1254] Number of Closed Islands

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-10-25 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/number-of-closed-islands/)

**Topics:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

Constraints:

- 1 <= grid.length, grid[0].length <= 100

- 0 <= grid[i][j] <=1

**Examples / sample tests:**

```
[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
[[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
[[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]
```

---

## Problem Summary
We are given a 2D grid representing a map, where `0`s are land and `1`s are water. An **island** is a group of `0`s connected 4-directionally. A **closed island** is an island that is completely surrounded by water (`1`s) on all sides, meaning no part of it touches the grid's boundaries (top, bottom, left, or right edges). Our goal is to count the total number of closed islands.

## Intuition
The problem asks us to count islands, which immediately suggests a **graph traversal algorithm** like Depth-First Search (DFS) or Breadth-First Search (BFS). The tricky part is the "closed" condition. An island is *not* closed if any of its land cells (`0`s) are on the edge of the grid, or if any of its land cells are connected to another land cell that is on the edge.

This observation gives us the key idea: **we can eliminate all non-closed islands first.** If an island touches the boundary, it's not closed. We can effectively "drown" these boundary-touching islands by changing their `0`s to `1`s. After this preprocessing step, any `0`s remaining in the grid *must* belong to closed islands. Then, we can simply count the remaining islands using a standard island-counting approach.

## Approach
We will use a two-phase approach involving Depth-First Search (DFS) to solve this problem.

1.  **Phase 1: Drown Boundary-Touching Islands**
    *   Iterate through all cells on the **boundary** of the grid (the first row, last row, first column, and last column).
    *   If we find a land cell (`0`) on the boundary, it means this land is part of an island that is *not* closed.
    *   From this boundary `0`, start a DFS traversal. During the DFS, change every `0` encountered (and all `0`s connected to it) to `1` (water). This effectively "drowns" the entire island connected to the boundary, removing it from consideration.

2.  **Phase 2: Count Remaining Closed Islands**
    *   After Phase 1, all `0`s that remain in the grid *must* belong to closed islands (because any `0` connected to the boundary would have been drowned).
    *   Now, iterate through the *entire* grid again.
    *   If we find a `0`, it signifies the start of a new **closed island**. Increment our `closed_islands_count`.
    *   From this `0`, start another DFS traversal. Again, change every `0` encountered (and all `0`s connected to it) to `1`. This marks the entire closed island as visited and prevents us from counting its parts multiple times.

3.  **Return `closed_islands_count`**.

**The DFS Helper Function:**
We'll use a single `dfs(r, c)` helper function:
*   **Base Cases:**
    *   If `(r, c)` is outside the grid boundaries, return.
    *   If `grid[r][c]` is `1` (water, or already visited/drowned), return.
*   **Action:**
    *   Change `grid[r][c]` to `1` (marking it as visited/drowned).
*   **Recursive Calls:**
    *   Recursively call `dfs` for all four neighbors: `(r+1, c)`, `(r-1, c)`, `(r, c+1)`, `(r, c-1)`.

## Visualization

Let's illustrate with a simplified grid.
`0` = Land, `1` = Water.

**Initial Grid:**
```
1 1 1 1 1
1 0 0 0 1
1 0 1 0 1
1 0 0 0 1
0 1 1 1 1  <- (4,0) is a boundary '0'
```

**Phase 1: Drown Boundary-Touching Islands**
*   We find `grid[4][0]` is `0` (land) and on the boundary.
*   Call `dfs(4,0)`.
    *   `dfs(4,0)` changes `grid[4][0]` to `1`. No other `0` neighbors.
*   No other `0`s on the boundary.

**Grid after Phase 1:**
```
1 1 1 1 1
1 0 0 0 1
1 0 1 0 1
1 0 0 0 1
1 1 1 1 1
```
Notice the `0` at `(4,0)` is now `1`.

**Phase 2: Count Remaining Closed Islands**
*   Initialize `closed_islands_count = 0`.
*   Iterate through the grid.
*   Find `grid[1][1]` is `0`.
    *   `closed_islands_count` becomes `1`.
    *   Call `dfs(1,1)`. This will change `grid[1][1], grid[1][2], grid[1][3], grid[2][1], grid[2][3], grid[3][1], grid[3][2], grid[3][3]` to `1`s.
    *   This entire connected component is now drowned.

**Grid after `dfs(1,1)`:**
```
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
```
*   Continue iterating. No more `0`s are found.

**Final Result:** `closed_islands_count = 1`.

## Dry Run
Let's walk through **Example 1**:
`grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]`
Dimensions: `R=5`, `C=8`

**Initial Grid:**
```
1 1 1 1 1 1 1 0  (0,7)
1 0 0 0 0 1 1 0  (1,7)
1 0 1 0 1 1 1 0  (2,7)
1 0 0 0 0 1 0 1
1 1 1 1 1 1 1 0  (4,7)
```

**Phase 1: Drowning Boundary-Touching Islands**
Iterate through boundary cells:
1.  `grid[0][7]` is `0`. Call `dfs(0,7)`.
    *   `dfs(0,7)` changes `grid[0][7]` to `1`. Explores neighbors.
    *   `dfs(1,7)` changes `grid[1][7]` to `1`. Explores neighbors.
    *   `dfs(2,7)` changes `grid[2][7]` to `1`. Explores neighbors.
    *   `dfs(3,7)` is `1` (water), so it stops.
    *   The chain `(0,7)-(1,7)-(2,7)` is drowned.
2.  `grid[4][7]` is `0`. Call `dfs(4,7)`.
    *   `dfs(4,7)` changes `grid[4][7]` to `1`. No `0` neighbors.
    *   This single `0` is drowned.

**Grid after Phase 1:**
```
1 1 1 1 1 1 1 1
1 0 0 0 0 1 1 1
1 0 1 0 1 1 1 1
1 0 0 0 0 1 0 1
1 1 1 1 1 1 1 1
```
All `0`s that were on the boundary or connected to the boundary are now `1`s.

**Phase 2: Counting Closed Islands**
`closed_islands_count = 0`
Iterate through the entire grid:
1.  `grid[1][1]` is `0`.
    *   `closed_islands_count` becomes `1`.
    *   Call `dfs(1,1)`. This DFS will explore and change all connected `0`s to `1`s.
    *   The island formed by `(1,1), (1,2), (1,3), (1,4), (2,1), (2,3), (3,1), (3,2), (3,3), (3,4)` is drowned.
    *   This is the first closed island.
2.  `grid[3][6]` is `0`.
    *   `closed_islands_count` becomes `2`.
    *   Call `dfs(3,6)`. This DFS changes `grid[3][6]` to `1`. No other `0` neighbors.
    *   This is the second closed island.
3.  Continue iterating. No more `0`s are found.

**Final Result:** `closed_islands_count = 2`. This matches Example 1 output.

## Complexity
*   **Time Complexity**: O(R * C), where R is the number of rows and C is the number of columns.
    *   In Phase 1, we iterate through all boundary cells (O(R+C)) and perform DFS. Each cell is visited and processed by DFS at most once.
    *   In Phase 2, we iterate through all cells (O(R*C)) and perform DFS for each unvisited land cell. Again, each cell is visited and processed by DFS at most once.
    *   Therefore, the total time complexity is proportional to the number of cells in the grid.
*   **Space Complexity**: O(R * C).
    *   The DFS recursion stack can go as deep as R * C in the worst case (e.g., a grid entirely filled with land).
    *   We modify the grid in-place, so no additional grid-sized data structure is used.

## Edge Cases
*   **Grid full of `1`s (water)**: The loops for finding `0`s won't trigger any DFS. `closed_islands_count` remains `0`. Correct.
*   **Grid full of `0`s (land)**: All `0`s are on the boundary. Phase 1 will drown every single `0`. Phase 2 will find no `0`s. `closed_islands_count` remains `0`. Correct, as no island can be closed if the entire grid is land.
*   **Single `0` in the middle, surrounded by `1`s**: `[[1,1,1],[1,0,1],[1,1,1]]`. Phase 1 finds no boundary `0`s. Phase 2 finds `grid[1][1]` as `0`, increments count to `1`, and drowns it. Result `1`. Correct.
*   **Single `0` on the boundary**: `[[0,1],[1,1]]`. Phase 1 finds `grid[0][0]` as `0` on boundary, drowns it. Phase 2 finds no `0`s. Result `0`. Correct.
*   **Smallest grid (1x1)**: `[[0]]` -> Phase 1 drowns `(0,0)`. Result `0`. `[[1]]` -> Result `0`. Correct.

## Solution

```python
import sys

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        # Increase recursion limit for deep DFS, common in grid problems.
        # Max R*C is 100*100 = 10000, so 10^5 is a safe limit.
        sys.setrecursionlimit(10**5) 

        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            # Base cases for DFS:
            # 1. If current cell (r, c) is out of bounds
            if not (0 <= r < R and 0 <= c < C):
                return
            # 2. If current cell is water (1) or has already been visited/drowned (changed to 1)
            if grid[r][c] == 1:
                return

            # Mark the current land cell as visited by changing it to water (1)
            grid[r][c] = 1

            # Recursively explore all 4-directionally connected neighbors
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left

        # Phase 1: Drown all islands that are connected to the grid's boundary.
        # These islands cannot be "closed" because they touch the edge.
        # Iterate through all cells on the grid's border.
        for r in range(R):
            for c in range(C):
                # Check if the cell is on the boundary (first/last row or first/last column)
                # AND if it's land (0).
                if (r == 0 or r == R - 1 or c == 0 or c == C - 1) and grid[r][c] == 0:
                    dfs(r, c) # Start DFS to drown this boundary-connected island

        # Phase 2: Count the remaining islands.
        # Any '0's left in the grid at this point must belong to closed islands.
        closed_islands_count = 0
        # Iterate through the entire grid (including inner cells).
        for r in range(R):
            for c in range(C):
                # If we find a land cell (0) that hasn't been drowned in Phase 1,
                # it means we've found a new closed island.
                if grid[r][c] == 0:
                    closed_islands_count += 1
                    # Perform DFS to "drown" this closed island.
                    # This marks all its connected land cells as visited (1)
                    # and prevents us from counting parts of the same island multiple times.
                    dfs(r, c)

        return closed_islands_count

```

## Why This Works
The solution works by leveraging the definition of a "closed island." A closed island is one that is *not* connected to the grid's boundary. By first identifying and "drowning" (changing `0`s to `1`s) all landmasses that *are* connected to the boundary, we effectively remove all non-closed islands from the grid. After this initial cleanup, any `0`s that remain in the grid must, by definition, be part of islands that are entirely surrounded by `1`s and do not touch the boundary. We then perform a standard island counting procedure on this modified grid, and each `0` we encounter will initiate a DFS that explores and counts exactly one closed island.

---
<sub>Generated 2026-10-25 05:09 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
