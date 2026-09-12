# [3414] Maximum Score of Non-overlapping Intervals

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-09-12 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/)

**Topics:** Array, Binary Search, Dynamic Programming, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 2D integer array intervals, where intervals[i] = [l_i, r_i, weight_i]. Interval i starts at position l_i and ends at r_i, and has a weight of weight_i. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.

Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

Example 1:

Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

Output: [2,3]

Explanation:

You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

Example 2:

Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

Output: [1,3,5,6]

Explanation:

You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

Constraints:

- 1 <= intevals.length <= 5 * 10^4

- intervals[i].length == 3

- intervals[i] = [l_i, r_i, weight_i]

- 1 <= l_i <= r_i <= 10^9

- 1 <= weight_i <= 10^9

**Examples / sample tests:**

```
[[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]
[[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]
```

---

## Problem Summary
The problem asks us to select a maximum of 4 non-overlapping intervals from a given list, such that the sum of their weights is maximized. If multiple sets of intervals yield the same maximum score, we must return the one with the lexicographically smallest list of original indices.

## Intuition
This problem is a variation of the classic **Weighted Interval Scheduling** problem.
1.  **Small `k` is key**: The constraint of choosing "up to 4" intervals is very small. If `k` were large, this would be a more complex problem, but `k=4` suggests that we can incorporate the count of chosen intervals directly into our dynamic programming state.
2.  **Dynamic Programming (DP)**: Interval scheduling problems are typically solved with DP. We need to decide for each interval whether to include it or not, and this decision depends on previous choices.
3.  **Sorting**: A common strategy for interval problems is to sort them. Sorting by **right boundary** is particularly useful because it simplifies finding non-overlapping previous intervals.
4.  **Lexicographical Requirement**: This is the trickiest part. Standard DP usually just finds the maximum score. To find the *indices* and specifically the *lexicographically smallest* set of indices, our DP state needs to store not just the maximum score, but also the actual indices chosen. When scores are equal, we'll need a custom comparison to pick the lexicographically smaller index list. Since we only pick up to 4 intervals, storing a small tuple of indices is feasible.

## Approach
The optimal algorithm uses dynamic programming with a state that tracks both the maximum score and the chosen indices, combined with binary search for efficiency.

1.  **Augment Intervals**: First, we need to keep track of the original index of each interval. We'll transform each `[l, r, weight]` into `[l, r, weight, original_index]`.
2.  **Sort Intervals**: Sort the augmented intervals. The primary sort key is the **right boundary (`r`)**. If `r` values are equal, sort by **left boundary (`l`)**, and then by **original index** for deterministic tie-breaking. This sorting order is crucial for the DP and binary search steps.
3.  **DP State Definition**: We'll use a 2D DP table, `dp[k][i]`, where:
    *   `k` represents the number of intervals chosen so far (from 0 to 4).
    *   `i` represents the index of the current interval being considered in the *sorted* `augmented_intervals` array.
    *   `dp[k][i]` will store a tuple: `(max_score, idx1, idx2, idx3, idx4)`.
        *   `max_score`: The maximum total weight achieved.
        *   `idx1, idx2, idx3, idx4`: The original indices of the chosen intervals, sorted in ascending order. Unused slots are filled with `-1` to maintain a fixed tuple length for consistent lexicographical comparison.
    *   Initialize `dp[k][i]` to `(-1, -1, -1, -1, -1)` for `k > 0` (representing an invalid or unreachable state) and `dp[0][i]` to `(0, -1, -1, -1, -1)` for all `i` (representing a valid state with 0 score and 0 intervals).
4.  **Custom Comparison Function (`is_better`)**: We need a helper function to compare two DP states. It should prioritize:
    *   Higher score.
    *   If scores are equal, the state with the lexicographically smaller tuple of indices.
    *   Invalid states (score of -1) are always worse than valid states.
