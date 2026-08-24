# [1872] Stone Game VIII

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-08-24 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/stone-game-viii/)

**Topics:** Array, Math, Dynamic Programming, Minimax, Prefix Sum, Game Theory, Zero-Sum Game

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, while the number of stones is more than one, they will do the following:

- Choose an integer x > 1, and remove the leftmost x stones from the row.

- Add the sum of the removed stones' values to the player's score.

- Place a new stone, whose value is equal to that sum, on the left side of the row.

The game stops when only one stone is left in the row.

The score difference between Alice and Bob is (Alice's score - Bob's score). Alice's goal is to maximize the score difference, and Bob's goal is the minimize the score difference.

Given an integer array stones of length n where stones[i] represents the value of the i^th stone from the left, return the score difference between Alice and Bob if they both play optimally.

Example 1:

Input: stones = [-1,2,-3,4,-5]
Output: 5
Explanation:
- Alice removes the first 4 stones, adds (-1) + 2 + (-3) + 4 = 2 to her score, and places a stone of
  value 2 on the left. stones = [2,-5].
- Bob removes the first 2 stones, adds 2 + (-5) = -3 to his score, and places a stone of value -3 on
  the left. stones = [-3].
The difference between their scores is 2 - (-3) = 5.

Example 2:

Input: stones = [7,-6,5,10,5,-2,-6]
Output: 13
Explanation:
- Alice removes all stones, adds 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 to her score, and places a
  stone of value 13 on the left. stones = [13].
The difference between their scores is 13 - 0 = 13.

Example 3:

Input: stones = [-10,-12]
Output: -22
Explanation:
- Alice can only make one move, which is to remove both stones. She adds (-10) + (-12) = -22 to her
  score and places a stone of value -22 on the left. stones = [-22].
The difference between their scores is (-22) - 0 = -22.

Constraints:

- n == stones.length

- 2 <= n <= 10^5

- -10^4 <= stones[i] <= 10^4

**Examples / sample tests:**

```
[-1,2,-3,4,-5]
[7,-6,5,10,5,-2,-6]
[-10,-12]
```

---

## Problem Summary
Alice and Bob play a game with a row of `n` stones. Alice starts. On each turn, a player removes the leftmost `x > 1` stones, adds their sum to their score, and replaces them with a single new stone of that sum. The game ends when only one stone remains. Alice wants to maximize (Alice's score - Bob's score), while Bob wants to minimize it. We need to find the final score difference if both play optimally.

## Intuition
This is a **zero-sum game** where players make choices to optimize a score difference. Such problems are typically solved using **minimax dynamic programming**.

1.  **Game State:** The key observation is how the row of stones changes. When `x` stones are removed and replaced by their sum `S`, the new row starts with `S`, followed by the remaining original stones. This means the *first stone* in the row is always a cumulative sum of some prefix of the *original* `stones` array. Let `P[k]` be the sum of the first `k` original stones (`stones[0]` through `stones[k-1]`).
2.  **DP State:** Let `dp[i]` represent the maximum score difference the *current player* can achieve if the game state is `[P[i], stones[i], stones[i+1], ..., stones[n-1]]`. Here, `P[i]` is the value of the first stone (which is the sum of `stones[0]` to `stones[i-1]`), and `stones[i]` onwards are the original stones that haven't been merged yet.
3.  **Game End:** The game ends when only one stone is left. In our `dp[i]` state, this means `n - i + 1 = 1`, which simplifies to `i = n`. If `i=n`, the row is just `[P[n]]`, no more moves are possible. So, `dp[n] = 0`.
4.  **Recurrence:** For a state `dp[i]` (where `i < n`), the current player must choose `x` stones from the left, where `x > 1`. These `x` stones are `P[i], stones[i], ..., stones[i+x-2]`. The sum of these stones is `P[i+x-1]`. The player adds `P[i+x-1]` to their score. The new game state for the opponent will be `[P[i+x-1], stones[i+x-1], ..., stones[n-1]]`, which corresponds to `dp[i+x-1]`. Since the opponent wants to minimize the score difference (or maximize their own gain), the current player's score difference will be `P[i+x-1] - dp[i+x-1]`. The current player wants to maximize this value.
    So, `dp[i] = max_{j=i+1 to n} (P[j] - dp[j])`. (Here, `j = i+x-1`).
5.  **Optimization:** The `max` operation over a suffix `j=i+1 to n` can be optimized. We can compute `dp[i]` from `i=n-1` down to `1`. We maintain a `max_val_suffix` variable that stores `max_{k=i+1 to n} (P[k] - dp[k])`. This allows computing each `dp[i]` in `O(1)` time.
6.  **Initial Move:** The very first move Alice makes is special. She doesn't start with a `P[0]` stone (which would be 0). Instead, she starts with the original `stones[0], ..., stones[n-1]`. If she chooses `x` stones (`x` from `2` to `n`), she takes `stones[0], ..., stones[x-1]`. Their sum is `P[x]`. Her score increases by `P[x]`. The new state for Bob is `[P[x], stones[x], ..., stones[n-1]]`, which corresponds to `dp[x]`. So, Alice's total score difference for this first move is `P[x] - dp[x]`. Alice will choose `x` to maximize this.

