# [3364] Minimum Positive Sum Subarray 

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-11-14 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-positive-sum-subarray/)

**Topics:** Array, Sliding Window, Prefix Sum

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums and two integers l and r. Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive) and whose sum is greater than 0.

Return the minimum sum of such a subarray. If no such subarray exists, return -1.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [3, -2, 1, 4], l = 2, r = 3

Output: 1

Explanation:

The subarrays of length between l = 2 and r = 3 where the sum is greater than 0 are:

- [3, -2] with a sum of 1

- [1, 4] with a sum of 5

- [3, -2, 1] with a sum of 2

- [-2, 1, 4] with a sum of 3

Out of these, the subarray [3, -2] has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

Example 2:

Input: nums = [-2, 2, -3, 1], l = 2, r = 3

Output: -1

Explanation:

There is no subarray of length between l and r that has a sum greater than 0. So, the answer is -1.

Example 3:

Input: nums = [1, 2, 3, 4], l = 2, r = 4

Output: 3

Explanation:

The subarray [1, 2] has a length of 2 and the minimum sum greater than 0. So, the answer is 3.

Constraints:

- 1 <= nums.length <= 100

- 1 <= l <= r <= nums.length

- -1000 <= nums[i] <= 1000

**Examples / sample tests:**

```
[3,-2,1,4]
2
3
[-2,2,-3,1]
2
3
[1,2,3,4]
2
4
```

---

## Problem Summary
We need to find the smallest positive sum among all subarrays of a given integer array `nums`. The length of these subarrays must be between `l` and `r` (inclusive). If no such subarray exists, return -1.

## Intuition
The problem asks us to inspect subarrays and find one with specific properties (length within `[l, r]` and a positive sum) that also has the minimum sum among all such candidates. Since the input array size `N` is quite small (up to 100), we can afford to check **every single possible subarray**. For each subarray, we'll calculate its sum and length, then apply the given conditions to determine if it's a candidate for our minimum.

## Approach
We will use a nested loop structure to iterate through all possible subarrays. For each subarray, we'll efficiently calculate its sum and length, then check if it meets the criteria to update our minimum positive sum.

1.  Initialize a variable `min_positive_sum` to a very large value (e.g., `float('inf')`). This ensures that any valid positive sum we find will be smaller and will correctly update this variable.
2.  Get the length of the input array, `n = len(nums)`.
3.  Start an **outer loop** using an index `i` from `0` to `n - 1`. This `i` will represent the **starting index** of a potential subarray.
4.  Inside the outer loop, initialize `current_sum = 0`. This variable will accumulate the sum of the subarray that starts at `i` and extends to the current `j`.
5.  Start an **inner loop** using an index `j` from `i` to `n - 1`. This `j` will represent the **ending index** of the current subarray.
6.  In each iteration of the inner loop:
    a.  Add `nums[j]` to `current_sum`. At this point, `current_sum` holds the sum of the subarray `nums[i...j]`.
    b.  Calculate the **length** of the current subarray: `current_length = j - i + 1`.
    c.  Check if `current_length` falls within the specified range: `l <= current_length <= r`.
    d.  If the length condition is met **AND** `current_sum` is strictly greater than `0`:
        i.  Update `min_positive_sum` by taking the minimum of its current value and `current_sum`: `min_positive_sum = min(min_positive_sum, current_sum)`.
7.  After both loops have completed, we have checked all possible subarrays.
8.  Finally, if `min_positive_sum` is still `float('inf')`, it means no subarray satisfied both the length and positive sum conditions. In this case, return `-1`.
9.  Otherwise, return the final `min_positive_sum`.

## Visualization
Let's visualize how the nested loops explore subarrays for `nums = [3, -2, 1, 4]`, `l = 2`, `r = 3`. The `min_positive_sum` starts at `inf`.

