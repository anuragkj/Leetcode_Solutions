# [1140] Stone Game II

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-08-09 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/stone-game-ii/)

**Topics:** Array, Math, Dynamic Programming, Minimax, Prefix Sum, Game Theory, Zero-Sum Game

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example 1:

Input: piles = [2,7,9,4,4]

Output: 10

Explanation:

- If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 stones in total.

- If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 stones in total.

So we return 10 since it's larger.

Example 2:

Input: piles = [1,2,3,4,5,100]

Output: 104

Constraints:

- 1 <= piles.length <= 100

- 1 <= piles[i] <= 10^4

**Examples / sample tests:**

```
[2,7,9,4,4]
[1,2,3,4,5,100]
```

---

## Problem Summary
Alice and Bob play a game with piles of stones arranged in a row. Players take turns taking stones from the beginning of the remaining piles. On each turn, a player can take `X` piles (where `1 <= X <= 2M`), and then `M` is updated to `max(M, X)`. Initially, `M=1` and Alice starts. The goal is for Alice to maximize her total stones, assuming both play optimally.

## Intuition
This is a classic **game theory** problem, specifically a **zero-sum game** (since the total number of stones is fixed, maximizing one player's score is equivalent to minimizing the other's). When players play **optimally**, we use a **minimax** strategy: Alice tries to maximize her score, knowing Bob will try to minimize Alice's score (or maximize his own).

The state of the game is determined by two factors:
1.  The **index of the first remaining pile** (`i`).
2.  The **current value of `M`** (`m`).

This immediately suggests **Dynamic Programming (DP)**. Since players take piles from the beginning, the subproblems naturally involve suffixes of the `piles` array (`piles[i:]`). We'll work **backwards** from the end of the piles to fill our DP table.

## Approach
1.  **Define DP State**: Let `dp[i][m]` be the maximum number of stones the *current player* can get if it's their turn, starting from `piles[i]` with the current `M` value being `m`.

2.  **Precompute Suffix Sums**: To efficiently calculate the sum of stones in a range `piles[i:j]`, we'll precompute `suffix_sum[k]`, which stores the sum of `piles[k]` through `piles[n-1]`. This allows `sum(piles[i:j])` to be calculated as `suffix_sum[i] - suffix_sum[j]`.

3.  **Base Cases**:
    *   If `i >= n` (no piles left), the current player gets 0 stones. This is implicitly handled by initializing our DP table with zeros and ensuring `suffix_sum[n]` is 0.
    *   If the current player can take all remaining piles (i.e., `n - i <= 2 * m`, or `i + 2 * m >= n`), they will do so to maximize their score. In this case, `dp[i][m] = suffix_sum[i]`.

4.  **Recursive Relation (Minimax)**:
    *   For `dp[i][m]`, the current player considers taking `X` piles, where `1 <= X <= 2 * m`.
    *   The number of stones the current player takes in this turn is `current_take = suffix_sum[i] - suffix_sum[i+X]`.
    *   After taking `X` piles, the game state changes to `(i+X, max(m, X))`.
    *   Now it's the *opponent's* turn. The opponent will play optimally from this new state and get `dp[i+X][max(m, X)]` stones from the remaining `suffix_sum[i+X]` piles.
    *   Therefore, the current player will get `suffix_sum[i+X] - dp[i+X][max(m, X)]` stones from the subgame starting at `piles[i+X]`.
    *   The total stones for the current player for a given `X` choice is:
        `current_take + (stones_from_subgame)`
        `= (suffix_sum[i] - suffix_sum[i+X]) + (suffix_sum[i+X] - dp[i+X][max(m, X)])`
        `= suffix_sum[i] - dp[i+X][max(m, X)]`
    *   The current player wants to maximize this value over all possible `X`. So, `dp[i][m] = max(suffix_sum[i] - dp[i+X][max(m, X)])` for `1 <= X <= 2 * m`.

5.  **Iteration Order**: We fill the `dp` table bottom-up:
    *   `i` (starting pile index) from `n-1` down to `0`.
    *   `m` (current `M` value) from `1` up to `n` (since `M` can grow up to `n` if a player takes `n` piles).

6.  **Final Result**: Alice starts at `piles[0]` with `M=1`. So, the answer is `dp[0][1]`.

## Visualization

Let `N` be `len(piles)`.
We use a 2D DP table `dp[i][m]` of size `N x (N+1)`.
`suffix_sum` array of size `N+1`.

```
DP Table (dp[i][m]):
m (current M) -> 1   2   3   ...   N
i (start index)
|
v
N-1  [val][val][val]...[val]  <-- Compute this row first
N-2  [val][val][val]...[val]  <-- Then this row
...
0    [val][val][val]...[val]  <-- Finally this row (dp[0][1] is our answer)

Computation Direction:
- `i` iterates from `N-1` down to `0`.
- `m` iterates from `1` up to `N`.

Dependency:
To calculate `dp[i][m]`, we look at `dp[i+X][max(m, X)]` for various `X`.
Since `i+X > i`, `dp[i][m]` depends on values in rows *below* it (rows with larger `i` indices), which have already been computed.
```

