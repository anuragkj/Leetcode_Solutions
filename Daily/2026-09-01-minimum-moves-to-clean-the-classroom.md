# [3568] Minimum Moves to Clean the Classroom

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-09-01 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/)

**Topics:** Array, Hash Table, Bit Manipulation, Breadth-First Search, Matrix

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

- 'S': Starting position of the student

- 'L': Litter that must be collected (once collected, the cell becomes empty)

- 'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)

- 'X': Obstacle the student cannot pass through

- '.': Empty space

You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.

Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.

Example 1:

Input: classroom = ["S.", "XL"], energy = 2

Output: 2

Explanation:

- The student starts at cell (0, 0) with 2 units of energy.

- Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.

- A valid sequence of moves to collect all litter is as follows:

- Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.

- Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.

- The student collects all the litter using 2 moves. Thus, the output is 2.

Example 2:

Input: classroom = ["LS", "RL"], energy = 4

Output: 3

Explanation:

- The student starts at cell (0, 1) with 4 units of energy.

- A valid sequence of moves to collect all litter is as follows:

- Move 1: From (0, 1) → (0, 0) to collect the first litter 'L' with 1 unit of energy used and 3 units remaining.

- Move 2: From (0, 0) → (1, 0) to 'R' to reset and restore energy back to 4.

- Move 3: From (1, 0) → (1, 1) to collect the second litter 'L'.

- The student collects all the litter using 3 moves. Thus, the output is 3.

Example 3:

Input: classroom = ["L.S", "RXL"], energy = 3

Output: -1

Explanation:

No valid path collects all 'L'.

Constraints:

- 1 <= m == classroom.length <= 20

- 1 <= n == classroom[i].length <= 20

- classroom[i][j] is one of 'S', 'L', 'R', 'X', or '.'

- 1 <= energy <= 50

- There is exactly one 'S' in the grid.

- There are at most 10 'L' cells in the grid.

**Examples / sample tests:**

```
["S.", "XL"]
2
["LS", "RL"]
4
["L.S", "RXL"]
3
```

---

## Problem Summary
You need to find the minimum moves to collect all 'L' (litter) items in an `m x n` grid. You start at 'S' with `energy` units. Each move costs 1 energy. If energy drops to 0, you can only move to an 'R' (reset) cell, which restores energy to full capacity. 'X' cells are obstacles.

## Intuition
This problem asks for the *minimum* number of moves, which is a classic indicator for **Breadth-First Search (BFS)**. BFS explores the grid layer by layer, guaranteeing the shortest path in terms of steps.

However, a simple `(row, col)` state isn't enough. We also need to track:
1.  **Current Energy:** Moving consumes energy, and 'R' cells restore it. This affects which moves are valid.
2.  **Collected Litter:** We need to know which 'L's have been picked up to determine if we've reached the goal. Since there are at most 10 'L's, a **bitmask** is perfect for this. Each 'L' can be assigned an index (0-9), and a bit in the mask is set if that 'L' is collected.

Combining these, a state in our BFS will be `(row, col, current_energy, collected_litter_mask)`. To optimize, we'll use a `max_energy_at_state[row][col][mask]` table. If we reach the same `(row, col, mask)` state with *less* energy than previously recorded, we don't need to explore that path further, as it's either longer or worse (less energy for future moves).

## Approach
The optimal approach uses a **BFS with state compression and pruning**:

1.  **Preprocessing:**
    *   Initialize `m` (rows) and `n` (columns) from the `classroom` grid.
    *   Find the starting position `(start_r, start_c)` of 'S'.
    *   Identify all 'L' cells. Store their coordinates in a list `litter_coords` and create a mapping `litter_to_idx` from `(r, c)` to a unique index (0 to `num_litter - 1`).
    *   If `num_litter` is 0, return 0 moves immediately.
    *   Calculate `full_mask = (1 << num_litter) - 1`, which represents all litter collected.

