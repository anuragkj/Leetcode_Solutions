# [3336] Find the Number of Subsequences With Equal GCD

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-07-14 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/)

**Topics:** Array, Math, Dynamic Programming, Number Theory

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums.

Your task is to find the number of pairs of non-empty subsequences (seq1, seq2) of nums that satisfy the following conditions:

- The subsequences seq1 and seq2 are disjoint, meaning no index of nums is common between them.

- The GCD of the elements of seq1 is equal to the GCD of the elements of seq2.

Return the total number of such pairs.

Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:

Input: nums = [1,2,3,4]

Output: 10

Explanation:

The subsequence pairs which have the GCD of their elements equal to 1 are:

- ([1, 2, 3, 4], [1, 2, 3, 4])

- ([1, 2, 3, 4], [1, 2, 3, 4])

- ([1, 2, 3, 4], [1, 2, 3, 4])

- ([1, 2, 3, 4], [1, 2, 3, 4])

- ([1, 2, 3, 4], [1, 2, 3, 4])

- ([1, 2, 3, 4], [1, 2, 3, 4])

- ([1, 2, 3, 4], [1, 2, 3, 4])

- ([1, 2, 3, 4], [1, 2, 3, 4])

- ([1, 2, 3, 4], [1, 2, 3, 4])

- ([1, 2, 3, 4], [1, 2, 3, 4])

Example 2:

Input: nums = [10,20,30]

Output: 2

Explanation:

The subsequence pairs which have the GCD of their elements equal to 10 are:

- ([10, 20, 30], [10, 20, 30])

- ([10, 20, 30], [10, 20, 30])

Example 3:

Input: nums = [1,1,1,1]

Output: 50

Constraints:

- 1 <= nums.length <= 200

- 1 <= nums[i] <= 200

**Examples / sample tests:**

```
[1,2,3,4]
[10,20,30]
[1,1,1,1]
```

---

## Problem Summary
The task is to count the number of pairs of non-empty subsequences, `(seq1, seq2)`, from a given integer array `nums`. These subsequences must be **disjoint** (no common elements by index) and their **Greatest Common Divisor (GCD)** must be equal: `gcd(seq1) == gcd(seq2)`. The final count should be returned modulo `10^9 + 7`.

