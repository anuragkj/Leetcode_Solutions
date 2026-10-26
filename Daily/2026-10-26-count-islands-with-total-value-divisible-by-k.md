# [3619] Count Islands With Total Value Divisible by K

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-10-26 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/)

**Topics:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an m x n matrix grid and a positive integer k. An island is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically).

The total value of an island is the sum of the values of all cells in the island.

Return the number of islands with a total value divisible by k.

Example 1:

Input: grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5

Output: 2

Explanation:

The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.

Example 2:

Input: grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3

Output: 6

Explanation:

The grid contains six islands, each with a total value that is divisible by 3.

Constraints:

- m == grid.length

- n == grid[i].length

- 1 <= m, n <= 1000

- 1 <= m * n <= 10^5

- 0 <= grid[i][j] <= 10^6

- 1 <= k <= 10^6

**Examples / sample tests:**

```
[[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]]
5
[[3,0,3,0],[0,3,0,3],[3,0,3,0]]
3
```

---

## Problem Summary
The task is to find all "islands" in a given `m x n` grid, where an island is a group of 4-directionally connected positive integers. For each island, we need to calculate the sum of its cell values and then count how many of these islands have a total value that is perfectly divisible by a given integer `k`.

## Intuition
The problem asks us to identify connected components (islands) in a grid. This immediately points towards **graph traversal algorithms** like **Depth-First Search (DFS)** or **Breadth-First Search (BFS)**.

Here's the breakdown of the thought process:
1.  **What constitutes an island?** Positive integers connected horizontally or vertically. `0`s act as water, separating islands.
2.  **How do we find an island?** We can iterate through every cell in the grid. If we find a cell that is "land" (a positive integer) and hasn't been visited yet, it must be part of a new, undiscovered island.
3.  **How do we explore an island?** Once we find the start of an island, we use DFS or BFS to visit all connected land cells. As we visit each cell, we add its value to a running sum for the current island.
4.  **How do we avoid recounting or infinite loops?** We need a way to mark cells as "visited" once they've been processed as part of an island. This ensures each cell is counted exactly once and prevents revisiting parts of the same island.
5.  **What do we do after exploring an island?** Once the DFS/BFS for an island completes, we'll have its total sum. We then check if this sum is divisible by `k`. If it is, we increment our final count.

## Approach
We will use an **iterative Depth-First Search (DFS)** approach to find and sum the values of each island. Iterative DFS uses an explicit stack, which is safer for large grids than recursive DFS to avoid Python's default recursion depth limit.

Here are the concrete steps:

1.  **Initialize Variables**:
    *   Get the dimensions of the `grid`: `m` (rows) and `n` (columns).
    *   Create a `visited` matrix of the same dimensions as `grid`, initialized with `False` for all cells. This will keep track of cells already processed.
    *   Initialize `count_divisible_islands = 0`. This will store our final answer.
    *   Define `directions` for 4-directional movement: `[(0, 1), (0, -1), (1, 0), (-1, 0)]` (right, left, down, up).

2.  **Iterate Through the Grid**:
    *   Loop through each cell `(r, c)` from `(0, 0)` to `(m-1, n-1)`.

3.  **Identify New Islands**:
    *   Inside the loop, for each cell `(r, c)`:
        *   Check if `grid[r][c]` is a **positive integer** (i.e., `grid[r][c] > 0`) AND if it has **not been visited yet** (`not visited[r][c]`).
        *   If both conditions are true, we've found the starting point of a new, unvisited island.

4.  **Perform Iterative DFS**:
    *   If a new island is found at `(r, c)`:
        *   Initialize `current_island_sum = 0`.
        *   Create a `stack` and push `(r, c)` onto it.
        *   Mark `visited[r][c] = True`.
        *   **While the `stack` is not empty**:
            *   Pop a cell `(curr_r, curr_c)` from the `stack`.
            *   Add `grid[curr_r][curr_c]` to `current_island_sum`.
            *   **Explore Neighbors**: For each `(dr, dc)` in `directions`:
                *   Calculate the neighbor's coordinates: `nr = curr_r + dr`, `nc = curr_c + dc`.
                *   **Check Validity**:
                    *   Ensure `(nr, nc)` is within the grid boundaries (`0 <= nr < m` and `0 <= nc < n`).
                    *   Ensure `grid[nr][nc]` is **positive** (land).
                    *   Ensure `(nr, nc)` has **not been visited yet** (`not visited[nr][nc]`).
                *   If all conditions are met, mark `visited[nr][nc] = True` and push `(nr, nc)` onto the `stack`.

