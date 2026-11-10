# [3693] Climbing Stairs II

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-11-10 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/climbing-stairs-ii/)

**Topics:** Array, Dynamic Programming

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are climbing a staircase with n + 1 steps, numbered from 0 to n.

You are also given a 1-indexed integer array costs of length n, where costs[i] is the cost of step i.

From step i, you can jump only to step i + 1, i + 2, or i + 3. The cost of jumping from step i to step j is defined as: costs[j] + (j - i)^2

You start from step 0 with cost = 0.

Return the minimum total cost to reach step n.

Example 1:

Input: n = 4, costs = [1,2,3,4]

Output: 13

Explanation:

One optimal path is 0 → 1 → 2 → 4

			Jump
			Cost Calculation
			Cost

			0 → 1
			costs[1] + (1 - 0)^2 = 1 + 1
			2

			1 → 2
			costs[2] + (2 - 1)^2 = 2 + 1
			3

			2 → 4
			costs[4] + (4 - 2)^2 = 4 + 4
			8

Thus, the minimum total cost is 2 + 3 + 8 = 13

Example 2:

Input: n = 4, costs = [5,1,6,2]

Output: 11

Explanation:

One optimal path is 0 → 2 → 4

			Jump
			Cost Calculation
			Cost

			0 → 2
			costs[2] + (2 - 0)^2 = 1 + 4
			5

			2 → 4
			costs[4] + (4 - 2)^2 = 2 + 4
			6

Thus, the minimum total cost is 5 + 6 = 11

Example 3:

Input: n = 3, costs = [9,8,3]

Output: 12

Explanation:

The optimal path is 0 → 3 with total cost = costs[3] + (3 - 0)^2 = 3 + 9 = 12

Constraints:

- 1 <= n == costs.length <= 10^5​​​​​​​

- 1 <= costs[i] <= 10^4

**Examples / sample tests:**

```
4
[1,2,3,4]
4
[5,1,6,2]
3
[9,8,3]
```

---

## Problem Summary
You are climbing a staircase from step 0 to step `n`. You start at step 0 with an initial cost of 0. You are given a `costs` array where `costs[i]` is the cost associated with step `i`. From any step `i`, you can jump to step `i+1`, `i+2`, or `i+3`. The cost of a jump from step `i` to step `j` is calculated as `costs[j] + (j - i)^2`. Your task is to find the **minimum total cost** to reach step `n`.

## Intuition
The problem asks for the **minimum cost** to reach a specific destination (step `n`) by making a sequence of choices (jumps). This is a classic scenario for **Dynamic Programming (DP)**. The key insight is that the minimum cost to reach any given step `j` must depend on the minimum costs to reach the steps from which you could have jumped to `j`. Since you can only jump from `j-1`, `j-2`, or `j-3` to reach `j`, the minimum cost to reach `j` can be found by taking the minimum of the costs from these three preceding steps, plus the cost of the jump itself.

## Approach
We will use dynamic programming to solve this problem.

1.  **Define DP State**: Let `dp[i]` represent the **minimum total cost to reach step `i`**.
2.  **Initialize DP Array**:
    *   Create a `dp` array of size `n + 1` (to store costs for steps 0 through `n`).
    *   Set `dp[0] = 0`, as we start at step 0 with no initial cost.
    *   Initialize all other `dp[i]` values to `float('inf')` to signify that these steps are not yet reachable or have an unknown, very high cost.
3.  **Handle `costs` Array Indexing**: The problem states `costs` is a 1-indexed array where `costs[i]` is the cost of step `i`. In Python, lists are 0-indexed. Therefore, `costs[j]` (the cost of step `j` in the problem statement) will correspond to `costs[j-1]` in the Python list.
4.  **Iterate and Fill DP Array**:
    *   Loop from `j = 1` to `n` (inclusive). For each `j`, we want to calculate `dp[j]`.
    *   Inside the loop, we consider the three possible previous steps `i` from which we could have jumped to `j`: `j-1`, `j-2`, and `j-3`.
    *   For each valid previous step `i` (i.e., `i >= 0`):
        *   Calculate the cost of jumping from `i` to `j`: `dp[i] + costs[j-1] + (j - i)^2`.
            *   `dp[i]` is the minimum cost to reach step `i`.
            *   `costs[j-1]` is the cost of landing on step `j` (using 0-indexed Python list).
            *   `(j - i)^2` is the "effort" cost of the jump.
        *   Update `dp[j]` with the minimum cost found so far: `dp[j] = min(dp[j], calculated_jump_cost)`.
