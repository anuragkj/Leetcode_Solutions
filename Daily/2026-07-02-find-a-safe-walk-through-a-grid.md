# [3286] Find a Safe Walk Through a Grid

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-07-02 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/find-a-safe-walk-through-a-grid/)

**Topics:** Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an m x n binary matrix grid and an integer health.

You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).

You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

Example 1:

Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.

Example 2:

Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3

Output: false

Explanation:

A minimum of 4 health points is needed to reach the final cell safely.

Example 3:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.

Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.

Constraints:

- m == grid.length

- n == grid[i].length

- 1 <= m, n <= 50

- 2 <= m * n

- 1 <= health <= m + n

- grid[i][j] is either 0 or 1.

**Examples / sample tests:**

```
[[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
1
[[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]]
3
[[1,1,1],[1,0,1],[1,1,1]]
5
```

---

## Problem Summary
You are given a grid of safe (0) and unsafe (1) cells, and an initial `health` value. Starting at `(0,0)`, you need to find if there's a path to `(m-1, n-1)` by moving up, down, left, or right. Unsafe cells reduce your health by 1, while safe cells don't. You must reach the destination with at least 1 health point remaining.

## Intuition
This problem asks for a path that minimizes health loss. Since moving through a safe cell costs 0 health and an unsafe cell costs 1 health, this is a **shortest path problem** where edge weights are either 0 or 1. This specific type of shortest path problem can be efficiently solved using a **0-1 Breadth-First Search (BFS)**, which is a variation of BFS that uses a **deque (double-ended queue)** to prioritize 0-cost moves.

## Approach
The optimal approach is a **0-1 BFS** algorithm:

1.  **State Definition**: We need to keep track of the minimum health points lost to reach any cell `(r, c)` from the starting cell `(0,0)`. Let's store this in a 2D array `min_loss[r][c]`.
2.  **Initialization**:
    *   Create an `m x n` matrix `min_loss` and initialize all its cells to `float('inf')`.
    *   Set `min_loss[0][0] = 0`, as no health is lost to reach the starting cell itself.
    *   Initialize a `collections.deque` (double-ended queue) and add the starting state `(0, 0, 0)` to it. The tuple represents `(current_loss, row, col)`.
3.  **BFS Traversal**:
    *   While the `deque` is not empty:
        *   Pop the state `(current_loss, r, c)` from the **front** of the `deque`.
        *   **Pruning**: If `current_loss` is already greater than `min_loss[r][c]`, it means we've found a better or equal path to `(r, c)` previously, so skip this state.
        *   **Explore Neighbors**: For each of the four possible adjacent cells `(nr, nc)` (up, down, left, right):
            *   Check if `(nr, nc)` is within the grid boundaries.
            *   Calculate the `loss_on_cell` for `(nr, nc)`: it's `grid[nr][nc]` (0 if safe, 1 if unsafe).
            *   Calculate `new_loss = current_loss + loss_on_cell`.
            *   If `new_loss < min_loss[nr][nc]`:
                *   Update `min_loss[nr][nc] = new_loss`.
                *   If `loss_on_cell == 0` (safe cell), push `(new_loss, nr, nc)` to the **front** of the `deque`. This prioritizes exploring paths with no immediate health loss.
                *   If `loss_on_cell == 1` (unsafe cell), push `(new_loss, nr, nc)` to the **back** of the `deque`. This explores paths with health loss after all 0-cost paths have been considered.
4.  **Result**: After the BFS completes, `min_loss[m-1][n-1]` will contain the minimum health loss required to reach the target cell.
    *   If `min_loss[m-1][n-1]` is still `float('inf')`, it means the target cell is unreachable. Return `False`.
    *   Otherwise, check if `health - min_loss[m-1][n-1] >= 1`. If true, return `True`; otherwise, return `False`.

## Visualization
The core idea of 0-1 BFS is to prioritize moves that don't cost health (0-cost edges) over moves that do (1-cost edges). This is achieved by using a deque:

```mermaid
graph TD
    A[Start: (0,0), Loss 0] --> B{Add (0,0,0) to Deque Front}
    B --> C{Deque not empty?}
    C -- Yes --> D[Pop (loss, r, c) from Deque Front]
    D --> E{For each Neighbor (nr, nc)}
    E --> F{Calculate new_loss = loss + grid[nr][nc]}
    F --> G{If new_loss < min_loss[nr][nc]}
    G --> H[Update min_loss[nr][nc] = new_loss]
    H --> I{Is grid[nr][nc] == 0 (Safe)?}
    I -- Yes --> J[Add (new_loss, nr, nc) to Deque FRONT]
    I -- No (Unsafe) --> K[Add (new_loss, nr, nc) to Deque BACK]
    J --> C
    K --> C
    C -- No --> L[End BFS]
    L --> M{Check min_loss[m-1][n-1]}
```

## Dry Run
Let's trace Example 1: `grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]`, `health = 1`.
`m=3, n=5`. Target: `(2,4)`.

1.  Initialize `min_loss` grid with `inf`, `min_loss[0][0] = 0`.
    `deque = [(0, 0, 0)]` (loss, row, col)

2.  **Pop `(0,0,0)`**:
    *   Neighbor `(0,1)`: `grid[0][1]=1`. `new_loss=0+1=1`. `min_loss[0][1]` becomes 1. Add `(1,0,1)` to **back**.
    *   Neighbor `(1,0)`: `grid[1][0]=0`. `new_loss=0+0=0`. `min_loss[1][0]` becomes 0. Add `(0,1,0)` to **front**.
    *   `deque` is now `[(0,1,0), (1,0,1)]`. Notice `(0,1,0)` (0-cost) is prioritized.

