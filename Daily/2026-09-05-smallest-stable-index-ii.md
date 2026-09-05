# [3904] Smallest Stable Index II

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-09-05 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/smallest-stable-index-ii/)

**Topics:** Array, Prefix Sum

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums of length n and an integer k.

For each index i, define its instability score as max(nums[0..i]) - min(nums[i..n - 1]).

In other words:

- max(nums[0..i]) is the largest value among the elements from index 0 to index i.

- min(nums[i..n - 1]) is the smallest value among the elements from index i to index n - 1.

An index i is called stable if its instability score is less than or equal to k.

Return the smallest stable index. If no such index exists, return -1.

Example 1:

Input: nums = [5,0,1,4], k = 3

Output: 3

Explanation:

- At index 0: The maximum in [5] is 5, and the minimum in [5, 0, 1, 4] is 0, so the instability score is 5 - 0 = 5.

- At index 1: The maximum in [5, 0] is 5, and the minimum in [0, 1, 4] is 0, so the instability score is 5 - 0 = 5.

- At index 2: The maximum in [5, 0, 1] is 5, and the minimum in [1, 4] is 1, so the instability score is 5 - 1 = 4.

- At index 3: The maximum in [5, 0, 1, 4] is 5, and the minimum in [4] is 4, so the instability score is 5 - 4 = 1.

- This is the first index with an instability score less than or equal to k = 3. Thus, the answer is 3.

Example 2:

Input: nums = [3,2,1], k = 1

Output: -1

Explanation:

- At index 0, the instability score is 3 - 1 = 2.

- At index 1, the instability score is 3 - 1 = 2.

- At index 2, the instability score is 3 - 1 = 2.

- None of these values is less than or equal to k = 1, so the answer is -1.

Example 3:

Input: nums = [0], k = 0

Output: 0

Explanation:

At index 0, the instability score is 0 - 0 = 0, which is less than or equal to k = 0. Therefore, the answer is 0.

Constraints:

- 1 <= nums.length <= 10^5

- 0 <= nums[i] <= 10^9

- 0 <= k <= 10^9

**Examples / sample tests:**

```
[5,0,1,4]
3
[3,2,1]
1
[0]
0
```

---

## Problem Summary
We are given an array `nums` and an integer `k`. For each index `i`, we calculate an **instability score** as the maximum value in `nums` from index `0` to `i`, minus the minimum value in `nums` from index `i` to `n-1`. An index `i` is **stable** if its instability score is less than or equal to `k`. Our goal is to find and return the **smallest stable index**. If no such index exists, we return -1.

## Intuition
The core of this problem is calculating `max(nums[0..i])` and `min(nums[i..n-1])` for every possible index `i`.

A straightforward approach would be to iterate through each index `i` from `0` to `n-1`. For each `i`, we would then iterate from `0` to `i` to find the maximum, and from `i` to `n-1` to find the minimum. This would take `O(i)` time for the maximum and `O(n-i)` time for the minimum, resulting in an `O(N)` calculation for each `i`. Since there are `N` indices, the total time complexity would be `O(N^2)`. Given `N` can be up to `10^5`, `N^2` (`10^10`) is too slow and would lead to a Time Limit Exceeded (TLE) error.

We need a faster way to get these range maximums and minimums. Notice a pattern:
*   `max(nums[0..i])` depends on `max(nums[0..i-1])` and `nums[i]`. Specifically, `max(nums[0..i]) = max(max(nums[0..i-1]), nums[i])`. This is a **prefix maximum** pattern. We can compute all prefix maximums in a single pass from left to right.
*   `min(nums[i..n-1])` depends on `min(nums[i+1..n-1])` and `nums[i]`. Specifically, `min(nums[i..n-1]) = min(nums[i], min(nums[i+1..n-1]))`. This is a **suffix minimum** pattern. We can compute all suffix minimums in a single pass from right to left.

By precomputing these two arrays, `prefMax` and `suffMin`, we can find `max(nums[0..i])` and `min(nums[i..n-1])` in `O(1)` time for any `i`. This transforms the `O(N^2)` problem into an `O(N)` problem, which is efficient enough for the given constraints.

## Approach
The optimal algorithm involves three main steps: precomputing prefix maximums, precomputing suffix minimums, and then iterating to find the first stable index.

