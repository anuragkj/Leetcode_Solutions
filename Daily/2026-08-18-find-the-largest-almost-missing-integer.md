# [3471] Find the Largest Almost Missing Integer

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-08-18 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/find-the-largest-almost-missing-integer/)

**Topics:** Array, Hash Table

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums and an integer k.

An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.

Return the largest almost missing integer from nums. If no such integer exists, return -1.

A subarray is a contiguous sequence of elements within an array.

Example 1:

Input: nums = [3,9,2,1,7], k = 3

Output: 7

Explanation:

- 1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].

- 2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
	3 appears in 1 subarray of size 3: [3, 9, 2].
	7 appears in 1 subarray of size 3: [2, 1, 7].
	9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].

We return 7 since it is the largest integer that appears in exactly one subarray of size k.

Example 2:

Input: nums = [3,9,7,2,1,7], k = 4

Output: 3

Explanation:

- 1 appears in 2 subarrays of size 4: [9, 7, 2, 1], [7, 2, 1, 7].

- 2 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].

- 3 appears in 1 subarray of size 4: [3, 9, 7, 2].

- 7 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].

- 9 appears in 2 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1].

We return 3 since it is the largest and only integer that appears in exactly one subarray of size k.

Example 3:

Input: nums = [0,0], k = 1

Output: -1

Explanation:

There is no integer that appears in only one subarray of size 1.

Constraints:

- 1 <= nums.length <= 50

- 0 <= nums[i] <= 50

- 1 <= k <= nums.length

**Examples / sample tests:**

```
[3,9,2,1,7]
3
[3,9,7,2,1,7]
4
[0,0]
1
```

---

## Problem Summary
We are given an array `nums` and an integer `k`. An integer `x` is considered "almost missing" if it appears in exactly one subarray of size `k` within `nums`. Our goal is to find the largest such "almost missing" integer. If no such integer exists, we should return -1.

## Intuition
The core of this problem is to count how many times each number appears across *all* subarrays of size `k`. A naive approach would be to generate all subarrays, then for each number, count its occurrences. This could be inefficient.

However, the problem statement and hints provide a crucial simplification by breaking it down into three distinct cases based on the value of `k` relative to `n` (the length of `nums`):

1.  **`k = n`**: If `k` is equal to the length of `nums`, there's only one subarray of size `k` – the entire `nums` array itself. In this scenario, every number present in `nums` appears in exactly one subarray (the only one). Thus, the "largest almost missing integer" is simply the largest number in `nums`.

2.  **`k = 1`**: If `k` is 1, each subarray of size `k` is just a single element `[nums[i]]`. An integer `x` appears in exactly one such subarray if and only if `x` itself appears exactly once in the entire `nums` array. So, we need to find the largest number that is unique in `nums`.

3.  **`1 < k < n`**: This is the most interesting case. A key observation (also provided as a hint) is that for `1 < k < n`, only the **first element (`nums[0]`)** and the **last element (`nums[n-1]`)** of the original array `nums` can potentially appear in exactly one subarray of size `k`. All other elements `nums[i]` (where `0 < i < n-1`) will appear in *more than one* subarray of size `k`.
    *   `nums[0]` is only the first element of the very first subarray `nums[0...k-1]`. It cannot be the first element of any other `k`-sized subarray, nor can it be an interior element of any subarray that starts after index 0.
    *   `nums[n-1]` is only the last element of the very last subarray `nums[n-k...n-1]`. It cannot be the last element of any other `k`-sized subarray, nor can it be an interior element of any subarray that ends before index `n-1`.
    *   Any element `nums[i]` where `0 < i < n-1` will be part of at least two distinct subarrays: one starting at `i-1` (e.g., `nums[i-1...i+k-2]`) and one starting at `i` (e.g., `nums[i...i+k-1]`). Since `k > 1`, these are distinct.
    Therefore, for this case, we only need to count the total occurrences of `nums[0]` and `nums[n-1]` across *all* `N-k+1` subarrays of size `k`. If either count is exactly 1, that number is a candidate. We then return the largest of these candidates.

