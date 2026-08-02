# [877] Stone Game

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-08-02 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/stone-game/)

**Topics:** Array, Math, Dynamic Programming, Game Theory

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation:
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.

Example 2:

Input: piles = [3,7,2,3]
Output: true

Constraints:

- 2 <= piles.length <= 500

- piles.length is even.

- 1 <= piles[i] <= 500

- sum(piles[i]) is odd.

**Examples / sample tests:**

```
[5,3,4,5]
[3,7,2,3]
```

---

## Problem Summary
Alice and Bob play a game with an even number of stone piles arranged in a row. Players take turns picking a pile from either end. Alice starts. The total number of stones is odd, preventing ties. The goal is to end with the most stones. We need to determine if Alice wins assuming optimal play.

## Intuition
This problem is a classic example of a **game theory** problem, specifically an impartial game. Players play optimally to maximize their own score. The key to cracking this problem lies in a crucial observation about the constraints:
1.  **Even number of piles (`piles.length` is even)**: This means Alice and Bob will each take exactly half of the piles. If there are `N` piles, Alice takes `N/2` piles and Bob takes `N/2` piles.
2.  **Total sum of stones is odd**: This guarantees there are no ties. One player *must* have more stones than the other. If Alice's score is `S_A` and Bob's is `S_B`, then `S_A + S_B = TotalSum` (odd). This implies `S_A != S_B`. If Alice can ensure `S_A > S_B`, she wins. This is equivalent to ensuring `S_A > TotalSum / 2`.

Consider the piles by their **original indices**: `P0, P1, P2, P3, ..., P(N-1)`.
Alice has a powerful strategy due to the even number of piles: she can always choose to collect *either* all the piles at **even original indices** (`P0, P2, P4, ...`) *or* all the piles at **odd original indices** (`P1, P3, P5, ...`).

Let's see how:
*   **Strategy 1: Target Even-Indexed Piles**
    *   Alice's first move: She takes `P0` (an even-indexed pile).
    *   Now the remaining piles are `P1, P2, ..., P(N-1)`. Bob can take `P1` or `P(N-1)`. Both `P1` and `P(N-1)` are odd-indexed piles (since `N-1` is odd if `N` is even).
    *   No matter which odd-indexed pile Bob takes, Alice is left with a choice where `P2` (the next even-indexed pile) is available at one of the ends of the remaining row.
    *   This pattern continues: Alice always takes an even-indexed pile, forcing Bob to take an odd-indexed pile. By the end, Alice will have collected all `P0, P2, P4, ...`.
*   **Strategy 2: Target Odd-Indexed Piles**
    *   Alice's first move: She takes `P(N-1)` (an odd-indexed pile).
    *   Now the remaining piles are `P0, P1, ..., P(N-2)`. Bob can take `P0` or `P(N-2)`. Both `P0` and `P(N-2)` are even-indexed piles.
    *   Similarly, Alice can always force Bob to take an even-indexed pile, allowing her to take the next odd-indexed pile. By the end, Alice will have collected all `P1, P3, P5, ...`.

Since Alice can guarantee she gets *either* the sum of all even-indexed piles (`SumEven`) *or* the sum of all odd-indexed piles (`SumOdd`), she will simply choose the strategy that yields the larger sum. Because the total sum of stones is odd, `SumEven` and `SumOdd` cannot be equal. Therefore, one of them must be strictly greater than the other. Alice can always secure the larger sum, which means she will always get more than half of the total stones.

**Conclusion**: Alice always wins this game.

## Approach
1.  Recognize that this is a game theory problem with specific constraints: an even number of piles and an odd total sum of stones.
2.  Understand the strategic advantage of the first player (Alice) in such a game: she can always ensure she collects either all the piles at even original indices or all the piles at odd original indices.
3.  Since the total sum of stones is odd, the sum of stones at even indices (`SumEven`) and the sum of stones at odd indices (`SumOdd`) cannot be equal. One must be strictly greater than the other.
4.  Alice will simply choose the strategy that allows her to collect the set of piles with the larger sum.
5.  By doing so, Alice guarantees herself more than half of the total stones.
6.  Therefore, Alice always wins the game.
7.  The solution is simply to `return True`.

## Visualization
Let's visualize Alice's strategic choice for `piles = [P0, P1, P2, P3, P4, P5]`. Alice can commit to taking either all even-indexed piles or all odd-indexed piles.

```mermaid
graph TD
    A[Start Game with Piles: P0, P1, P2, P3, P4, P5] --> B{Alice's First Move: Take P0 or P5?}

    B -- Take P0 (Even Index) --> C{Alice commits to targeting Even-Indexed Piles (P0, P2, P4)}
    C --> D[Remaining: P1, P2, P3, P4, P5]
    D --> E{Bob's Move: Take P1 or P5? (Both are Odd-Indexed)}
    E -- Bob takes P1 --> F[Remaining: P2, P3, P4, P5]
    E -- Bob takes P5 --> G[Remaining: P1, P2, P3, P4]
    F --> H{Alice's Move: Take P2 (Even Index)}
    G --> H
    H --> I[...Alice continues taking Even-Indexed Piles, Bob takes Odd-Indexed Piles...]
    I --> J[Alice collects all P0, P2, P4]

    B -- Take P5 (Odd Index) --> K{Alice commits to targeting Odd-Indexed Piles (P1, P3, P5)}
    K --> L[Remaining: P0, P1, P2, P3, P4]
    L --> M{Bob's Move: Take P0 or P4? (Both are Even-Indexed)}
    M -- Bob takes P0 --> N[Remaining: P1, P2, P3, P4]
    M -- Bob takes P4 --> O[Remaining: P0, P1, P2, P3]
    N --> P{Alice's Move: Take P1 (Odd Index)}
    O --> P
    P --> Q[...Alice continues taking Odd-Indexed Piles, Bob takes Even-Indexed Piles...]
    Q --> R[Alice collects all P1, P3, P5]

    J --> S{Alice compares Sum(P0,P2,P4) vs Sum(P1,P3,P5)}
    R --> S
    S --> T[Alice chooses the path that yields the higher sum]
    T --> U[Since total sum is odd, one sum is always greater. Alice always wins.]
```

