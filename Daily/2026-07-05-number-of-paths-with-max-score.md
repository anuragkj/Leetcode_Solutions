# [1301] Number of Paths with Max Score

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-07-05 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/number-of-paths-with-max-score/)

**Topics:** Array, Dynamic Programming, Matrix

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.


You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.


Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.


In case there is no path, return [0, 0].




Example 1:

Input: board = ["E23","2X2","12S"]
Output: [7,1]

Example 2:

Input: board = ["E12","1X1","21S"]
Output: [4,2]

Example 3:

Input: board = ["E11","XXX","11S"]
Output: [0,0]




Constraints:




- 2 <= board.length == board[i].length <= 100

**Examples / sample tests:**

```
["E23","2X2","12S"]
["E12","1X1","21S"]
["E11","XXX","11S"]
```

---

## Problem Summary
You are given a square grid with numeric characters (1-9), obstacles ('X'), a start ('S'), and an end ('E'). Starting at 'S' (bottom-right), you can move up, left, or up-left (diagonally) to reach 'E' (top-left), avoiding 'X's. The goal is to find the maximum sum of numeric characters collected along any valid path, and the number of such paths, modulo 10^9 + 7. If no path exists, return `[0, 0]`.

## Intuition
This problem asks for an optimal path (maximum sum) and the count of such paths on a grid with restricted movements. This is a classic setup for **Dynamic Programming (DP)**.

1.  **Direction of Movement**: We start at 'S' (bottom-right) and move towards 'E' (top-left) by going up, left, or up-left. This means to reach a cell `(r, c)`, we must have come from `(r+1, c)` (down), `(r, c+1)` (right), or `(r+1, c+1)` (down-right). This "backward" dependency (from `(r+1, c)` to `(r, c)`) suggests that we should fill our DP table by iterating from the bottom-right corner towards the top-left corner.

2.  **Two DP Tables**: We need to track two pieces of information for each cell `(r, c)`:
    *   The **maximum score** achievable to reach `(r, c)` from 'S'. Let's call this `dp_score[r][c]`.
    *   The **number of paths** that achieve `dp_score[r][c]`. Let's call this `dp_paths[r][c]`.

3.  **Base Case**: The starting point 'S' is at `(N-1, N-1)`. When we are at 'S', we haven't collected any numeric characters yet, so its score is `0`. There is one way to be at 'S' (by starting there), so `dp_paths[N-1][N-1] = 1`.

4.  **Transitions**: For any other cell `(r, c)` (not 'X', not 'S'):
    *   Its numeric value `val` is `int(board[r][c])`. If it's 'E', `val` is `0`.
    *   We look at the three cells from which we could have come: `(r+1, c)`, `(r, c+1)`, and `(r+1, c+1)`.
    *   We find the `max_prev_score` among these three cells (only considering reachable ones).
    *   `dp_score[r][c]` will be `max_prev_score + val`.
    *   `dp_paths[r][c]` will be the sum of `dp_paths` from all previous cells that contributed to `max_prev_score`. This is crucial for counting paths correctly when multiple paths yield the same maximum score. Remember to apply modulo `10^9 + 7`.

## Approach
1.  **Initialization**:
    *   Get the board size `N = len(board)`.
    *   Define `MOD = 10**9 + 7`.
    *   Create two `N x N` DP tables: `dp_score` and `dp_paths`.
    *   Initialize `dp_score` with `float('-inf')` to represent unreachable states.
    *   Initialize `dp_paths` with `0`.

2.  **Base Case**:
    *   Set `dp_score[N-1][N-1] = 0` (score at 'S' is 0).
    *   Set `dp_paths[N-1][N-1] = 1` (one path to 'S' itself).

3.  **Iterate DP Tables**:
    *   Loop `r` from `N-1` down to `0` (inclusive).
    *   Loop `c` from `N-1` down to `0` (inclusive).

4.  **Handle Current Cell `(r, c)`**:
    *   If `board[r][c]` is `'X'`, this cell is an obstacle; skip it (it remains unreachable, `dp_score` stays `float('-inf')`, `dp_paths` stays `0`).
    *   If `(r, c)` is the 'S' cell (`N-1, N-1`), skip it as its base case is already handled.