## Approach
We will implement the solution by handling the three cases identified in the intuition:

1.  **Initialize `n = len(nums)` and `max_almost_missing = -1`**.

2.  **Case 1: `k == n`**
    *   Return `max(nums)`. This is the largest element in the entire array.

3.  **Case 2: `k == 1`**
    *   Use a `collections.Counter` (or a hash map/dictionary) to count the frequency of each number in `nums`.
    *   Iterate through the `(number, count)` pairs in the frequency map.
    *   If a `count` is exactly 1, it means that `number` appears uniquely in `nums`. Update `max_almost_missing = max(max_almost_missing, number)`.
    *   Return the final `max_almost_missing`.

4.  **Case 3: `1 < k < n`**
    *   Identify the first element `val0 = nums[0]` and the last element `val_n_minus_1 = nums[n-1]`.
    *   Initialize `count_val0 = 0` and `count_val_n_minus_1 = 0`. These will track how many subarrays of size `k` contain `val0` and `val_n_minus_1`, respectively.
    *   Iterate `i` from `0` to `n - k` (inclusive). This `i` represents the starting index of each subarray of size `k`.
        *   For each `current_subarray = nums[i : i + k]`:
            *   Check if `val0` is present in `current_subarray`. If yes, increment `count_val0`.
            *   Check if `val_n_minus_1` is present in `current_subarray`. If yes, increment `count_val_n_minus_1`.
    *   After iterating through all subarrays:
        *   If `count_val0 == 1`, update `max_almost_missing = max(max_almost_missing, val0)`.
        *   If `count_val_n_minus_1 == 1`, update `max_almost_missing = max(max_almost_missing, val_n_minus_1)`.
        *   (Note: If `val0 == val_n_minus_1`, both counts will be identical, and the logic correctly handles this by potentially updating `max_almost_missing` with the same value twice, which is harmless.)
    *   Return the final `max_almost_missing`.

## Visualization
Let's visualize the `1 < k < n` case with `nums = [A, B, C, D, E, F, G]` and `k = 3`.
`n = 7`.
`nums[0]` is `A`. `nums[n-1]` is `G`.

```
Original Array:
Indices:   0  1  2  3  4  5  6
Elements: [A, B, C, D, E, F, G]

Subarrays of size k=3:

1. [A, B, C]   <-- Contains A. Does NOT contain G.
   ^
   Starts at index 0.

2.    [B, C, D]  <-- Does NOT contain A. Does NOT contain G.
      ^
      Starts at index 1.

3.       [C, D, E] <-- Does NOT contain A. Does NOT contain G.
         ^
         Starts at index 2.

4.          [D, E, F] <-- Does NOT contain A. Does NOT contain G.
            ^
            Starts at index 3.

5.             [E, F, G] <-- Does NOT contain A. Contains G.
               ^
               Starts at index 4. (n - k = 7 - 3 = 4)

Summary of occurrences:
- A (nums[0]): Appears in 1 subarray ([A, B, C])
- G (nums[n-1]): Appears in 1 subarray ([E, F, G])
- B: Appears in [A,B,C] and [B,C,D] (2 subarrays)
- C: Appears in [A,B,C], [B,C,D], [C,D,E] (3 subarrays)
- D: Appears in [B,C,D], [C,D,E], [D,E,F] (3 subarrays)
- E: Appears in [C,D,E], [D,E,F], [E,F,G] (3 subarrays)
- F: Appears in [D,E,F], [E,F,G] (2 subarrays)

This visualization clearly shows why only A (nums[0]) and G (nums[n-1]) are candidates for appearing in exactly one subarray.
```

## Dry Run
Let's walk through **Example 1: `nums = [3,9,2,1,7], k = 3`**

