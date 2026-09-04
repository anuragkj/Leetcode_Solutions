# [3903] Smallest Stable Index I

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-09-04 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/smallest-stable-index-i/)

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

- 1 <= nums.length <= 100

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
We are given an array `nums` and an integer `k`. For each index `i`, we calculate an "instability score" by finding the maximum value in the prefix `nums[0..i]` and subtracting the minimum value in the suffix `nums[i..n-1]`. An index `i` is "stable" if its instability score is less than or equal to `k`. The goal is to find the **smallest stable index**. If no such index exists, return -1.

## Intuition
The core of this problem is calculating two values for each index `i`: `max(nums[0..i])` and `min(nums[i..n-1])`. If we were to calculate these from scratch for every `i`, it would involve iterating through subarrays, making the process slow.

However, notice a pattern:
*   `max(nums[0..i])` depends on `max(nums[0..i-1])` and `nums[i]`. This is a **prefix maximum**.
*   `min(nums[i..n-1])` depends on `min(nums[i+1..n-1])` and `nums[i]`. This is a **suffix minimum**.

This observation is key! We can precompute all prefix maximums and all suffix minimums in linear time. Once these are precomputed, calculating the instability score for any index `i` becomes a simple `O(1)` lookup and subtraction.

## Approach
The most efficient approach involves precomputing prefix maximums and suffix minimums, then iterating through the array once to find the smallest stable index.

1.  **Initialize `n`**: Get the length of the `nums` array.
2.  **Precompute Prefix Maximums**:
    *   Create an array `prefix_max` of the same length as `nums`.
    *   `prefix_max[0]` will be `nums[0]`.
    *   For each subsequent index `i` from `1` to `n-1`, `prefix_max[i]` is the maximum of `prefix_max[i-1]` and `nums[i]`. This array stores `max(nums[0..i])` for all `i`.
3.  **Precompute Suffix Minimums**:
    *   Create an array `suffix_min` of the same length as `nums`.
    *   `suffix_min[n-1]` will be `nums[n-1]`.
    *   For each preceding index `i` from `n-2` down to `0`, `suffix_min[i]` is the minimum of `suffix_min[i+1]` and `nums[i]`. This array stores `min(nums[i..n-1])` for all `i`.
4.  **Find Smallest Stable Index**:
    *   Iterate through the array from `i = 0` to `n-1`.
    *   For each `i`, retrieve `current_max = prefix_max[i]` and `current_min = suffix_min[i]`.
    *   Calculate the `instability_score = current_max - current_min`.
    *   If `instability_score <= k`, then `i` is a stable index. Since we are iterating from left to right, the first `i` that satisfies this condition is the **smallest stable index**. Return `i` immediately.
5.  **Handle No Stable Index**: If the loop completes without finding any stable index, it means no such index exists. In this case, return `-1`.

## Visualization
Let's visualize the precomputation and calculation for `nums = [5, 0, 1, 4]`.

```
Original Array (nums):
Index:  0   1   2   3
Value: [5,  0,  1,  4]

1. Prefix Maximums (max from left up to current index):
   prefix_max[0] = nums[0] = 5
   prefix_max[1] = max(prefix_max[0], nums[1]) = max(5, 0) = 5
   prefix_max[2] = max(prefix_max[1], nums[2]) = max(5, 1) = 5
   prefix_max[3] = max(prefix_max[2], nums[3]) = max(5, 4) = 5
   Result: [5,  5,  5,  5]

2. Suffix Minimums (min from current index to right):
   suffix_min[3] = nums[3] = 4
   suffix_min[2] = min(suffix_min[3], nums[2]) = min(4, 1) = 1
   suffix_min[1] = min(suffix_min[2], nums[1]) = min(1, 0) = 0
   suffix_min[0] = min(suffix_min[1], nums[0]) = min(0, 5) = 0
   Result: [0,  0,  1,  4]

3. Calculating Instability Score for each index i (e.g., for i=2):
   nums:        [5, 0, 1, 4]
                 ^-----^       (max(nums[0..2]) is prefix_max[2] = 5)
                    ^----^     (min(nums[2..3]) is suffix_min[2] = 1)

   Instability Score at i=2:
     prefix_max[2] (which is 5)
   - suffix_min[2] (which is 1)
   = 5 - 1 = 4
```

## Dry Run
Let's walk through **Example 1: `nums = [5, 0, 1, 4]`, `k = 3`**

`n = 4`

**Step 1: Precompute Prefix Maximums**
| Index `i` | `nums[i]` | `prefix_max[i-1]` | `max(prefix_max[i-1], nums[i])` | `prefix_max` array |
| :-------- | :-------- | :---------------- | :------------------------------ | :----------------- |
| 0         | 5         | -                 | 5                               | `[5, _, _, _]`     |
| 1         | 0         | 5                 | `max(5, 0) = 5`                 | `[5, 5, _, _]`     |
| 2         | 1         | 5                 | `max(5, 1) = 5`                 | `[5, 5, 5, _]`     |
| 3         | 4         | 5                 | `max(5, 4) = 5`                 | `[5, 5, 5, 5]`     |
**Final `prefix_max`: `[5, 5, 5, 5]`**