5.  **Return Result**: After the loop completes, `dp[n]` will hold the minimum total cost to reach step `n`.

## Visualization

Let's visualize the `dp` table and dependencies for `n=4`.
`costs` refers to the 0-indexed Python list `costs`.

```
Steps:     0      1      2      3      4
dp:      [0,    inf,   inf,   inf,   inf]  (Initial state)

costs:     -    costs[0] costs[1] costs[2] costs[3]
           -      (c1)     (c2)     (c3)     (c4)

Calculating dp[j]:
----------------------------------------------------------------------------------------------------------------------------------------------------
j = 1: (cost_of_step_1 = costs[0])
   From step 0: dp[0] + costs[0] + (1-0)^2  = 0 + c1 + 1^2
   dp[1] = min(cost from 0)
dp:      [0,    dp[1], inf,   inf,   inf]

j = 2: (cost_of_step_2 = costs[1])
   From step 1: dp[1] + costs[1] + (2-1)^2  = dp[1] + c2 + 1^2
   From step 0: dp[0] + costs[1] + (2-0)^2  = 0 + c2 + 2^2
   dp[2] = min(cost from 1, cost from 0)
dp:      [0,    dp[1], dp[2], inf,   inf]

j = 3: (cost_of_step_3 = costs[2])
   From step 2: dp[2] + costs[2] + (3-2)^2  = dp[2] + c3 + 1^2
   From step 1: dp[1] + costs[2] + (3-1)^2  = dp[1] + c3 + 2^2
   From step 0: dp[0] + costs[2] + (3-0)^2  = 0 + c3 + 3^2
   dp[3] = min(cost from 2, cost from 1, cost from 0)
dp:      [0,    dp[1], dp[2], dp[3], inf]

j = 4: (cost_of_step_4 = costs[3])
   From step 3: dp[3] + costs[3] + (4-3)^2  = dp[3] + c4 + 1^2
   From step 2: dp[2] + costs[3] + (4-2)^2  = dp[2] + c4 + 2^2
   From step 1: dp[1] + costs[3] + (4-1)^2  = dp[1] + c4 + 3^2
   dp[4] = min(cost from 3, cost from 2, cost from 1)
dp:      [0,    dp[1], dp[2], dp[3], dp[4]]
```

## Dry Run
Let's trace Example 1: `n = 4`, `costs = [1,2,3,4]`

`costs` (the 0-indexed Python list) is `[1, 2, 3, 4]`.
`dp` array of size `n+1 = 5`. Initialize `dp = [0, float('inf'), float('inf'), float('inf'), float('inf')]`.

| Step `j` | `costs[j-1]` (cost of step `j`) | Possible previous steps `i` | Cost from `i` to `j` (`dp[i] + costs[j-1] + (j-i)^2`) | `dp[j]` (min cost to reach step `j`) | `dp` array state |
| :------- | :--------------------------------- | :-------------------------- | :------------------------------------------------------- | :----------------------------------- | :------------------------------------------------------- |
| Initial  | -                                  | -                           | -                                                        | -                                    | `[0, inf, inf, inf, inf]`                                |
| `j = 1`  | `costs[0] = 1`                     | `i = 0`                     | `dp[0] + 1 + (1-0)^2 = 0 + 1 + 1 = 2`                    | `2`                                  | `[0, 2, inf, inf, inf]`                                  |
| `j = 2`  | `costs[1] = 2`                     | `i = 1`                     | `dp[1] + 2 + (2-1)^2 = 2 + 2 + 1 = 5`                    | `min(5, 6) = 5`                      | `[0, 2, 5, inf, inf]`                                    |
|          |                                    | `i = 0`                     | `dp[0] + 2 + (2-0)^2 = 0 + 2 + 4 = 6`                    |                                      |                                                          |
| `j = 3`  | `costs[2] = 3`                     | `i = 2`                     | `dp[2] + 3 + (3-2)^2 = 5 + 3 + 1 = 9`                    | `min(9, 9, 12) = 9`                  | `[0, 2, 5, 9, inf]`                                      |
|          |                                    | `i = 1`                     | `dp[1] + 3 + (3-1)^2 = 2 + 3 + 4 = 9`                    |                                      |                                                          |
|          |                                    | `i = 0`                     | `dp[0] + 3 + (3-0)^2 = 0 + 3 + 9 = 12`                   |                                      |                                                          |
| `j = 4`  | `costs[3] = 4`                     | `i = 3`                     | `dp[3] + 4 + (4-3)^2 = 9 + 4 + 1 = 14`                   | `min(14, 13, 15) = 13`               | `[0, 2, 5, 9, 13]`                                       |
|          |                                    | `i = 2`                     | `dp[2] + 4 + (4-2)^2 = 5 + 4 + 4 = 13`                   |                                      |                                                          |
|          |                                    | `i = 1`                     | `dp[1] + 4 + (4-1)^2 = 2 + 4 + 9 = 15`                   |                                      |                                                          |