## Dry Run
Let's trace `piles = [2,7,9,4,4]`. `n = 5`.

1.  **Precompute Suffix Sums**:
    `suffix_sum = [26, 24, 17, 8, 4, 0]`
    (e.g., `suffix_sum[0]=2+7+9+4+4=26`, `suffix_sum[4]=4`, `suffix_sum[5]=0`)

2.  **Initialize DP Table**: `dp` table of size `5 x 6` (indices `0..4` for `i`, `0..5` for `m`) initialized to `0`.

3.  **Fill DP Table (Bottom-Up)**:

    *   **`i = 4` (piles `[4]`)**:
        *   For any `m >= 1`: `i + 2*m = 4 + 2*m`. Since `n=5`, `4 + 2*m >= 5` is true for `m >= 1`.
        *   Base case applies: current player can take all remaining piles.
        *   `dp[4][m] = suffix_sum[4] = 4` for all `m` from `1` to `5`.

    *   **`i = 3` (piles `[4,4]`)**:
        *   For any `m >= 1`: `i + 2*m = 3 + 2*m`. Since `n=5`, `3 + 2*m >= 5` is true for `m >= 1`.
        *   Base case applies: current player can take all remaining piles.
        *   `dp[3][m] = suffix_sum[3] = 8` for all `m` from `1` to `5`.

    *   **`i = 2` (piles `[9,4,4]`)**:
        *   `m = 1`: `i + 2*m = 2 + 2*1 = 4`. `4 < n=5`. Not base case.
            *   `X=1`: Take `piles[2]=9`. Score: `suffix_sum[2] - dp[2+1][max(1,1)] = suffix_sum[2] - dp[3][1] = 17 - 8 = 9`.
            *   `X=2`: Take `piles[2:4]=[9,4]`. Score: `suffix_sum[2] - dp[2+2][max(1,2)] = suffix_sum[2] - dp[4][2] = 17 - 4 = 13`.
            *   `dp[2][1] = max(9, 13) = 13`.
        *   `m = 2`: `i + 2*m = 2 + 2*2 = 6`. `6 >= n=5`. Base case applies.
            *   `dp[2][2] = suffix_sum[2] = 17`.
        *   For `m > 2`, `dp[2][m] = 17` (base case applies).

    *   **`i = 1` (piles `[7,9,4,4]`)**:
        *   `m = 1`: `i + 2*m = 1 + 2*1 = 3`. `3 < n=5`. Not base case.
            *   `X=1`: Take `piles[1]=7`. Score: `suffix_sum[1] - dp[1+1][max(1,1)] = suffix_sum[1] - dp[2][1] = 24 - 13 = 11`.
            *   `X=2`: Take `piles[1:3]=[7,9]`. Score: `suffix_sum[1] - dp[1+2][max(1,2)] = suffix_sum[1] - dp[3][2] = 24 - 8 = 16`.
            *   `dp[1][1] = max(11, 16) = 16`.
        *   `m = 2`: `i + 2*m = 1 + 2*2 = 5`. `5 >= n=5`. Base case applies.
            *   `dp[1][2] = suffix_sum[1] = 24`.
        *   For `m > 2`, `dp[1][m] = 24` (base case applies).

    *   **`i = 0` (piles `[2,7,9,4,4]`)**:
        *   `m = 1`: `i + 2*m = 0 + 2*1 = 2`. `2 < n=5`. Not base case.
            *   `X=1`: Take `piles[0]=2`. Score: `suffix_sum[0] - dp[0+1][max(1,1)] = suffix_sum[0] - dp[1][1] = 26 - 16 = 10`.
            *   `X=2`: Take `piles[0:2]=[2,7]`. Score: `suffix_sum[0] - dp[0+2][max(1,2)] = suffix_sum[0] - dp[2][2] = 26 - 17 = 9`.
            *   `dp[0][1] = max(10, 9) = 10`.
        *   For `m > 1`, `dp[0][m]` would be calculated, but we only need `dp[0][1]`.

4.  **Final Result**: `dp[0][1] = 10`. This matches Example 1.

## Complexity
*   **Time Complexity**: `O(N^3)`
    *   We have `N` states for `i` (from `0` to `N-1`).
    *   We have `N` states for `m` (from `1` to `N`).
    *   For each `(i, m)` state, we iterate `X` from `1` up to `2*m`. In the worst case, `m` can be `N`, so `X` iterates up to `2N` times.
    *   Total: `N * N * (2N) = O(N^3)`. Given `N <= 100`, `100^3 = 1,000,000` operations, which is efficient enough.
