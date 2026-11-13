# [3420] Count Non-Decreasing Subarrays After K Operations

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-11-13 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/)

**Topics:** Array, Stack, Segment Tree, Queue, Sliding Window, Monotonic Stack, Monotonic Queue

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an array nums of n integers and an integer k.

For each subarray of nums, you can apply up to k operations on it. In each operation, you increment any element of the subarray by 1.

Note that each subarray is considered independently, meaning changes made to one subarray do not persist to another.

Return the number of subarrays that you can make non-decreasing ​​​​​after performing at most k operations.

An array is said to be non-decreasing if each element is greater than or equal to its previous element, if it exists.

Example 1:

Input: nums = [6,3,1,2,4,4], k = 7

Output: 17

Explanation:

Out of all 21 possible subarrays of nums, only the subarrays [6, 3, 1], [6, 3, 1, 2], [6, 3, 1, 2, 4] and [6, 3, 1, 2, 4, 4] cannot be made non-decreasing after applying up to k = 7 operations. Thus, the number of non-decreasing subarrays is 21 - 4 = 17.

Example 2:

Input: nums = [6,3,1,3,6], k = 4

Output: 12

Explanation:

The subarray [3, 1, 3, 6] along with all subarrays of nums with three or fewer elements, except [6, 3, 1], can be made non-decreasing after k operations. There are 5 subarrays of a single element, 4 subarrays of two elements, and 2 subarrays of three elements except [6, 3, 1], so there are 1 + 5 + 4 + 2 = 12 subarrays that can be made non-decreasing.

Constraints:

- 1 <= nums.length <= 10^5

- 1 <= nums[i] <= 10^9

- 1 <= k <= 10^9

**Examples / sample tests:**

```
[6,3,1,2,4,4]
7
[6,3,1,3,6]
4
```

---

## Problem Summary
You are given an array `nums` and an integer `k`. For every possible subarray of `nums`, you can increment its elements at most `k` times in total. The goal is to count how many subarrays can be made non-decreasing using these operations. Each subarray is considered independently.