1.  **Initialize `n`**: Get the length of the input array `nums`.
2.  **Precompute Prefix Maximums**:
    *   Create an array `prefMax` of size `n`.
    *   `prefMax[i]` will store the maximum value in the subarray `nums[0...i]`.
    *   Initialize `prefMax[0] = nums[0]`.
    *   For `i` from `1` to `n-1`: `prefMax[i] = max(prefMax[i-1], nums[i])`.
3.  **Precompute Suffix Minimums**:
    *   Create an array `suffMin` of size `n`.
    *   `suffMin[i]` will store the minimum value in the subarray `nums[i...n-1]`.
    *   Initialize `suffMin[n-1] = nums[n-1]`.
    *   For `i` from `n-2` down to `0`: `suffMin[i] = min(suffMin[i+1], nums[i])`.
4.  **Find Smallest Stable Index**:
    *   Iterate `i` from `0` to `n-1`.
    *   For each `i`, calculate the `instability_score = prefMax[i] - suffMin[i]`.
    *   If `instability_score <= k`, then `i` is a stable index. Since we are iterating from the smallest `i` upwards, this `i` is the **smallest stable index**. Return `i` immediately.
5.  **Handle No Stable Index**: If the loop completes without finding any stable index (i.e., no `instability_score <= k` was found), return `-1`.

## Visualization

Let's visualize the process with `nums = [5, 0, 1, 4]` and `k = 3`.

```
nums:      [ 5,   0,   1,   4 ]
Indices:     0    1    2    3

1. Precompute Prefix Maximums (prefMax):
   prefMax[0] = nums[0] = 5
   prefMax[1] = max(prefMax[0], nums[1]) = max(5, 0) = 5
   prefMax[2] = max(prefMax[1], nums[2]) = max(5, 1) = 5
   prefMax[3] = max(prefMax[2], nums[3]) = max(5, 4) = 5
   prefMax:   [ 5,   5,   5,   5 ]

2. Precompute Suffix Minimums (suffMin):
   suffMin[3] = nums[3] = 4
   suffMin[2] = min(suffMin[3], nums[2]) = min(4, 1) = 1
   suffMin[1] = min(suffMin[2], nums[1]) = min(1, 0) = 0
   suffMin[0] = min(suffMin[1], nums[0]) = min(0, 5) = 0
   suffMin:   [ 0,   0,   1,   4 ]

3. Calculate Instability Scores and Find Smallest Stable Index:

   For index i = 0:
     max(nums[0..0]) = prefMax[0] = 5
     min(nums[0..3]) = suffMin[0] = 0
     Score = 5 - 0 = 5. Is 5 <= k (3)? No.

   For index i = 1:
     max(nums[0..1]) = prefMax[1] = 5
     min(nums[1..3]) = suffMin[1] = 0
     Score = 5 - 0 = 5. Is 5 <= k (3)? No.

   For index i = 2:
     max(nums[0..2]) = prefMax[2] = 5
     min(nums[2..3]) = suffMin[2] = 1
     Score = 5 - 1 = 4. Is 4 <= k (3)? No.

   For index i = 3:
     max(nums[0..3]) = prefMax[3] = 5
     min(nums[3..3]) = suffMin[3] = 4
     Score = 5 - 4 = 1. Is 1 <= k (3)? Yes!

   Return 3.
```

## Dry Run
Let's walk through Example 1: `nums = [5,0,1,4], k = 3`.

1.  **Initialization**:
    *   `n = 4`

2.  **Precompute `prefMax`**:
    *   `prefMax = [0, 0, 0, 0]` (initial placeholder)
    *   `prefMax[0] = nums[0] = 5`
    *   `i = 1`: `prefMax[1] = max(prefMax[0], nums[1]) = max(5, 0) = 5`
    *   `i = 2`: `prefMax[2] = max(prefMax[1], nums[2]) = max(5, 1) = 5`
    *   `i = 3`: `prefMax[3] = max(prefMax[2], nums[3]) = max(5, 4) = 5`
    *   Result: `prefMax = [5, 5, 5, 5]`

3.  **Precompute `suffMin`**:
    *   `suffMin = [0, 0, 0, 0]` (initial placeholder)
    *   `suffMin[3] = nums[3] = 4`
    *   `i = 2`: `suffMin[2] = min(suffMin[3], nums[2]) = min(4, 1) = 1`
    *   `i = 1`: `suffMin[1] = min(suffMin[2], nums[1]) = min(1, 0) = 0`
    *   `i = 0`: `suffMin[0] = min(suffMin[1], nums[0]) = min(0, 5) = 0`
    *   Result: `suffMin = [0, 0, 1, 4]`

