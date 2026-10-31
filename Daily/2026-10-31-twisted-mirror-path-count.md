# [3665] Twisted Mirror Path Count

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-10-31 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/twisted-mirror-path-count/)

**Topics:** Array, Dynamic Programming, Matrix

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given an m x n binary grid grid where:

- grid[i][j] == 0 represents an empty cell, and

- grid[i][j] == 1 represents a mirror.

A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). It can move only right or down. If the robot attempts to move into a mirror cell, it is reflected before entering that cell:

- If it tries to move right into a mirror, it is turned down and moved into the cell directly below the mirror.

- If it tries to move down into a mirror, it is turned right and moved into the cell directly to the right of the mirror.

If this reflection would cause the robot to move outside the grid boundaries, the path is considered invalid and should not be counted.

Return the number of unique valid paths from (0, 0) to (m - 1, n - 1).

Since the answer may be very large, return it modulo 10^9 + 7.

Note: If a reflection moves the robot into a mirror cell, the robot is immediately reflected again based on the direction it used to enter that mirror: if it entered while moving right, it will be turned down; if it entered while moving down, it will be turned right. This process will continue until either the last cell is reached, the robot moves out of bounds or the robot moves to a non-mirror cell.

Example 1:

Input: grid = [[0,1,0],[0,0,1],[1,0,0]]

Output: 5

Explanation:

			Number
			Full Path

			1
			(0, 0) → (0, 1) [M] → (1, 1) → (1, 2) [M] → (2, 2)

			2
			(0, 0) → (0, 1) [M] → (1, 1) → (2, 1) → (2, 2)

			3
			(0, 0) → (1, 0) → (1, 1) → (1, 2) [M] → (2, 2)

			4
			(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2)

			5
			(0, 0) → (1, 0) → (2, 0) [M] → (2, 1) → (2, 2)

	[M] indicates the robot attempted to enter a mirror cell and instead reflected.

Example 2:

Input: grid = [[0,0],[0,0]]

Output: 2

Explanation:

			Number
			Full Path

			1
			(0, 0) → (0, 1) → (1, 1)

			2
			(0, 0) → (1, 0) → (1, 1)

Example 3:

Input: grid = [[0,1,1],[1,1,0]]

Output: 1

Explanation:

			Number
			Full Path

			1
			(0, 0) → (0, 1) [M] → (1, 1) [M] → (1, 2)

(0, 0) → (1, 0) [M] → (1, 1) [M] → (2, 1) goes out of bounds, so it is invalid.

Constraints:

	m == grid.length
	n == grid[i].length
	2 <= m, n <= 500
	grid[i][j] is either 0 or 1.
	grid[0][0] == grid[m - 1][n - 1] == 0

**Examples / sample tests:**

```
[[0,1,0],[0,0,1],[1,0,0]]
[[0,0],[0,0]]
[[0,1,1],[1,1,0]]
```

---

## Problem Summary
A robot navigates an `m x n` binary grid from `(0, 0)` to `(m-1, n-1)`, moving only right or down. If it attempts to move into a mirror cell (`1`), it reflects: right-attempt reflects down, down-attempt reflects right. This reflection can chain if it lands on another mirror, using the direction it *just used to enter* the mirror. Paths going out of bounds are invalid. Count unique valid paths modulo `10^9 + 7`.

## Intuition
This problem asks for the number of unique paths, which is a classic **Dynamic Programming (DP)** pattern. Typically, `dp[i][j]` stores the number of ways to reach cell `(i, j)`. The main challenge here is the **mirror reflection rule**, especially the "chained reflection" part.

The key insight is that the robot *never actually enters* a mirror cell. It's always redirected *before* entering. This means the robot always lands on an **empty cell (`0`)**. When a reflection occurs, it's like a "teleport" to a new empty cell. The chained reflection rule implies that the *direction of entry* into a mirror cell dictates its subsequent reflection.

To handle these complex "jumps" efficiently, we can **precompute** all possible destinations. For any empty cell `(r, c)`, if the robot tries to move right or down, we want to know its *final landing spot* after all potential reflections. This precomputation can then be used in a standard DP approach.

