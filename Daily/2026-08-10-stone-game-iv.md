# [1510] Stone Game IV

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-08-10 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/stone-game-iv/)

**Topics:** Math, Dynamic Programming, Minimax, Game Theory, Nim Game, Sprague–Grundy Theorem, Zero-Sum Game

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.

Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).

Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).

Constraints:

- 1 <= n <= 10^5

**Examples / sample tests:**

```
1
2
4
```

---

## Problem Summary
Alice and Bob take turns removing a non-zero square number of stones from a pile. Alice starts. The player who cannot make a move loses. We need to determine if Alice wins, assuming both play optimally.

## Intuition
This is a classic **game theory** problem, specifically an impartial game. When players play optimally, the outcome of a game state (number of stones) can be classified as either a **winning (W)** or **losing (L)** state for the player whose turn it is.

The key observations are:
1.  A state is a **losing state (L)** if *all* possible moves from it lead to **winning states (W)** for the *next* player.
2.  A state is a **winning state (W)** if there exists *at least one* move from it that leads to a **losing state (L)** for the *next* player.
3.  The base case: `0` stones is a **losing state** because the current player cannot make any move.

This recursive definition, combined with the fact that we'll encounter the same subproblems (number of stones) multiple times, strongly suggests using **Dynamic Programming**. We can build up our solution from `0` stones to `n` stones.

## Approach
We will use a dynamic programming array, `dp`, to store whether a given number of stones represents a winning or losing state for the current player.

1.  **Initialize `dp` array**: Create a boolean array `dp` of size `n + 1`. `dp[i]` will be `True` if the player whose turn it is can win with `i` stones, and `False` otherwise.
2.  **Base Case**: Set `dp[0] = False`. If there are `0` stones, the current player cannot make a move and thus loses.
3.  **Iterate and Fill `dp`**: Loop `i` from `1` to `n` (representing the number of stones):
    *   For each `i`, we want to determine `dp[i]`. Assume initially that `i` is a losing state (`dp[i] = False`).
    *   Consider all possible square numbers `k*k` that can be removed from `i` (i.e., `k*k <= i`).
    *   For each `k*k`, if the current player removes `k*k` stones, `i - k*k` stones will remain for the next player.
    *   Check the value of `dp[i - k*k]`:
        *   If `dp[i - k*k]` is `False` (meaning `i - k*k` is a losing state for the *next* player), then the current player can make this move and force the opponent into a losing state. Therefore, `i` is a **winning state** for the current player. Set `dp[i] = True` and `break` from the inner loop (no need to check further moves for `i`, as one winning move is enough).
        *   If `dp[i - k*k]` is `True` for *all* possible `k*k` moves (meaning all moves lead to winning states for the *next* player), then `i` remains a **losing state** for the current player (`dp[i]` stays `False`).
4.  **Result**: After filling the `dp` array up to `n`, `dp[n]` will tell us if Alice (the first player) can win with `n` stones.

## Visualization

Let's visualize the `dp` array and how `dp[i]` depends on previous states.
`dp[i]` is `True` (Alice wins) if she can move to a state `j` where `dp[j]` is `False` (Bob loses).

```
dp array (size n+1):
Index: 0  1  2  3  4  5  6  7  8  9 ... n
Value: F  ?  ?  ?  ?  ?  ?  ?  ?  ? ... ?

To determine dp[i]:
  Iterate k from 1 up to sqrt(i):
    Let square_move = k*k
    If dp[i - square_move] is FALSE (meaning opponent would be in a losing state):
      Then dp[i] is TRUE (current player wins)
      Break (found a winning move)
  If no such move found, dp[i] remains FALSE.

Example for dp[4]:
  dp[0] = F (base case)
  dp[1] = T (can remove 1, leaves 0. dp[0] is F)
  dp[2] = F (can only remove 1, leaves 1. dp[1] is T. All moves lead to W for opponent)
  dp[3] = T (can remove 1, leaves 2. dp[2] is F)

  Now for dp[4]:
  1. Try removing 1*1 = 1 stone:
     Remaining stones: 4 - 1 = 3.
     Check dp[3]. dp[3] is T. (This move leads to a winning state for Bob).
  2. Try removing 2*2 = 4 stones:
     Remaining stones: 4 - 4 = 0.
     Check dp[0]. dp[0] is F. (This move leads to a losing state for Bob!).
     Since we found a move to a losing state for Bob, Alice wins.
     Set dp[4] = TRUE and stop checking further moves for i=4.

Resulting dp table (partial):
Index: 0  1  2  3  4  5  6  7  8  9
Value: F  T  F  T  T  F  T  F  T  T
```