```mermaid
graph TD
    A[Start: min_positive_sum = inf] --> B{Outer loop: i from 0 to n-1};

    B --> C{i = 0};
    C --> D[current_sum = 0];
    D --> E{Inner loop: j from i to n-1};
    E --> F{j = 0: nums[0]=3};
    F --> G[current_sum = 3];
    G --> H[current_length = 1];
    H --> I{Check: 2 <= 1 <= 3? No};
    I --> J{j = 1: nums[1]=-2};
    J --> K[current_sum = 3 + (-2) = 1];
    K --> L[current_length = 2];
    L --> M{Check: 2 <= 2 <= 3? Yes};
    M --> N{Check: current_sum (1) > 0? Yes};
    N --> O[min_positive_sum = min(inf, 1) = 1];
    O --> P{j = 2: nums[2]=1};
    P --> Q[current_sum = 1 + 1 = 2];
    Q --> R[current_length = 3];
    R --> S{Check: 2 <= 3 <= 3? Yes};
    S --> T{Check: current_sum (2) > 0? Yes};
    T --> U[min_positive_sum = min(1, 2) = 1];
    U --> V{j = 3: nums[3]=4};
    V --> W[current_sum = 2 + 4 = 6];
    W --> X[current_length = 4];
    X --> Y{Check: 2 <= 4 <= 3? No};
    Y --> Z{Inner loop ends};

    Z --> AA{i = 1};
    AA --> BB[current_sum = 0];
    BB --> CC{Inner loop: j from 1 to n-1};
    CC --> DD{j = 1: nums[1]=-2};
    DD --> EE[current_sum = -2];
    EE --> FF[current_length = 1];
    FF --> GG{Check: 2 <= 1 <= 3? No};
    GG --> HH{j = 2: nums[2]=1};
    HH --> II[current_sum = -2 + 1 = -1];
    II --> JJ[current_length = 2];
    JJ --> KK{Check: 2 <= 2 <= 3? Yes};
    KK --> LL{Check: current_sum (-1) > 0? No};
    LL --> MM{j = 3: nums[3]=4};
    MM --> NN[current_sum = -1 + 4 = 3];
    NN --> OO[current_length = 3];
    OO --> PP{Check: 2 <= 3 <= 3? Yes};
    PP --> QQ{Check: current_sum (3) > 0? Yes};
    QQ --> RR[min_positive_sum = min(1, 3) = 1];
    RR --> SS{Inner loop ends};

    SS --> TT{... continue for i=2, i=3 ...};
    TT --> UU{Outer loop ends};
    UU --> VV{Final Check: min_positive_sum (1) == inf? No};
    VV --> WW[Return 1];
```

## Dry Run
Let's trace Example 1: `nums = [3, -2, 1, 4]`, `l = 2`, `r = 3`.
`n = 4`
`min_positive_sum = float('inf')`

| `i` | `j` | `nums[j]` | `current_sum` | `current_length` | `l <= len <= r` | `sum > 0` | `min_positive_sum` | Subarray | Notes |
| :-- | :-- | :-------- | :------------ | :--------------- | :-------------- | :-------- | :----------------- | :------- | :---- |
| 0   |     |           | `0`           |                  |                 |           | `inf`              |          | Start outer loop `i=0` |
| 0   | 0   | `3`       | `3`           | `1`              | `False`         |           | `inf`              | `[3]`    | Length 1, not in `[2,3]` |
| 0   | 1   | `-2`      | `1`           | `2`              | `True`          | `True`    | `1`                | `[3, -2]`| Update `min_positive_sum` |
| 0   | 2   | `1`       | `2`           | `3`              | `True`          | `True`    | `1`                | `[3, -2, 1]` | `min(1, 2) = 1` |
| 0   | 3   | `4`       | `6`           | `4`              | `False`         |           | `1`                | `[3, -2, 1, 4]` | Length 4, not in `[2,3]` |
| 1   |     |           | `0`           |                  |                 |           | `1`                |          | Start outer loop `i=1` |
| 1   | 1   | `-2`      | `-2`          | `1`              | `False`         |           | `1`                | `[-2]`   | Length 1 |
| 1   | 2   | `1`       | `-1`          | `2`              | `True`          | `False`   | `1`                | `[-2, 1]`| Sum not positive |
| 1   | 3   | `4`       | `3`           | `3`              | `True`          | `True`    | `1`                | `[-2, 1, 4]` | `min(1, 3) = 1` |
| 2   |     |           | `0`           |                  |                 |           | `1`                |          | Start outer loop `i=2` |
| 2   | 2   | `1`       | `1`           | `1`              | `False`         |           | `1`                | `[1]`    | Length 1 |
| 2   | 3   | `4`       | `5`           | `2`              | `True`          | `True`    | `1`                | `[1, 4]` | `min(1, 5) = 1` |
| 3   |     |           | `0`           |                  |                 |           | `1`                |          | Start outer loop `i=3` |
| 3   | 3   | `4`       | `4`           | `1`              | `False`         |           | `1`                | `[4]`    | Length 1 |