5.  **Fill DP Table**: Iterate `k` from 1 to 4 (number of intervals) and `i` from 0 to `N-1` (index in `augmented_intervals`):
    *   For each `augmented_intervals[i] = [l_i, r_i, w_i, original_idx_i]`:
        *   **Option 1: Don't include `augmented_intervals[i]`**: The best score for `k` intervals up to `i` is the same as the best score for `k` intervals up to `i-1`. This state is `dp[k][i-1]` (or an invalid state if `i=0`).
        *   **Option 2: Include `augmented_intervals[i]`**:
            *   We need to find a previous interval `augmented_intervals[j]` that does not overlap with `augmented_intervals[i]`. This means `augmented_intervals[j].r < l_i`.
            *   Use **binary search** (`bisect_left`) on the `r` values of `augmented_intervals[0...i-1]` to find the largest index `j` such that `augmented_intervals[j].r < l_i`.
            *   Retrieve the DP state `dp[k-1][j]` (or `(0, -1, -1, -1, -1)` if `k=1` and no such `j` exists, meaning `augmented_intervals[i]` is the first interval chosen).
            *   If `dp[k-1][j]` is a valid state, calculate `new_score = w_i + dp[k-1][j].score`.
            *   Combine the indices from `dp[k-1][j]` with `original_idx_i`, sort them, and pad with `-1`s to form the `new_indices_tuple`.
            *   This forms `option2_state = (new_score,) + new_indices_tuple`.
        *   **Update `dp[k][i]`**: Compare `option1_state` and `option2_state` using the `is_better` function and store the result in `dp[k][i]`.
6.  **Retrieve Result**: After filling the entire DP table, the overall maximum score and lexicographically smallest indices will be found by comparing `dp[k][N-1]` for all `k` from 0 to 4 using the `is_better` function. Finally, filter out the `-1`s from the chosen index tuple to get the final list.

## Visualization
The core idea involves iterating through sorted intervals and, for each, deciding whether to include it. If included, we look back for the best previous non-overlapping set using binary search.

```mermaid
graph TD
    subgraph Intervals (sorted by right boundary)
        A[0: [l0,r0,w0,orig0]]
        B[1: [l1,r1,w1,orig1]]
        C[2: [l2,r2,w2,orig2]]
        ...
        I[i: [li,ri,wi,origi]]
        ...
        N[N-1: [lN-1,rN-1,wN-1,origN-1]]
    end

    subgraph DP Table
        dp_k_minus_1["dp[k-1] row (previous count of intervals)"]
        dp_k_i_minus_1["dp[k][i-1] (current count, previous interval)"]
    end

    I -- Current interval `i` --> Calculate_dp_k_i
    Calculate_dp_k_i["Calculate dp[k][i]"]

    Calculate_dp_k_i -- Option 1: Exclude interval `i` --> dp_k_i_minus_1
    Calculate_dp_k_i -- Option 2: Include interval `i` --> Find_j

    Find_j["Binary Search for `j`: largest index s.t. intervals[j].r < intervals[i].l"]
    Find_j -- Found `j` --> C
    C -- Get `dp[k-1][j]` --> dp_k_minus_1

    dp_k_minus_1 -- (score_prev, indices_prev) --> Combine_with_i
    Combine_with_i["Combine: `score_prev + wi` and `sorted(indices_prev + [origi])`"]
    Combine_with_i -- (new_score, new_indices) --> Compare_options

    Compare_options["Compare (score, indices) from Option 1 and Option 2 using `is_better`"]
    Compare_options -- Choose best (score, indices) --> dp_k_i["dp[k][i]"]

    style I fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#ccf,stroke:#333,stroke-width:2px
```

## Dry Run
Let's trace Example 1: `intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]`

1.  **Augment & Sort**:
    Original indices: `0: [1,3,2], 1: [4,5,2], 2: [1,5,5], 3: [6,9,3], 4: [6,7,1], 5: [8,9,1]`
    Sorted `augmented_intervals` (by `r`, then `l`, then `original_idx`):
    `N = 6`
    `sorted_intervals = [`
    `  (0): [1,3,2,0]`
    `  (1): [4,5,2,1]`
    `  (2): [1,5,5,2]`
    `  (3): [6,7,1,4]`
    `  (4): [6,9,3,3]`
    `  (5): [8,9,1,5]`
    `]`

