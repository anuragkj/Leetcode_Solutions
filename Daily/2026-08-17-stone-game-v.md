# [1563] Stone Game V

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-08-17 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/stone-game-v/)

**Topics:** Array, Math, Dynamic Programming, Game Theory

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's score is initially zero.

Return the maximum score that Alice can obtain.

Example 1:

Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.

Example 2:

Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28

Example 3:

Input: stoneValue = [4]
Output: 0

Constraints:

- 1 <= stoneValue.length <= 500

- 1 <= stoneValue[i] <= 10^6

**Examples / sample tests:**

```
[6,2,3,4,5,5]
[7,7,7,7,7,7,7]
[4]
```

---

## Problem Summary
Alice and Bob play a game with a row of stones. Alice divides the row into two non-empty parts. Bob discards the part with the higher sum of values (or Alice chooses if sums are equal). Alice's score increases by the value of the remaining part. The game continues with the remaining part until only one stone is left. Alice wants to maximize her total score.

## Intuition
This problem involves making optimal choices over a sequence of items, where the outcome of a choice affects future choices on a sub-sequence. This structure is a strong indicator for **Dynamic Programming (DP)**. The key observation is that the game always continues on a *contiguous subsegment* of the original stones. If we can find the maximum score for any subsegment `[i...j]`, we can use these results to find the maximum score for larger segments.

Alice's goal is to maximize her score. When she splits a segment, she gets an immediate score, and then the game continues on a smaller segment. Bob's action is fixed (discard the max sum, or let Alice choose if equal). Alice will always make the choice that leads to the highest possible total score.

## Approach
We will use a **bottom-up dynamic programming** approach combined with **prefix sums** for efficient sum calculations.

1.  **Precompute Prefix Sums:**
    *   Create an array `prefix_sums` where `prefix_sums[k]` stores the sum of `stoneValue[0]` to `stoneValue[k-1]`. `prefix_sums[0]` will be 0.
    *   This allows calculating the sum of any subsegment `stoneValue[i...j]` in O(1) time as `prefix_sums[j+1] - prefix_sums[i]`.

2.  **Initialize DP Table:**
    *   Create a 2D DP table `dp[N][N]`, where `N` is the number of stones.
    *   `dp[i][j]` will store the maximum score Alice can obtain from the subsegment `stoneValue[i...j]`.
    *   Initialize all `dp` values to 0. If `i == j` (a single stone), the game ends, so `dp[i][i]` is 0, which is correctly handled by initialization.

3.  **Iterate DP States (Bottom-Up):**
    *   We build up the `dp` table by considering subsegments of increasing `length`.
    *   `length` will range from 2 (two stones) up to `N` (the entire row).
    *   For each `length`, iterate through all possible starting indices `i` for a subsegment of that length.
    *   The ending index `j` will be `i + length - 1`.

4.  **Calculate Transitions for `dp[i][j]`:**
    *   For each subsegment `stoneValue[i...j]`, Alice considers all possible split points `k` (where `i <= k < j`).
    *   A split at `k` divides the segment into `left_row = stoneValue[i...k]` and `right_row = stoneValue[k+1...j]`.
    *   Calculate `left_sum = sum(stoneValue[i...k])` and `right_sum = sum(stoneValue[k+1...j])` using prefix sums.
    *   **Determine Alice's score for this split `k`:**
        *   If `left_sum > right_sum`: Bob discards `left_row`. Alice gets `right_sum`. The game continues with `right_row`. The total score for this split is `right_sum + dp[k+1][j]`.
        *   If `right_sum > left_sum`: Bob discards `right_row`. Alice gets `left_sum`. The game continues with `left_row`. The total score for this split is `left_sum + dp[i][k]`.
        *   If `left_sum == right_sum`: Alice chooses which to discard. She will choose to keep the row that yields a higher *future* score. So, the score for this split is `max(left_sum + dp[i][k], right_sum + dp[k+1][j])`.
    *   `dp[i][j]` is the maximum score Alice can achieve among all possible split points `k`. Update `dp[i][j] = max(dp[i][j], current_split_score)`.

5.  **Result:**
    *   After filling the `dp` table, `dp[0][N-1]` will contain the maximum score Alice can obtain from the entire row of stones.

## Visualization

Let `dp[i][j]` be the maximum score for stones `stoneValue[i...j]`.
To calculate `dp[i][j]`, Alice tries all possible split points `k`.

```
Current Segment: stoneValue[i ... j]
                 <----------------->
Split at k:      stoneValue[i ... k] | stoneValue[k+1 ... j]
                 <----------------->   <------------------->
                 Left Row            | Right Row
                 (sum_left)          | (sum_right)

If sum_left > sum_right:
  Alice's score = sum_right + dp[k+1][j]  (game continues with Right Row)

If sum_right > sum_left:
  Alice's score = sum_left + dp[i][k]    (game continues with Left Row)

If sum_left == sum_right:
  Alice's score = max( sum_left + dp[i][k],   // Keep Left Row
                       sum_right + dp[k+1][j] ) // Keep Right Row

dp[i][j] = max(Alice's score for all possible k from i to j-1)
```