## Intuition
The core of this problem lies in efficiently calculating the minimum operations needed to make a subarray `nums[L...R]` non-decreasing.
To make `[a_1, a_2, ..., a_m]` non-decreasing with minimum operations, we process elements from left to right.
1. The first element `a_1` doesn't need to be incremented (it has no predecessor). Its value after operations, `a_1'`, is `a_1`.
2. For `a_2`, its value `a_2'` must be at least `a_1'`. To minimize operations, we set `a_2' = max(a_2, a_1')`. The cost for `a_2` is `max(0, a_1' - a_2)`.
3. In general, for `a_i`, its value `a_i'` must be at least `a_{i-1}'`. We set `a_i' = max(a_i, a_{i-1}')`. The cost for `a_i` is `max(0, a_{i-1}' - a_i)`.
The total cost for a subarray is the sum of these individual costs.

Notice that for a fixed left endpoint `L`, as the right endpoint `R` increases, the total cost `cost(nums[L...R])` is non-decreasing. This monotonic property suggests that for each `L`, we can use **binary search** to find the maximum `R` such that `cost(nums[L...R]) <= k`. If we can efficiently calculate `cost(nums[L...R])`, we can sum up `(max_R_for_L - L + 1)` for all `L` to get the total count.

Calculating `cost(nums[L...R])` naively takes `O(R-L+1)` time. With `N` choices for `L`, `N` for `R`, and `log N` for binary search, this would be `O(N^2 log N)`, too slow for `N=10^5`. We need a faster way to query subarray costs. This is where a **sparse table** comes in.

## Approach
The optimal approach involves two main steps:
1.  **Precompute a Sparse Table:** Build a 2D array `dp[e][i]` that stores information about subarrays of length `2^e` starting at index `i`. Specifically, `dp[e][i]` will store a tuple `(last_val_after_ops, total_ops)`.
    *   `last_val_after_ops`: The value of the last element (`nums[i + 2^e - 1]`) after operations, assuming `nums[i]` was the first element of its segment and not forced by a preceding element.
    *   `total_ops`: The minimum operations needed to make `nums[i ... i + 2^e - 1]` non-decreasing, again assuming `nums[i]` is the first element.

    **Building `dp`:**
    *   **Base Case (`e=0`):** For subarrays of length `2^0 = 1`, `dp[0][i] = (nums[i], 0)`. A single element needs 0 operations and its value remains `nums[i]`.
    *   **Recursive Step (`e > 0`):** To compute `dp[e][i]`, we combine two segments of length `2^(e-1)`:
        *   Left segment: `nums[i ... i + 2^(e-1) - 1]`, with info `(last1, ops1) = dp[e-1][i]`.
        *   Right segment: `nums[i + 2^(e-1) ... i + 2^e - 1]`, with info `(last2_orig, ops2_orig) = dp[e-1][i + 2^(e-1)]`.
        The first element of the right segment (`nums[i + 2^(e-1)]`) must be at least `last1`.
        Let `val_at_right_segment_start_orig = nums[i + 2^(e-1)]`.
        The `delta` operations needed for this element is `max(0, last1 - val_at_right_segment_start_orig)`.
        This `delta` increases the value of `nums[i + 2^(e-1)]` by `delta`, which in turn increases all subsequent elements in the right segment by `delta` to maintain the non-decreasing property.
        So, the combined `total_ops` is `ops1 + ops2_orig + delta`.
        The combined `last_val_after_ops` is `last2_orig + delta`.
        Thus, `dp[e][i] = (last2_orig + delta, ops1 + ops2_orig + delta)`.
    This precomputation takes `O(N log N)` time and space.

2.  **Iterate `L` and Binary Search for `R` using `query_cost`:**
    *   Initialize `total_non_decreasing_subarrays = 0`.
    *   For each `L` from `0` to `N-1`:
        *   Perform a binary search for `R` in the range `[L, N-1]`. The goal is to find the largest `R` such that `query_cost(L, R) <= k`.
        *   The `query_cost(L, R)` function uses the sparse table to calculate the total operations for `nums[L...R]` in `O(log N)` time. It does this by decomposing the range `[L, R]` into `O(log N)` segments of lengths `2^e` (e.g., `[L, L+2^e1-1]`, then `[L+2^e1, L+2^e1+2^e2-1]`, etc.). For each segment, it applies the same `delta` logic as in the sparse table construction, accumulating costs and updating the `current_val_after_ops` for the next segment.
        *   Once `max_R_for_L` is found, all subarrays `nums[L...j]` for `L <= j <= max_R_for_L` are valid. Add `(max_R_for_L - L + 1)` to `total_non_decreasing_subarrays`.
    This step takes `O(N * log N * log N) = O(N log^2 N)` time.

The overall time complexity is `O(N log^2 N)` and space complexity is `O(N log N)`.

## Visualization

Let's visualize the `query_cost(L, R)` function for `nums = [6,3,1,2,4,4]`, `k=7`, and `L=1, R=5` (subarray `[3,1,2,4,4]`).

```
nums: [6, 3, 1, 2, 4, 4]
Indices: 0  1  2  3  4  5

Query cost for nums[1...5] (subarray [3,1,2,4,4])

Initial state:
  current_val_after_ops = nums[1] = 3
  total_cost = 0
  current_pos = 1

Iteration 1:
  current_pos = 1, R = 5
  remaining_len = 5 - 1 + 1 = 5
  Largest e s.t. 2^e <= 5 is e=2 (2^2=4).
  Segment: nums[1...1+4-1] = nums[1...4] (i.e., [3,1,2,4])
  
  Retrieve from sparse table: dp[2][1] = (5, 3)
    (last_val_for_segment_if_first_is_original = 5, cost_for_segment_if_first_is_original = 3)
  
  Original value at segment start: nums[1] = 3
  Delta needed at segment start: max(0, current_val_after_ops - nums[1]) = max(0, 3 - 3) = 0
  
  Update:
    total_cost += (3 + 0) = 3
    current_val_after_ops = (5 + 0) = 5
    current_pos += 4 = 5

Iteration 2:
  current_pos = 5, R = 5
  remaining_len = 5 - 5 + 1 = 1
  Largest e s.t. 2^e <= 1 is e=0 (2^0=1).
  Segment: nums[5...5+1-1] = nums[5...5] (i.e., [4])
  
  Retrieve from sparse table: dp[0][5] = (4, 0)
    (last_val_for_segment_if_first_is_original = 4, cost_for_segment_if_first_is_original = 0)
  
  Original value at segment start: nums[5] = 4
  Delta needed at segment start: max(0, current_val_after_ops - nums[5]) = max(0, 5 - 4) = 1
  
  Update:
    total_cost += (0 + 1) = 4
    current_val_after_ops = (4 + 1) = 5
    current_pos += 1 = 6

Loop ends (current_pos = 6 > R = 5).

Final total_cost = 4.
```

## Dry Run
Let's walk through **Example 1:** `nums = [6,3,1,2,4,4]`, `k = 7`. `N = 6`.

**1. Sparse Table `dp` Construction (partial):**
`MAX_E = floor(log2(6)) = 2`.
`

---
<sub>Generated 2026-11-13 07:08 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