2.  **DP Table Initialization**:
    `dp[0][i] = (0, -1, -1, -1, -1)` for all `i`.
    `dp[k][i] = (-1, -1, -1, -1, -1)` for `k > 0`.

3.  **Filling DP (Partial Trace)**:
    *   **`k = 1` (choosing 1 interval)**:
        *   `i = 0` (`[1,3,2,0]`): `dp[1][0] = (2, 0, -1, -1, -1)` (score 2, index 0)
        *   `i = 1` (`[4,5,2,1]`):
            *   Option 1 (exclude): `dp[1][0] = (2, 0, -1, -1, -1)`
            *   Option 2 (include `[4,5,2,1]`): `l_i=4`. `j=0` (since `sorted_intervals[0].r=3 < 4`). `prev_dp_state = dp[0][0] = (0, -1, -1, -1, -1)`. New score `2+0=2`, indices `[1]`. State `(2, 1, -1, -1, -1)`.
            *   `dp[1][1] = is_better((2,0,...), (2,1,...)) = (2, 0, -1, -1, -1)` (lexicographically smaller indices)
        *   `i = 2` (`[1,5,5,2]`):
            *   Option 1: `dp[1][1] = (2, 0, -1, -1, -1)`
            *   Option 2 (include `[1,5,5,2]`): `l_i=1`. `j=-1` (no non-overlapping previous). `prev_dp_state = (0, -1, -1, -1, -1)`. New score `5+0=5`, indices `[2]`. State `(5, 2, -1, -1, -1)`.
            *   `dp[1][2] = is_better((2,0,...), (5,2,...)) = (5, 2, -1, -1, -1)` (higher score)
        *   ... (continues for `i=3,4,5`) ...
        *   `dp[1][5]` will be `(5, 2, -1, -1, -1)` (max score 5 from index 2)

    *   **`k = 2` (choosing 2 intervals)**:
        *   `i = 0` (`[1,3,2,0]`): `dp[2][0] = (-1,...)` (cannot pick 2 intervals from 1)
        *   `i = 1` (`[4,5,2,1]`):
            *   Option 1: `dp[2][0] = (-1,...)`
            *   Option 2 (include `[4,5,2,1]`): `l_i=4`. `j=0`. `prev_dp_state = dp[1][0] = (2, 0, -1, -1, -1)`. New score `2+2=4`, indices `sorted([0,1])=[0,1]`. State `(4, 0, 1, -1, -1)`.
            *   `dp[2][1] = (4, 0, 1, -1, -1)`
        *   `i = 2` (`[1,5,5,2]`):
            *   Option 1: `dp[2][1] = (4, 0, 1, -1, -1)`
            *   Option 2 (include `[1,5,5,2]`): `l_i=1`. `j=-1`. `prev_dp_state = (-1,...)` (cannot pick 1 interval before `[1,5,5,2]` for `k-1=1`). So `option2_state = (-1,...)`.
            *   `dp[2][2] = (4, 0, 1, -1, -1)`
        *   `i = 3` (`[6,7,1,4]`):
            *   Option 1: `dp[2][2] = (4, 0, 1, -1, -1)`
            *   Option 2 (include `[6,7,1,4]`): `l_i=6`. `j=2` (since `sorted_intervals[2].r=5 < 6`). `prev_dp_state = dp[1][2] = (5, 2, -1, -1, -1)`. New score `1+5=6`, indices `sorted([2,4])=[2,4]`. State `(6, 2, 4, -1, -1)`.
            *   `dp[2][3] = is_better((4,0,1,...), (6,2,4,...)) = (6, 2, 4, -1, -1)`
        *   `i = 4` (`[6,9,3,3]`):
            *   Option 1: `dp[2][3] = (6, 2, 4, -1, -1)`
            *   Option 2 (include `[6,9,3,3]`): `l_i=6`. `j=2`. `prev_dp_state = dp[1][2] = (5, 2, -1, -1, -1)`. New score `3+5=8`, indices `sorted([2,3])=[2,3]`. State `(8, 2, 3, -1, -1)`.
            *   `dp[2][4] = is_better((6,2,4,...), (8,2,3,...)) = (8, 2, 3, -1, -1)`
        *   `i = 5` (`[8,9,1,5]`):
            *   Option 1: `dp[2][4] = (8, 2, 3, -1, -1)`
            *   Option 2 (include `[8,9,1,5]`): `l_i=8`. `j=3`. `prev_dp_state = dp[1][3] = (5, 2, -1, -1, -1)`. New score `1+5=6`, indices `sorted([2,5])=[2,5]`. State `(6, 2, 5, -1, -1)`.
            *   `dp[2][5] = is_better((8,2,3,...), (6,2,5,...)) = (8, 2, 3, -1, -1)`

