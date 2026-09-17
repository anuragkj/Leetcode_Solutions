# [1477] Find Two Non-overlapping Sub-arrays Each With Target Sum

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-09-17 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/)

**Topics:** Array, Hash Table, Binary Search, Dynamic Programming, Sliding Window

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.

Example 2:

Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.

Example 3:

Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.

Constraints:

- 1 <= arr.length <= 10^5

- 1 <= arr[i] <= 1000

- 1 <= target <= 10^8

**Examples / sample tests:**

```
[3,2,2,4,3]
3
[7,3,4,7]
7
[4,3,2,6,2,3,4]
6
```

---

## Problem Summary
You are given an array of positive integers `arr` and a `target` sum. The goal is to find two sub-arrays within `arr` that are **non-overlapping**, each sum up to `target`, and whose combined lengths are as small as possible. If no such pair of sub-arrays exists, return -1.

## Intuition
The problem asks us to find two sub-arrays. The "non-overlapping" constraint is crucial. If we find a sub-array `A` ending at index `i` and another sub-array `B` starting at index `j`, they are non-overlapping if `i < j`. This suggests a strategy where we consider all possible "split points" in the array. For each split point, we find the shortest valid sub-array to its left and the shortest valid sub-array to its right, then sum their lengths.

To efficiently find the shortest sub-arrays:
1.  We can pre-compute, for each index `i`, the **minimum length** of a sub-array with sum `target` that **ends at or before `i`**. Let's call this `dp_left[i]`.
2.  Similarly, we can pre-compute, for each index `i`, the **minimum length** of a sub-array with sum `target` that **starts at or after `i`**. Let's call this `dp_right[i]`.

Once we have these two arrays, we can iterate through all possible split points. If the first sub-array ends at index `i` and the second starts at index `i+1`, then we can combine `dp_left[i]` and `dp_right[i+1]` to get a candidate total length. We take the minimum of all such combinations.

## Approach
The optimal approach involves three main steps:
1.  **Compute `dp_left` array:** Iterate through the array from left to right using a **sliding window** technique.
    *   Maintain a `current_sum` and a `left` pointer for the window `arr[left...right]`.
    *   As the `right` pointer moves, add `arr[right]` to `current_sum`.
    *   If `current_sum` exceeds `target`, shrink the window from the `left` by subtracting `arr[left]` and incrementing `left` until `current_sum` is no longer greater than `target`.
    *   If `current_sum` equals `target`, we've found a valid sub-array `arr[left...right]`. Calculate its length (`right - left + 1`).
    *   `dp_left[right]` will store the minimum length found **so far** (from `arr[0...right]`) that sums to `target`. This means `dp_left[right]` is the minimum of `dp_left[right-1]` and the length of any `target`-sum sub-array ending at `right`. Initialize `dp_left` with `infinity`.

2.  **Compute `dp_right` array:** Iterate through the array from right to left, again using a **sliding window**.
    *   Maintain a `current_sum` and a `right_boundary` pointer for the window `arr[left_ptr...right_boundary]`.
    *   As the `left_ptr` moves from right to left, add `arr[left_ptr]` to `current_sum`.
    *   If `current_sum` exceeds `target`, shrink the window from the `right_boundary` by subtracting `arr[right_boundary]` and decrementing `right_boundary` until `current_sum` is no longer greater than `target`.
    *   If `current_sum` equals `target`, we've found a valid sub-array `arr[left_ptr...right_boundary]`. Calculate its length (`right_boundary - left_ptr + 1`).
    *   `dp_right[left_ptr]` will store the minimum length found **so far** (from `arr[left_ptr...n-1]`) that sums to `target`. This means `dp_right[left_ptr]` is the minimum of `dp_right[left_ptr+1]` and the length of any `target`-sum sub-array starting at `left_ptr`. Initialize `dp_right` with `infinity`.

3.  **Combine `dp_left` and `dp_right`:** Iterate from `i = 0` to `n-2` (where `n` is the length of `arr`).
    *   For each `i`, consider `dp_left[i]` (shortest sub-array ending at or before `i`) and `dp_right[i+1]` (shortest sub-array starting at or after `i+1`).
    *   If both `dp_left[i]` and `dp_right[i+1]` are not `infinity` (meaning valid sub-arrays were found), update the overall minimum total length with `dp_left[i] + dp_right[i+1]`.
    *   Initialize the overall minimum total length with `infinity`.
    *   If the overall minimum total length remains `infinity` after checking all `i`, return -1; otherwise, return the minimum found.

