# [486] Predict the Winner

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-08-01 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/predict-the-winner/)

**Topics:** Array, Math, Dynamic Programming, Recursion, Game Theory

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

Example 1:

Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return false.

Example 2:

Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Constraints:

- 1 <= nums.length <= 20

- 0 <= nums[i] <= 10^7

**Examples / sample tests:**

```
[1,5,2]
[1,5,233,7]
```

---

## Problem Summary
Two players take turns choosing numbers from either end of an array, adding them to their score. Player 1 starts. Both play optimally to maximize their own score. We need to determine if Player 1 can achieve a score greater than or equal to Player 2's score.

## Intuition
This is a **game theory** problem where two players play optimally. When players play optimally, it often suggests a **minimax** strategy, which can be solved using **dynamic programming** or **recursion with memoization**.

Instead of tracking absolute scores for Player 1 and Player 2, it's simpler to track the **score difference** (Player 1's score - Player 2's score).
*   If it's Player 1's turn, they want to **maximize** this difference.
*   If it's Player 2's turn, they want to **minimize** this difference (or equivalently, maximize `P2_score - P1_score`).

Let's define `dp(i, j)` as the maximum score difference the *current player* can achieve when playing with the subarray `nums[i...j]`.

When it's the current player's turn with `nums[i...j]`:
1.  **Option 1: Take `nums[i]`**. The current player's score increases by `nums[i]`. Now it's the opponent's turn with `nums[i+1...j]`. The opponent will play optimally, achieving `dp(i+1, j)` for *their* turn. From the current player's perspective, this `dp(i+1, j)` is a *loss* to their own score difference. So, the current player's score difference for this option is `nums[i] - dp(i+1, j)`.
2.  **Option 2: Take `nums[j]`**. Similarly, the current player's score difference for this option is `nums[j] - dp(i, j-1)`.

The current player will choose the option that maximizes their own score difference:
`dp(i, j) = max(nums[i] - dp(i+1, j), nums[j] - dp(i, j-1))`

The base cases are:
*   If `i > j`: No elements left, score difference is `0`.
*   If `i == j`: Only one element left, the current player takes `nums[i]`. Score difference is `nums[i]`.

Finally, Player 1 starts with the entire array `nums[0...n-1]`. If `dp(0, n-1) >= 0`, Player 1 can win.

## Approach
We will use a **top-down dynamic programming (recursion with memoization)** approach.

1.  **Define a recursive function `max_diff(left, right)`**: This function will calculate the maximum score difference the *current player* can achieve when playing with the subarray `nums[left...right]`.
2.  **Memoization**: Use a dictionary or a 2D array, `memo`, to store the results of `max_diff(left, right)`. Before computing, check if `memo[(left, right)]` already exists. If so, return the stored value.
3.  **Base Cases**:
    *   If `left > right`: This means there are no elements left in the subarray. The score difference is `0`.
    *   If `left == right`: This means there's only one element `nums[left]` left. The current player takes it, so the score difference is `nums[left]`.
4.  **Recursive Step**:
    *   Calculate `score_if_take_left = nums[left] - max_diff(left + 1, right)`. This represents taking the leftmost number and then subtracting the optimal outcome of the opponent on the remaining subarray.
    *   Calculate `score_if_take_right = nums[right] - max_diff(left, right - 1)`. This represents taking the rightmost number and then subtracting the optimal outcome of the opponent on the remaining subarray.
    *   The current player chooses the move that yields the maximum score difference: `result = max(score_if_take_left, score_if_take_right)`.
5.  **Store and Return**: Store `result` in `memo[(left, right)]` and then return `result`.
6.  **Initial Call**: Call `max_diff(0, n - 1)` where `n` is the length of `nums`.
7.  **Final Check**: If the result of `max_diff(0, n - 1)` is greater than or equal to `0`, Player 1 wins, so return `True`. Otherwise, return `False`.

## Visualization
Imagine a game tree where each node represents a state `(left, right)` of the array. From each state, the current player has two choices: take `nums[left]` or `nums[right]`. The value of a node `(left, right)` is the maximum score difference the current player can achieve.