**Step 2: Precompute Suffix Minimums**
| Index `i` | `nums[i]` | `suffix_min[i+1]` | `min(suffix_min[i+1], nums[i])` | `suffix_min` array |
| :-------- | :-------- | :---------------- | :------------------------------ | :----------------- |
| 3         | 4         | -                 | 4                               | `[_, _, _, 4]`     |
| 2         | 1         | 4                 | `min(4, 1) = 1`                 | `[_, _, 1, 4]`     |
| 1         | 0         | 1                 | `min(1, 0) = 0`                 | `[_, 0, 1, 4]`     |
| 0         | 5         | 0                 | `min(0, 5) = 0`                 | `[0, 0, 1, 4]`     |
**Final `suffix_min`: `[0, 0, 1, 4]`**

**Step 3: Find Smallest Stable Index**
| Index `i` | `prefix_max[i]` | `suffix_min[i]` | Instability Score (`prefix_max[i] - suffix_min[i]`) | `Score <= k` (k=3)? | Action     |
| :-------- | :-------------- | :-------------- | :--------------------------------------------------- | :------------------ | :--------- |
| 0         | 5               | 0               | `5 - 0 = 5`                                          | `5 <= 3` is False   | Continue   |
| 1         | 5               | 0               | `5 - 0 = 5`                                          | `5 <= 3` is False   | Continue   |
| 2         | 5               | 1               | `5 - 1 = 4`                                          | `4 <= 3` is False   | Continue   |
| 3         | 5               | 4               | `5 - 4 = 1`                                          | `1 <= 3` is True    | Return `3` |

**Final Result: `3`**

## Complexity
*   **Time Complexity**: `O(N)`. We iterate through the array once to compute prefix maximums (`O(N)`), once to compute suffix minimums (`O(N)`), and once more to check stability for each index (`O(N)`). The total time complexity is `O(N) + O(N) + O(N) = O(N)`.
*   **Space Complexity**: `O(N)`. We use two additional arrays, `prefix_max` and `suffix_min`, each of size `N`. Thus, the total space complexity is `O(N)`.

## Edge Cases
*   **`n = 1` (single element array)**:
    *   `nums = [0], k = 0`
    *   `prefix_max = [0]`, `suffix_min = [0]`
    *   At `i=0`: `score = 0 - 0 = 0`. `0 <= 0` is True. Returns `0`. Correct.
*   **No stable index exists**:
    *   `nums = [3, 2, 1], k = 1`
    *   `prefix_max = [3, 3, 3]`, `suffix_min = [1, 1, 1]`
    *   Scores for `i=0,1,2` are all `3-1=2`. `2 <= 1` is always False. The loop completes, and `-1` is returned. Correct.
*   **All elements are the same**:
    *   `nums = [7, 7, 7], k = 0`
    *   `prefix_max = [7, 7, 7]`, `suffix_min = [7, 7, 7]`
    *   At `i=0`: `score = 7 - 7 = 0`. `0 <= 0` is True. Returns `0`. Correct.
*   **Large values for `nums[i]` and `k`**: The solution uses standard integer types in Python, which handle arbitrary precision integers, so overflow is not an issue. The logic remains the same regardless of value magnitude.

## Solution
```python
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Handle edge case for empty array (though constraints say n >= 1)
        if n == 0:
            return -1

        # 1. Precompute Prefix Maximums
        # prefix_max[i] stores max(nums[0...i])
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])

        # 2. Precompute Suffix Minimums
        # suffix_min[i] stores min(nums[i...n-1])
        suffix_min = [0] * n
        suffix_min[n-1] = nums[n-1]
        for i in range(n - 2, -1, -1): # Iterate from n-2 down to 0
            suffix_min[i] = min(suffix_min[i+1], nums[i])

        # 3. Find the smallest stable index
        for i in range(n):
            # Instability score for index i is max(nums[0..i]) - min(nums[i..n-1])
            instability_score = prefix_max[i] - suffix_min[i]
            
            # Check if the current index is stable
            if instability_score <= k:
                return i # Return the smallest stable index found

        # If no stable index is found after checking all indices
        return -1

```

## Why This Works
This approach works because it efficiently calculates the required `max(nums[0..i])` and `min(nums[i..n-1])` for every index `i` using **dynamic programming** principles (specifically, prefix sums/products/min/max patterns). By precomputing these values in `O(N)` time and `O(N)` space, we reduce the calculation for each index `i` to `O(1)`. Since we iterate through indices `i` from `0` to `n-1` and return the first stable index found, we are guaranteed to find the *smallest* such index. If the loop completes, it means no index satisfied the stability condition, correctly resulting in -1.

---
<sub>Generated 2026-09-04 05:00 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