## Visualization

```mermaid
graph TD
    subgraph Array
        A[arr[0]] --- B[arr[1]] --- C[arr[2]] --- D[arr[3]] --- E[arr[4]] --- F[arr[5]] --- G[arr[6]]
    end

    subgraph dp_left Calculation (Left to Right)
        L0(dp_left[0]) --- L1(dp_left[1]) --- L2(dp_left[2]) --- L3(dp_left[3]) --- L4(dp_left[4]) --- L5(dp_left[5]) --- L6(dp_left[6])
        style L0 fill:#f9f,stroke:#333,stroke-width:2px
        style L1 fill:#f9f,stroke:#333,stroke-width:2px
        style L2 fill:#f9f,stroke:#333,stroke-width:2px
        style L3 fill:#f9f,stroke:#333,stroke-width:2px
        style L4 fill:#f9f,stroke:#333,stroke-width:2px
        style L5 fill:#f9f,stroke:#333,stroke-width:2px
        style L6 fill:#f9f,stroke:#333,stroke-width:2px
        L0 -- "Min length in arr[0...0]" --> A
        L1 -- "Min length in arr[0...1]" --> B
        L2 -- "Min length in arr[0...2]" --> C
        L3 -- "Min length in arr[0...3]" --> D
        L4 -- "Min length in arr[0...4]" --> E
        L5 -- "Min length in arr[0...5]" --> F
        L6 -- "Min length in arr[0...6]" --> G
    end

    subgraph dp_right Calculation (Right to Left)
        R0(dp_right[0]) --- R1(dp_right[1]) --- R2(dp_right[2]) --- R3(dp_right[3]) --- R4(dp_right[4]) --- R5(dp_right[5]) --- R6(dp_right[6])
        style R0 fill:#9cf,stroke:#333,stroke-width:2px
        style R1 fill:#9cf,stroke:#333,stroke-width:2px
        style R2 fill:#9cf,stroke:#333,stroke-width:2px
        style R3 fill:#9cf,stroke:#333,stroke-width:2px
        style R4 fill:#9cf,stroke:#333,stroke-width:2px
        style R5 fill:#9cf,stroke:#333,stroke-width:2px
        style R6 fill:#9cf,stroke:#333,stroke-width:2px
        R0 -- "Min length in arr[0...N-1]" --> A
        R1 -- "Min length in arr[1...N-1]" --> B
        R2 -- "Min length in arr[2...N-1]" --> C
        R3 -- "Min length in arr[3...N-1]" --> D
        R4 -- "Min length in arr[4...N-1]" --> E
        R5 -- "Min length in arr[5...N-1]" --> F
        R6 -- "Min length in arr[6...N-1]" --> G
    end

    subgraph Final Combination
        SplitPoint(Split Point 'i')
        Subarray1(Sub-array 1: ends at or before 'i')
        Subarray2(Sub-array 2: starts at or after 'i+1')
        TotalLength(Total Length = dp_left[i] + dp_right[i+1])

        SplitPoint --> Subarray1
        SplitPoint --> Subarray2
        Subarray1 --> TotalLength
        Subarray2 --> TotalLength
        dp_left[i] -- "Length of Subarray 1" --> Subarray1
        dp_right[i+1] -- "Length of Subarray 2" --> Subarray2
    end

    L6 -- "Computed" --> SplitPoint
    R0 -- "Computed" --> SplitPoint
```

The diagram illustrates how `dp_left[i]` captures the best sub-array ending anywhere up to `i`, and `dp_right[i+1]` captures the best sub-array starting anywhere from `i+1` onwards. By iterating through all possible split points `i`, we guarantee that the two chosen sub-arrays are non-overlapping.

## Dry Run
Let's trace Example 1: `arr = [3,2,2,4,3]`, `target = 3`. `n = 5`.
Initialize `dp_left = [inf, inf, inf, inf, inf]`, `dp_right = [inf, inf, inf, inf, inf]`.
`min_total_len = inf`.