4.  **Find Smallest Stable Index**:
    `k = 3`

| `i` | `prefMax[i]` | `suffMin[i]` | `instability_score = prefMax[i] - suffMin[i]` | `instability_score <= k`? | Result |
| :-- | :----------- | :----------- | :-------------------------------------------- | :------------------------ | :----- |
| 0   | 5            | 0            | `5 - 0 = 5`                                   | `5 <= 3` is False         |        |
| 1   | 5            | 0            | `5 - 0 = 5`                                   | `5 <= 3` is False         |        |
| 2   | 5            | 1            | `5 - 1 = 4`                                   | `4 <= 3` is False         |        |
| 3   | 5            | 4            | `5 - 4 = 1`                                   | `1 <= 3` is True          | Return 3 |

The final result is `3`.

## Complexity
*   **Time Complexity**: `O(N)`. We iterate through the array once to compute `prefMax` (O(N)), once to compute `suffMin` (O(N)), and once more to check instability scores (O(N)). The total time complexity is dominated by these three linear passes, resulting in O(N).
*   **Space Complexity**: `O(N)`. We use two additional arrays, `prefMax` and `suffMin`, each of size `N`, to store the precomputed values. This results in O(N) auxiliary space.

## Edge Cases
*   **`nums.length = 1`**:
    *   `nums = [0], k = 0`
    *   `prefMax = [0]`, `suffMin = [0]`
    *   At `i=0`: `score = prefMax[0] - suffMin[0] = 0 - 0 = 0`. `0 <= 0` is true. Returns `0`. Correct.
*   **No stable index exists**:
    *   `nums = [3,2,1], k = 1`
    *   `prefMax = [3,3,3]`, `suffMin = [1,1,1]`
    *   All scores are `3 - 1 = 2`. Since `2 <= 1` is always false, the loop finishes, and `-1` is returned. Correct.
*   **All indices are stable**:
    *   `nums = [1,2,3], k = 10`
    *   `prefMax = [1,2,3]`, `suffMin = [1,2,3]`
    *   At `i=0`: `score = 1 - 1 = 0`. `0 <= 10` is true. Returns `0`. Correct (smallest stable index).
*   **Large values in `nums` or `k`**: Python's arbitrary-precision integers handle large numbers automatically, so `max - min` calculations will not overflow. The logic remains sound.

## Solution

```python
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Step 1: Precompute prefix maximums
        # prefMax[i] stores the maximum value in nums[0...i]
        prefMax = [0] * n
        prefMax[0] = nums[0]
        for i in range(1, n):
            prefMax[i] = max(prefMax[i-1], nums[i])

        # Step 2: Precompute suffix minimums
        # suffMin[i] stores the minimum value in nums[i...n-1]
        suffMin = [0] * n
        suffMin[n-1] = nums[n-1]
        for i in range(n - 2, -1, -1): # Iterate from n-2 down to 0
            suffMin[i] = min(suffMin[i+1], nums[i])

        # Step 3: Iterate through indices and check instability score
        for i in range(n):
            # The instability score for index i is max(nums[0...i]) - min(nums[i...n-1])
            # Using our precomputed arrays, this is simply prefMax[i] - suffMin[i]
            instability_score = prefMax[i] - suffMin[i]

            # If the score is less than or equal to k, this is a stable index.
            # Since we iterate from left to right (smallest i to largest i),
            # the first one we find is guaranteed to be the smallest stable index.
            if instability_score <= k:
                return i
        
        # If the loop completes without finding any stable index, return -1.
        return -1

```

## Why This Works
This approach works by efficiently breaking down the problem into manageable parts. By precomputing the `prefMax` and `suffMin` arrays, we transform the `O(N)` calculation of range maximums and minimums for each index `i` into an `O(1)` lookup. This allows us to calculate the instability score for all `N` indices in `O(N)` time after the initial `O(N)` precomputation. Since we iterate through indices `i` from `0` to `n-1`, the first `i` for which `instability_score <= k` is guaranteed to be the smallest such index, fulfilling the problem's requirement. If no such index is found after checking all possibilities, returning -1 is correct.

---
<sub>Generated 2026-09-05 04:52 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