3.  **Pop `(0,1,0)`** (from `(1,0)`):
    *   Neighbor `(2,0)`: `grid[2][0]=0`. `new_loss=0+0=0`. `min_loss[2][0]` becomes 0. Add `(0,2,0)` to **front**.
    *   Neighbor `(1,1)`: `grid[1][1]=1`. `new_loss=0+1=1`. `min_loss[1][1]` becomes 1. Add `(1,1,1)` to **back**.
    *   `deque` is now `[(0,2,0), (1,0,1), (1,1,1)]`.

4.  This process continues. The 0-1 BFS will systematically explore all paths, always prioritizing those with fewer health losses. It will find a path from `(0,0)` to `(2,4)` that consists entirely of safe cells (`grid[r][c] = 0`). For example, `(0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2) -> (1,2) -> (0,2) -> (0,3) -> (0,4) -> (1,4) -> (2,4)`.

5.  The total health loss for this path is `0`.
    Therefore, the algorithm will determine `min_loss[2][4] = 0`.

6.  **Final Check**: `health - min_loss[2][4] >= 1`
    `1 - 0 >= 1` which simplifies to `1 >= 1`. This is `True`.

7.  **Result**: `True`.

## Complexity
*   **Time Complexity**: O(M * N). Each cell `(r, c)` is added to the deque and processed at most once for its minimum loss. When a cell is processed, its 4 neighbors are checked. Thus, the total operations are proportional to the number of cells `M*N` and the number of edges `4*M*N`.
*   **Space Complexity**: O(M * N). This is for storing the `min_loss` matrix and for the `deque`, which in the worst case might hold all cells.

## Edge Cases
*   **Start is target**: If `(0,0)` is also `(m-1, n-1)` (e.g., a 1x1 grid, though constraints say `m*n >= 2`), `min_loss[0][0]` is 0. The condition `health - 0 >= 1` correctly determines reachability.
*   **Unreachable target**: If the target cell `(m-1, n-1)` cannot be reached from `(0,0)` (e.g., surrounded by walls or grid boundaries), `min_loss[m-1][n-1]` will remain `float('inf')`, and the solution correctly returns `False`.
*   **All cells are unsafe (1)**: The algorithm will correctly accumulate health loss for each step.
*   **All cells are safe (0)**: The algorithm will find a path with 0 health loss, as 0-cost moves are prioritized.
*   **`health = 1`**: This is the strictest condition. The solution correctly requires `min_loss[m-1][n-1]` to be 0 for a `True` result.
*   **Smallest grid (e.g., 1x2 or 2x1)**: The BFS logic handles these dimensions correctly, as long as `m*n >= 2`.

## Solution

```python
import collections
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        # min_loss[r][c] stores the minimum health points lost to reach (r, c) from (0, 0).
        # Initialize with infinity for all cells.
        min_loss = [[float('inf')] * n for _ in range(m)]
        
        # The starting cell (0, 0) has 0 initial health loss.
        min_loss[0][0] = 0

        # Deque for 0-1 BFS. Stores tuples: (current_loss, row, col)
        # 0-cost edges (safe cells) are added to the front of the deque.
        # 1-cost edges (unsafe cells) are added to the back of the deque.
        deque = collections.deque([(0, 0, 0)])

        # Possible movements: up, down, left, right (dr, dc)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while deque:
            current_loss, r, c = deque.popleft()

            # If we've already found a path to (r, c) with less or equal loss,
            # there's no need to process this path further as it won't be optimal.
            if current_loss > min_loss[r][c]:
                continue

            # Explore all four adjacent neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check if the neighbor is within the grid boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    # Determine the health loss incurred by moving into the new cell (nr, nc).
                    # grid[nr][nc] is 0 for a safe cell, 1 for an unsafe cell.
                    loss_on_cell = grid[nr][nc]
                    new_loss = current_loss + loss_on_cell

                    # If this new path to (nr, nc) has less total loss than any previously found path
                    if new_loss < min_loss[nr][nc]:
                        min_loss[nr][nc] = new_loss  # Update the minimum loss for (nr, nc)
                        
                        # Prioritize 0-cost moves: add to the front of the deque
                        if loss_on_cell == 0:
                            deque.appendleft((new_loss, nr, nc))
                        # 1-cost moves: add to the back of the deque
                        else:
                            deque.append((new_loss, nr, nc))
        
        # After the BFS completes, min_loss[m-1][n-1] will hold the minimum health loss
        # required to reach the target cell (m-1, n-1).
        final_min_loss = min_loss[m-1][n-1]

        # If the target cell was unreachable, its min_loss will still be infinity.
        if final_min_loss == float('inf'):
            return False
        
        # Otherwise, check if the initial health is sufficient to reach the target
        # with at least 1 health point remaining.
        return health - final_min_loss >= 1

```

## Why This Works
This solution correctly finds the minimum health loss required to reach the target cell because **0-1 BFS is an optimized version of Dijkstra's algorithm for graphs with edge weights restricted to 0 or 1**. By using a deque and pushing 0-cost edges to the front and 1-cost edges to the back, the algorithm ensures that cells reachable with less health loss are always processed before cells reachable with more health loss. This guarantees that when a cell `(r, c)` is first popped from the front of the deque, `min_loss[r][c]` already holds the absolute minimum health loss to reach it. Therefore, by the time the BFS finishes, `min_loss[m-1][n-1]` will accurately represent the minimum health expenditure, allowing us to determine if the initial `health` is sufficient to complete the walk safely.

---
<sub>Generated 2026-07-02 04:43 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