2.  **BFS Initialization:**
    *   Create a `deque` (double-ended queue) for the BFS, `q`.
    *   Initialize a 3D array `max_energy_at_state[m][n][1 << num_litter]` with -1. This table will store the maximum energy achieved when reaching a specific `(row, col, mask)` state.
    *   Enqueue the initial state: `(start_r, start_c, initial_energy, 0, 0)` into `q`. The elements are `(row, col, current_energy, collected_litter_mask, moves)`.
    *   Set `max_energy_at_state[start_r][start_c][0] = initial_energy`.

3.  **BFS Loop:**
    *   While `q` is not empty:
        *   Dequeue `(r, c, current_e, mask, moves)`.
        *   **Goal Check:** If `mask == full_mask`, all litter has been collected. Return `moves`. This is the minimum because BFS explores shortest paths first.
        *   **Explore Neighbors:** For each of the four adjacent cells `(nr, nc)` (up, down, left, right):
            *   **Boundary Check:** If `(nr, nc)` is outside the grid, skip.
            *   **Obstacle Check:** If `classroom[nr][nc]` is 'X', skip.
            *   **Calculate Next State:**
                *   `next_e = current_e - 1` (cost of moving).
                *   `next_mask = mask`.
                *   **Energy Rules:**
                    *   If `next_e < 0` (ran out of energy):
                        *   If `classroom[nr][nc]` is 'R', `next_e` becomes `initial_energy` (reset).
                        *   Otherwise (cannot move with 0 energy to a non-'R' cell), skip this move.
                    *   If `classroom[nr][nc]` is 'R', `next_e` *always* becomes `initial_energy` (reset, even if `current_e` was positive).
                *   **Litter Collection:** If `classroom[nr][nc]` is 'L', update `next_mask` by setting the corresponding bit: `next_mask |= (1 << litter_to_idx[(nr, nc)])`.
            *   **Pruning:** If `next_e > max_energy_at_state[nr][nc][next_mask]`:
                *   This means we found a better path (same or fewer moves, but with more energy) to this `(nr, nc, next_mask)` state.
                *   Update `max_energy_at_state[nr][nc][next_mask] = next_e`.
                *   Enqueue `(nr, nc, next_e, next_mask, moves + 1)`.

4.  **No Solution:** If the `q` becomes empty and `full_mask` was never reached, it's impossible to collect all litter. Return -1.

## Visualization
Imagine the grid as a map. For each cell `(r, c)` and each possible combination of collected litter (represented by `mask`), we keep track of the *maximum energy* we've ever had when reaching that specific `(r, c, mask)` combination. This `max_energy_at_state` table is crucial for pruning.

```mermaid
graph TD
    subgraph Grid (m x n)
        A[Cell (0,0)]
        B[Cell (0,1)]
        C[Cell (1,0)]
        D[Cell (1,1)]
    end

    subgraph Mask States (2^num_litter)
        M0[Mask 000...0]
        M1[Mask 000...1]
        M2[Mask 000...10]
        ...
        MF[Mask 111...1]
    end

    subgraph max_energy_at_state[r][c][mask]
        E000["max_energy_at_state[0][0][M0]"]
        E001["max_energy_at_state[0][0][M1]"]
        E010["max_energy_at_state[0][1][M0]"]
        E111["max_energy_at_state[1][1][MF]"]
    end

    A --- E000
    A --- E001
    B --- E010
    D --- E111

    style E000 fill:#f9f,stroke:#333,stroke-width:2px
    style E001 fill:#f9f,stroke:#333,stroke-width:2px
    style E010 fill:#f9f,stroke:#333,stroke-width:2px
    style E111 fill:#f9f,stroke:#333,stroke-width:2px

    subgraph BFS Queue
        Q["(r, c, energy, mask, moves)"]
    end

    Q --> E000
    E000 --> Q
    E000 -- (move) --> E010
    E010 -- (move, collect L) --> E111
    E111 -- (goal) --> Result[Return moves]
```
In this diagram, each `max_energy_at_state` entry is a "node" in our conceptual search graph. When we explore a path, we update the `max_energy_at_state` for the new `(r, c, mask)` if we arrive with more energy. The BFS queue holds the states to explore next.