## Dry Run
Let's trace for `n = 1`:

1.  **Initialize `dp`**: `dp = [False, False]` (size `n+1 = 2`)
    *   `dp[0]` is already `False` (base case).

2.  **Loop `i` from `1` to `1`**:
    *   **`i = 1`**:
        *   Initially, `dp[1]` is `False`.
        *   **Inner loop for `k`**: `k` goes from `1` up to `int(math.sqrt(1)) = 1`.
            *   **`k = 1`**:
                *   `square_move = 1 * 1 = 1`.
                *   `remaining_stones = i - square_move = 1 - 1 = 0`.
                *   Check `dp[remaining_stones]`, which is `dp[0]`.
                *   `dp[0]` is `False`.
                *   Since `dp[0]` is `False`, it means if Alice removes 1 stone, Bob will be left with 0 stones, which is a losing state for Bob.
                *   Therefore, `dp[1]` becomes `True`.
                *   `break` from the inner loop (Alice found a winning move).

3.  **End of loop**: The loop finishes.

**Final Result**: `dp[1]` is `True`. Alice wins.

## Complexity
*   **Time Complexity**: O(N * sqrt(N)). The outer loop runs `N` times (for `i` from `1` to `N`). The inner loop runs `sqrt(i)` times (for `k` from `1` to `sqrt(i)`). In the worst case, `i` is `N`, so the inner loop runs `sqrt(N)` times.
*   **Space Complexity**: O(N). We use a boolean array `dp` of size `N + 1` to store the results of subproblems.

## Edge Cases
*   **`n = 1`**: Alice removes 1 stone, leaving 0. Bob has no moves and loses. Alice wins. Our `dp[1]` correctly evaluates to `True`.
*   **`n = 2`**: Alice can only remove 1 stone, leaving 1. Bob then removes 1 stone, leaving 0. Alice has no moves and loses. Bob wins, so Alice loses. Our `dp[2]` correctly evaluates to `False`.
*   **`n` is a perfect square (e.g., `n = 4`)**: Alice can remove `n` stones (e.g., 4 stones), leaving 0. Bob has no moves and loses. Alice wins. Our `dp[4]` correctly evaluates to `True` because `dp[4 - 2*2] = dp[0]` which is `False`.
The DP approach naturally handles these cases by building up the solution from smaller states.

## Solution

```python
import math

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] will store True if the current player can win with 'i' stones,
        # and False otherwise.
        # The array is of size n+1 to cover states from 0 to n.
        dp = [False] * (n + 1)

        # Base case: dp[0] is False. If there are 0 stones, the current player
        # cannot make a move and thus loses.

        # Iterate through all possible number of stones from 1 up to n.
        for i in range(1, n + 1):
            # For each 'i' stones, try all possible square number moves.
            # A player can remove k*k stones, where k*k <= i.
            # We only need to check k up to sqrt(i).
            for k in range(1, int(math.sqrt(i)) + 1):
                square_move = k * k
                
                # If the current player removes 'square_move' stones,
                # the opponent will be left with 'i - square_move' stones.
                
                # If dp[i - square_move] is False, it means the opponent
                # will be in a losing state.
                # If the current player can force the opponent into a losing state,
                # then the current state 'i' is a winning state for the current player.
                if not dp[i - square_move]:
                    dp[i] = True
                    # Once we find a winning move for the current state 'i',
                    # we don't need to check any other moves for 'i'.
                    # The current player just needs one path to victory.
                    break
        
        # The final answer for Alice starting with 'n' stones is dp[n].
        return dp[n]

```

## Why This Works
This dynamic programming solution works because it correctly implements the principles of optimal play in an impartial game. By iterating from `0` to `n` stones, we ensure that when we calculate `dp[i]`, the results for all smaller states `dp[j]` (where `j < i`) are already computed and represent the optimal outcome for those states. A state `i` is marked as `True` (winning) if the current player can make *any* move that leads to a state `j` where `dp[j]` is `False` (a losing state for the *next* player). Conversely, if *all* possible moves from `i` lead to states `j` where `dp[j]` is `True` (winning states for the *next* player), then `i` is marked as `False` (losing) for the current player. This "minimax" logic, applied bottom-up, guarantees that `dp[n]` accurately reflects whether Alice can win assuming perfect play.

---
<sub>Generated 2026-08-10 02:42 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
