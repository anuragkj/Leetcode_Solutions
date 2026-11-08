# [1267] Count Servers that Communicate

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-11-08 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/count-servers-that-communicate/)

**Topics:** Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix, Counting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:

Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:

Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

Constraints:

- m == grid.length

- n == grid[i].length

- 1 <= m <= 250

- 1 <= n <= 250

- grid[i][j] == 0 or 1

**Examples / sample tests:**

```
[[1,0],[0,1]]
[[1,0],[1,1]]
[[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
```

---

## Problem Summary
Given a grid representing a server center, where `1` is a server and `0` is empty, we need to count how many servers can communicate with at least one other server. Two servers communicate if they are in the same row or the same column.

## Intuition
A server communicates with another if there's *any* other server in its row OR *any* other server in its column. This means a server is **isolated** (doesn't communicate) only if it's the *sole* server in its row AND the *sole* server in its column. Therefore, we can find all servers that are *not* isolated. This happens if its row has more than one server, or its column has more than one server.

## Approach
The most straightforward approach involves two passes over the grid:

1.  **First Pass: Count Servers per Row and Column**:
    *   Initialize two lists: `row_counts` (of size `m`) and `col_counts` (of size `n`), both filled with zeros.
    *   Iterate through each cell `(r, c)` of the `grid`.
    *   If `grid[r][c]` is `1` (meaning there's a server):
        *   Increment `row_counts[r]` by 1.
        *   Increment `col_counts[c]` by 1.
    *   After this pass, `row_counts[r]` will store the total number of servers in row `r`, and `col_counts[c]` will store the total number of servers in column `c`.

2.  **Second Pass: Count Communicating Servers**:
    *   Initialize a variable `communicating_servers = 0`.
    *   Iterate through each cell `(r, c)` of the `grid` again.
    *   If `grid[r][c]` is `1` (there's a server):
        *   Check if `row_counts[r] > 1` OR `col_counts[c] > 1`.
        *   If this condition is true, it means the server at `(r, c)` has at least one other server in its row or at least one other server in its column. Thus, it communicates.
        *   Increment `communicating_servers` by 1.
    *   After this pass, `communicating_servers` will hold the total count of servers that communicate.

3.  **Return `communicating_servers`**.

## Visualization
Let's use Example 3: `grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]`

**Grid:**
```
  C0 C1 C2 C3
R0[1, 1, 0, 0]
R1[0, 0, 1, 0]
R2[0, 0, 1, 0]
R3[0, 0, 0, 1]
```

**1. First Pass: Populate `row_counts` and `col_counts`**

*   Initialize `row_counts = [0, 0, 0, 0]` and `col_counts = [0, 0, 0, 0]`
*   Processing `(0,0)`: `grid[0][0]=1` -> `row_counts[0]=1`, `col_counts[0]=1`
*   Processing `(0,1)`: `grid[0][1]=1` -> `row_counts[0]=2`, `col_counts[1]=1`
*   Processing `(1,2)`: `grid[1][2]=1` -> `row_counts[1]=1`, `col_counts[2]=1`
*   Processing `(2,2)`: `grid[2][2]=1` -> `row_counts[2]=1`, `col_counts[2]=2`
*   Processing `(3,3)`: `grid[3][3]=1` -> `row_counts[3]=1`, `col_counts[3]=1`

**After First Pass:**
*   `row_counts = [2, 1, 2, 1]`
*   `col_counts = [1, 1, 2, 1]`

**2. Second Pass: Count Communicating Servers**

*   Initialize `communicating_servers = 0`
*   **Server at (0,0):** `grid[0][0]=1`. `row_counts[0]=2` (which is `>1`). **Communicates!** `communicating_servers = 1`.
*   **Server at (0,1):** `grid[0][1]=1`. `row_counts[0]=2` (which is `>1`). **Communicates!** `communicating_servers = 2`.
*   **Server at (1,2):** `grid[1][2]=1`. `row_counts[1]=1` (not `>1`), but `col_counts[2]=2` (which is `>1`). **Communicates!** `communicating_servers = 3`.
*   **Server at (2,2):** `grid[2][2]=1`. `row_counts[2]=2` (which is `>1`). **Communicates!** `communicating_servers = 4`.
*   **Server at (3,3):** `grid[3][3]=1`. `row_counts[3]=1` (not `>1`), AND `col_counts[3]=1` (not `>1`). Does **NOT** communicate. `communicating_servers` remains 4.

**Final Result: `communicating_servers = 4`**

## Dry Run
Let's walk through Example 1: `grid = [[1,0],[0,1]]`

| Step | `r` | `c` | `grid[r][c]` | `row_counts` | `col_counts` | `communicating_servers` | Notes |
| :--- | :-: | :-: | :----------: | :----------- | :----------- | :---------------------- | :---- |
| **Initial** | | | | `[0,0]` | `[0,0]` | `0` | `m=2, n=2` |
| **Pass 1: Populate Counts** | | | | | | | |
| 1 | 0 | 0 | `1` | `[1,0]` | `[1,0]` | `0` | Server found, update counts |
| 2 | 0 | 1 | `0` | `[1,0]` | `[1,0]` | `0` | No server |
| 3 | 1 | 0 | `0` | `[1,0]` | `[1,0]` | `0` | No server |
| 4 | 1 | 1 | `1` | `[1,1]` | `[1,1]` | `0` | Server found, update counts |
| **End Pass 1** | | | | `[1,1]` | `[1,1]` | `0` | `row_counts` and `col_counts` are finalized |
| **Pass 2: Count Communicating** | | | | | | | |
| 5 | 0 | 0 | `1` | `[1,1]` | `[1,1]` | `0` | `row_counts[0]=1` (not `>1`), `col_counts[0]=1` (not `>1`). Condition `False`. |
| 6 | 0 | 1 | `0` | `[1,1]` | `[1,1]` | `0` | No server |
| 7 | 1 | 0 | `0` | `[1,1]` | `[1,1]` | `0` | No server |
| 8 | 1 | 1 | `1` | `[1,1]` | `[1,1]` | `0` | `row_counts[1]=1` (not `>1`), `col_counts[1]=1` (not `>1`). Condition `False`. |
| **Final Result** | | | | | | `0` | |

## Complexity
*   **Time Complexity**: **O(M*N)**. We iterate through the `M x N` grid twice. Each cell operation is constant time.
*   **Space Complexity**: **O(M+N)**. We use `row_counts` (size `M`) and `col_counts` (size `N`) to store server counts.

## Edge Cases
*   **Single server grid**: `[[1]]`
    *   `row_counts = [1]`, `col_counts = [1]`.
    *   The server at `(0,0)` has `row_counts[0]=1` and `col_counts[0]=1`. Neither is `>1`.
    *   Result: `0`. Correct, as it has no other server to communicate with.
*   **No servers in grid**: `[[0,0],[0,0]]`
    *   `row_counts = [0,0]`, `col_counts = [0,0]`.
    *   No servers are found in the second pass.
    *   Result: `0`. Correct.
*   **All servers in one row**: `[[1,1,1]]`
    *   `row_counts = [3]`, `col_counts = [1,1,1]`.
    *   All three servers will have `row_counts[0]=3` (which is `>1`).
    *   Result: `3`. Correct.
*   **All servers in one column**: `[[1],[1],[1]]`
    *   `row_counts = [1,1,1]`, `col_counts = [3]`.
    *   All three servers will have `col_counts[0]=3` (which is `>1`).
    *   Result: `3`. Correct.
*   **Grid with all servers**: `[[1,1],[1,1]]`
    *   `row_counts = [2,2]`, `col_counts = [2,2]`.
    *   All four servers will have `row_counts[r]>1` and `col_counts[c]>1`.
    *   Result: `4`. Correct.

## Solution

```python
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Step 1: Initialize counts for each row and column
        row_counts = [0] * m
        col_counts = [0] * n

        # Step 2: First pass - Populate row_counts and col_counts
        # Iterate through the grid to find all servers and update their respective row/column counts.
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
        
        # Step 3: Second pass - Count communicating servers
        # Iterate through the grid again. For each server, check if it communicates.
        communicating_servers = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # A server communicates if there's more than one server in its row
                    # OR more than one server in its column.
                    if row_counts[r] > 1 or col_counts[c] > 1:
                        communicating_servers += 1
        
        return communicating_servers

```

## Why This Works
This approach works because it directly applies the definition of communication. By pre-calculating the total number of servers in each row and column, we can efficiently determine if any given server is part of a group (i.e., its row or column contains at least one other server). If a server's row count is greater than one, it communicates with others in that row. Similarly, if its column count is greater than one, it communicates with others in that column. The `OR` condition correctly captures that a server only needs *one* such connection to be considered communicating. Servers that are the *only* one in their row AND the *only* one in their column will have both `row_counts[r] == 1` and `col_counts[c] == 1`, failing the `> 1` condition, and thus correctly not being counted as communicating.

---
<sub>Generated 2026-11-08 06:34 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