## Dry Run
Let's trace Example 1: `classroom = ["S.", "XL"], energy = 2`

*   `m=2, n=2`
*   `S` at `(0,0)`, `L` at `(1,1)`
*   `litter_coords = [(1,1)]`. `num_litter = 1`. `full_mask = (1 << 1) - 1 = 1`.
*   `litter_to_idx = {(1,1): 0}`.
*   `max_energy_at_state` is a `2x2x2` array, initialized to -1.

| Step | Dequeued `(r, c, e, mask, moves)` | New `(nr, nc, next_e, next_mask, moves+1)` | `max_energy_at_state` Update | Queue `[(r, c, e, mask, moves)]` | Notes |
| :--- | :-------------------------------- | :------------------------------------------ | :--------------------------- | :------------------------------- | :---- |
| 0    | (Initial)                         |                                             | `[0][0][0] = 2`              | `[(0,0,2,0,0)]`                  | Start at (0,0) with 2 energy, 0 litter collected, 0 moves. |
| 1    | `(0,0,2,0,0)`                     |                                             |                              | `[]`                             | `mask=0` != `full_mask=1`. |
|      |                                   | `(0,1,1,0,1)` (R)                           | `[0][1][0] = 1`              | `[(0,1,1,0,1)]`                  | Move R: `(0,0) -> (0,1)`. `e=2-1=1`. `mask=0`. `1 > -1`. Enqueue. |
|      |                                   | `(1,0)` (D)                                 |                              |                                  | `classroom[1][0]` is 'X'. Skip. |
| 2    | `(0,1,1,0,1)`                     |                                             |                              | `[]`                             | `mask=0` != `full_mask=1`. |
|      |                                   | `(1,1,0,1,2)` (D)                           | `[1][1][1] = 0`              | `[(1,1,0,1,2)]`                  | Move D: `(0,1) -> (1,1)`. `e=1-1=0`. Cell is 'L' (idx 0). `mask=0 | (1<<0) = 1`. `0 > -1`. Enqueue. |
|      |                                   | `(0,0,0,0,2)` (L)                           |                              |                                  | Move L: `(0,1) -> (0,0)`. `e=1-1=0`. `0` not `> max_energy_at_state[0][0][0](2)`. Skip. |
| 3    | `(1,1,0,1,2)`                     |                                             |                              | `[]`                             | `mask=1` == `full_mask=1`. **Return `moves=2`**. |

Final Result: 2

## Complexity
*   **Time Complexity:** `O(M * N * 2^L * E)` where `M` is rows, `N` is columns, `L` is `num_litter`, and `E` is `initial_energy`.
    *   There are `M * N * 2^L` unique `(row, col, mask)` states.
    *   Each such state can be visited up to `E` times (once for each possible energy level, due to the `max_energy_at_state` pruning).
    *   For each visit, we explore 4 neighbors.
    *   Given `M, N <= 20`, `L <= 10`, `E <= 50`, this is `20 * 20 * 2^10 * 50 = 400 * 1024 * 50 = 20,480,000` operations in the worst case, which is feasible within typical time limits.
*   **Space Complexity:** `O(M * N * 2^L)`
    *   The `max_energy_at_state` table uses `M * N * 2^L` integers.
    *   The BFS queue can hold up to `M * N * 2^L` states in the worst case (if all states are at the same BFS level).
    *   This is `20 * 20 * 2^10 = 409,600` integers, which is also feasible.