```mermaid
graph TD
    A[P1's Turn: (0, N-1)] --> B{Take nums[0]}
    A --> C{Take nums[N-1]}

    B --> D[P2's Turn: (1, N-1)]
    C --> E[P2's Turn: (0, N-2)]

    D --> F{Take nums[1]}
    D --> G{Take nums[N-1]}

    E --> H{Take nums[0]}
    E --> I{Take nums[N-2]}

    subgraph Player 1's Choices (Maximize)
        A
    end

    subgraph Player 2's Choices (Minimize P1's score diff)
        D
        E
    end

    style A fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#fbb,stroke:#333,stroke-width:2px
    style E fill:#fbb,stroke:#333,stroke-width:2px
```
In this diagram:
*   `A` is Player 1's turn with the full array.
*   `B` and `C` represent Player 1's choices.
*   `D` and `E` are Player 2's turns on the remaining subarrays. Player 2 will make choices `F, G` or `H, I` to minimize Player 1's score difference.
*   The `dp(i, j)` function calculates the optimal outcome for the current player at state `(i, j)`. Player 1 maximizes `(P1_score - P2_score)`, while Player 2 effectively minimizes `(P1_score - P2_score)` (by maximizing `(P2_score - P1_score)`).

## Dry Run
Let's trace `nums = [1,5,2]` (Example 1). `n = 3`.
We want to calculate `max_diff(0, 2)`.
`memo` table is initially empty.

| Call `max_diff(left, right)` | `left` | `right` | `nums[left]` | `nums[right]` | Option 1 (take `nums[left]`) | Option 2 (take `nums[right]`) | Result (`max`) | `memo` update |
| :--------------------------- | :----: | :-----: | :----------: | :-----------: | :----------------------------: | :----------------------------: | :------------: | :------------ |
| `max_diff(0, 2)`             | 0      | 2       | 1            | 2             | `1 - max_diff(1, 2)`           | `2 - max_diff(0, 1)`           |                |               |
| &nbsp;&nbsp;`max_diff(1, 2)` | 1      | 2       | 5            | 2             | `5 - max_diff(2, 2)`           | `2 - max_diff(1, 1)`           |                |               |
| &nbsp;&nbsp;&nbsp;&nbsp;`max_diff(2, 2)` | 2      | 2       | 2            | 2             | Base case: `nums[2]`           |                                | `2`            | `memo[(2,2)]=2` |
| &nbsp;&nbsp;&nbsp;&nbsp;`max_diff(1, 1)` | 1      | 1       | 5            | 5             | Base case: `nums[1]`           |                                | `5`            | `memo[(1,1)]=5` |
| &nbsp;&nbsp;`max_diff(1, 2)` | 1      | 2       | 5            | 2             | `5 - 2 = 3`                    | `2 - 5 = -3`                   | `max(3, -3) = 3` | `memo[(1,2)]=3` |
| &nbsp;&nbsp;`max_diff(0, 1)` | 0      | 1       | 1            | 5             | `1 - max_diff(1, 1)`           | `5 - max_diff(0, 0)`           |                |               |
| &nbsp;&nbsp;&nbsp;&nbsp;`max_diff(1, 1)` | 1      | 1       | 5            | 5             | (From memo)                    |                                | `5`            |               |
| &nbsp;&nbsp;&nbsp;&nbsp;`max_diff(0, 0)` | 0      | 0       | 1            | 1             | Base case: `nums[0]`           |                                | `1`            | `memo[(0,0)]=1` |
| &nbsp;&nbsp;`max_diff(0, 1)` | 0      | 1       | 1            | 5             | `1 - 5 = -4`                   | `5 - 1 = 4`                    | `max(-4, 4) = 4` | `memo[(0,1)]=4` |
| `max_diff(0, 2)`             | 0      | 2       | 1            | 2             | `1 - 3 = -2`                   | `2 - 4 = -2`                   | `max(-2, -2) = -2` | `memo[(0,2)]=-2` |

Final result: `max_diff(0, 2) = -2`.
Since `-2 < 0`, Player 1 cannot win. The function returns `False`. This matches Example 1.