## Approach
The solution involves two main phases:
1.  **Precomputation of Reflection Paths (`memo_chain` and `go` tables):**
    *   We need to determine the final destination for any reflection chain. Let `memo_chain[r][c][dir_entered]` store the final `(R, C)` if the robot *lands* at `(r, c)` (which must be a mirror) and *entered* `(r, c)` by moving in `dir_entered` (0 for Right, 1 for Down). If `(r, c)` is empty, it's the final destination. If out of bounds, it's `(-1, -1)`.
    *   This `memo_chain` table can be filled using **dynamic programming by iterating backwards** from `(m-1, n-1)` to `(0, 0)`. This ensures that when we compute `memo_chain[r][c]`, any subsequent reflection targets `(r+1, c)` or `(r, c+1)` have already been computed.
        *   If `grid[r][c] == 0`: `memo_chain[r][c][0] = (r, c)`, `memo_chain[r][c][1] = (r, c)`.
        *   If `grid[r][c] == 1`:
            *   If `dir_entered == 0` (entered by moving Right): Reflects down to `(r+1, c)`. The next reflection in the chain will be based on entering `(r+1, c)` by moving Down. So, `memo_chain[r][c][0] = memo_chain[r+1][c][1]`.
            *   If `dir_entered == 1` (entered by moving Down): Reflects right to `(r, c+1)`. The next reflection in the chain will be based on entering `(r, c+1)` by moving Right. So, `memo_chain[r][c][1] = memo_chain[r][c+1][0]`.
        *   Handle out-of-bounds cases by storing `(-1, -1)`.
    *   Once `memo_chain` is filled, we build a `go[r][c][dir_attempted]` table. This table stores the *final landing cell* if the robot is at `(r, c)` and *attempts* to move in `dir_attempted` (0 for Right, 1 for Down).
        *   If the target cell `(next_r, next_c)` is out of bounds: `go[r][c][dir_attempted] = (-1, -1)`.
        *   If `grid[next_r][next_c] == 0`: `go[r][c][dir_attempted] = (next_r, next_c)`.
        *   If `grid[next_r][next_c] == 1`: This triggers a reflection. We use `memo_chain` to find the final destination. For example, if `dir_attempted == 0` (tried Right), it reflects down to `(next_r+1, next_c)`. The chain continues as if entering `(next_r+1, next_c)` by moving Down. So, `go[r][c][0] = memo_chain[next_r+1][next_c][1]`. Similar logic applies for `dir_attempted == 1`.

2.  **Dynamic Programming Path Counting:**
    *   Initialize `dp[0][0] = 1` (one way to start at `(0,0)`). All other `dp[i][j]` are `0`.
    *   Iterate through the grid cells `(r, c)` in **row-major order** (from `(0,0)` to `(m-1, n-1)`).
    *   For each cell `(r, c)`:
        *   If `dp[r][c] == 0`, skip (no paths reach this cell).
        *   **Try to move Right:** Get `(target_r, target_c) = go[r][c][0]`. If `(target_r, target_c)` is valid (not `(-1, -1)`), add `dp[r][c]` to `dp[target_r][target_c]`.
        *   **Try to move Down:** Get `(target_r, target_c) = go[r][c][1]`. If `(target_r, target_c)` is valid, add `dp[r][c]` to `dp[target_r][target_c]`.
        *   Remember to take the sum modulo `10^9 + 7`.
    *   The final answer is `dp[m-1][n-1]`.

## Visualization
Let's illustrate with a `2x2` grid: `grid = [[0,1],[0,0]]`.
`[M]` indicates a mirror cell. `[OOB]` indicates out of bounds.

```mermaid
graph TD
    subgraph Grid
        A((0,0)) --- B((0,1)[M])
        |             |
        C((1,0)) --- D((1,1))
    end

    style B fill:#f9f,stroke:#333,stroke-width:2px
    style A fill:#afa,stroke:#333,stroke-width:2px
    style D fill:#afa,stroke:#333,stroke-width:2px
    style C fill:#afa,stroke:#333,stroke-width:2px

    subgraph DP Propagation
        dp_A(dp[0][0]=1)
        dp_C(dp[1][0]=1)
        dp_D(dp[1][1]=2)

        dp_A -- "Try Right to (0,1) [M]" --> R1(Reflect Down to (1,1))
        R1 --> dp_D
        linkStyle 0 stroke:green,stroke-width:2px,fill:none;
        linkStyle 1 stroke:green,stroke-width:2px,fill:none;

        dp_A -- "Try Down to (1,0)" --> dp_C
        linkStyle 2 stroke:blue,stroke-width:2px,fill:none;

        dp_C -- "Try Right to (1,1)" --> dp_D
        linkStyle 3 stroke:green,stroke-width:2px,fill:none;

        dp_C -- "Try Down to (2,0) [OOB]" --> OOB1(Invalid Path)
        linkStyle 4 stroke:red,stroke-width:2px,fill:none;

        dp_D -- "Try Right to (1,2) [OOB]" --> OOB2(Invalid Path)
        linkStyle 5 stroke:red,stroke-width:2px,fill:none;

        dp_D -- "Try Down to (2,1) [OOB]" --> OOB3(Invalid Path)
        linkStyle 6 stroke:red,stroke-width:2px,fill:none;
    end
```
In this example:
*   From `(0,0)`:
    *   Trying to move Right to `(0,1)` (a mirror) reflects Down to `(1,1)`. `dp[1][1]` gets `dp[0][0]` (1).
    *   Trying to move Down to `(1,0)` (empty). `dp[1][0]` gets `dp[0][0]` (1).
