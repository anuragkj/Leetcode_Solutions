# [1621] Number of Sets of K Non-Overlapping Line Segments

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-09-16 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/)

**Topics:** Math, Dynamic Programming, Combinatorics, Prefix Sum

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given n points on a 1-D plane, where the i^th point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.

Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 10^9 + 7.

Example 1:

Input: n = 4, k = 2
Output: 5
Explanation: The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.

Example 2:

Input: n = 3, k = 1
Output: 3
Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.

Example 3:

Input: n = 30, k = 7
Output: 796297179
Explanation: The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 10^9 + 7 gives us 796297179.

Constraints:

- 2 <= n <= 1000

- 1 <= k <= n-1

**Examples / sample tests:**

```
4
2
3
1
30
7
```

---

## Problem Summary
Given `n` points on a 1-D line at integer coordinates `0, 1, ..., n-1`, we need to find the number of ways to draw exactly `k` non-overlapping line segments. Each segment must cover at least two points (i.e., have length at least 1). Segments can share endpoints. The result should be returned modulo `10^9 + 7`.

## Intuition
This problem asks us to count combinations of segments under specific constraints. The "non-overlapping" and "share endpoints" conditions, combined with the need to select a fixed number of segments (`k`), strongly suggest a **Dynamic Programming (DP)** approach.

Let's think about how we can build up the solution. If we consider points from left to right, when we are at point `i`, we have two main choices for forming segments:
1.  **Don't use point `i`** as the right endpoint of any segment. In this case, we rely on the ways we could form segments using points up to `i-1`.
2.  **Use point `i`** as the right endpoint of the `k`-th segment. If we draw a segment `(p, i)`, then the previous `k-1` segments must have been formed using points up to `p`.

This structure leads to a DP state where `dp[i][j]` represents the number of ways to draw `j` segments using points `0, ..., i-1`.

## Approach
We will use dynamic programming. Let `dp[i][j]` be the number of ways to draw exactly `j` non-overlapping line segments using the first `i` points (i.e., points `0, 1, ..., i-1`).

1.  **DP State Definition:**
    `dp[i][j]` = Number of ways to draw `j` segments using points `0, ..., i-1`.
    `i` ranges from `0` to `n`. `j` ranges from `0` to `k`.

2.  **Base Cases:**
    *   `dp[i][0] = 1` for all `i` from `0` to `n`. There is always one way to draw zero segments (by doing nothing).
    *   `dp[0][j] = 0` for `j > 0`. With zero points, we cannot draw any segments.
    *   If `i < j + 1`, then `dp[i][j] = 0`. To draw `j` segments, we need at least `j+1` points (e.g., `(0,1), (1,2), ..., (j-1,j)` uses `j+1` points).

3.  **Recurrence Relation:**
    To calculate `dp[i][j]`:
    *   **Option 1: Point `i-1` is NOT the right endpoint of any segment.**
        In this case, all `j` segments must be formed using points `0, ..., i-2`. The number of ways is `dp[i-1][j]`.
    *   **Option 2: Point `i-1` IS the right endpoint of the `j`-th segment.**
        Let this `j`-th segment be `(p, i-1)`, where `0 <= p < i-1`.
        The remaining `j-1` segments must be formed using points `0, ..., p`. The number of ways to do this is `dp[p+1][j-1]`.
        We need to sum this over all possible `p`. So, we sum `dp[x][j-1]` for `x` from `1` to `i-1`.
        This sum is `sum_{x=1}^{i-1} dp[x][j-1]`.

    Combining these options:
    `dp[i][j] = dp[i-1][j] + sum_{x=1}^{i-1} dp[x][j-1]`

4.  **Optimization (Prefix Sum):**
    The `sum_{x=1}^{i-1} dp[x][j-1]` part can be computed efficiently using a prefix sum.
    Let `S[i][j-1] = sum_{x=1}^{i} dp[x][j-1]`.
    Then `sum_{x=1}^{i-1} dp[x][j-1]` is simply `S[i-1][j-1]`.
    So, the recurrence becomes: `dp[i][j] = dp[i-1][j] + S[i-1][j-1]`.
    And `S[i][j-1] = S[i-1][j-1] + dp[i][j-1]`.

    We can implement this with `O(N)` space by noticing that `dp[i][j]` only depends on values from the current column (`j`) at `i-1` and values from the previous column (`j-1`).