5.  **Calculate `current_val`**:
    *   If `board[r][c]` is a digit, `current_val = int(board[r][c])`.
    *   If `board[r][c]` is `'E'`, `current_val = 0` (we don't collect 'E' itself).

6.  **Find Max Score and Path Count from Neighbors**:
    *   Initialize `max_prev_score = float('-inf')` and `num_max_paths = 0`.
    *   Consider the three possible "previous" cells: `(r+1, c)` (down), `(r, c+1)` (right), and `(r+1, c+1)` (down-right).
    *   For each potential previous cell `(pr, pc)`:
        *   Check if `(pr, pc)` is within board bounds (`pr < N` and `pc < N`).
        *   Check if `(pr, pc)` is reachable (`dp_score[pr][pc] != float('-inf')`).
        *   If valid and reachable:
            *   Let `candidate_score = dp_score[pr][pc]`.
            *   If `candidate_score > max_prev_score`: Update `max_prev_score = candidate_score` and `num_max_paths = dp_paths[pr][pc]`.
            *   If `candidate_score == max_prev_score`: Add `dp_paths[pr][pc]` to `num_max_paths` (modulo `MOD`).

7.  **Update `dp_score[r][c]` and `dp_paths[r][c]`**:
    *   If `max_prev_score` is still `float('-inf')`, it means `(r, c)` is unreachable from 'S'. Its `dp_score` and `dp_paths` remain their initial values.
    *   Otherwise, `dp_score[r][c] = max_prev_score + current_val`.
    *   `dp_paths[r][c] = num_max_paths`.

8.  **Final Result**:
    *   After filling the DP tables, the answer is `[dp_score[0][0], dp_paths[0][0]]`.
    *   If `dp_score[0][0]` is `float('-inf')` (meaning 'E' is unreachable), return `[0, 0]`.

## Visualization

Let's illustrate the DP table filling for `board = ["E23","2X2","12S"]`.
`N=3`. We iterate from `(2,2)` backwards to `(0,0)`.
`dp_score` initialized with `-inf`, `dp_paths` with `0`.
`S` is at `(2,2)`, `E` is at `(0,0)`.

**Initial State (after base case for 'S'):**

`dp_score` (Max Score to reach cell):
```
-inf  -inf  -inf
-inf  -inf  -inf
-inf  -inf    0  (S)
```

`dp_paths` (Number of paths for Max Score):
```
  0     0     0
  0     0     0
  0     0     1  (S)
```

**After processing cells `(2,1)` and `(2,0)`:**

`board[2][1] = '2'`. Came from `(2,2)` (score 0, paths 1). `dp_score[2][1] = 0 + 2 = 2`, `dp_paths[2][1] = 1`.
`board[2][0] = '1'`. Came from `(2,1)` (score 2, paths 1). `dp_score[2][0] = 2 + 1 = 3`, `dp_paths[2][0] = 1`.

`dp_score`:
```
-inf  -inf  -inf
-inf  -inf  -inf
  3     2     0
```

`dp_paths`:
```
  0     0     0
  0     0     0
  1     1     1
```

**After processing cells `(1,2)` and `(1,0)` (skipping `(1,1)` which is 'X'):**

`board[1][2] = '2'`. Came from `(2,2)` (score 0, paths 1). `dp_score[1][2] = 0 + 2 = 2`, `dp_paths[1][2] = 1`.
`board[1][0] = '2'`. Came from `(2,0)` (score 3, paths 1) or `(2,1)` (score 2, paths 1). Max is 3.
`dp_score[1][0] = 3 + 2 = 5`, `dp_paths[1][0] = 1`.

`dp_score`:
```
-inf  -inf  -inf
  5   -inf    2
  3     2     0
```

`dp_paths`:
```
  0     0     0
  1     0     1
  1     1     1
```

**After processing cells `(0,2)`, `(0,1)`, and `(0,0)`:**

`board[0][2] = '3'`. Came from `(1,2)` (score 2, paths 1). `dp_score[0][2] = 2 + 3 = 5`, `dp_paths[0][2] = 1`.
`board[0][1] = '2'`. Came from `(0,2)` (score 5, paths 1) or `(1,2)` (score 2, paths 1). Max is 5.
`dp_score[0][1] = 5 + 2 = 7`, `dp_paths[0][1] = 1`.
`board[0][0] = 'E'`. Came from `(1,0)` (score 5, paths 1) or `(0,1)` (score 7, paths 1). Max is 7.
`dp_score[0][0] = 7 + 0 = 7`, `dp_paths[0][0] = 1`.

`dp_score`:
```
  7     7     5
  5   -inf    2
  3     2     0
```

`dp_paths`:
```
  1     1     1
  1     0     1
  1     1     1
```

The final result is `[dp_score[0][0], dp_paths[0][0]] = [7, 1]`.

## Dry Run

Let's trace Example 1: `board = ["E23","2X2","12S"]`
`N = 3`, `MOD = 10^9 + 7`.

**DP Tables Initialization:**
`dp_score = [[-inf, -inf, -inf], [-inf, -inf, -inf], [-inf, -inf, -inf]]`
`dp_paths = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]`

**Base Case (S at (2,2)):**
`dp_score[2][2] = 0`
`dp_paths[2][2] = 1`

**Iteration (r from 2 down to 0, c from 2 down to 0):**

| `r` | `c` | `board[r][c]` | `current_val` | Neighbors (pr, pc) | `dp_score[pr][pc]` | `dp_paths[pr][pc]` | `max_prev_score` | `num_max_paths` | `dp_score[r][c]` | `dp_paths[r][c]` |
| :-- | :-- | :------------ | :------------ | :----------------- | :----------------- | :----------------- | :--------------- | :-------------- | :--------------- | :--------------- |
| 2   | 2   | 'S'           | -             | -                  | -                  | -                  | -                | -               | 0                | 1                |
| 2   | 1   | '2'           | 2             | (2,2)              | 0                  | 1                  | 0                | 1               | 2                | 1                |
| 2   | 0   | '1'           | 1             | (2,1)              | 2                  | 1                  | 2                | 1               | 3                | 1                |
| 1   | 2   | '2'           | 2             | (2,2)              | 0                  | 1                  | 0                | 1               | 2                | 1                |
| 1   | 1   | 'X'           | -             | -                  | -                  | -                  | -                | -               | -inf             | 0                |
| 1   | 0   | '2'           | 2             | (2,0)              | 3                  | 1                  | 3                | 1               | 5                | 1                |
|     |     |               |               | (2,1)              | 2                  | 1                  |                  |                 |                  |                  |
| 0   | 2   | '3'           | 3             | (1,2)              | 2                  | 1                  | 2                | 1               | 5                | 1                |
| 0   | 1   | '2'           | 2             | (0,2)              | 5                  | 1                  | 5                | 1               | 7                | 1                |
|     |     |               |               | (1,2)              | 2                  | 1                  |                  |                 |                  |                  |
| 0   | 0   | 'E'           | 0             | (0,1)              | 7                  | 1                  | 7                | 1               | 7                | 1                |
|     |     |               |               | (1,0)              | 5                  | 1                  |                  |                 |                  |                  |

**Final Result:** `dp_score[0][0] = 7`, `dp_paths[0][0] = 1`. Return `[7, 1]`.

## Complexity

*   **Time Complexity**: O(N^2)
    We iterate through each cell of the `N x N` board exactly once. For each cell, we perform a constant number of operations (checking up to 3 neighbors, comparisons, additions, modulo).
*   **Space Complexity**: O(N^2)
    We use two `N x N` DP tables (`dp_score` and `dp_paths`) to store intermediate results.

## Edge Cases

*   **No Path**: If 'E' is unreachable (e.g., surrounded by 'X's or 'S' is isolated), `dp_score[0][0]` will remain `float('-inf')`. The solution correctly returns `[0, 0]` in this scenario.
*   **Board with only 'E' and 'S'**: For `N=2`, `board = ["ES", "XX"]`. 'S' is at `(1,1)`, 'E' at `(0,0)`. No path exists. `dp_score[0][0]` will be `-inf`, returning `[0,0]`.
*   **All paths have the same maximum score**: The `num_max_paths` logic correctly sums `dp_paths` from all neighbors that achieve `max_prev_score`, ensuring all such paths are counted.
*   **Modulo Arithmetic**: The `MOD` constant is applied correctly to `num_max_paths` at each step to prevent integer overflow.
*   **'E' and 'S' values**: The problem states 'E' and 'S' are markers, not numeric characters. The solution correctly assigns `0` value to these cells when calculating sums.

## Solution

```python
import math
from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        N = len(board)
        MOD = 10**9 + 7

        # dp_score[r][c] stores the maximum score to reach (r, c) from 'S'
        # dp_paths[r][c] stores the number of paths to achieve dp_score[r][c]
        dp_score = [[float('-inf')] * N for _ in range(N)]
        dp_paths = [[0] * N for _ in range(N)]

        # Base case: Starting point 'S' at (N-1, N-1)
        # Score at 'S' itself is 0 (we don't collect 'S' value)
        # There is 1 path to 'S' itself
        dp_score[N-1][N-1] = 0
        dp_paths[N-1][N-1] = 1

        # Iterate from bottom-right to top-left
        # r goes from N-1 down to 0
        # c goes from N-1 down to 0
        for r in range(N - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                # If current cell is an obstacle 'X', it's unreachable.
                # If current cell is 'S', it's the base case, already handled.
                if board[r][c] == 'X' or (r == N - 1 and c == N - 1):
                    continue

                # Determine the numeric value of the current cell
                # 'E' and 'S' contribute 0 to the score. Digits contribute their value.
                current_val = 0
                if board[r][c].isdigit():
                    current_val = int(board[r][c])
                # If board[r][c] is 'E', current_val remains 0.

                max_prev_score = float('-inf')
                num_max_paths = 0

                # Check possible previous cells: (r+1, c) (down), (r, c+1) (right), (r+1, c+1) (down-right)
                # These are the cells from which we can move to (r, c)
                for dr, dc in [(1, 0), (0, 1), (1, 1)]:
                    pr, pc = r + dr, c + dc # Coordinates of the "previous" cell
                    
                    # Check if the previous cell is within bounds and reachable
                    if pr < N and pc < N and dp_score[pr][pc] != float('-inf'):
                        candidate_score = dp_score[pr][pc]
                        
                        if candidate_score > max_prev_score:
                            # Found a new maximum score path
                            max_prev_score = candidate_score
                            num_max_paths = dp_paths[pr][pc]
                        elif candidate_score == max_prev_score:
                            # Found another path with the same maximum score
                            num_max_paths = (num_max_paths + dp_paths[pr][pc]) % MOD

                # If current cell (r, c) is reachable from any valid previous cell
                if max_prev_score != float('-inf'):
                    dp_score[r][c] = max_prev_score + current_val
                    dp_paths[r][c] = num_max_paths
                # Else, dp_score[r][c] remains float('-inf') and dp_paths[r][c] remains 0,
                # indicating it's unreachable.

        # The final result is at the 'E' cell (0, 0)
        # If dp_score[0][0] is still -inf, it means 'E' is unreachable.
        if dp_score[0][0] == float('-inf'):
            return [0, 0]
        else:
            return [dp_score[0][0], dp_paths[0][0]]

```

## Why This Works

This dynamic programming approach works because the problem exhibits **optimal substructure** and **overlapping subproblems**. The maximum score (and corresponding path count) to reach any cell `(r, c)` can be optimally determined by knowing the maximum scores and path counts of the cells from which `(r, c)` can be reached (down, right, and down-right). By iterating from the destination ('S' at bottom-right) backwards to the source ('E' at top-left), we ensure that when we compute the values for `dp_score[r][c]` and `dp_paths[r][c]`, the required values from its "future" (or "previous" in terms of movement) cells are already computed and are optimal. This bottom-up (or end-to-start) computation guarantees that the final result for `dp_score[0][0]` and `dp_paths[0][0]` is correct. The path counting logic correctly aggregates paths from all preceding cells that lead to the maximum score, handling ties by summing their counts modulo `10^9 + 7`.

---
<sub>Generated 2026-07-05 04:43 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