*   From `(1,0)`:
    *   Trying to move Right to `(1,1)` (empty). `dp[1][1]` gets `dp[1][0]` (1), making `dp[1][1]` now 2.
    *   Trying to move Down to `(2,0)` (out of bounds). Invalid.
The final `dp[1][1]` is 2.

## Dry Run
Let's walk through Example 1: `grid = [[0,1,0],[0,0,1],[1,0,0]]`, `m=3, n=3`.
`MOD = 10^9 + 7`.

**1. Precomputation (Conceptual `go` table entries):**
*   `go[0][0][0]` (move Right from `(0,0)` to `(0,1)`): `grid[0][1]` is mirror. Reflects Down to `(1,1)`. `grid[1][1]` is empty. Final: `(1,1)`.
*   `go[0][0][1]` (move Down from `(0,0)` to `(1,0)`): `grid[1][0]` is empty. Final: `(1,0)`.
*   `go[1][0][0]` (move Right from `(1,0)` to `(1,1)`): `grid[1][1]` is empty. Final: `(1,1)`.
*   `go[1][0][1]` (move Down from `(1,0)` to `(2,0)`): `grid[2][0]` is mirror. Reflects Right to `(2,1)`. `grid[2][1]` is empty. Final: `(2,1)`.
*   `go[1][1][0]` (move Right from `(1,1)` to `(1,2)`): `grid[1][2]` is mirror. Reflects Down to `(2,2)`. `grid[2][2]` is empty. Final: `(2,2)`.
*   `go[1][1][1]` (move Down from `(1,1)` to `(2,1)`): `grid[2][1]` is empty. Final: `(2,1)`.
*   `go[2][0][0]` (move Right from `(2,0)` to `(2,1)`): `grid[2][1]` is empty. Final: `(2,1)`.
*   `go[2][0][1]` (move Down from `(2,0)` to `(3,0)`): Out of bounds. Final: `(-1,-1)`.
*   `go[2][1][0]` (move Right from `(2,1)` to `(2,2)`): `grid[2][2]` is empty. Final: `(2,2)`.
*   `go[2][1][1]` (move Down from `(2,1)` to `(3,1)`): Out of bounds. Final: `(-1,-1)`.

**2. DP Table Calculation:**
Initialize `dp = [[0,0,0],[0,0,0],[0,0,0]]`.
`dp[0][0] = 1`.

| `r` | `c` | `dp[r][c]` | Action (from `(r,c)`) | Target (Right) | `dp` update | Target (Down) | `dp` update |
| :-- | :-- | :--------- | :-------------------- | :------------- | :---------- | :------------ | :---------- |
| 0   | 0   | 1          | Try Right             | `go[0][0][0]=(1,1)` | `dp[1][1] += 1` (`dp[1][1]=1`) | `go[0][0][1]=(1,0)` | `dp[1][0] += 1` (`dp[1][0]=1`) |
| 0   | 1   | 0          | Skip (mirror)         |                |             |               |             |
| 0   | 2   | 0          | Skip (no paths yet)   |                |             |               |             |
| 1   | 0   | 1          | Try Right             | `go[1][0][0]=(1,1)` | `dp[1][1] += 1` (`dp[1][1]=2`) | `go[1][0][1]=(2,1)` | `dp[2][1] += 1` (`dp[2][1]=1`) |
| 1   | 1   | 2          | Try Right             | `go[1][1][0]=(2,2)` | `dp[2][2] += 2` (`dp[2][2]=2`) | `go[1][1][1]=(2,1)` | `dp[2][1] += 2` (`dp[2][1]=3`) |
| 1   | 2   | 0          | Skip (mirror)         |                |             |               |             |
| 2   | 0   | 0          | Skip (mirror)         |                |             |               |             |
| 2   | 1   | 3          | Try Right             | `go[2][1][0]=(2,2)` | `dp[2][2] += 3` (`dp[2][2]=5`) | `go[2][1][1]=(-1,-1)` | (invalid)   |
| 2   | 2   | 5          | (End cell)            |                |             |               |             |

Final Result: `dp[2][2] = 5`. This matches Example 1.