5.  **Algorithm Steps (O(N) space):**
    a.  Initialize `MOD = 10^9 + 7`.
    b.  Create a 1D array `dp` of size `n+1`, initialized with `1`s. This `dp` array will store `dp[i][j-1]` values from the previous iteration (for `j-1` segments). Initially, it represents `dp[i][0] = 1` for all `i`.
    c.  Loop `j` from `1` to `k` (number of segments):
        i.   Create a new 1D array `new_dp` of size `n+1`, initialized with `0`s. This will store `dp[i][j]` values for the current `j`.
        ii.  Initialize `current_prefix_sum = 0`. This variable will accumulate `sum_{x=1}^{i-1} dp[x][j-1]`.
        iii. Loop `i` from `1` to `n` (number of points):
            1.  If `i < j + 1` (not enough points to form `j` segments), set `new_dp[i] = 0`.
            2.  Else (`i >= j + 1`):
                *   Update `current_prefix_sum`: `current_prefix_sum = (current_prefix_sum + dp[i-1]) % MOD`. Here, `dp[i-1]` refers to `dp[i-1][j-1]` from the previous iteration.
                *   Calculate `new_dp[i]`: `new_dp[i] = (new_dp[i-1] + current_prefix_sum) % MOD`. Here, `new_dp[i-1]` refers to `dp[i-1][j]` from the current iteration.
        iv. After the inner loop, set `dp = new_dp` to prepare for the next `j`.
    d.  Return `dp[n]`, which holds `dp[n][k]`.

## Visualization
The DP table `dp[i][j]` (where `i` is rows, `j` is columns) shows how each cell `dp[i][j]` depends on values from the previous row in the same column (`dp[i-1][j]`) and a sum of values from the previous column (`dp[x][j-1]` for `x < i`). The prefix sum optimization makes the sum efficient.

```mermaid
graph TD
    subgraph DP Table (conceptual)
        A[dp[i][j]]
        B[dp[i-1][j]]
        C[dp[i-1][j-1]]
        D[dp[i-2][j-1]]
        E[dp[1][j-1]]
    end

    B -- "Don't use point i-1" --> A
    C -- "Use point i-1 as end of segment (p, i-1), previous j-1 segments end at p" --> A
    D -- "..." --> A
    E -- "..." --> A

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:1px
    style C fill:#cfc,stroke:#333,stroke-width:1px
    style D fill:#cfc,stroke:#333,stroke-width:1px
    style E fill:#cfc,stroke:#333,stroke-width:1px

    linkStyle 0 stroke:#f66,stroke-width:2px,fill:none;
    linkStyle 1 stroke:#66f,stroke-width:2px,fill:none;
    linkStyle 2 stroke:#66f,stroke-width:2px,fill:none;
    linkStyle 3 stroke:#66f,stroke-width:2px,fill:none;
```
In the `O(N)` space optimized version:
- `new_dp[i]` is `A`.
- `new_dp[i-1]` is `B`.
- `dp[i-1]` (from the previous `j` iteration) is `C`.
- `current_prefix_sum` accumulates `C, D, E, ...` for the current `i`.

## Dry Run
Let's trace `n=4, k=2` using the `O(N)` space optimized approach.
`MOD = 10^9 + 7`

1.  **Initialization:**
    `dp = [1, 1, 1, 1, 1]` (Represents `dp[i][0]` for `i=0..4`)

2.  **`j = 1` (calculating ways to form 1 segment):**
    `new_dp = [0, 0, 0, 0, 0]`
    `current_prefix_sum = 0`

    *   `i = 1`: `1 < j+1` (1 < 2). `new_dp[1] = 0`.
    *   `i = 2`: `2 >= j+1` (2 >= 2).
        `current_prefix_sum = (0 + dp[1]) % MOD = (0 + 1) % MOD = 1`.
        `new_dp[2] = (new_dp[1] + current_prefix_sum) % MOD = (0 + 1) % MOD = 1`.
        (1 way: `(0,1)`)
    *   `i = 3`: `3 >= j+1` (3 >= 2).
        `current_prefix_sum = (1 + dp[2]) % MOD = (1 + 1) % MOD = 2`.
        `new_dp[3] = (new_dp[2] + current_prefix_sum) % MOD = (1 + 2) % MOD = 3`.
        (3 ways: `(0,1), (0,2), (1,2)`)
    *   `i = 4`: `4 >= j+1` (4 >= 2).
        `current_prefix_sum = (2 + dp[3]) % MOD = (2 + 1) % MOD = 3`.
        `new_dp[4] = (new_dp[3] + current_prefix_sum) % MOD = (3 + 3) % MOD = 6`.
        (6 ways: `(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)`)

    After `j=1` loop: `dp = new_dp = [0, 0, 1, 3, 6]`

3.  **`j = 2` (calculating ways to form 2 segments):**
    `new_dp = [0, 0, 0, 0, 0]`
    `current_prefix_sum = 0`

    *   `i = 1`: `1 < j+1` (1 < 3). `new_dp[1] = 0`.
    *   `i = 2`: `2 < j+1` (2 < 3). `new_dp[2] = 0`.
    *   `i = 3`: `3 >= j+1` (3 >= 3).
        `current_prefix_sum = (0 + dp[2]) % MOD = (0 + 1) % MOD = 1`.
        `new_dp[3] = (new_dp[2] + current_prefix_sum) % MOD = (0 + 1) % MOD = 1`.
        (1 way: `{(0,1), (1,2)}`)
    *   `i = 4`: `4 >= j+1` (4 >= 3).
        `current_prefix_sum = (1 + dp[3]) % MOD = (1 + 3) % MOD = 4`.
        `new_dp[4] = (new_dp[3] + current_prefix_sum) % MOD = (1 + 4) % MOD = 5`.
        (5 ways: `{(0,1),(1,2)}, {(0,1),(2,3)}, {(0,2),(2,3)}, {(0,1),(1,3)}, {(1,2),(2,3)}`)

    After `j=2` loop: `dp = new_dp = [0, 0, 0, 1, 5]`