## Dry Run
Let's use Example 1: `piles = [5, 3, 4, 5]`

1.  **Analyze the input**:
    *   `piles.length = 4` (even).
    *   Total sum of stones = `5 + 3 + 4 + 5 = 17` (odd).
    *   These constraints confirm the "Alice always wins" property applies.

2.  **Alice's potential strategies**:
    *   **Strategy A: Collect even-indexed piles**
        *   Piles at even original indices: `piles[0]` (value 5) and `piles[2]` (value 4).
        *   `SumEven = 5 + 4 = 9`.
    *   **Strategy B: Collect odd-indexed piles**
        *   Piles at odd original indices: `piles[1]` (value 3) and `piles[3]` (value 5).
        *   `SumOdd = 3 + 5 = 8`.

3.  **Alice's optimal choice**:
    *   Alice compares `SumEven` (9) and `SumOdd` (8).
    *   Since `9 > 8`, Alice chooses Strategy A, aiming to collect the even-indexed piles.

4.  **Outcome**:
    *   Alice's score will be 9.
    *   Bob's score will be 8.
    *   Since Alice's score (9) > Bob's score (8), Alice wins.

5.  **Final Result**: The function returns `true`.

## Complexity
*   **Time Complexity**: O(1)
    *   The solution directly returns `True` without iterating through the `piles` array or performing any calculations dependent on its size. The reasoning for Alice always winning is based on the problem's constraints, not on the specific values in `piles`.
*   **Space Complexity**: O(1)
    *   No additional data structures are used, and the memory usage is constant regardless of the input size.

## Edge Cases
The problem statement's constraints are crucial and define the "always true" nature of the solution:
*   `piles.length` is even: This is fundamental to Alice's strategy of choosing between even-indexed or odd-indexed piles. If `piles.length` were odd, the game dynamics would change significantly, and the first player would not necessarily win.
*   `sum(piles[i])` is odd: This guarantees that `SumEven` and `SumOdd` cannot be equal, ensuring one sum is strictly greater than the other. This means a tie is impossible, and Alice can always secure a strictly larger share.
*   `piles.length = 2` (minimum size): E.g., `[10, 1]`. `SumEven = 10`, `SumOdd = 1`. Alice takes 10, Bob takes 1. Alice wins. The logic holds.
*   `piles.length = 500` (maximum size): The logic scales perfectly, as it doesn't depend on the specific size, only its parity.
*   `piles[i]` values (1 to 500): The specific values don't alter the strategic advantage, only the magnitude of the scores. The "always win" conclusion remains valid.

## Solution

```python
from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # This problem is a classic game theory puzzle with a clever trick.
        # The problem statement guarantees two crucial conditions:
        # 1. `piles.length` is even.
        # 2. The total sum of stones (`sum(piles[i])`) is odd.
        #
        # Let's analyze these conditions:
        # - Since `piles.length` is even, Alice (the first player) and Bob
        #   will each take exactly half of the piles.
        # - The total sum being odd means there can be no ties; one player
        #   must end up with strictly more stones than the other.
        #
        # Alice's winning strategy:
        # Alice can always guarantee she collects either all the piles at
        # even original indices (e.g., piles[0], piles[2], piles[4], ...)
        # OR all the piles at odd original indices (e.g., piles[1], piles[3], piles[5], ...).
        #
        # How does she do this?
        # 1. Alice calculates the sum of all even-indexed piles (`SumEven`).
        # 2. Alice calculates the sum of all odd-indexed piles (`SumOdd`).
        #
        # Since the total sum of stones (`SumEven + SumOdd`) is odd, it's
        # impossible for `SumEven` to be equal to `SumOdd`. Therefore, one
        # of these sums must be strictly greater than the other.
        #
        # Alice simply chooses the strategy that yields the larger sum.
        # For example, if `SumEven > SumOdd`, Alice starts by taking `piles[0]`.
        # This forces Bob to pick either `piles[1]` or `piles[N-1]` (both odd-indexed).
        # No matter what Bob picks, Alice can then pick `piles[2]` (the next
        # even-indexed pile available at an end). This pattern continues,
        # allowing Alice to collect all even-indexed piles.
        # A similar strategy works if `SumOdd > SumEven`, by starting with `piles[N-1]`.
        #
        # By executing this strategy, Alice ensures her score is `max(SumEven, SumOdd)`.
        # Since `max(SumEven, SumOdd)` is always strictly greater than
        # `(SumEven + SumOdd) / 2` (because `SumEven != SumOdd`), Alice
        # will always end up with more than half of the total stones.
        #
        # Therefore, Alice always wins the game under these conditions.
        return True

```

## Why This Works
This solution works because of a specific property of the game when the number of piles is even. Alice, as the first player, can always choose a strategy to collect either all the piles originally at even indices or all the piles originally at odd indices. Since the total sum of stones is guaranteed to be odd, the sum of stones at even indices and the sum of stones at odd indices cannot be equal. Therefore, one of these sums must be strictly greater than the other. Alice will simply choose the strategy that yields the larger sum, guaranteeing her more than half of the total stones, and thus, a win.

---
<sub>Generated 2026-08-02 04:06 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