The DP table is filled diagonally, from smaller segments to larger ones:

```
DP Table (dp[i][j])
j
^
|   ...
|     dp[i][j]  <-- Depends on values like dp[i][k] and dp[k+1][j]
|     /    \        (which are for smaller segments, already computed)
|    /      \
|   dp[i][k] dp[k+1][j]
|  (smaller segments)
|
+----------------> i
```

## Dry Run
Let's trace Example 1: `stoneValue = [6,2,3,4,5,5]`, `N = 6`.

1.  **Prefix Sums:**
    `prefix_sums = [0, 6, 8, 11, 15, 20, 25]`
    `get_sum(i, j)` = `prefix_sums[j+1] - prefix_sums[i]`

2.  **DP Table `dp[6][6]` initialized to 0s.**

3.  **Filling `dp` table (simplified for brevity, focusing on key steps):**

| `length` | `i` | `j` | `stoneValue[i...j]` | `k` | `left_row` | `right_row` | `left_sum` | `right_sum` | `dp[i][k]` | `dp[k+1][j]` | `current_split_score` | `dp[i][j]` (max over k) |
| :------- | :-- | :-- | :------------------ | :-- | :--------- | :---------- | :--------- | :---------- | :--------- | :----------- | :-------------------- | :---------------------- |
| 2        | 0   | 1   | `[6,2]`             | 0   | `[6]`      | `[2]`       | 6          | 2           | 0          | 0            | `2 + dp[1][1] = 2`    | `2`                     |
| 2        | 1   | 2   | `[2,3]`             | 1   | `[2]`      | `[3]`       | 2          | 3           | 0          | 0            | `2 + dp[1][1] = 2`    | `2`                     |
| ...      | ... | ... | ...                 | ... | ...        | ...         | ...        | ...         | ...        | ...          | ...                   | ...                     |
| 3        | 0   | 2   | `[6,2,3]`           | 0   | `[6]`      | `[2,3]`     | 6          | 5           | 0          | `dp[1][2]=2` | `5 + dp[1][2] = 7`    |                         |
|          |     |     |                     | 1   | `[6,2]`    | `[3]`       | 8          | 3           | `dp[0][1]=2` | 0            | `3 + dp[2][2] = 3`    | `max(7,3) = 7`          |
| 3        | 1   | 3   | `[2,3,4]`           | 1   | `[2]`      | `[3,4]`     | 2          | 7           | 0          | `dp[2][3]=4` | `2 + dp[1][1] = 2`    |                         |
|          |     |     |                     | 2   | `[2,3]`    | `[4]`       | 5          | 4           | `dp[1][2]=2` | 0            | `4 + dp[3][3] = 4`    | `max(2,4) = 4`          |
| ...      | ... | ... | ...                 | ... | ...        | ...         | ...        | ...          | ...         | ...          | ...                   | ...                     |
| 6        | 0   | 5   | `[6,2,3,4,5,5]`     | 0   | `[6]`      | `[2,3,4,5,5]` | 6          | 19          | 0          | `dp[1][5]=?` | `6 + dp[1][5]`        |                         |
|          |     |     |                     | 1   | `[6,2]`    | `[3,4,5,5]` | 8          | 17          | `dp[0][1]=2` | `dp[2][5]=?` | `8 + dp[2][5]`        |                         |
|          |     |     |                     | **2** | `[6,2,3]`  | `[4,5,5]`   | **11**     | **14**      | `dp[0][2]=7` | `dp[3][5]=?` | `11 + dp[0][2] = 11 + 7 = 18` | `...max(..., 18, ...)` |
|          |     |     |                     | 3   | `[6,2,3,4]` | `[5,5]`     | 15         | 10          | `dp[0][3]=?` | `dp[4][5]=?` | `10 + dp[4][5]`       |                         |
|          |     |     |                     | 4   | `[6,2,3,4,5]` | `[5]`       | 20         | 5           | `dp[0][4]=?` | 0            | `5 + dp[5][5] = 5`    | `18`                    |

The example's first round split `[6,2,3], [4,5,5]` corresponds to `k=2`.
`left_sum = 11`, `right_sum = 14`. Bob discards `right_row`. Alice gets `11`. Game continues with `left_row = [6,2,3]`.
The score from this split is `11 + dp[0][2]`. We found `dp[0][2] = 7`. So, `11 + 7 = 18`.
This `18` will be one of the candidates for `dp[0][5]`. After checking all `k`, `dp[0][5]` will be the maximum, which turns out to be `18`.

Final Result: `dp[0][5] = 18`.

## Complexity
*   **Time Complexity:** O(N^3)
    *   Precomputing prefix sums takes O(N).
    *   The DP table has N\*N states.
    *   Each state `dp[i][j]` requires iterating through `j-i` possible split points `k`, which is up to O(N) operations.
    *   Inside the `k` loop, sum calculations are O(1) using prefix sums.
    *   Total: O(N \* N \* N) = O(N^3). Given N=500, N^3 = 125 million operations, which is acceptable.