**1. Calculate `dp_left`:**
`left = 0`, `current_sum = 0`, `min_len_found_so_far = inf`

| `right` | `arr[right]` | `current_sum` (before while) | `left` (after while) | `current_sum` (after while) | `current_sum == target?` | `current_window_len` | `min_len_found_so_far` | `dp_left[right]` |
| :------ | :----------- | :--------------------------- | :------------------- | :-------------------------- | :----------------------- | :------------------- | :--------------------- | :--------------- |
| 0       | 3            | 3                            | 0                    | 3                           | Yes                      | 1                    | 1                      | 1                |
| 1       | 2            | 5                            | 1                    | 2                           | No                       | -                    | 1                      | 1                |
| 2       | 2            | 4                            | 2                    | 2                           | No                       | -                    | 1                      | 1                |
| 3       | 4            | 6                            | 4                    | 0                           | No                       | -                    | 1                      | 1                |
| 4       | 3            | 3                            | 4                    | 3                           | Yes                      | 1                    | 1                      | 1                |

`dp_left` becomes `[1, 1, 1, 1, 1]`.

**2. Calculate `dp_right`:**
`left_ptr = n-1` down to `0`. `right_boundary = n-1`. `current_sum = 0`. `min_len_found_so_far = inf`.

| `left_ptr` | `arr[left_ptr]` | `current_sum` (before while) | `right_boundary` (after while) | `current_sum` (after while) | `current_sum == target?` | `current_window_len` | `min_len_found_so_far` | `dp_right[left_ptr]` |
| :--------- | :-------------- | :--------------------------- | :----------------------------- | :-------------------------- | :----------------------- | :------------------- | :--------------------- | :------------------- |
| 4          | 3               | 3                            | 4                              | 3                           | Yes                      | 1                    | 1                      | 1                    |
| 3          | 4               | 7                            | 2                              | 0                           | No                       | -                    | 1                      | 1                    |
| 2          | 2               | 2                            | 2                              | 2                           | No                       | -                    | 1                      | 1                    |
| 1          | 2               | 4                            | 1                              | 2                           | No                       | -                    | 1                      | 1                    |
| 0          | 3               | 5                            | 0                              | 3                           | Yes                      | 1                    | 1                      | 1                    |

`dp_right` becomes `[1, 1, 1, 1, 1]`.

**3. Combine `dp_left` and `dp_right`:**
`min_total_len = inf`

| `i` | `dp_left[i]` | `dp_right[i+1]` | `dp_left[i] + dp_right[i+1]` | `min_total_len` |
| :-- | :----------- | :-------------- | :--------------------------- | :-------------- |
| 0   | 1            | 1               | 2                            | 2               |
| 1   | 1            | 1               | 2                            | 2               |
| 2   | 1            | 1               | 2                            | 2               |
| 3   | 1            | 1               | 2                            | 2               |

Final `min_total_len = 2`.
The function returns `2`.

## Complexity
*   **Time Complexity:** O(N).
    *   The `dp_left` array is computed in a single pass (O(N)) using a sliding window, where each element is visited at most twice (once by `right`, once by `left`).
    *   The `dp_right` array is computed similarly in a single pass from right to left (O(N)).
    *   The final combination step iterates through the array once (O(N)).
    *   Total time complexity is O(N) + O(N) + O(N) = O(N).
*   **Space Complexity:** O(N).
    *   We use two auxiliary arrays, `dp_left` and `dp_right`, each of size `N`.
    *   Total space complexity is O(N) + O(N) = O(N).

## Edge Cases
*   **`arr` has less than 2 elements:** The loop `for i in range(n - 1)` will not run if `n < 2`. `min_total_len` will remain `float('inf')`, correctly returning -1.
*   **No sub-arrays sum to `target`:** Both `dp_left` and `dp_right` will remain `float('inf')` throughout. `min_total_len` will remain `float('inf')`, correctly returning -1.
*   **Only one sub-array sums to `target`:** One of `dp_left[i]` or `dp_right[i+1]` will always be `float('inf')` for any valid split point `i`. `min_total_len` will remain `float('inf')`, correctly returning -1.
*   **All elements are positive (as per constraints):** This simplifies the sliding window logic, as we only need to shrink the window from one side when the sum exceeds the target. No need to handle negative numbers or zero.
*   **`target` is very large:** `current_sum` can grow large, but Python's arbitrary-precision integers handle this automatically.

