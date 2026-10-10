# [2333] Minimum Sum of Squared Difference

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-10-10 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-sum-of-squared-difference/)

**Topics:** Array, Binary Search, Greedy, Sorting, Heap (Priority Queue)

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])^2 for each 0 <= i < n.

You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.

Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

Note: You are allowed to modify the array elements to become negative integers.

Example 1:

Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
Output: 579
Explanation: The elements in nums1 and nums2 cannot be modified because k1 = 0 and k2 = 0.
The sum of square difference will be: (1 - 2)^2 + (2 - 10)^2 + (3 - 20)^2 + (4 - 19)^2 = 579.

Example 2:

Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
Output: 43
Explanation: One way to obtain the minimum sum of square difference is:
- Increase nums1[0] once.
- Increase nums2[2] once.
The minimum of the sum of square difference will be:
(2 - 5)^2 + (4 - 8)^2 + (10 - 7)^2 + (12 - 9)^2 = 43.
Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.

Constraints:

- n == nums1.length == nums2.length

- 1 <= n <= 10^5

- 0 <= nums1[i], nums2[i] <= 10^5

- 0 <= k1, k2 <= 10^9

**Examples / sample tests:**

```
[1,2,3,4]
[2,10,20,19]
0
0
[1,4,10,12]
[5,8,6,9]
1
1
```

---

## Problem Summary
You are given two arrays, `nums1` and `nums2`, and two integers `k1` and `k2`. Your goal is to minimize the sum of squared differences, defined as `sum((nums1[i] - nums2[i])^2)`. You can modify any element in `nums1` by `+1` or `-1` at most `k1` times, and similarly for `nums2` at most `k2` times.

