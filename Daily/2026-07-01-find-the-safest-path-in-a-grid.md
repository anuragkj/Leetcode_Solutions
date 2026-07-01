# [2812] Find the Safest Path in a Grid

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-07-01 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/find-the-safest-path-in-a-grid/)

**Topics:** Array, Binary Search, Breadth-First Search, Union-Find, Heap (Priority Queue), Matrix

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

- A cell containing a thief if grid[r][c] = 1

- An empty cell if grid[r][c] = 0

You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

Example 1:

Input: grid = [[1,0,0],[0,0,0],[0,0,1]]
Output: 0
Explanation: All paths from (0, 0) to (n - 1, n - 1) go through the thieves in cells (0, 0) and (n - 1, n - 1).

Example 2:

Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

Example 3:

Input: grid = [[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 3) is cell (1, 2). The distance between them is | 0 - 1 | + | 3 - 2 | = 2.
- The closest cell of the path to the thief at cell (3, 0) is cell (3, 2). The distance between them is | 3 - 3 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

Constraints:

- 1 <= grid.length == n <= 400

- grid[i].length == n

- grid[i][j] is either 0 or 1.

- There is at least one thief in the grid.

**Examples / sample tests:**

```
[[1,0,0],[0,0,0],[0,0,1]]
[[0,0,1],[0,0,0],[0,0,0]]
[[0,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
```

---

## Problem Summary
You're given a grid with thieves (1) and empty cells (0). You start at (0,0) and want to reach (n-1, n-1) by moving to adjacent cells. The **safeness factor** of a path is the minimum Manhattan distance from any cell on that path to any thief. Your goal is to find the **maximum possible safeness factor** among all valid paths.

## Intuition
This problem asks us to maximize a minimum value, which is a classic pattern for **binary search on the answer**. If we can find a path with a safeness factor of `k`, we can also find a path with any safeness factor less than `k` (by simply using the same path). This monotonicity allows binary search.

The core idea is:
1.  **Pre-computation**: For every cell `(r, c)` in the grid, calculate its **safeness score**: the minimum Manhattan distance from `(r, c)` to *any* thief. This can be efficiently done using a **multi-source Breadth-First Search (BFS)**, starting simultaneously from all thief locations.
2.  **Binary Search `check` function**: Once we have the safeness score for every cell, we can binary search for the maximum possible safeness factor, let's call it `k`. For a given `k`, our `check(k)` function will determine if a path exists from `(0,0)` to `(n-1,n-1)` using *only* cells whose safeness score is `k` or greater. This check is another standard **BFS (or DFS)**.

## Approach
The solution involves two main phases:

1.  **Calculate `safeness_score` for all cells (Multi-source BFS):**
    *   Initialize a `safeness_score` grid of the same size as `grid`, with all values set to -1 (or infinity) to mark them as unvisited.
    *   Create a queue and add all cells `(r, c)` where `grid[r][c] == 1` (thieves) to this queue. Set `safeness_score[r][c] = 0` for these thief cells.
    *   Perform a standard BFS:
        *   Dequeue a cell `(r, c)`.
        *   For each of its 4 adjacent neighbors `(nr, nc)`:
            *   If `(nr, nc)` is within grid bounds and `safeness_score[nr][nc]` is still -1 (meaning it hasn't been visited yet by any thief's "wave"):
                *   Set `safeness_score[nr][nc] = safeness_score[r][c] + 1`.
                *   Enqueue `(nr, nc)`.
    *   After this BFS, `safeness_score[r][c]` will contain the Manhattan distance from `(r, c)` to its nearest thief.

2.  **Binary Search for the maximum safeness factor `k`:**
    *   Define a search range for `k`: `low = 0` (minimum possible safeness) and `high = 2 * (n - 1)` (maximum possible Manhattan distance in an `n x n` grid).
    *   Initialize `max_safeness = 0`.
    *   While `low <= high`:
        *   Calculate `mid = low + (high - low) // 2`.
        *   Call a helper function `can_reach_with_safeness(mid)`:
            *   This function performs another BFS (or DFS) to check if a path exists from `(0,0)` to `(n-1,n-1)` using *only* cells `(r, c)` where `safeness_score[r][c] >= mid`.
            *   **Important initial check**: If `safeness_score[0][0] < mid` or `safeness_score[n-1][n-1] < mid`, then `(0,0)` or `(n-1,n-1)` are not safe enough, so `can_reach_with_safeness` immediately returns `False`.
            *   If `can_reach_with_safeness(mid)` returns `True`:
                *   It means `mid` is a possible safeness factor. We try to find an even higher one.
                *   Set `max_safeness = mid`.
                *   Set `low = mid + 1`.
            *   Else (`can_reach_with_safeness(mid)` returns `False`):
                *   `mid` is too high; we need a lower safeness factor.
                *   Set `high = mid - 1`.
    *   Return `max_safeness`.

## Visualization

Let's visualize the `safeness_score` grid for `grid = [[0,0,1],[0,0,0],[0,0,0]]` (Example 2).
The thief is at (0,2).

**Initial grid:**
```
0 0 1
0 0 0
0 0 0
```

**After Multi-source BFS (safeness_score grid):**
Each number represents the Manhattan distance to the nearest thief.
```
2 1 0  <- Thief at (0,2)
3 2 1
4 3 2
```

Now, let's visualize the `can_reach_with_safeness(k)` check for `k=2`.
Cells with `safeness_score < 2` are blocked (marked 'X').
`safeness_score[0][1]=1`, `safeness_score[1][2]=1`. These are blocked.

**Grid for `check(2)`:**
`S` = Start (0,0), `E` = End (2,2), `.` = traversable, `X` = blocked.
```
S . X  (0,0) score 2, (0,1) score 1 (blocked), (0,2) score 0 (blocked)
. . X  (1,0) score 3, (1,1) score 2, (1,2) score 1 (blocked)
. . E  (2,0) score 4, (2,1) score 3, (2,2) score 2
```
A path from `S` to `E` exists: `(0,0) -> (1,0) -> (1,1) -> (2,1) -> (2,2)`.
All cells on this path have a safeness score of at least 2. So `check(2)` returns `True`.

If we tried `check(3)`:
`safeness_score[0][0]` is 2, which is `< 3`. So `check(3)` would immediately return `False`.

## Dry Run
Let's trace Example 1: `grid = [[1,0,0],[0,0,0],[0,0,1]]`
`n = 3`

**Step 1: Multi-source BFS to compute `safeness_score`**

| Cell `(r,c)` | `grid[r][c]` | `safeness_score` (initial) | `q` (initial) |
| :----------- | :----------- | :------------------------- | :------------ |
| (0,0)        | 1            | 0                          | `[(0,0)]`     |
| (0,1)        | 0            | -1                         |               |
| (0,2)        | 0            | -1                         |               |
| (1,0)        | 0            | -1                         |               |
| (1,1)        | 0            | -1                         |               |
| (1,2)        | 0            | -1                         |               |
| (2,0)        | 0            | -1                         |               |
| (2,1)        | 0            | -1                         |               |
| (2,2)        | 1            | 0                          | `[(0,0), (2,2)]` |

**BFS Iterations:**

1.  `q.popleft() -> (0,0)`. Neighbors: `(0,1)`, `(1,0)`.
    *   `safeness_score[0][1] = 1`, `q.append((0,1))`
    *   `safeness_score[1][0] = 1`, `q.append((1,0))`
    `q = [(2,2), (0,1), (1,0)]`
2.  `q.popleft() -> (2,2)`. Neighbors: `(1,2)`, `(2,1)`.
    *   `safeness_score[1][2] = 1`, `q.append((1,2))`
    *   `safeness_score[2][1] = 1`, `q.append((2,1))`
    `q = [(0,1), (1,0), (1,2), (2,1)]`
3.  `q.popleft() -> (0,1)`. Neighbors: `(0,0)` (visited), `(0,2)`, `(1,1)`.
    *   `safeness_score[0][2] = 2`, `q.append((0,2))`
    *   `safeness_score[1][1] = 2`, `q.append((1,1))`
    `q = [(1,0), (1,2), (2,1), (0,2), (1,1)]`
4.  `q.popleft() -> (1,0)`. Neighbors: `(0,0)` (visited), `(1,1)` (visited), `(2,0)`.
    *   `safeness_score[2][0] = 2`, `q.append((2,0))`
    `q = [(1,2), (2,1), (0,2), (1,1), (2,0)]`
... (BFS continues until queue is empty)

**Final `safeness_score` grid:**
```
[[0, 1, 2],
 [1, 2, 1],
 [2, 1, 0]]
```

**Step 2: Binary Search**
`n = 3`. `low = 0`, `high = 2 * (3-1) = 4`. `max_safeness = 0`.

| `low` | `high` | `mid` | `can_reach_with_safeness(mid)` | Action                               | `max_safeness` |
| :---- | :----- | :---- | :----------------------------- | :----------------------------------- | :------------- |
| 0     | 4      | 2     | `safeness_score[0][0]` (0) < 2. Returns `False`. | `high = 2 - 1 = 1`                   | 0              |
| 0     | 1      | 0     | `safeness_score[0][0]` (0) >= 0. `safeness_score[2][2]` (0) >= 0. Path exists (all cells >= 0). Returns `True`. | `max_safeness = 0`, `low = 0 + 1 = 1` | 0              |
| 1     | 1      | 1     | `safeness_score[0][0]` (0) < 1. Returns `False`. | `high = 1 - 1 = 0`                   | 0              |
| 1     | 0      |       | Loop terminates (`low > high`) |                                      |                |

**Final Result:** `max_safeness = 0`. This matches Example 1 output.

## Complexity
*   **Time Complexity**: `O(N^2 log(N))`
    *   The multi-source BFS to calculate `safeness_score` takes `O(N^2)` time, as each cell is visited and enqueued at most once.
    *   The binary search performs `log(MaxSafenessFactor)` iterations. `MaxSafenessFactor` is `O(N)`, so this is `O(log N)` iterations.
    *   Inside each binary search iteration, the `can_reach_with_safeness` function performs another BFS, which takes `O(N^2)` time.
    *   Total: `O(N^2 + N^2 log N) = O(N^2 log N)`.
*   **Space Complexity**: `O(N^2)`
    *   `safeness_score` grid: `O(N^2)`.
    *   Queue for BFS: `O(N^2)` in the worst case (all cells enqueued).
    *   `visited` grid for `can_reach_with_safeness`: `O(N^2)`.

## Edge Cases
*   **`n = 1`**:
    *   `grid = [[1]]`: `(0,0)` is a thief. `safeness_score[0][0] = 0`. The path is just `(0,0)`. Max safeness is 0. Our code handles this: `low=0, high=0`, `mid=0`. `check(0)` returns `True`. `max_safeness=0`. Correct.
    *   Problem states "There is at least one thief in the grid", so `[[0]]` is not a valid input.
*   **Start or End cell is a thief**:
    *   If `grid[0][0] == 1` or `grid[n-1][n-1] == 1`, then `safeness_score` for that cell will be 0. Any path must include this cell, so its safeness factor cannot be greater than 0. The binary search will correctly converge to 0. (Example 1 demonstrates this).
*   **Grid full of thieves**:
    *   `grid = [[1,1],[1,1]]`. All `safeness_score` values are 0. Max safeness will be 0. Correct.
*   **No path exists even with safeness 0**:
    *   This scenario is not possible in a connected grid where movement is allowed to all adjacent cells. A path will always exist if `n > 0`. The question is about the safeness of that path.

## Solution

```python
import collections
from typing import List

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1: Multi-source BFS to calculate safeness_score for all cells.
        # safeness_score[r][c] will store the minimum Manhattan distance from (r,c) to any thief.
        # Initialize with -1 to mark unvisited cells.
        safeness_score = [[-1] * n for _ in range(n)]
        q = collections.deque()

        # Directions for BFS (up, down, left, right)
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        # Populate the queue with all thief cells and set their initial safeness_score to 0.
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    safeness_score[r][c] = 0

        # Perform the multi-source BFS
        while q:
            r, c = q.popleft()

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                # Check bounds and if the neighbor cell has not been visited yet (safeness_score is -1)
                if 0 <= nr < n and 0 <= nc < n and safeness_score[nr][nc] == -1:
                    safeness_score[nr][nc] = safeness_score[r][c] + 1
                    q.append((nr, nc))

        # Step 2: Binary Search for the maximum possible safeness factor.
        # The range for safeness factor is [0, 2 * (n - 1)].
        # 0 is the minimum (e.g., if (0,0) is a thief).
        # 2 * (n - 1) is the maximum possible Manhattan distance in an n x n grid.
        low = 0
        high = 2 * (n - 1) 
        max_safeness = 0 # Stores the maximum safeness factor found so far

        # Helper function to check if a path exists from (0,0) to (n-1,n-1)
        # such that every cell on the path has a safeness_score of at least 'k'.
        def can_reach_with_safeness(k: int) -> bool:
            # If the start or end cell itself does not meet the minimum safeness factor 'k',
            # then no such path can exist.
            if safeness_score[0][0] < k or safeness_score[n-1][n-1] < k:
                return False
            
            # Standard BFS to find a path
            path_q = collections.deque([(0, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True

            while path_q:
                r, c = path_q.popleft()

                # If we reached the destination, a valid path exists for this 'k'
                if r == n - 1 and c == n - 1:
                    return True

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]

                    # Check bounds, if the cell has not been visited in this path-finding BFS,
                    # AND if its safeness_score meets the current criteria 'k'.
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and safeness_score[nr][nc] >= k:
                        visited[nr][nc] = True
                        path_q.append((nr, nc))
            
            # If BFS completes and destination is not reached, no path exists for this 'k'.
            return False

        # Binary search loop
        while low <= high:
            mid = low + (high - low) // 2
            if can_reach_with_safeness(mid):
                # If a path exists with safeness 'mid', it's a possible answer.
                # Try for a higher safeness factor.
                max_safeness = mid
                low = mid + 1
            else:
                # If no path exists with safeness 'mid', we need to try a lower factor.
                high = mid - 1
        
        return max_safeness

```

## Why This Works
The solution works by leveraging the **monotonicity** of the problem: if a path exists with a safeness factor of `k`, then a path also exists for any safeness factor `k' < k`. This property allows us to use **binary search** to find the maximum `k`.

The first multi-source BFS efficiently pre-computes the `safeness_score` for every cell, which is the minimum distance to *any* thief. This `safeness_score` is exactly what determines if a cell can be part of a path with a certain safeness factor. The `can_reach_with_safeness(k)` function then uses a standard BFS to check for connectivity, effectively filtering out any cells that are "too close" to a thief (i.e., `safeness_score < k`). By iteratively adjusting the binary search range based on the result of `can_reach_with_safeness(mid)`, we converge to the largest possible `k` for which a valid path exists.

---
<sub>Generated 2026-07-01 05:09 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