4.  **Final Result:**
    The loop for `j` finishes. Return `dp[n]`, which is `dp[4] = 5`. This matches Example 1.

## Complexity
*   **Time Complexity:** `O(N * K)`. The outer loop runs `k` times, and the inner loop runs `n` times. Each operation inside the loop is constant time. Given `N, K <= 1000`, this is `1000 * 1000 = 10^6` operations, which is efficient enough.
*   **Space Complexity:** `O(N)`. We use two 1D arrays of size `n+1` (`dp` and `new_dp`) at any given time.

## Edge Cases
*   **`n=2, k=1`**: The smallest valid input. Points `0, 1`. One segment `(0,1)`. Expected output: `1`.
    Our DP: `dp[2][1]` will be `1`. Correct.
*   **`k = n-1`**: Maximum possible `k`. E.g., `n=3, k=2`. Points `0,1,2`. Only one way: `{(0,1), (1,2)}`. Expected output: `1`.
    Our DP: `dp[3][2]` will be `1`. Correct.
*   **`k` is too large for `n`**: The condition `i < j+1` correctly handles cases where there aren't enough points to form `j` segments, resulting in `0` ways. For example, `n=3, k=3` would result in `0` ways because `3` segments require at least `4` points.
*   **Modulo Arithmetic**: The modulo operation is applied at each addition to prevent integer overflow, ensuring the result stays within the required range.

## Solution

```python
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[i] will store the number of ways to draw 'j' segments
        # using points from 0 to i-1 (i points total).
        # Initially, dp stores the base case for j=0:
        # dp[i] = 1 for all i (one way to draw 0 segments: do nothing).
        dp = [1] * (n + 1)

        # Iterate for each number of segments from 1 to k
        for j in range(1, k + 1):
            # new_dp will store the results for the current 'j' segments.
            # It's initialized to all zeros.
            new_dp = [0] * (n + 1)
            
            # current_prefix_sum accumulates the sum of dp[x][j-1] for x from 1 to i-1.
            # This is used for the "use point i-1 as right endpoint" case.
            current_prefix_sum = 0

            # Iterate for each number of points from 1 to n.
            # 'i' represents the count of points (0 to i-1).
            for i in range(1, n + 1):
                # Base case: To draw 'j' segments, we need at least 'j+1' points.
                # If 'i' (number of points) is less than 'j+1', it's impossible
                # to form 'j' segments. So, new_dp[i] remains 0.
                if i >= j + 1:
                    # Case 1: Point i-1 is used as the right endpoint of the j-th segment.
                    # This segment is (p, i-1) for some 0 <= p < i-1.
                    # The previous j-1 segments must be formed using points 0 to p.
                    # The number of ways to form j-1 segments using points 0 to p is dp[p+1][j-1].
                    # In our O(N) space setup, dp[p+1][j-1] is stored in dp[p+1] from the previous iteration.
                    # We sum dp[x][j-1] for x from 1 to i-1.
                    # This sum is accumulated in current_prefix_sum.
                    # dp[i-1] here refers to dp[i-1][j-1] from the previous iteration.
                    current_prefix_sum = (current_prefix_sum + dp[i-1]) % MOD
                    
                    # Case 2: Point i-1 is NOT used as the right endpoint of any segment.
                    # In this case, we need to form j segments using points 0 to i-2.
                    # This is new_dp[i-1] (which is dp[i-1][j] from the current iteration).
                    new_dp[i] = (new_dp[i-1] + current_prefix_sum) % MOD
            
            # After processing all 'i' for the current 'j', update dp to new_dp.
            # This makes new_dp (current j-th column) the dp for the next iteration (j+1)-th column.
            dp = new_dp
        
        # The final result is dp[n], which represents the number of ways to draw 'k' segments
        # using 'n' points (0 to n-1).
        return dp[n]

```

## Why This Works
The dynamic programming approach works by systematically building up solutions for smaller subproblems. `dp[i][j]` correctly counts all ways to form `j` segments using points `0, ..., i-1` by considering two mutually exclusive and exhaustive cases for the point `i-1`:
1.  **Point `i-1` is not used as an endpoint:** All `j` segments must be formed using points `0, ..., i-2`. This is covered by `dp[i-1][j]`.
2.  **Point `i-1` is used as the right endpoint of the `j`-th segment:** This segment is `(p, i-1)`. The remaining `j-1` segments must be formed using points `0, ..., p`. By summing `dp[x][j-1]` for all valid `x` (representing `p+1`), we account for all possible starting points `p` for the last segment.

The prefix sum optimization efficiently calculates the sum part of the recurrence, reducing the inner loop's complexity from `O(N)` to `O(1)`, leading to an overall `O(NK)` time complexity. The `O(N)` space optimization is achieved by only storing the results for the

---
<sub>Generated 2026-09-16 05:08 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