The final result is `dp[4] = 13`. This matches Example 1.

## Complexity
*   **Time Complexity**: `O(N)`. We iterate through the `dp` array from `j = 1` to `n`. For each `j`, we perform a constant number of operations (checking up to 3 previous `dp` values and calculating jump costs). Thus, the total time complexity is linear with respect to `n`.
*   **Space Complexity**: `O(N)`. We use a `dp` array of size `n + 1` to store the minimum costs to reach each step.

## Edge Cases
*   **`n = 1`**: The smallest possible `n`. The solution correctly calculates `dp[1]` based only on a jump from step 0. `dp[1] = dp[0] + costs[0] + (1-0)^2 = 0 + costs[0] + 1`. This is correct as the only path is `0 -> 1`.
*   **`n = 2`**: The solution correctly considers jumps from `0` and `1` to reach `2`. `dp[2] = min(dp[1] + costs[1] + (2-1)^2, dp[0] + costs[1] + (2-0)^2)`. This correctly evaluates the two possible paths to step 2.
*   **Large `n` and `costs`**: `n` can be up to `10^5`, and `costs[i]` up to `10^4`. The maximum possible total cost can be large (e.g., `10^5 * (10^4 + 3^2) ≈ 10^9`). Python's arbitrary-precision integers handle such large values without overflow, so the solution remains correct.

## Solution

```python
import math
from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # dp[i] will store the minimum cost to reach step i.
        # The staircase has n+1 steps, numbered 0 to n.
        # So, dp array needs to be of size n+1.
        dp = [float('inf')] * (n + 1)

        # Base case: Starting at step 0 has 0 cost.
        dp[0] = 0

        # Iterate from step 1 up to step n to fill the dp array.
        for j in range(1, n + 1):
            # The problem states 'costs' is 1-indexed, meaning costs[i] is for step i.
            # In Python, lists are 0-indexed, so costs[j] (problem statement)
            # corresponds to costs[j-1] (Python list).
            cost_of_step_j = costs[j-1]

            # Consider jumping from step j-1 (distance = 1)
            # Ensure j-1 is a valid step (>= 0)
            if j - 1 >= 0:
                # Cost = min_cost_to_prev_step + cost_of_current_step + (distance^2)
                dp[j] = min(dp[j], dp[j-1] + cost_of_step_j + (1 * 1))

            # Consider jumping from step j-2 (distance = 2)
            # Ensure j-2 is a valid step (>= 0)
            if j - 2 >= 0:
                dp[j] = min(dp[j], dp[j-2] + cost_of_step_j + (2 * 2))

            # Consider jumping from step j-3 (distance = 3)
            # Ensure j-3 is a valid step (>= 0)
            if j - 3 >= 0:
                dp[j] = min(dp[j], dp[j-3] + cost_of_step_j + (3 * 3))
        
        # The minimum cost to reach step n is dp[n].
        return dp[n]

```

## Why This Works
This dynamic programming approach works because it adheres to the principles of **optimal substructure** and **overlapping subproblems**. The problem exhibits optimal substructure because the optimal (minimum cost) path to reach step `n` must necessarily involve an optimal path to one of the preceding steps (`n-1`, `n-2`, or `n-3`). It has overlapping subproblems because the minimum cost to reach a particular step (e.g., step 2) might be needed to calculate the minimum cost for multiple subsequent steps (e.g., step 3, step 4, step 5). By building up the `dp` array iteratively from step 0 to `n`, we ensure that when we calculate `dp[j]`, the minimum costs for all necessary previous steps (`dp[j-1]`, `dp[j-2]`, `dp[j-3]`) have already been correctly computed. This guarantees that `dp[n]` will hold the overall minimum total cost to reach the final step.

---
<sub>Generated 2026-11-10 07:40 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