## Complexity
*   **Time Complexity:** `O(m * n)`.
    *   The `memo_chain` table is filled in `O(m * n)` time by iterating through each cell once.
    *   The `go` table is filled in `O(m * n)` time by iterating through each cell once and performing constant-time lookups in `memo_chain`.
    *   The `dp` table is filled in `O(m * n)` time by iterating through each cell once and performing constant-time lookups in `go`.
    *   Total time complexity is `O(m * n)`.
*   **Space Complexity:** `O(m * n)`.
    *   `grid`: `O(m * n)`.
    *   `memo_chain`: `O(m * n * 2)` for `(r, c, dir_entered)` states, which simplifies to `O(m * n)`.
    *   `go`: `O(m * n * 2)` for `(r, c, dir_attempted)` states, which simplifies to `O(m * n)`.
    *   `dp`: `O(m * n)`.
    *   Total space complexity is `O(m * n)`.

## Edge Cases
*   **Minimum grid size (2x2):** The logic handles `m=2, n=2` correctly, as demonstrated in the thought process. Boundary checks (`next_r >= m`, `next_c >= n`) prevent out-of-bounds access.
*   **All empty cells (no mirrors):** The `memo_chain` and `go` tables will correctly resolve to direct moves, and the DP will behave like a standard unique paths problem.
*   **Many mirrors / long reflection chains:** The `memo_chain` precomputation handles arbitrary length reflection chains efficiently because it's built iteratively from the end of potential chains. Each `memo_chain` entry depends on already computed `memo_chain` entries for cells further away.
*   **Paths going out of bounds:** Any reflection or direct move that would lead outside the grid is marked with `(-1, -1)` in the `go` table. The DP step then correctly ignores these invalid targets.
*   **Start/End cells are guaranteed empty:** `grid[0][0] == grid[m-1][n-1] == 0`. This simplifies initialization (`dp[0][0]=1`) and the final result (`dp[m-1][n-1]`), as we don't need to consider reflections at the start or end points themselves.

## Solution