## Solution

```python
from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        
        # dp_left[i] stores the minimum length of a subarray with sum 'target'
        # that ends at or before index i.
        # Initialize with float('inf') as no such subarray might exist initially.
        dp_left = [float('inf')] * n
        
        current_sum = 0
        left = 0
        # Tracks the minimum length of a target subarray found up to the current 'right' pointer.
        min_len_found_so_far = float('inf') 
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window from the left if the current sum exceeds the target.
            # Since arr[i] are positive, this ensures current_sum eventually becomes <= target.
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
            
            # If the current window sum equals the target, we found a valid subarray.
            if current_sum == target:
                current_window_len = right - left + 1
                min_len_found_so_far = min(min_len_found_so_far, current_window_len)
            
            # Store the minimum length found up to this point (ending at or before 'right').
            dp_left[right] = min_len_found_so_far

        # dp_right[i] stores the minimum length of a subarray with sum 'target'
        # that starts at or after index i.
        # Initialize with float('inf').
        dp_right = [float('inf')] * n
        
        current_sum = 0
        # 'right_boundary' tracks the rightmost index of the current window, moving left.
        right_boundary = n - 1 
        # Tracks the minimum length of a target subarray found from the current 'left_ptr' to the end.
        min_len_found_so_far = float('inf') 
        
        # Iterate from right to left to build dp_right.
        for left_ptr in range(n - 1, -1, -1):
            current_sum += arr[left_ptr]
            
            # Shrink the window from the right if the current sum exceeds the target.
            while current_sum > target:
                current_sum -= arr[right_boundary]
                right_boundary -= 1
            
            # If the current window sum equals the target, we found a valid subarray.
            if current_sum == target:
                current_window_len = right_boundary - left_ptr + 1
                min_len_found_so_far = min(min_len_found_so_far, current_window_len)
            
            # Store the minimum length found up to this point (starting at or after 'left_ptr').
            dp_right[left_ptr] = min_len_found_so_far
            
        # Finally, combine results from dp_left and dp_right to find the minimum total length.
        # We iterate through all possible split points 'i'.
        # The first subarray ends at or before 'i', and the second subarray starts at or after 'i+1'.
        min_total_len = float('inf')
        for i in range(n - 1): # 'i' goes from 0 to n-2, representing the end of the first subarray's potential range
            # Ensure both parts have found a valid subarray (i.e., their lengths are not infinity).
            if dp_left[i] != float('inf') and dp_right[i+1] != float('inf'):
                min_total_len = min(min_total_len, dp_left[i] + dp_right[i+1])
        
        # If min_total_len is still infinity, it means no two such non-overlapping subarrays were found.
        return min_total_len if min_total_len != float('inf') else -1

```

## Why This Works
This approach works because it systematically explores all possible ways to split the array into two non-overlapping regions, where each region contains a shortest possible sub-array summing to `target`.
1.  **`dp_left[i]`** correctly stores the minimum length of *any* sub-array with sum `target` that can be found within `arr[0...i]`. This means if we pick a sub-array for the "left part" that ends at or before `i`, `dp_left[i]` gives us its minimum possible length.
2.  **`dp_right[i+1]`** similarly stores the minimum length of *any* sub-array with sum `target` that can be found within `arr[i+1...n-1]`. This means if we pick a sub-array for the "right part" that starts at or after `i+1`, `dp_right[i+1]` gives us its minimum possible length.
3.  By iterating through all possible split points `i` (where the first sub-array ends at or before `i` and the second starts at or after `i+1`), we guarantee that the two chosen sub-arrays are strictly non-overlapping. Since `dp_left` and `dp_right` already provide the *minimum* lengths for their respective ranges, summing them up and taking the overall minimum ensures we find the globally optimal solution. The use of `float('inf')` correctly handles cases where no such sub-arrays exist.

---
<sub>Generated 2026-09-17 05:14 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