*   **Space Complexity:** O(N^2)
    *   The `dp` table takes O(N^2) space.
    *   The `prefix_sums` array takes O(N) space.
    *   Total: O(N^2). Given N=500, N^2 = 250,000 integers, which is acceptable.

## Edge Cases
*   **`stoneValue.length == 1`**: The game ends immediately as there's only one stone. Alice's score is 0. Our solution handles this with an explicit `if n == 1: return 0` check. If not, the `dp[0][0]` would remain 0, and the loops for `length` starting from 2 would not execute, correctly returning 0.
*   **All stones have the same value**: For example, `[7,7,7,7]`. This frequently leads to `left_sum == right_sum`. Alice's logic correctly handles this by choosing the split that maximizes her future score from the remaining segment.
*   **Smallest `N` (N=2)**: `[10, 20]`.
    *   `dp[0][1]` for `[10,20]`. Only one split `k=0`: `left=[10]`, `right=[20]`. `left_sum=10`, `right_sum=20`. Bob discards `right_row`. Alice gets `left_sum=10`. Game continues with `left_row=[10]`. Score: `10 + dp[0][0] = 10 + 0 = 10`. `dp[0][1]` becomes 10. Correct.

## Solution

```python
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        # Base case: If only one stone, the game ends immediately. Alice's score is 0.
        if n == 1:
            return 0

        # 1. Precompute prefix sums for O(1) sum calculation of any subsegment.
        # prefix_sums[k] stores the sum of stoneValue[0]...stoneValue[k-1].
        # prefix_sums[0] is 0.
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i+1] = prefix_sums[i] + stoneValue[i]

        # Helper function to get sum of stoneValue[i...j]
        def get_sum(i, j):
            if i > j: # This case should not happen with correct loop bounds, but for robustness.
                return 0
            return prefix_sums[j+1] - prefix_sums[i]

        # 2. Initialize DP table.
        # dp[i][j] stores the maximum score Alice can obtain from the subsegment stoneValue[i...j].
        # All values are initialized to 0. For segments of length 1 (i.e., dp[i][i]),
        # the score is 0 as the game ends, which matches the initialization.
        dp = [[0] * n for _ in range(n)]

        # 3. Iterate DP states: Build up solutions for increasing subsegment lengths.
        # 'length' represents the number of stones in the current subsegment.
        for length in range(2, n + 1):
            # 'i' is the starting index of the subsegment.
            # 'j' is the ending index of the subsegment.
            for i in range(n - length + 1):
                j = i + length - 1

                # Alice wants to maximize her score for this segment [i...j].
                # Initialize with 0 as scores are non-negative.
                max_current_segment_score = 0 

                # Alice tries all possible split points 'k'.
                # 'k' divides [i...j] into [i...k] (left_row) and [k+1...j] (right_row).
                # Both parts must be non-empty, so k ranges from i to j-1.
                for k in range(i, j):
                    left_sum = get_sum(i, k)
                    right_sum = get_sum(k+1, j)

                    current_split_score = 0
                    if left_sum > right_sum:
                        # Bob throws away the left_row (max value). Alice gets right_sum.
                        # Game continues with the right_row [k+1...j].
                        current_split_score = right_sum + dp[k+1][j]
                    elif right_sum > left_sum:
                        # Bob throws away the right_row (max value). Alice gets left_sum.
                        # Game continues with the left_row [i...k].
                        current_split_score = left_sum + dp[i][k]
                    else: # left_sum == right_sum
                        # Alice chooses which row to throw away to maximize her score.
                        # She will keep the row that leads to a higher future score.
                        score_if_keep_left = left_sum + dp[i][k]
                        score_if_keep_right = right_sum + dp[k+1][j]
                        current_split_score = max(score_if_keep_left, score_if_keep_right)
                    
                    # Alice takes the best score among all possible splits 'k'.
                    max_current_segment_score = max(max_current_segment_score, current_split_score)
                
                dp[i][j] = max_current_segment_score
        
        # The result is the maximum score Alice can get from the entire row [0...n-1].
        return dp[0][n-1]

```

## Why This Works
This solution correctly applies dynamic programming because the problem exhibits **optimal substructure** and **overlapping subproblems**. The maximum score for a given segment of stones `[i...j]` depends on the maximum scores achievable from its subsegments (`[i...k]` and `[k+1...j]`). By building up the `dp` table for increasing segment lengths, we ensure that when we calculate `dp[i][j]`, the required `dp` values for smaller subsegments (like `dp[i][k]` and `dp[k+1][j]`) have already been computed. Alice's strategy is to pick the split that maximizes her immediate score plus the optimal future score from the remaining segment, which is precisely what the `max` operations capture. Bob's fixed rule (discard max sum) and Alice's optimal choice when sums are equal are correctly modeled, guaranteeing the overall maximum score for Alice.

---
<sub>Generated 2026-08-17 02:06 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