```python
from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        # memo_chain[r][c][dir_entered] stores the final (R, C) if the robot lands at (r,c)
        # (which must be a mirror) and entered by moving in dir_entered.
        # dir_entered = 0: entered by moving RIGHT (from (r, c-1))
        # dir_entered = 1: entered by moving DOWN (from (r-1, c))
        # If (r,c) is an empty cell, it means the reflection chain stops there.
        # If the path goes out of bounds, it's represented by (-1, -1).
        # We initialize with (None, None) to distinguish from valid (r,c) or invalid (-1,-1).
        memo_chain = [[[(None, None) for _ in range(2)] for _ in range(n)] for _ in range(m)]

        # Precompute memo_chain using dynamic programming, iterating backwards.
        # This ensures that when we compute memo_chain[r][c][dir], the values for
        # (r+1, c) and (r, c+1) (which are "further" from the end of potential chains)
        # are already computed.
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                # Case 1: Current cell (r, c) is empty.
                # If a reflection chain leads to an empty cell, that's the final landing spot.
                if grid[r][c] == 0:
                    memo_chain[r][c][0] = (r, c) # If entered by moving Right, stop here
                    memo_chain[r][c][1] = (r, c) # If entered by moving Down, stop here
                # Case 2: Current cell (r, c) is a mirror.
                else: # grid[r][c] == 1
                    # If entered by moving RIGHT (dir_entered = 0)
                    # Reflection rule: turn DOWN, move to (r+1, c).
                    # The next reflection in the chain will be based on entering (r+1, c) by moving DOWN (dir=1).
                    next_r, next_c = r + 1, c
                    if next_r >= m: # Reflection target out of bounds
                        memo_chain[r][c][0] = (-1, -1)
                    else:
                        memo_chain[r][c][0] = memo_chain[next_r][next_c][1]

                    # If entered by moving DOWN (dir_entered = 1)
                    # Reflection rule: turn RIGHT, move to (r, c+1).
                    # The next reflection in the chain will be based on entering (r, c+1) by moving RIGHT (dir=0).
                    next_r, next_c = r, c + 1
                    if next_c >= n: # Reflection target out of bounds
                        memo_chain[r][c][1] = (-1, -1)
                    else:
                        memo_chain[r][c][1] = memo_chain[next_r][next_c][0]

        # go[r][c][dir_attempted] stores the final (R, C) if the robot starts at (r,c)
        # and attempts to move in dir_attempted.
        # dir_attempted = 0: attempt to move RIGHT to (r, c+1)
        # dir_attempted = 1: attempt to move DOWN to (r+1, c)
        go = [[[(None, None) for _ in range(2)] for _ in range(n)] for _ in range(m)]

        # Populate the 'go' table using the precomputed memo_chain.
        for r in range(m):
            for c in range(n):
                # Try to move RIGHT from (r, c) to (r, c+1)
                target_cell_r, target_cell_c = r, c + 1
                if target_cell_c >= n: # Attempted move leads out of bounds
                    go[r][c][0] = (-1, -1)
                elif grid[target_cell_r][target_cell_c] == 0: # Target cell is empty
                    go[r][c][0] = (target_cell_r, target_cell_c)
                else: # Target cell is a mirror
                    # Reflection rule: turn DOWN, move to (target_cell_r + 1, target_cell_c).
                    # The chain continues based on entering (target_cell_r + 1, target_cell_c) by moving DOWN (dir=1).
                    reflection_start_r, reflection_start_c = target_cell_r + 1, target_cell_c
                    if reflection_start_r >= m: # Initial reflection target out of bounds
                        go[r][c][0] = (-1, -1)
                    else:
                        go[r][c][0] = memo_chain[reflection_start_r][reflection_start_c][1]

                # Try to move DOWN from (r, c) to (r+1, c)
                target_cell_r, target_cell_c = r + 1, c
                if target_cell_r >= m: # Attempted move leads out of bounds
                    go[r][c][1] = (-1, -1)
                elif grid[target_cell_r][target_cell_c] == 0: # Target cell is empty
                    go[r][c][1] = (target_cell_r, target_cell_c)
                else: # Target cell is a mirror
                    # Reflection rule: turn RIGHT, move to (target_cell_r, target_cell_c + 1).
                    # The chain continues based on entering (target_cell_r, target_cell_c + 1) by moving RIGHT (dir=0).
                    reflection_start_r, reflection_start_c = target_cell_r, target_cell_c + 1
                    if reflection_start_c >= n: # Initial reflection target out of bounds
                        go[r][c][1] = (-1, -1)
                    else:
                        go[r][c][1] = memo_chain[reflection_start_r][reflection_start_c][0]

        # dp[r][c] stores the number of unique valid paths to reach cell (r, c).
        # Only empty cells can be reached.
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 # Start at (0,0) with one path.

        # Iterate through the grid in row-major order.
        # This ensures that when we compute dp[target_r][target_c],
        # dp[r][c] (which is "earlier" in the path) has already been computed.
        for r in range(m):
            for c in range(n):
                # If no paths reach (r, c), we can't extend from it.
                if dp[r][c] == 0:
                    continue

                # From (r, c), try to move RIGHT
                target_r, target_c = go[r][c][0]
                if target_r != -1: # Check if the move leads to a valid cell
                    dp[target_r][target_c] = (dp[target_r][target_c] + dp[r][c]) % MOD

                # From (r, c), try to move DOWN
                target_r, target_c = go[r][c][1]
                if target_r != -1: # Check if the move leads to a valid cell
                    dp[target_r][target_c] = (dp[target_r][target_c] + dp[r][c]) % MOD

        return dp[m - 1][n - 1]

```

## Why This Works
This solution works by breaking down a complex pathfinding problem into manageable subproblems using dynamic programming.
1.  **Precomputation (`memo_chain` and `go` tables):** By precomputing all possible "jump" destinations (including chained reflections and out-of-bounds checks), we transform the complex reflection logic into simple `O(1)` lookups. The backward iteration for `memo_chain` correctly resolves dependencies, ensuring that the final destination of any reflection chain is determined before it's needed.
2.  **Dynamic Programming (`dp` table):** The `dp[r][c]` state correctly accumulates the number of unique paths to reach each empty cell. The row-major iteration order guarantees that when we process cell `(r, c)`, all cells `(r', c')` from which `(r, c)` could be reached (i.e., `r' <= r` and `c' <= c`, with at least one inequality strict) have already had their `dp` values computed and propagated. This ensures that `dp[r][c]` holds the total count of paths from `(0,0)` to `(r,c)`.
3.  **Modulus Arithmetic:** Applying the modulo operation at each addition prevents integer overflow for large path counts.
4.  **Correctness of Reflection Rules:** The interpretation of "direction it used to enter that mirror" as the *immediate prior move* (or reflection step) is crucial and is correctly implemented in `memo_chain` and `go` table logic, matching the provided examples. The robot always lands on an empty cell.

Together, these steps ensure that all valid paths are counted exactly once, and invalid paths (out of bounds) are correctly discarded, leading to the correct total number of unique valid paths.

---
<sub>Generated 2026-10-31 06:12 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
