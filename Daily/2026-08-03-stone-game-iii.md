# [1406] Stone Game III

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-08-03 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/stone-game-iii/)

**Topics:** Array, Math, Dynamic Programming, Game Theory

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the first remaining stones in the row.

The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.

Example 1:

Input: stoneValue = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.

Example 2:

Input: stoneValue = [1,2,3,-9]
Output: "Alice"
Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. In the next move, Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. In the next move, Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.

Example 3:

Input: stoneValue = [1,2,3,6]
Output: "Tie"
Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.

Constraints:

- 1 <= stoneValue.length <= 5 * 10^4

- -1000 <= stoneValue[i] <= 1000

**Examples / sample tests:**

```
[1,2,3,7]
[1,2,3,-9]
[1,2,3,6]
```

---

## Problem Summary
Alice and Bob take turns removing 1, 2, or 3 stones from the beginning of a row. Each stone has an integer value. Both players aim to maximize their own score (sum of stone values taken). Alice starts first. The goal is to determine if Alice wins, Bob wins, or it's a tie, assuming optimal play from both.

## Intuition
This is a classic **game theory** problem, specifically an **impartial game** where the available moves depend only on the state, not on whose turn it is. Since both players play **optimally**, this problem can be solved using **dynamic programming** with a **minimax** approach.

The key insight is to consider the **score difference** (Alice's score - Bob's score) rather than their individual scores.
*   Alice wants to **maximize** this difference.
*   Bob wants to **minimize** this difference (which is equivalent to maximizing his own score, thus reducing Alice's score relative to his).

We can define `dp[i]` as the maximum score difference the *current player* can achieve when it's their turn and stones from index `i` to the end of the `stoneValue` array are remaining.

## Approach
1.  **Define DP State**: Let `dp[i]` be the maximum score difference (current player's score - opponent's score) that the *current player* can achieve when it's their turn and the stones `stoneValue[i], stoneValue[i+1], ..., stoneValue[N-1]` are available.
2.  **Base Cases**: If there are no stones left (`i >= N`), the score difference is `0`. To handle this gracefully in our DP array, we'll pad `dp` with zeros for indices `N, N+1, N+2`.
3.  **DP Transition**: To calculate `dp[i]`, the current player considers three optimal moves:
    *   **Take 1 stone**: The current player takes `stoneValue[i]`. Their score increases by `stoneValue[i]`. Now it's the *next player's* turn, starting from index `i+1`. The next player will play optimally to achieve `dp[i+1]` (from *their* perspective). From the *current player's* perspective, this `dp[i+1]` is a *loss* to their own score difference. So, this option yields a difference of `stoneValue[i] - dp[i+1]`.
    *   **Take 2 stones**: (If `i+1 < N`) The current player takes `stoneValue[i] + stoneValue[i+1]`. The next player plays from `i+2`. This option yields a difference of `(stoneValue[i] + stoneValue[i+1]) - dp[i+2]`.
    *   **Take 3 stones**: (If `i+2 < N`) The current player takes `stoneValue[i] + stoneValue[i+1] + stoneValue[i+2]`. The next player plays from `i+3`. This option yields a difference of `(stoneValue[i] + stoneValue[i+1] + stoneValue[i+2]) - dp[i+3]`.
    The current player will choose the move that maximizes their score difference:
    `dp[i] = max( (stoneValue[i] - dp[i+1]), (stoneValue[i] + stoneValue[i+1] - dp[i+2]), (stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3]) )`
    We must be careful with array bounds when accessing `stoneValue[i+1]` and `stoneValue[i+2]`.
4.  **Iteration Order**: We fill the `dp` table from right to left (from `i = N-1` down to `0`) because `dp[i]` depends on `dp[i+1]`, `dp[i+2]`, and `dp[i+3]`.
5.  **Final Result**: After computing `dp[0]`, which represents the maximum score difference Alice can achieve starting from the beginning:
    *   If `dp[0] > 0`, Alice wins.
    *   If `dp[0] < 0`, Bob wins.
    *   If `dp[0] == 0`, it's a Tie.

## Visualization
Let `N` be the length of `stoneValue`. We use a `dp` array of size `N+3` to simplify base cases where `i+k >= N`. `dp[N]`, `dp[N+1]`, `dp[N+2]` are initialized to 0.

```mermaid
graph TD
    subgraph DP Table Calculation (Right to Left)
        N_minus_1[dp[N-1]] --> N[dp[N]=0]
        N_minus_2[dp[N-2]] --> N_minus_1
        N_minus_2 --> N[dp[N]=0]
        N_minus_3[dp[N-3]] --> N_minus_2
        N_minus_3 --> N_minus_1
        N_minus_3 --> N[dp[N]=0]
        ...
        i[dp[i]] --> i_plus_1[dp[i+1]]
        i[dp[i]] --> i_plus_2[dp[i+2]]
        i[dp[i]] --> i_plus_3[dp[i+3]]
        ...
        dp0[dp[0]] --> dp1[dp[1]]
        dp0[dp[0]] --> dp2[dp[2]]
        dp0[dp[0]] --> dp3[dp[3]]
    end

    subgraph Decision Logic for dp[i]
        A[Current Player at index i] --> B{Take 1 stone: `val[i] - dp[i+1]`};
        A --> C{Take 2 stones: `val[i]+val[i+1] - dp[i+2]`};
        A --> D{Take 3 stones: `val[i]+val[i+1]+val[i+2] - dp[i+3]`};
        B --> E[dp[i] = max(B, C, D)];
        C --> E;
        D --> E;
    end
```

## Dry Run
Let's trace `stoneValue = [1,2,3,7]`. `N = 4`.
Initialize `dp = [0, 0, 0, 0, 0, 0, 0]` (size `N+3 = 7`). `dp[4]=0, dp[5]=0, dp[6]=0`.

| `i` | `stoneValue[i]` | Options (current player's score - next player's optimal difference) | `dp[i]` (max of options) |
| :-- | :-------------- | :------------------------------------------------------------------ | :------------------------ |
| `3` | `7`             | 1 stone: `7 - dp[4]` = `7 - 0` = `7`                               | `7`                       |
| `2` | `3`             | 1 stone: `3 - dp[3]` = `3 - 7` = `-4`                             | `10`                      |
|     |                 | 2 stones: `(3+7) - dp[4]` = `10 - 0` = `10`                       |                           |
| `1` | `2`             | 1 stone: `2 - dp[2]` = `2 - 10` = `-8`                            | `12`                      |
|     |                 | 2 stones: `(2+3) - dp[3]` = `5 - 7` = `-2`                        |                           |
|     |                 | 3 stones: `(2+3+7) - dp[4]` = `12 - 0` = `12`                     |                           |
| `0` | `1`             | 1 stone: `1 - dp[1]` = `1 - 12` = `-11`                           | `-1`                      |
|     |                 | 2 stones: `(1+2) - dp[2]` = `3 - 10` = `-7`                       |                           |
|     |                 | 3 stones: `(1+2+3) - dp[3]` = `6 - 7` = `-1`                      |                           |

Final result: `dp[0] = -1`. Since `dp[0] < 0`, **Bob wins**. This matches Example 1.

## Complexity
*   **Time Complexity**: `O(N)`. We iterate through the `dp` array once from `N-1` down to `0`. Each `dp[i]` calculation involves a constant number of arithmetic operations and array lookups (at most 3 options).
*   **Space Complexity**: `O(N)`. We use a `dp` array of size `N+3` to store the maximum score differences.

## Edge Cases
*   **`stoneValue.length = 1`**: Alice takes the single stone. `dp[0]` will be `stoneValue[0]`. The solution handles this as `i=0` will only consider taking 1 stone, and `dp[1]` will be 0.
*   **`stoneValue.length = 2` or `3`**: Similar to above, the loops correctly handle the available options (1, 2, or 3 stones) based on remaining stones.
*   **All negative stone values**: Alice will try to minimize her loss (or maximize Bob's loss). The DP formulation correctly calculates the optimal difference even with negative values.
*   **All positive stone values**: Alice will try to maximize her gain. The DP formulation correctly finds the best strategy.
The `float('-inf')` initialization ensures that even if all options result in negative differences, the maximum (least negative) is correctly chosen.

## Solution
```python
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        # dp[i] will store the maximum score difference (current player's score - opponent's score)
        # that the current player can achieve when stones from index i to n-1 are remaining.
        # We need dp[n], dp[n+1], dp[n+2] to be 0 as base cases (no stones left).
        # So, dp array size will be n + 3.
        dp = [0] * (n + 3) 
        
        # Iterate from the end of the stoneValue array backwards
        # i represents the starting index of the remaining stones for the current player's turn
        for i in range(n - 1, -1, -1):
            current_max_diff = float('-inf')
            
            # Option 1: Take 1 stone
            # Current player takes stoneValue[i].
            # The next player will play optimally from index i+1, resulting in dp[i+1] difference (from their perspective).
            # So, current player's difference = stoneValue[i] - dp[i+1]
            current_max_diff = max(current_max_diff, stoneValue[i] - dp[i+1])
            
            # Option 2: Take 2 stones
            # Check if there are at least 2 stones remaining (i+1 < n) to access stoneValue[i+1]
            if i + 1 < n:
                # Current player takes stoneValue[i] + stoneValue[i+1].
                # The next player plays optimally from index i+2.
                # Current player's difference = (stoneValue[i] + stoneValue[i+1]) - dp[i+2]
                current_max_diff = max(current_max_diff, (stoneValue[i] + stoneValue[i+1]) - dp[i+2])
            
            # Option 3: Take 3 stones
            # Check if there are at least 3 stones remaining (i+2 < n) to access stoneValue[i+2]
            if i + 2 < n:
                # Current player takes stoneValue[i] + stoneValue[i+1] + stoneValue[i+2].
                # The next player plays optimally from index i+3.
                # Current player's difference = (stoneValue[i] + stoneValue[i+1] + stoneValue[i+2]) - dp[i+3]
                current_max_diff = max(current_max_diff, (stoneValue[i] + stoneValue[i+1] + stoneValue[i+2]) - dp[i+3])
            
            dp[i] = current_max_diff
            
        # After filling the dp table, dp[0] represents the maximum score difference
        # Alice can achieve starting from the beginning of the game.
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"

```

## Why This Works
This dynamic programming approach correctly models the optimal play of both Alice and Bob using a **minimax strategy**. By defining `dp[i]` as the *maximum score difference the current player can achieve*, we implicitly account for the opponent's optimal play. When the current player makes a move, they add stones to their score, but then the *next player* (the opponent) will play optimally from the new state. The opponent's optimal play is to maximize *their* score difference, which from the current player's perspective, means minimizing the current player's score difference. This is captured by subtracting `dp[i+k]` (the opponent's optimal difference) from the current player's immediate gain. By iterating backward from the end of the game, we ensure that `dp[i+k]` values are always computed before `dp[i]`, guaranteeing correct optimal subproblem solutions.

---
<sub>Generated 2026-08-03 04:09 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