## Intuition
The core idea is to understand how modifications affect the sum of squared differences.
1.  **Combined Operations:** Modifying `nums1[i]` by `+1` or `-1` has the same effect on `abs(nums1[i] - nums2[i])` as modifying `nums2[i]` by `-1` or `+1` respectively. In essence, we have a total of `K = k1 + k2` operations, and each operation allows us to reduce any `abs(nums1[i] - nums2[i])` by 1 (as long as it's greater than 0).
2.  **Greedy Choice:** To minimize a sum of squares, `sum(diff^2)`, we should always prioritize reducing the *largest* absolute differences. Why? Because the function `f(x) = x^2` grows quadratically. Reducing a large `x` by 1 (e.g., from 10 to 9) saves `10^2 - 9^2 = 19`, which is much more than reducing a small `x` by 1 (e.g., from 2 to 1), which saves `2^2 - 1^2 = 3`. The "gain" from reducing a difference by 1 is `x^2 - (x-1)^2 = 2x - 1`, which is maximized when `x` is maximized.
3.  **Efficient Application:** Since `K` can be very large (`2 * 10^9`), we cannot simulate each operation one by one. Instead, we can count the frequencies of each absolute difference. Then, starting from the largest difference, we can efficiently reduce all occurrences of that difference by 1, moving them to the next smaller difference category, until we run out of operations.

## Approach
We will use a frequency array to keep track of the counts of each absolute difference.

1.  **Calculate Initial Differences:** For each `i`, compute `diffs[i] = abs(nums1[i] - nums2[i])`.
2.  **Combine Operations:** Sum `k1` and `k2` to get `K = k1 + k2`, representing the total number of modifications available.
3.  **Find Maximum Difference:** Determine `max_d`, the largest absolute difference found in `diffs`. This will define the size of our frequency array.
4.  **Populate Frequency Array:** Create a `counts` array of size `max_d + 1`, initialized to zeros. Iterate through `diffs`, and for each `d` in `diffs`, increment `counts[d]`.
5.  **Greedy Reduction:** Iterate `d` from `max_d` down to `1`:
    *   If `K` is 0, we have no more operations, so break the loop.
    *   If `counts[d]` is 0, there are no differences of this size, so continue to the next smaller `d`.
    *   We have `counts[d]` differences of size `d`. We want to reduce them to `d-1`. Each such reduction costs 1 operation.
    *   Calculate `num_to_reduce = min(K, counts[d])`. This is the number of differences of size `d` that we can actually reduce.
    *   Update `counts`: `counts[d] -= num_to_reduce` (these `d`s are no longer `d`).
    *   Update `counts`: `counts[d-1] += num_to_reduce` (these `d`s are now `d-1`).
    *   Update `K`: `K -= num_to_reduce` (we used `num_to_reduce` operations).
6.  **Calculate Final Sum of Squares:** After the reduction loop, iterate through the `counts` array from `d = 0` to `max_d`. For each `d`, add `counts[d] * (d * d)` to a running total.
7.  **Return** the total sum of squares.

## Visualization
Let's visualize the `counts` array and how it changes during the greedy reduction.

**Example:** `diffs = [4, 4, 4, 3]`, `K = 2`

**1. Initial `counts` array (after step 4):**
```
Index (Difference): 0   1   2   3   4
Count:              0   0   0   1   3
```
This means there is 1 difference of value 3, and 3 differences of value 4.

**2. Greedy Reduction (Step 5):**

*   **`d = 4`:**
    *   `K = 2`, `counts[4] = 3`.
    *   `num_to_reduce = min(K, counts[4]) = min(2, 3) = 2`.
    *   We reduce 2 of the '4's to '3's.
    *   `counts[4]` becomes `3 - 2 = 1`.
    *   `counts[3]` becomes `1 + 2 = 3`.
    *   `K` becomes `2 - 2 = 0`.

    **`counts` array after `d=4` processing:**
    ```
    Index (Difference): 0   1   2   3   4
    Count:              0   0   0   3   1
    ```
    Now there are 3 differences of value 3, and 1 difference of value 4.

*   **`d = 3`:**
    *   `K = 0`. The loop breaks.

**3. Final Sum Calculation (Step 6):**
*   `counts[3] * 3^2 = 3 * 9 = 27`
*   `counts[4] * 4^2 = 1 * 16 = 16`
*   Total sum = `27 + 16 = 43`.

## Dry Run

Let's walk through **Example 1**:
`nums1 = [1,2,3,4]`, `nums2 = [2,10,20,19]`, `k1 = 0`, `k2 = 0`

| Step | Description                                   | `diffs`                               | `K` | `max_d` | `counts` array (relevant parts) | `total_sum_sq` |
| :--- | :-------------------------------------------- | :------------------------------------ | :-- | :------ | :------------------------------ | :------------- |
| 1    | Calculate initial absolute differences        | `[abs(1-2), abs(2-10), abs(3-20), abs(4-19)]` = `[1, 8, 17, 15]` | -   | -       | -                               | -              |
| 2    | Combine `k1`, `k2`                          | -                                     | `0` | -       | -                               | -              |
| 3    | Find `max_d`                                  | -                                     | -   | `17`    | -                               | -              |
| 4    | Populate `counts` array (size 18)             | -                                     | -   | -       | `counts[1]=1, counts[8]=1, counts[15]=1, counts[17]=1` | -              |
| 5    | **Greedy Reduction Loop (`d` from `max_d` down to `1`):** |                                       |     |         |                                 |                |
| 5.1  | `d = 17`: `K = 0`. Loop breaks.               | -                                     | `0` | `17`    | `counts[1]=1, counts[8]=1, counts[15]=1, counts[17]=1` | -              |
| 6    | **Calculate Final Sum of Squares:**           |                                       |     |         |                                 |                |
| 6.1  | `d = 1`: `counts[1] * 1^2 = 1 * 1 = 1`        | -                                     | -   | -       | -                               | `1`            |
| 6.2  | `d = 8`: `counts[8] * 8^2 = 1 * 64 = 64`      | -                                     | -   | -       | -                               | `1 + 64 = 65`  |
| 6.3  | `d = 15`: `counts[15] * 15^2 = 1 * 225 = 225` | -                                     | -   | -       | -                               | `65 + 225 = 290` |
| 6.4  | `d = 17`: `counts[17] * 17^2 = 1 * 289 = 289` | -                                     | -   | -       | -                               | `290 + 289 = 579` |
| 7    | **Return `total_sum_sq`**                     | -                                     | -   | -       | -                               | `579`          |

The final result `579` matches Example 1.

## Complexity
*   **Time Complexity:** `O(N + max_diff)`.
    *   Calculating initial differences: `O(N)`.
    *   Finding `max_d`: `O(N)`.
    *   Populating frequency array: `O(N)`.
    *   Greedy reduction loop: `O(max_d)` (iterates from `max_d` down to 1).
    *   Calculating final sum: `O(max_d)`.
    *   Given `N <= 10^5` and `max_diff <= 10^5`, this is efficient enough.
*   **Space Complexity:** `O(max_diff)`.
    *   For the `counts` frequency array. `max_diff` can be up to `10^5`.

## Edge Cases
*   **`k1 = 0, k2 = 0`:** `K` will be 0. The greedy reduction loop will immediately break, and the initial sum of squares will be calculated correctly.
*   **`K` is very large (enough to make all differences 0):** The loop will continue until `K` becomes 0 or all differences are reduced to 0. All counts will eventually shift to `counts[0]`, resulting in a final sum of 0.
*   **All `nums1[i] == nums2[i]` initially:** All `diffs` will be 0. `max_d` will be 0. The reduction loop `range(max_d, 0, -1)` will not run. The final sum will correctly be 0.
*   **`n = 1`:** The logic holds perfectly for a single pair of numbers.
*   **Large `nums1[i], nums2[i]` but small `diff`:** E.g., `nums1=[100000], nums2=[99999]`. `diff=1`. Handled correctly as `max_d` would be small.
*   **Small `nums1[i], nums2[i]` but large `diff`:** E.g., `nums1=[0], nums2=[100000]`. `diff=100000`. Handled correctly as `max_d` would be large, and the `counts` array would accommodate it.

## Solution

```python
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        
        # Step 1: Calculate initial absolute differences
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        
        # Step 2: Combine k1 and k2 for total operations
        K = k1 + k2
        
        # Step 3: Find the maximum difference to determine frequency array size
        max_d = 0
        if diffs: # Handle case where diffs might be empty (though constraints say n >= 1)
            max_d = max(diffs)
        
        # Step 4: Populate frequency array
        # counts[d] will store how many times difference 'd' appears
        counts = [0] * (max_d + 1)
        for d in diffs:
            counts[d] += 1
            
        # Step 5: Greedy reduction
        # Iterate from the largest difference down to 1
        for d in range(max_d, 0, -1):
            if K == 0:
                break # No more operations left
            
            if counts[d] == 0:
                continue # No differences of this size
            
            # We have counts[d] differences of size 'd'.
            # We want to reduce them to 'd-1'. Each reduction costs 1 operation.
            # We can reduce at most K of these differences.
            num_to_reduce = min(K, counts[d])
            
            counts[d] -= num_to_reduce    # These 'd's are no longer 'd'
            counts[d-1] += num_to_reduce  # They become 'd-1'
            K -= num_to_reduce            # Update remaining operations
            
        # Step 6: Calculate final sum of squares
        total_sum_sq = 0
        for d in range(max_d + 1):
            total_sum_sq += counts[d] * (d * d)
            
        return total_sum_sq

```

## Why This Works
This solution works due to the **greedy choice property** inherent in minimizing the sum of squares. The function `f(x) = x^2` is convex, meaning its rate of change increases as `x` increases. Specifically, reducing a difference `x` to `x-1` decreases the squared sum by `x^2 - (x-1)^2 = 2x - 1`. This reduction is maximized when `x` is as large as possible. Therefore, to achieve the minimum total sum of squared differences, we must always apply our operations to the largest available absolute differences first. The frequency array approach efficiently simulates this greedy strategy by processing all occurrences of the current largest difference simultaneously, allowing us to handle very large `K` values without iterating `K` times.

---
<sub>Generated 2026-10-10 06:18 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