Final result: `min_positive_sum` is `1`.

## Complexity
*   **Time Complexity:** `O(N^2)`. The outer loop runs `N` times, and the inner loop runs up to `N` times. Inside the inner loop, operations like addition, subtraction, and comparison are constant time `O(1)`. Thus, the total time complexity is `N * N = O(N^2)`. Given `N <= 100`, `N^2 = 100^2 = 10,000` operations, which is very efficient.
*   **Space Complexity:** `O(1)`. We only use a few variables (`n`, `min_positive_sum`, `current_sum`, `current_length`) to store state, regardless of the input array's size.

## Edge Cases
*   **No valid subarray:** If `min_positive_sum` remains `float('inf')` after checking all subarrays (e.g., `nums = [-2, 2, -3, 1], l = 2, r = 3`), the solution correctly returns `-1`.
*   **All numbers positive:** If all numbers in `nums` are positive, many subarrays will have positive sums. The solution will correctly find the minimum among those that meet the length criteria (e.g., `nums = [1, 2, 3, 4], l = 2, r = 4` yields `3`).
*   **All numbers negative or zero:** If all numbers are negative or zero, no subarray will have a positive sum. The solution will correctly return `-1`.
*   **`l` equals `r`:** The length check `l <= current_length <= r` naturally handles cases where `l` and `r` are the same, effectively searching for subarrays of a fixed length.
*   **`nums.length` is small (e.g., 1):** The loops correctly handle small array sizes. For `n=1`, `i=0`, `j=0`. `current_length` will be 1. If `l=1, r=1`, it will be considered. If `l > 1`, it won't be considered.

## Solution
```python
from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_positive_sum = float('inf') # Initialize with a very large value to find the true minimum

        # Iterate through all possible starting points of a subarray
        for i in range(n):
            current_sum = 0 # Reset sum for each new starting point
            # Iterate through all possible ending points for the current starting point
            for j in range(i, n):
                current_sum += nums[j] # Extend the subarray and update its sum
                current_length = j - i + 1 # Calculate the length of the current subarray nums[i...j]

                # Check if the subarray length is within the specified range [l, r]
                if l <= current_length <= r:
                    # If the sum is positive, consider it for the minimum
                    if current_sum > 0:
                        min_positive_sum = min(min_positive_sum, current_sum)
        
        # After checking all subarrays, if min_positive_sum is still infinity,
        # it means no valid subarray (length in [l,r] and sum > 0) was found.
        if min_positive_sum == float('inf'):
            return -1
        else:
            # Otherwise, return the smallest positive sum found
            return int(min_positive_sum) 
```

## Why This Works
This solution works by exhaustively checking every possible contiguous subarray. The nested loops (`i` for start, `j` for end) ensure that all `N * (N+1) / 2` subarrays are considered. For each subarray, we efficiently calculate its sum incrementally and its length. By applying the given constraints (`l <= current_length <= r` and `current_sum > 0`) to every candidate and continuously updating `min_positive_sum`, we are guaranteed to find the absolute minimum positive sum that satisfies all conditions. The small constraint on `N` (up to 100) makes this `O(N^2)` approach computationally feasible and optimal for the given problem constraints.

---
<sub>Generated 2026-11-14 06:56 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