1.  **Initialization**:
    *   `n = len(nums) = 5`
    *   `max_almost_missing = -1`

2.  **Check Cases**:
    *   `k == n`? `3 == 5` is False.
    *   `k == 1`? `3 == 1` is False.
    *   This falls into the **`1 < k < n` case** (`1 < 3 < 5` is True).

3.  **`1 < k < n` Logic**:
    *   `val0 = nums[0] = 3`
    *   `val_n_minus_1 = nums[n-1] = nums[4] = 7`
    *   `count_val0 = 0`
    *   `count_val_n_minus_1 = 0`

4.  **Iterate through subarrays**: `range(n - k + 1)` means `range(5 - 3 + 1) = range(3)`, so `i` will be `0, 1, 2`.

    | `i` | `current_subarray` | `val0` (3) in subarray? | `count_val0` | `val_n_minus_1` (7) in subarray? | `count_val_n_minus_1` |
    | :-- | :----------------- | :---------------------- | :----------- | :------------------------------- | :-------------------- |
    | 0   | `nums[0:3]` = `[3,9,2]` | Yes                     | 1            | No                               | 0                     |
    | 1   | `nums[1:4]` = `[9,2,1]` | No                      | 1            | No                               | 0                     |
    | 2   | `nums[2:5]` = `[2,1,7]` | No                      | 1            | Yes                              | 1                     |

5.  **After loop**:
    *   `count_val0 = 1`
    *   `count_val_n_minus_1 = 1`

6.  **Check counts for candidates**:
    *   `max_almost_missing = -1`
    *   Is `count_val0 == 1`? Yes (`1 == 1`).
        *   `max_almost_missing = max(-1, val0) = max(-1, 3) = 3`.
    *   Is `count_val_n_minus_1 == 1`? Yes (`1 == 1`).
        *   `max_almost_missing = max(3, val_n_minus_1) = max(3, 7) = 7`.

7.  **Final Result**: `7`. This matches Example 1.

## Complexity
*   **Time Complexity**:
    *   **Case `k = n`**: `O(N)` to find the maximum element in `nums`.
    *   **Case `k = 1`**: `O(N)` to build the frequency counter and `O(N)` in the worst case to iterate through unique elements. Total `O(N)`.
    *   **Case `1 < k < n`**: We iterate `N - k + 1` times (for each subarray). Inside the loop, checking `val in current_subarray` takes `O(k)` time in the worst case (if `val` is not found or is at the end). So, the total time is `O((N - k + 1) * k)`. Since `N` is up to 50, `N*K` is at most `50*50 = 2500`, which is very efficient.
    *   **Overall**: The dominant factor is `O(N*K)` for the `1 < k < n` case. Given the constraints (`N <= 50`), this is highly efficient.

*   **Space Complexity**:
    *   **Case `k = n`**: `O(1)` (excluding input storage).
    *   **Case `k = 1`**: `O(N)` in the worst case for the `collections.Counter` if all elements in `nums` are unique.
    *   **Case `1 < k < n`**: `O(1)` as we only store a few counters.
    *   **Overall**: `O(N)` in the worst case (for `k=1`).

## Edge Cases
*   **`nums` with all identical elements**: e.g., `[0,0], k=1`.
    *   `k=1` case applies. `Counter` will be `{0: 2}`. Since `0` appears twice, its count is not 1. `max_almost_missing` remains -1. Correct.
*   **`nums` with only two elements**: e.g., `[1,2], k=1`.
    *   `k=1` case. `Counter` is `{1:1, 2:1}`. Both 1 and 2 have count 1. `max_almost_missing` becomes `max(-1,1)=1`, then `max(1,2)=2`. Returns 2. Correct.
*   **`nums` with only two elements, `k=2`**: e.g., `[1,2], k=2`.
    *   `k=n` case. `max([1,2]) = 2`. Correct.