## Intuition
The core challenge lies in simultaneously building two disjoint subsequences and tracking their GCDs. The constraints `nums.length <= 200` and `nums[i] <= 200` are crucial. The small maximum value for `nums[i]` (let's call it `MAX_VAL = 200`) suggests that we can use a dynamic programming approach where GCDs are part of the state.

1.  **Disjointness**: For each number `x` in `nums`, we have three choices:
    *   `x` goes into `seq1`.
    *   `x` goes into `seq2`.
    *   `x` goes into neither `seq1` nor `seq2`.
    This ensures that `seq1` and `seq2` are always disjoint.

2.  **Tracking GCDs**: We need to keep track of the GCD of `seq1` and `seq2` as we process elements. A common trick for GCD of an empty set is to define `gcd(0, x) = x`. This allows us to use `0` to represent an empty subsequence's GCD, and when the first element `x` is added, its GCD naturally becomes `x`.

3.  **Dynamic Programming State**: Let `dp[g1][g2]` be the number of ways to form two disjoint subsequences `seq1` and `seq2` from the elements processed so far, such that `gcd(seq1) = g1` and `gcd(seq2) = g2`. Here, `g1=0` means `seq1` is empty, and `g2=0` means `seq2` is empty. The dimensions of this DP table would be `(MAX_VAL + 1) x (MAX_VAL + 1)`.

4.  **Transitions**: When processing a new number `x` from `nums`:
    For each existing state `(g1, g2)` with `count = dp[g1][g2]` ways:
    *   **`x` goes to neither**: The state `(g1, g2)` remains, and its count increases by `count`.
    *   **`x` goes to `seq1`**: The new state becomes `(gcd(g1, x), g2)`. Its count increases by `count`.
    *   **`x` goes to `seq2`**: The new state becomes `(g1, gcd(g2, x))`. Its count increases by `count`.

5.  **Final Answer**: After processing all numbers, we need to sum `dp[g][g]` for all `g` from `1` to `MAX_VAL`. This sum represents the total number of pairs `(seq1, seq2)` where both are non-empty (since `g > 0`) and `gcd(seq1) == gcd(seq2) == g`.

The time complexity will be `N * MAX_VAL^2 * log(MAX_VAL)` (where `log(MAX_VAL)` is for GCD calculation), which is roughly `200 * 200^2 * log(200) = 6.4 * 10^7`, feasible within typical time limits.

## Approach
1.  **Initialization**:
    *   Define `MOD = 10^9 + 7`.
    *   Determine `MAX_VAL = 200` (from constraints).
    *   Create a 2D DP table `dp` of size `(MAX_VAL + 1) x (MAX_VAL + 1)`, initialized with zeros.
    *   Set the base case: `dp[0][0] = 1`. This represents one way to have two empty subsequences before processing any numbers.

2.  **Iterate through `nums`**:
    For each number `x` in the input array `nums`:
    *   Create a temporary 2D DP table `new_dp` of the same size, initialized as a deep copy of the current `dp` table. This `new_dp` will store the results after considering `x`. The initial copy handles the case where `x` is not added to either subsequence.
    *   Iterate through all possible `g1` from `0` to `MAX_VAL`.
    *   Iterate through all possible `g2` from `0` to `MAX_VAL`.
    *   If `dp[g1][g2]` is `0`, continue (no ways to reach this state).
    *   Let `count = dp[g1][g2]`.
    *   **Add `x` to `seq1`**: Calculate `new_g1 = math.gcd(g1, x)`. Add `count` to `new_dp[new_g1][g2]`, taking modulo `MOD`.
    *   **Add `x` to `seq2`**: Calculate `new_g2 = math.gcd(g2, x)`. Add `count` to `new_dp[g1][new_g2]`, taking modulo `MOD`.
    *   *(Note: The `new_dp` was initialized as a copy of `dp`, so `x` going to neither is implicitly handled by `new_dp[g1][g2] = (new_dp[g1][g2] + count)` if we were to explicitly add it. Since `new_dp` starts as `dp`, `dp[g1][g2]` is already in `new_dp[g1][g2]`, so we don't add it again.)*
    *   After iterating through all `(g1, g2)` pairs, update `dp = new_dp`.

3.  **Calculate Final Result**:
    *   Initialize `total_pairs = 0`.
    *   Iterate `g` from `1` to `MAX_VAL`.
    *   Add `dp[g][g]` to `total_pairs`, taking modulo `MOD`.
    *   Return `total_pairs`.

## Visualization

Let's visualize the DP table `dp[g1][g2]` and how an element `x` updates it.
`g1` represents `gcd(seq1)` (x-axis), `g2` represents `gcd(seq2)` (y-axis). `0` means empty.

```mermaid
graph TD
    subgraph Initial State (dp)
        A[dp[0][0] = 1]
        B[Other dp[g1][g2] = 0]
    end

    subgraph Processing element 'x'
        direction LR
        C{For each (g1, g2) in dp with count > 0} --> D[Create new_dp as a copy of dp]
        C --> E[count = dp[g1][g2]]

        E --> F1{x goes to neither}
        F1 --> G1[new_dp[g1][g2] += count]

        E --> F2{x goes to seq1}
        F2 --> H1[new_g1 = gcd(g1, x)]
        H1 --> I1[new_dp[new_g1][g2] += count]

        E --> F3{x goes to seq2}
        F3 --> H2[new_g2 = gcd(g2, x)]
        H2 --> I2[new_dp[g1][new_g2] += count]

        G1 & I1 & I2 --> J[After all (g1, g2) processed, set dp = new_dp]
    end

    subgraph Example Update for x=2, from dp[1][0]=C
        K[dp_prev[1][0] = C] --> L1[new_dp[1][0] += C  (2 to neither)]
        K --> L2[new_dp[gcd(1,2)][0] = new_dp[1][0] += C  (2 to seq1)]
        K --> L3[new_dp[1][gcd(0,2)] = new_dp[1][2] += C  (2 to seq2)]
    end
```

## Dry Run
Let's trace `nums = [10, 20, 30]` (Example 2). `MAX_VAL = 30`, `MOD = 10^9 + 7`.
`dp` table is `31x31`. Only showing relevant non-zero entries.

**Initial**:
`dp[0][0] = 1`

---
**Process `x = 10`**:
`new_dp` is initially `dp`.
- From `dp[0][0] = 1`:
    - `x` to neither: `new_dp[0][0] = (new_dp[0][0] + 1) % MOD = 1`
    - `x` to `seq1`: `new_g1 = gcd(0, 10) = 10`. `new_dp[10][0] = (new_dp[10][0] + 1) % MOD = 1`
    - `x` to `seq2`: `new_g2 = gcd(0, 10) = 10`. `new_dp[0][10] = (new_dp[0][10] + 1) % MOD = 1`
`dp` becomes `new_dp`.
**`dp` after `x=10`**:
`dp[0][0]=1, dp[10][0]=1, dp[0][10]=1`

---
**Process `x = 20`**:
`new_dp` is initially `dp` from previous step.
- From `dp[0][0] = 1`:
    - `x` to neither: `new_dp[0][0] = (new_dp[0][0] + 1) % MOD = 2`
    - `x` to `seq1`: `new_g1 = gcd(0, 20) = 20`. `new_dp[20][0] = (new_dp[20][0] + 1) % MOD = 1`
    - `x` to `seq2`: `new_g2 = gcd(0, 20) = 20`. `new_dp[0][20] = (new_dp[0][20] + 1) % MOD = 1`
- From `dp[10][0] = 1`:
    - `x` to neither: `new_dp[10][0] = (new_dp[10][0] + 1) % MOD = 2`
    - `x` to `seq1`: `new_g1 = gcd(10, 20) = 10`. `new_dp[10][0] = (new_dp[10][0] + 1) % MOD = 3`
    - `x` to `seq2`: `new_g2 = gcd(0, 20) = 20`. `new_dp[10][20] = (new_dp[10][20] + 1) % MOD = 1`
- From `dp[0][10] = 1`:
    - `x` to neither: `new_dp[0][10] = (new_dp[0][10] + 1) % MOD = 2`
    - `x` to `seq1`: `new_g1 = gcd(0, 20) = 20`. `new_dp[20][10] = (new_dp[20][10] + 1) % MOD = 1`
    - `x` to `seq2`: `new_g2 = gcd(10, 20) = 10`. `new_dp[0][10] = (new_dp[0][10] + 1) % MOD = 3`
`dp` becomes `new_dp`.
**`dp` after `x=20`**:
`dp[0][0]=2, dp[10][0]=3, dp[0][10]=3, dp[20][0]=1, dp[0][20]=1, dp[10][20]=1, dp[20][10]=1`

---
**Process `x = 30`**:
`new_dp` is initially `dp` from previous step.
We are interested in `dp[10][10]` for the final sum.
- From `dp[10][20] = 1`: (seq1 has GCD 10, seq2 has GCD 20)
    - `x` to neither: `new_dp[10][20] = (new_dp[10][20] + 1) % MOD = 2`
    - `x` to `seq1`: `new_g1 = gcd(10, 30) = 10`. `new_dp[10][20] = (new_dp[10][20] + 1) % MOD = 3`
    - `x` to `seq2`: `new_g2 = gcd(20, 30) = 10`. `new_dp[10][10] = (new_dp[10][10] + 1) % MOD = 1` (First contribution to `dp[10][10]`)
- From `dp[20][10] = 1`: (seq1 has GCD 20, seq2 has GCD 10)
    - `x` to neither: `new_dp[20][10] = (new_dp[20][10] + 1) % MOD = 2`
    - `x` to `seq1`: `new_g1 = gcd(20, 30) = 10`. `new_dp[10][10] = (new_dp[10][10] + 1) % MOD = 2` (Second contribution to `dp[10][10]`)
    - `x` to `seq2`: `new_g2 = gcd(10, 30) = 10`. `new_dp[20][10] = (new_dp[20][10] + 1) % MOD = 3`
`dp` becomes `new_dp`.

---
**Final Result Calculation**:
`total_pairs = 0`
Iterate `g` from `1` to `30`:
- For `g=10`: `total_pairs = (total_pairs + dp[10][10]) % MOD = (0 + 2) % MOD = 2`.
- All other `dp[g][g]` for `g > 0` will be `0`.

**Final Result: 2**. This matches Example 2.
The two pairs are:
1.  `seq1 = [10]`, `seq2 = [20, 30]`. `gcd(10)=10`, `gcd(20,30)=10`.
2.  `seq1 = [20, 30]`, `seq2 = [10]`. `gcd(20,30)=10`, `gcd(10)=10`.

## Complexity
*   **Time Complexity**: `O(N * MAX_VAL^2 * log(MAX_VAL))`
    *   `N` iterations for `nums` array.
    *   Each iteration involves iterating through `MAX_VAL^2` DP states.
    *   Each state update involves `math.gcd`, which takes `O(log(MAX_VAL))` time.
    *   Given `N=200`, `MAX_VAL=200`, this is approximately `200 * 200^2 * log(200) ≈ 200 * 40000 * 8 ≈ 6.4 * 10^7` operations, which is efficient enough.
*   **Space Complexity**: `O(MAX_VAL^2)`
    *   The `dp` table stores `(MAX_VAL + 1) x (MAX_VAL + 1)` integers.
    *   `201 * 201 ≈ 40000` integers, which is a small memory footprint.

## Edge Cases
*   **`nums` with one element (e.g., `[5]`)**: The final `total_pairs` will be `0`. This is correct because you cannot form two non-empty disjoint subsequences from a single element.
*   **`nums` where no two subsequences can have equal GCD (e.g., `[2, 3, 5]`)**: The final `total_pairs` will be `0`. The DP correctly tracks GCDs and will not find any `dp[g][g]` for `g > 0`.
*   **`nums` with all identical elements (e.g., `[1, 1, 1, 1]`)**: For `N` identical elements, the number of pairs of non-empty disjoint subsequences with equal GCD (which must be the element's value) is `3^N - 2*2^N + 1^N`. For `N=4`, this is `3^4 - 2*2^4 + 1^4 = 81 - 32 + 1 = 50`. The DP correctly calculates this by treating each element at a distinct index.
*   **`nums` where all elements are 1 (e.g., `[1, 2, 3, 4]` from Example 1)**: The problem statement's example explanation is confusing, but the DP correctly computes the result. For `[1,2,3,4]`, the only possible common GCD is 1. The DP will correctly count pairs `(seq1, seq2)` where `gcd(seq1)=1` and `gcd(seq2)=1`.

## Solution

```python
import math
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        MAX_VAL = 200 # Constraint: 1 <= nums[i] <= 200

        # dp[g1][g2] stores the number of ways to form two disjoint subsequences
        # seq1 and seq2 such that gcd(seq1) = g1 and gcd(seq2) = g2.
        # g1=0 means seq1 is empty, g2=0 means seq2 is empty.
        # math.gcd(0, x) correctly returns x, which is useful for initializing GCDs.
        dp = [[0] * (MAX_VAL + 1) for _ in range(MAX_VAL + 1)]

        # Base case: Before processing any number, both subsequences are empty.
        # There is 1 way to have two empty subsequences.
        dp[0][0] = 1

        # Iterate through each number in nums
        for x in nums:
            # Create a new DP table for the current iteration.
            # This ensures that updates are based on the dp state *before* processing x.
            # Initialize new_dp with the current dp values. This implicitly handles
            # the case where 'x' goes to neither subsequence (dp[g1][g2] contributes to new_dp[g1][g2]).
            new_dp = [row[:] for row in dp]

            # Iterate through all possible previous GCD pairs (g1, g2)
            for g1 in range(MAX_VAL + 1):
                for g2 in range(MAX_VAL + 1):
                    if dp[g1][g2] == 0:
                        continue # No ways to reach this state, so no new ways from it

                    count = dp[g1][g2]

                    # Option 1: Add x to subsequence 1
                    # Calculate the new GCD for seq1. math.gcd(0, x) correctly gives x.
                    new_g1 = math.gcd(g1, x)
                    new_dp[new_g1][g2] = (new_dp[new_g1][g2] + count) % MOD

                    # Option 2: Add x to subsequence 2
                    # Calculate the new GCD for seq2.
                    new_g2 = math.gcd(g2, x)
                    new_dp[g1][new_g2] = (new_dp[g1][new_g2] + count) % MOD
            
            # Update the dp table for the next iteration
            dp = new_dp

        total_pairs = 0
        # Sum up dp[g][g] for all g > 0.
        # dp[g][g] for g > 0 implies both subsequences are non-empty and have GCD 'g'.
        # If g=0, it would mean an empty subsequence, which is not allowed by problem statement.
        for g in range(1, MAX_VAL + 1):
            total_pairs = (total_pairs + dp[g][g]) % MOD

        return total_pairs

```

## Why This Works

The dynamic programming approach systematically explores all possible ways to assign each number in `nums` to `seq1`, `seq2`, or neither. By maintaining `dp[g1][g2]` as the count of ways to achieve `gcd(seq1)=g1` and `gcd(seq2)=g2` using elements processed so far, we ensure that:
1.  **Disjointness**: Each element `nums[i]` is considered only once and assigned to at most one subsequence, guaranteeing that `seq1` and `seq2` are disjoint by index.
2.  **GCD Tracking**: `math.gcd(0, x) = x` correctly initializes the GCD of an empty subsequence when its first element is added, and `math.gcd(g, x)` correctly updates the GCD for subsequent elements.
3.  **Non-empty Condition**: By summing `dp[g][g]` only for `g > 0`, we explicitly filter for cases where both `seq1` and `seq2` have a non-zero GCD, which implies they are non-empty.
This comprehensive state management and transition logic correctly counts all valid pairs according to the problem's conditions.

---
<sub>Generated 2026-07-14 03:46 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