5.  **Check Divisibility**:
    *   After the DFS for an island completes (i.e., the `stack` becomes empty), `current_island_sum` will hold the total value of that island.
    *   Check if `current_island_sum % k == 0`.
    *   If it is, increment `count_divisible_islands`.

6.  **Return Result**:
    *   After iterating through all cells in the grid, return `count_divisible_islands`.

## Visualization

Let's visualize the DFS process on a small grid with `k=5`.

**Grid:**
```
[[0, 2, 1],
 [0, 5, 0],
 [0, 0, 1]]
```

**Initial State:**
`visited` matrix (all False), `count_divisible_islands = 0`

**Iteration (0,0):** `grid[0][0]=0`. Skip.

**Iteration (0,1):** `grid[0][1]=2`. `visited[0][1]` is False. **Start DFS!**

1.  `stack = [(0,1)]`, `visited[0][1] = True`, `current_island_sum = 0`
2.  Pop `(0,1)`. `current_island_sum = 0 + 2 = 2`.
    *   Neighbors of `(0,1)`:
        *   `(0,0)`: `grid[0][0]=0`. Skip.
        *   `(0,2)`: `grid[0][2]=1`. Not visited. Push `(0,2)`, `visited[0][2]=True`. `stack = [(0,2)]`
        *   `(1,1)`: `grid[1][1]=5`. Not visited. Push `(1,1)`, `visited[1][1]=True`. `stack = [(0,2), (1,1)]`
        *   `(-1,1)`: Out of bounds. Skip.
3.  Pop `(1,1)`. `current_island_sum = 2 + 5 = 7`.
    *   Neighbors of `(1,1)`:
        *   `(1,0)`: `grid[1][0]=0`. Skip.
        *   `(1,2)`: `grid[1][2]=0`. Skip.
        *   `(2,1)`: `grid[2][1]=0`. Skip.
        *   `(0,1)`: Visited. Skip.
4.  Pop `(0,2)`. `current_island_sum = 7 + 1 = 8`.
    *   Neighbors of `(0,2)`:
        *   `(0,1)`: Visited. Skip.
        *   `(1,2)`: `grid[1][2]=0`. Skip.
        *   ... (other neighbors are out of bounds or water)
5.  `stack` is empty. DFS for this island finished.
    `current_island_sum = 8`. `8 % 5 != 0`. `count_divisible_islands` remains 0.

**Visited Grid after first island:**
```
[[0, T, T],
 [0, T, 0],
 [0, 0, 1]]
```
(T = True, F = False)

**Iteration (0,2):** `grid[0][2]=1`. `visited[0][2]` is True. Skip.

... (continue iterating) ...

**Iteration (2,2):** `grid[2][2]=1`. `visited[2][2]` is False. **Start DFS!**

1.  `stack = [(2,2)]`, `visited[2][2] = True`, `current_island_sum = 0`
2.  Pop `(2,2)`. `current_island_sum = 0 + 1 = 1`.
    *   Neighbors of `(2,2)`: All are out of bounds, water (0), or already visited.
3.  `stack` is empty. DFS for this island finished.
    `current_island_sum = 1`. `1 % 5 != 0`. `count_divisible_islands` remains 0.

**Final Result:** `count_divisible_islands = 0`.

## Dry Run
Let's walk through **Example 1**:
`grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]]`, `k = 5`

`m=5, n=5`. `visited` matrix initialized to all `False`. `count = 0`.

| Current Cell `(r, c)` | `grid[r][c]` | `visited[r][c]` | Action

---
<sub>Generated 2026-10-26 05:12 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