## Approach

1.  **Calculate Prefix Sums:** Create a `prefix_sum` array `P` of size `n+1`. `P[k]` will store the sum of `stones[0]` through `stones[k-1]`. `P[0]` will be `0`.
    `P[k] = P[k-1] + stones[k-1]` for `k = 1, ..., n`.

2.  **Initialize DP Array:** Create a `dp` array of size `n+1`. `dp[i]` will store the maximum score difference a player can achieve if the current game state is `[P[i], stones[i], ..., stones[n-1]]`.

3.  **Base Case:** Set `dp[n] = 0`. This is because if `i=n`, only one stone (`P[n]`) is left, and the game ends. No more moves, so the score difference from this state is 0.

4.  **Iterate DP (Bottom-Up):**
    *   Initialize `max_val_suffix = P[n] - dp[n]`. This variable will store `max_{j=i+1 to n} (P[j] - dp[j])` for the current `i`. For `i=n-1`, `j` can only be `n`, so it starts with `P[n] - dp[n]`.
    *   Loop `i` from `n-1` down to `1` (inclusive):
        *   `dp[i] = max_val_suffix`. This is the optimal score difference for the current state `[P[i], stones[i], ..., stones[n-1]]`.
        *   Update `max_val_suffix` for the next iteration (when `i` becomes `i-1`): `max_val_suffix = max(max_val_suffix, P[i] - dp[i])`. This incorporates the option of choosing `P[i]` and `stones[i]` (which would lead to state `dp[i]`) into the maximum for `dp[i-1]`.

5.  **Calculate Final Answer:** The `dp` array calculated above is for states where the first stone is already a sum `P[i]`. Alice's first move is from the original `stones` array.
    *   Initialize `final_max_diff = -infinity`.
    *   Loop `x` from `2` to `n` (inclusive):
        *   Alice chooses `x` stones from `stones[0], ..., stones[x-1]`. The sum is `P[x]`.
        *   Her score increases by `P[x]`.
        *   The new state for Bob is `[P[x], stones[x], ..., stones[n-1]]`, which has an optimal score difference of `dp[x]`.
        *   Alice's total score difference for this choice is `P[x] - dp[x]`.
        *   Update `final_max_diff = max(final_max_diff, P[x] - dp[x])`.

6.  **Return `final_max_diff`**.

## Visualization

Let's visualize the `dp` array and `max_val_suffix` calculation for `stones = [-1, 2, -3, 4, -5]` (`n=5`).

**Prefix Sums (P):**
`P[0]=0`, `P[1]=-1`, `P[2]=1`, `P[3]=-2`, `P[4]=2`, `P[5]=-3`

**DP Table (dp) and `max_val_suffix`:**
`dp` array initialized to `[?, ?, ?, ?, ?, 0]` (size `n+1=6`)

| `i` | `dp[i]` (before update) | `max_val_suffix` (before update) | `P[i]` | `P[i] - dp[i]` | `dp[i]` (after update) | `max_val_suffix` (after update) |
| :-- | :---------------------- | :------------------------------- | :----- | :------------- | :---------------------- | :-------------------------------- |
| `n=5` | -                       | -                                | `P[5]=-3` | -              | `dp[5]=0`               | `P[5]-dp[5] = -3-0 = -3`          |
| `4`   | -                       | `-3`                             | `P[4]=2`  | `2 - (-3) = 5` | `dp[4]=-3`              | `max(-3, 5) = 5`                  |
| `3`   | -                       | `5`                              | `P[3]=-2` | `-2 - 5 = -7`  | `dp[3]=5`               | `max(5, -7) = 5`                  |
| `2`   | -                       | `5`                              | `P[2]=1`  | `1 - 5 = -4`   | `dp[2]=5`               | `max(5, -4) = 5`                  |
| `1`   | -                       | `5`                              | `P[1]=-1` | `-1 - 5 = -6`  | `dp[1]=5`               | `max(5, -6) = 5`                  |

**Final `dp` array (relevant part):** `[?, 5, 5, 5, -3, 0]`

**Alice's First Move Calculation:**
Alice considers `x` from `2` to `n=5`. She wants to maximize `P[x] - dp[x]`.

| `x` | `P[x]` | `dp[x]` | `P[x] - dp[x]` |
| :-- | :----- | :------ | :------------- |
| `2` | `1`    | `5`     | `1 - 5 = -4`   |
| `3` | `-2`   | `5`     | `-2 - 5 = -7`  |
| `4` | `2`    | `-3`    | `2 - (-3) = 5` |
| `5` | `-3`   | `0`     | `-3 - 0 = -3`  |

`final_max_diff = max(-4, -7, 5, -3) = 5`.

## Dry Run

Let's walk through Example 1: `stones = [-1,2,-3,4,-5]`

**1. Calculate Prefix Sums (P):**
`n = 5`
`P = [0] * 6`
`P[1] = P[0] + stones[0] = 0 + (-1) = -

---
<sub>Generated 2026-08-24 02:09 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