*   **Space Complexity**: `O(N^2)`
    *   `dp` table: `N` rows, `N+1` columns, so `O(N^2)`.
    *   `suffix_sum` array: `N+1` elements, so `O(N)`.
    *   Total: `O(N^2)`. Given `N <= 100`, `100^2 = 10,000` cells, which is well within memory limits.

## Edge Cases
*   **`piles.length = 1`**: If `piles = [5]`, `n=1`.
    *   `suffix_sum = [5, 0]`.
    *   When `i=0, m=1`: `i + 2*m = 0 + 2*1 = 2`. Since `2 >= n=1`, the base case applies.
    *   `dp[0][1] = suffix_sum[0] = 5`. Correct, Alice takes the only pile.
*   **All piles are equal**: The logic remains the same; the optimal choices will still be determined by the minimax strategy.
*   **Large pile values**: `piles[i]` up to `10^4`. `suffix_sum` can reach `100 * 10^4 = 10^6`. This fits within standard integer types and doesn't affect complexity.

## Solution

```python
import math
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # Precompute suffix sums
        # suffix_sum[i] stores the sum of piles[i] to piles[n-1]
        # suffix_sum[n] will be 0, representing sum of an empty suffix
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i+1]

        # dp[i][m] stores the maximum stones the current player can get
        # when starting from piles[i] with current M value as m.
        # i: index of the first remaining pile (0 to n-1)
        # m: current M value (1 to n)
        # We need n rows (for i=0 to n-1) and n+1 columns (for m=0 to n, using 1-based indexing for m)
        dp = [[0] * (n + 1) for _ in range(n)]

        # Iterate i from n-1 down to 0 (working backwards from the end of piles)
        for i in range(n - 1, -1, -1):
            # Iterate m from 1 up to n (M can grow up to n)
            for m in range(1, n + 1):
                # Base case: If the current player can take all remaining piles, they do.
                # This happens if 2*m is greater than or equal to the number of remaining piles (n - i).
                # Or equivalently, if i + 2*m >= n.
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sum[i]
                else:
                    # Current player wants to maximize their score.
                    # Initialize with a very small number (or 0 since pile values are positive)
                    max_stones_for_current_player = 0 
                    
                    # Current player can take X piles, where 1 <= X <= 2*m.
                    # The loop for X implicitly ensures i+X < n because of the `if i + 2*m >= n` check.
                    # If `i + 2*m < n`, then `n - i > 2*m`.
                    # So, any `X` in `1..2*m` will satisfy `X < n - i`, meaning `i+X < n`.
                    # Thus, `dp[i+X]` will always be a valid index in the dp table.
                    for x in range(1, 2 * m + 1):
                        # The total stones from piles[i:] is suffix_sum[i].
                        # If current player takes x piles, the remaining piles are piles[i+x:].
                        # The next player (opponent) will play from piles[i+x:] with new M = max(m, x).
                        # The opponent will get dp[i+x][max(m, x)] stones from piles[i+x:].
                        # So, the current player gets (total stones in piles[i+x:] - opponent's stones) from the subgame.
                        # This is (suffix_sum[i+x] - dp[i+x][max(m, x)]).
                        # Add the stones current player took in this turn: (suffix_sum[i] - suffix_sum[i+x]).
                        # Total for current player = (suffix_sum[i] - suffix_sum[i+x]) + (suffix_sum[i+x] - dp[i+x][max(m, x)]).
                        # This simplifies to: suffix_sum[i] - dp[i+x][max(m, x)].
                        
                        current_player_score_if_take_x = suffix_sum[i] - dp[i + x][max(m, x)]
                        max_stones_for_current_player = max(max_stones_for_current_player, current_player_score_if_take_x)
                    dp[i][m] = max_stones_for_current_player

        # Alice starts at piles[0] with M=1.
        # The value dp[0][1] represents the maximum stones Alice can get.
        return dp[0][1]

```

## Why This Works
This solution works because it correctly models the game as a **minimax problem** using **dynamic programming**. By defining `dp[i][m]` as the maximum stones the *current player* can get from `piles[i:]` with `M=m`, we capture the optimal play of both Alice and Bob. Alice (the current player) maximizes her score by choosing `X` such that `(total_stones_from_current_state - opponent's_optimal_score_from_next_state)` is maximized. Since the opponent also plays optimally, `opponent's_optimal_score_from_next_state` is precisely `dp[i+X][max(m,X)]`. The bottom-up approach ensures that when `dp[i][m]` is computed, all necessary `dp[i+X][max(m,X)]` values (which correspond to subproblems further down the pile list) have already been calculated. This guarantees that `dp[0][1]` will hold Alice's maximum possible score under optimal play.

---
<sub>Generated 2026-08-09 02:36 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
