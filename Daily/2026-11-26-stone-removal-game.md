# [3360] Stone Removal Game

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-11-26 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/stone-removal-game/)

**Topics:** Math, Simulation

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.

- Alice starts by removing exactly 10 stones on her first turn.

- For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.

The player who cannot make a move loses the game.

Given a positive integer n, return true if Alice wins the game and false otherwise.

Example 1:

Input: n = 12

Output: true

Explanation:

- Alice removes 10 stones on her first turn, leaving 2 stones for Bob.

- Bob cannot remove 9 stones, so Alice wins.

Example 2:

Input: n = 1

Output: false

Explanation:

- Alice cannot remove 10 stones, so Alice loses.

Constraints:

- 1 <= n <= 50

**Examples / sample tests:**

```
12
1
```

---

## Problem Summary
Alice and Bob take turns removing stones from a pile. Alice starts by removing 10 stones. In subsequent turns, each player removes exactly 1 fewer stone than the opponent's previous move. The player who cannot make a valid move loses. Given the initial number of stones `n`, determine if Alice wins.

## Intuition
The game involves a decreasing number of stones to be removed each turn (10, then 9, then 8, and so on). The initial number of stones `n` is very small (up to 50). This suggests that the game will end quickly, as the total number of stones removed cannot exceed `10 + 9 + ... + 1 = 55`. Therefore, we can **simulate** the game turn by turn, keeping track of the remaining stones and whose turn it is, until a player is unable to make a move.

## Approach
1.  Initialize `current_stones` with the given `n`.
2.  Initialize `stones_to_remove_this_turn` to `10`, as Alice removes 10 stones on her first turn.
3.  Initialize a boolean `is_alice_turn` to `True`.
4.  Enter a loop that continues until a winner is determined:
    a.  **Check for losing condition:** A player loses if they cannot make a valid move. A move is valid only if:
        *   The `stones_to_remove_this_turn` is a positive number.
        *   The `current_stones` in the pile are greater than or equal to `stones_to_remove_this_turn`.
        If either of these conditions is not met (`stones_to_remove_this_turn <= 0` or `current_stones < stones_to_remove_this_turn`), the current player loses.
        *   If `is_alice_turn` is `True` (Alice loses), return `False`.
        *   If `is_alice_turn` is `False` (Bob loses), return `True` (Alice wins).
    b.  **Make a move:** If the current player can make a move:
        *   Subtract `stones_to_remove_this_turn` from `current_stones`.
        *   Update `stones_to_remove_this_turn` for the *next* turn by decrementing it by 1 (`stones_to_remove_this_turn -= 1`).
        *   Switch turns by toggling `is_alice_turn` (`is_alice_turn = not is_alice_turn`).
5.  The loop will eventually terminate by returning `True` or `False`.

## Visualization

```
Game State Progression:
-------------------------------------------------------------------
Turn | Player | Stones to Remove (S) | Remaining Stones (N) | Outcome
-------------------------------------------------------------------
1    | Alice  | 10                   | N_initial            |
     |        |                      | N_initial - 10       |
-------------------------------------------------------------------
2    | Bob    | 9                    | N_initial - 10       |
     |        |                      | N_initial - 10 - 9   |
-------------------------------------------------------------------
3    | Alice  | 8                    | N_initial - 10 - 9   |
     |        |                      | N_initial - 10 - 9 - 8 |
-------------------------------------------------------------------
...  | ...    | ...                  | ...                  |
-------------------------------------------------------------------
K    | Current| S_k                  | N_k-1                | If N_k-1 < S_k or S_k <= 0:
     | Player |                      |                      |   Current player loses.
     |        |                      |                      |   If Current player is Alice, Alice loses (False).
     |        |                      |                      |   If Current player is Bob, Alice wins (True).
-------------------------------------------------------------------
```

## Dry Run
Let's trace Example 1: `n = 12`

| Turn | Player | `stones_to_remove_this_turn` | `current_stones` (before move) | Can Move? (`current_stones >= stones_to_remove_this_turn` AND `stones_to_remove_this_turn > 0`) | `current_stones` (after move) | `is_alice_turn` | Outcome |
| :--- | :----- | :--------------------------- | :----------------------------- | :------------------------------------------------------------------------------------------------- | :---------------------------- | :-------------- | :------ |
| -    | -      | 10                           | 12                             | -                                                                                                  | -                             | True            | -       |
| 1    | Alice  | 10                           | 12                             | Yes (12 >= 10 and 10 > 0)                                                                          | 12 - 10 = 2                   | False           | -       |
| 2    | Bob    | 9                            | 2                              | No (2 < 9)                                                                                         | -                             | True            | Bob loses. Alice wins. |

Final result: `true`

## Complexity
*   **Time Complexity:** O(1). The maximum number of stones to remove starts at 10 and decreases by 1 each turn. The game will therefore last at most 10 turns (10, 9, ..., 1). This is a constant number of operations, regardless of `n` (within its constraints).
*   **Space Complexity:** O(1). We only use a few variables to store the game state (`current_stones`, `stones_to_remove_this_turn`, `is_alice_turn`), which require constant memory.

## Edge Cases
*   `n = 1`: Alice needs to remove 10 stones but only 1 is available. `current_stones < stones_to_remove_this_turn` is true. Alice loses. The solution correctly returns `False`.
*   `n = 10`: Alice removes 10 stones. `current_stones` becomes 0. Bob needs to remove 9 stones but 0 are available. Bob loses. The solution correctly returns `True`.
*   `n = 50` (maximum constraint): The simulation will run through several turns.
    *   A: 10, `n=40`
    *   B: 9, `n=31`
    *   A: 8, `n=23`
    *   B: 7, `n=16`
    *   A: 6, `n=10`
    *   B: 5, `n=5`
    *   A: 4, `n=1`
    *   B: needs 3, has 1. Bob loses. Alice wins. The solution correctly returns `True`.
*   When `stones_to_remove_this_turn` becomes `0`: If a player just removed 1 stone, the next player would need to remove 0 stones. The condition `stones_to_remove_this_turn <= 0` correctly identifies this as an invalid move, causing the current player to lose.

## Solution

```python
class Solution:
    def canAliceWin(self, n: int) -> bool:
        current_stones = n
        stones_to_remove_this_turn = 10
        is_alice_turn = True

        # The game continues until a player cannot make a valid move.
        while True:
            # Check if the current player can make a valid move.
            # A move is valid if:
            # 1. The number of stones to remove is positive.
            # 2. There are enough stones in the pile.
            if stones_to_remove_this_turn <= 0 or current_stones < stones_to_remove_this_turn:
                # The current player cannot make a move, so they lose.
                # If it's Alice's turn, Alice loses (return False).
                # If it's Bob's turn, Bob loses, which means Alice wins (return True).
                return not is_alice_turn
            
            # If a move is possible, the current player makes it.
            current_stones -= stones_to_remove_this_turn
            
            # Prepare for the next turn:
            # The number of stones to remove decreases by 1.
            stones_to_remove_this_turn -= 1
            # Switch turns to the other player.
            is_alice_turn = not is_alice_turn

```

## Why This Works
This solution works because it directly **simulates** the game as described by the rules. The game's constraints (`n <= 50` and the decreasing number of stones removed per turn) guarantee that the game will always end in a very small, constant number of turns. By tracking the `current_stones`, `stones_to_remove_this_turn`, and `is_alice_turn`, the simulation precisely determines the winner by identifying the first player unable to make a valid move according to the problem's losing condition.

---
<sub>Generated 2026-11-26 08:49 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