*   **`nums[0]` is equal to `nums[n-1]`**: e.g., `[7,1,2,7], k=3`.
    *   `1 < k < n` case. `val0 = 7`, `val_n_minus_1 = 7`.
    *   The loop will count how many subarrays contain `7`.
    *   Subarrays: `[7,1,2]`, `[1,2,7]`. Both contain `7`.
    *   `count_val0` becomes 2, `count_val_n_minus_1` becomes 2.
    *   Since neither count is 1, `max_almost_missing` remains -1. Correct.
*   **No almost missing integer exists**: The initial `max_almost_missing = -1` handles this, as it will be returned if no candidates are found.

## Solution

```python
import collections
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Case 1: k = n
        # There's only one subarray (the entire nums array).
        # Every number in nums appears in exactly one subarray of size k.
        # So, the largest almost missing integer is simply the largest number in nums.
        if k == n:
            return max(nums)

        # Case 2: k = 1
        # Each subarray is a single element [nums[i]].
        # An integer x is almost missing if it appears exactly once in the entire nums array.
        # We need to find the largest such unique integer.
        if k == 1:
            # Use a Counter to get frequencies of all numbers in nums
            counts = collections.Counter(nums)
            max_almost_missing = -1
            # Iterate through the numbers and their counts
            for num, count in counts.items():
                if count == 1:  # If a number appears exactly once
                    max_almost_missing = max(max_almost_missing, num) # Update with the largest
            return max_almost_missing

        # Case 3: 1 < k < n
        # According to the problem's hint/observation, only nums[0] and nums[n-1]
        # can potentially appear in exactly one subarray of size k.
        # All other elements (nums[i] where 0 < i < n-1) will appear in multiple
        # subarrays of size k.
        #
        # We need to count how many subarrays of size k contain nums[0] and nums[n-1].
        
        val0 = nums[0]
        val_n_minus_1 = nums[n-1]

        count_val0_in_subarrays = 0
        count_val_n_minus_1_in_subarrays = 0

        # Iterate through all possible starting indices for subarrays of size k
        # There are (n - k + 1) such subarrays.
        for i in range(n - k + 1):
            current_subarray = nums[i : i + k] # Get the current subarray
            
            # Check if val0 is present in this subarray
            if val0 in current_subarray:
                count_val0_in_subarrays += 1
            
            # Check if val_n_minus_1 is present in this subarray
            # Note: If val0 == val_n_minus_1, both counters will track the same value's occurrences.
            # This is handled correctly when checking the counts later.
            if val_n_minus_1 in current_subarray:
                count_val_n_minus_1_in_subarrays += 1
        
        max_almost_missing = -1

        # If val0 appeared in exactly one subarray, it's a candidate
        if count_val0_in_subarrays == 1:
            max_almost_missing = max(max_almost_missing, val0)
        
        # If val_n_minus_1 appeared in exactly one subarray, it's a candidate
        if count_val_n_minus_1_in_subarrays == 1:
            max_almost_missing = max(max_almost_missing, val_n_minus_1)

        return max_almost_missing

```

## Why This Works
The solution's correctness hinges on efficiently categorizing and handling the three distinct relationships between `k` and `n`. For the trivial cases where `k=n` or `k=1`, the problem simplifies to finding the maximum element or the maximum unique element, respectively. The crucial insight, derived from the problem's structure and hints, lies in the `1 < k < n` case: only the elements at the very beginning (`nums[0]`) and very end (`nums[n-1]`) of the original array can possibly appear in exactly one subarray of size `k`. Any element `nums[i]` where `0 < i < n-1` will inevitably be part of at least two distinct `k`-sized subarrays. By focusing the counting effort solely on `nums[0]` and `nums[n-1]` across all `k`-sized subarrays, we drastically reduce the search space and efficiently identify the largest "almost missing" integer.

---
<sub>Generated 2026-08-18 02:00 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