## Complexity
*   **Time Complexity**: `O(N^2)`. There are `N` possible values for `left` and `N` possible values for `right`. Thus, there are `N * N` unique states `(left, right)`. Each state is computed once, and each computation takes `O(1)` time (constant time operations like `max` and arithmetic).
*   **Space Complexity**: `O(N^2)`. This is for the `memo` dictionary/table to store the results of the `N * N` states. The recursion stack depth can go up to `N` in the worst case, but this is dominated by the `O(N^2)` memoization table.

## Edge Cases
*   **`nums.length = 1`**: E.g., `[10]`.
    *   `max_diff(0, 0)` will be called. It's a base case, returning `nums[0] = 10`.
    *   Since `10 >= 0`, Player 1 wins. Correct, Player 1 takes the only number.
*   **`nums.length = 2`**: E.g., `[10, 1]`.
    *   `max_diff(0, 1)` will be called.
    *   Option 1 (take 10): `10 - max_diff(1, 1) = 10 - 1 = 9`.
    *   Option 2 (take 1): `1 - max_diff(0, 0) = 1 - 10 = -9`.
    *   `max_diff(0, 1) = max(9, -9) = 9`.
    *   Since `9 >= 0`, Player 1 wins. Correct, Player 1 takes 10, Player 2 takes 1.
*   **All zeros**: E.g., `[0, 0, 0]`.
    *   `max_diff(0, 2)` will eventually evaluate to `0`.
    *   Since `0 >= 0`, Player 1 wins. Correct, scores will be equal.
*   **Large numbers**: `nums[i]` up to `10^7`.
    *   Python handles large integers automatically, so the arithmetic for score differences works correctly without overflow. The logic remains the same.

## Solution
```python
from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # memo[left][right] stores the maximum score difference the current player
        # can achieve when playing with the subarray nums[left...right].
        # Using a dictionary for memoization, keys are (left, right) tuples.
        memo = {}

        def max_diff(left: int, right: int) -> int:
            # Base case 1: If the subarray is empty (left pointer crossed right pointer)
            # No elements left to pick, so the score difference from this point is 0.
            if left > right:
                return 0
            
            # Base case 2: If only one element is left in the subarray
            # The current player takes this element, adding its value to their score.
            # The opponent gets nothing from this turn.
            if left == right:
                return nums[left]
            
            # Check if this state has already been computed to avoid redundant calculations.
            if (left, right) in memo:
                return memo[(left, right)]
            
            # Option 1: Current player chooses nums[left]
            # Their score increases by nums[left].
            # Then, it becomes the opponent's turn for the subarray nums[left+1...right].
            # The opponent will play optimally, achieving max_diff(left+1, right) for *their* turn.
            # From the current player's perspective, this is a subtraction from their score difference.
            score_if_take_left = nums[left] - max_diff(left + 1, right)
            
            # Option 2: Current player chooses nums[right]
            # Similar logic as above, but taking the rightmost element.
            score_if_take_right = nums[right] - max_diff(left, right - 1)
            
            # The current player plays optimally, so they choose the option that maximizes
            # their own score difference.
            result = max(score_if_take_left, score_if_take_right)
            
            # Store the computed result in the memoization table before returning.
            memo[(left, right)] = result
            return result
        
        # Player 1 starts the game with the entire array nums[0...n-1].
        # If the maximum score difference Player 1 can achieve (P1_score - P2_score)
        # is non-negative, then Player 1 wins or ties, which means Player 1 wins.
        return max_diff(0, n - 1) >= 0

```

## Why This Works
This solution correctly models the game using the **minimax principle** through dynamic programming. By defining `max_diff(left, right)` as the maximum score difference the *current player* can achieve from `nums[left...right]`, we capture the optimal play of both participants. When it's a player's turn, they choose the move that maximizes their own score difference. This choice inherently accounts for the opponent's subsequent optimal move, which will be to minimize the current player's score difference (by maximizing their own). The recursive calls with memoization ensure that every possible optimal game path is explored exactly once for each subarray, leading to the true maximum score difference Player 1 can achieve against an optimal Player 2. If this final difference is non-negative, Player 1 wins.

---
<sub>Generated 2026-08-01 04:02 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
