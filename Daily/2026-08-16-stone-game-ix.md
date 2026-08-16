# [2029] Stone Game IX

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-08-16 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/stone-game-ix/)

**Topics:** Array, Math, Greedy, Minimax, Counting, Game Theory, Nim Game, Zero-Sum Game

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array stones, where stones[i] is the value of the i^th stone.

Alice and Bob take turns, with Alice starting first. On each turn, the player may remove any stone from stones. The player who removes a stone loses if the sum of the values of all removed stones is divisible by 3. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).

Assuming both players play optimally, return true if Alice wins and false if Bob wins.

Example 1:

Input: stones = [2,1]
Output: true
Explanation: The game will be played as follows:
- Turn 1: Alice can remove either stone.
- Turn 2: Bob removes the remaining stone.
The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.

Example 2:

Input: stones = [2]
Output: false
Explanation: Alice will remove the only stone, and the sum of the values on the removed stones is 2.
Since all the stones are removed and the sum of values is not divisible by 3, Bob wins the game.

Example 3:

Input: stones = [5,1,2,4,3]
Output: false
Explanation: Bob will always win. One possible way for Bob to win is shown below:
- Turn 1: Alice can remove the second stone with value 1. Sum of removed stones = 1.
- Turn 2: Bob removes the fifth stone with value 3. Sum of removed stones = 1 + 3 = 4.
- Turn 3: Alices removes the fourth stone with value 4. Sum of removed stones = 1 + 3 + 4 = 8.
- Turn 4: Bob removes the third stone with value 2. Sum of removed stones = 1 + 3 + 4 + 2 = 10.
- Turn 5: Alice removes the first stone with value 5. Sum of removed stones = 1 + 3 + 4 + 2 + 5 = 15.
Alice loses the game because the sum of the removed stones (15) is divisible by 3. Bob wins the game.

Constraints:

- 1 <= stones.length <= 10^5

- 1 <= stones[i] <= 10^4

**Examples / sample tests:**

```
[2,1]
[2]
[5,1,2,4,3]
```

---

This problem is a classic impartial game, which can often be solved by analyzing game states and player strategies. The key is that we only care about the sum of removed stones modulo 3.

## Problem Summary
Alice and Bob take turns removing stones. A player loses if, after their move, the sum of all removed stones is divisible by 3. If all stones are removed and the sum is not divisible by 3, Bob wins. Alice starts, both play optimally. Determine if Alice wins.

## Intuition
The core idea is that only the **remainder of the sum of stones modulo 3** matters. Let `S` be this sum. A player loses if they make a move that results in `S % 3 == 0`. This means players want to pick stones that result in `S % 3 != 0`.

Let's categorize stones by their value modulo 3:
*   `count0`: number of stones with value `x % 3 == 0`
*   `count1`: number of stones with value `x % 3 == 1`
*   `count2`: number of stones with value `x % 3 == 2`

**Crucial Observations:**
1.  **Alice's First Move:** Alice starts with `S = 0`. She cannot pick a stone with `x % 3 == 0`, as `(0 + x) % 3 == 0` would make her lose immediately. She must pick a stone with `x % 3 == 1` or `x % 3 == 2`. If she cannot (i.e., `count1 == 0` and `count2 == 0`), she loses.
2.  **Stones with `x % 3 == 0` (0-stones):** These stones are special. If the current sum `S % 3` is 1 or 2, picking a 0-stone does not change `S % 3`. It simply consumes a turn and a stone. This means 0-stones can be used to "pass the turn" without altering the `S % 3` state, as long as `S % 3 != 0`. If `S % 3 == 0`, a player *cannot* pick a 0-stone.
3.  **Optimal Play and `count0`:** Players will use 0-stones strategically. If a player is in a "losing" position (e.g., `S % 3 == 1` and only 2-stones are left), they can use a 0-stone to force the opponent into that same losing position. This means `count0` stones are effectively "turn-passers" that determine whose turn it is for the "real" game involving `count1` and `count2` stones.
    *   If `count0` is **even**, the 0-stones cancel out in terms of turn advantage. The player whose turn it is for the `count1`/`count2` subgame remains the same.
    *   If `count0` is **odd**, the 0-stones flip the turn advantage. The player whose turn it is for the `count1`/`count2` subgame becomes the *other* player.

This simplifies the problem into two main scenarios based on the parity of `count0`.

## Approach
1.  **Count Stone Types:** Iterate through the `stones` array and count `count0`, `count1`, and `count2`.
2.  **Handle Edge Case: No Valid First Move:** If `count1 == 0` and `count2 == 0`, Alice cannot make a valid first move (she would have to pick a

---
<sub>Generated 2026-08-16 02:08 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