4.  **Final Result**:
    Comparing `dp[k][5]` for `k=0..4`:
    *   `dp[0][5] = (0, -1, -1, -1, -1)`
    *   `dp[1][5] = (5, 2, -1, -1, -1)`
    *   `dp[2][5] = (8, 2, 3, -1, -1)`
    *   (Assuming `dp[3][5]` and `dp[4][5]` don't yield better results in this example)
    The best overall state is `(8, 2, 3, -1, -1)`.
    Filtering out `-1`s gives `[2, 3]`. This matches Example 1.

## Complexity
*   **Time Complexity**: `O(N log N)`
    *   Sorting the intervals takes `O(N log N)`.
    *   The DP table has `5 * N` states. Each state computation involves:
        *   A binary search (`bisect_left`) which takes `O(log N)`.
        *   List operations (filtering, sorting, padding indices) which take `O(k)` time, where `k` is at most 4. Since `k` is a constant, this is `O(1)`.
    *   Total DP time: `5 * N * (log N + O(1)) = O(N log N)`.
    *   Overall, the dominant factor is `O(N log N)`.
*   **Space Complexity**: `O(N)`
    *   `augmented_intervals` list: `O(N)`.
    *   `dp` table: `5 * N` states, each storing a tuple of constant size (score + 4 indices). This is `O(N)`.
    *   Overall, the space complexity is `O(N)`.

## Edge Cases
*   **Empty `intervals` list**: The problem constraints state `1 <= intervals.length`, so this won't occur. If it could, the code would correctly return `[]` as `best_overall_state` would remain `(0, -1, -1, -1, -1)`.
*   **Single interval**: `N=1`. The DP correctly processes this, resulting in the single interval's weight and index if chosen.
*   **All intervals overlap**: In this case, only one interval can be chosen. The DP will correctly find the single interval with the maximum weight (and lexicographically smallest index if ties exist).
*   **All intervals have zero weight**: The problem constraints state `1 <= weight_i`, so weights are always positive.
*   **Large coordinates/weights**: Python's arbitrary-precision integers handle large `l, r, weight` values without overflow.

## Solution

```python
import bisect
from typing import List, Tuple

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # 1. Augment intervals with their original indices
        # Each interval becomes [l_i, r_i, weight_i, original_index_i]
        augmented_intervals = []
        for i, (l, r, weight) in enumerate(intervals):
            augmented_intervals.append([l, r, weight, i])

        # 2. Sort intervals by right boundary, then left boundary, then original index.
        # This sorting is crucial for the DP approach and binary search.
        # - Sorting by `r` allows us to efficiently find non-overlapping previous intervals.
        # - Sorting by `l` (and then `original_index`) for ties in `r` ensures a deterministic order,
        #   which is important for consistent lexicographical comparison of indices.
        augmented_intervals.sort(key=lambda x: (x[1], x[0], x[3]))

        N = len(augmented_intervals)
        
        # Helper function to compare two DP states (score, idx1, idx2, idx3, idx4)
        # Returns the "better" state based on:
        # 1. Higher score.
        # 2. If scores are equal, lexicographically smaller tuple of indices.
        # Invalid states (score -1) are always worse than valid states.
        def is_better(state1: Tuple[int, int, int, int, int], state2: Tuple[int, int, int, int, int]) -> Tuple[int, int, int, int, int]:
            score1, indices1 = state1[0], state1[1:]
            score2, indices2 = state2[0], state2[1:]

            # Prioritize higher score
            if score1 > score2:
                return state1
            if score2 > score1

---
<sub>Generated 2026-09-12 04:56 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