## Edge Cases
*   **No litter ('L' cells):** The solution correctly handles this by returning 0 immediately if `litter_coords` is empty.
*   **Start on an 'L' cell:** The problem statement implies 'S' is distinct from 'L'. If 'S' were on an 'L', the initial mask would need to reflect that 'L' as collected. However, the problem states `classroom[i][j]` is *one of* 'S', 'L', 'R', 'X', or '.', meaning 'S' cannot simultaneously be 'L'.
*   **No path to collect all litter:** If the BFS queue becomes empty and `full_mask` is never reached, the solution correctly returns -1.
*   **Energy management:**
    *   Moving to an 'R' cell always resets energy to `initial_energy`, regardless of current energy.
    *   Moving with 0 energy is only allowed if the target cell is 'R'.
    *   Moving with 1 energy to a non-'R' cell results in 0 energy at the destination, from which further moves are restricted.
    The energy logic in the code correctly implements these rules.
*   **Grid boundaries and obstacles ('X'):** Handled by explicit checks.

## Solution

```python
import collections
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        start_pos = (-1, -1)
        litter_coords = [] # Stores (r, c) for each 'L'
        
        # Preprocessing: Find S and all Ls
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_pos = (r, c)
                elif classroom[r][c] == 'L':
                    litter_coords.append((r, c))
        
        # If no litter, 0 moves needed.
        if not litter_coords:
            return 0
        
        num_litter = len(litter_coords)
        full_mask = (1 << num_litter) - 1 # All bits set to 1 when all litter collected

        # Map (r, c) of litter to its index for bitmasking
        litter_to_idx = {coord: i for i, coord in enumerate(litter_coords)}

        # BFS state: (row, col, current_energy, collected_litter_mask, moves)
        q = collections.deque()

        # max_energy_at_state[r][c][mask] stores the maximum energy
        # achieved when reaching (r, c) with 'mask' collected litter.
        # Initialize with -1 to indicate not visited or lower energy.
        max_energy_at_state = [[[-1] * (1 << num_litter) for _ in range(n)] for _ in range(m)]

        # Initial state
        start_r, start_c = start_pos
        q.append((start_r, start_c, energy, 0, 0))
        max_energy_at_state[start_r][start_c][0] = energy

        # Directions: Up, Down, Left, Right
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while q:
            r, c, current_e, mask, moves = q.popleft()

            # If all litter collected, return moves
            if mask == full_mask:
                return moves

            # Explore neighbors
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                # Boundary check
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                cell_type = classroom[nr][nc]

                # Obstacle check
                if cell_type == 'X':
                    continue

                next_e = current_e - 1 # Cost of move

                # Energy check and update
                if next_e < 0: # Ran out of energy (current_e was 0)
                    if cell_type == 'R':
                        next_e = energy # Reset energy
                    else:
                        # Cannot move if 0 energy and not an 'R' cell
                        continue
                
                # If moving to an 'R' cell, energy is reset to full capacity
                # This applies even if current_e was > 0 before the move.
                if cell_type == 'R':
                    next_e = energy
                
                next_mask = mask
                # If moving to an 'L' cell, update mask
                if cell_type == 'L':
                    l_idx = litter_to_idx[(nr, nc)]
                    next_mask |= (1 << l_idx)
                
                # Pruning: Only enqueue if this path is better (more energy)
                # or if this state (nr, nc, next_mask) hasn't been visited yet
                if next_e > max_energy_at_state[nr][nc][next_mask]:
                    max_energy_at_state[nr][nc][next_mask] = next_e
                    q.append((nr, nc, next_e, next_mask, moves + 1))
        
        # If queue exhausted and full_mask not reached, it's impossible
        return -1

```

## Why This Works
This solution works because it combines **Breadth-First Search (BFS)** with a crucial **state optimization**. BFS inherently finds the shortest path in terms of the number of moves. By including `current_energy` and `collected_litter_mask` in our state definition, we ensure that every relevant aspect of the student's progress is tracked. The `max_energy_at_state` table acts as a pruning mechanism: if we arrive at a `(row, col, mask)` state with less energy than a previously found path to the *exact same state*, we know that the current path is suboptimal (it's either longer or equally long but leaves us with less energy for future moves), so we don't need to explore it further. This prevents redundant computations and ensures that when we first reach the `full_mask` state, it's via the minimum number of moves.

---
<sub>Generated 2026-09-01 05:32 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
