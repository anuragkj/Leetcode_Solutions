# [3514] Number of Unique XOR Triplets II

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-07-24 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/number-of-unique-xor-triplets-ii/)

**Topics:** Array, Math, Bit Manipulation, Enumeration

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums.

A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.

Return the number of unique XOR triplet values from all possible triplets (i, j, k).

Example 1:

Input: nums = [1,3]

Output: 2

Explanation:

The possible XOR triplet values are:

	(0, 0, 0) → 1 XOR 1 XOR 1 = 1
	(0, 0, 1) → 1 XOR 1 XOR 3 = 3
	(0, 1, 1) → 1 XOR 3 XOR 3 = 1
	(1, 1, 1) → 3 XOR 3 XOR 3 = 3

The unique XOR values are {1, 3}. Thus, the output is 2.

Example 2:

Input: nums = [6,7,8,9]

Output: 4

Explanation:

The possible XOR triplet values are {6, 7, 8, 9}. Thus, the output is 4.

Constraints:

- 1 <= nums.length <= 1500

- 1 <= nums[i] <= 1500

**Examples / sample tests:**

```
[1,3]
[6,7,8,9]
```

---

## Problem Summary
Given an array of integers `nums`, we need to find the number of **unique** XOR triplet values. A XOR triplet is defined as `nums[i] XOR nums[j] XOR nums[k]` where the indices satisfy `i <= j <= k`.

## Intuition
The problem asks for the count of *unique* XOR values, which immediately suggests using a `set` data structure to store the results and then returning its size.

A naive approach would involve three nested loops (`i`, `j`, `k`) to generate all triplets, leading to an `O(N^3)` time complexity. Given `N <= 1500`, `N^3` is too slow (`1500^3 ≈ 3.4 * 10^9`). We need a more efficient way to enumerate the unique XOR values.

Let's analyze the triplet `nums[i] XOR nums[j] XOR nums[k]` with the constraint `i <= j <= k`. We can iterate through the array, fixing one of the indices and building up possibilities. A common strategy for `i <= j <= k` problems is to fix the rightmost index, `k`, and then consider how `i` and `j` relate to `k`.

When we fix `k`:
1.  **Case 1: `j = k`**. The triplet becomes `nums[i] XOR nums[k] XOR nums[k]`. Since `X XOR X = 0`, this simplifies to `nums[i]`. For all `i` such that `i <= k`, `nums[i]` is a possible XOR triplet value.
2.  **Case 2: `j < k`**. The triplet is `nums[i] XOR nums[j] XOR nums[k]`. Here, `i <= j < k`. If we already know all possible unique `nums[i] XOR nums[j]` values for `i <= j < k`, we can simply XOR each of these with `nums[k]` to get new triplet values.

This observation leads to a dynamic programming-like approach: as we iterate `k` from `0` to `n-1`, we maintain a set of all unique `nums[x] XOR nums[y]` values where `x <= y < k`. Let's call this `current_pair_xors`.

## Approach
The optimal approach involves iterating through the array with `k` as the rightmost index of the triplet, and dynamically updating a set of previously seen pair XORs.

1.  Initialize an empty set, `all_triplet_xors`, to store all unique XOR values found. This will be our final result.
2.  Initialize another empty set, `current_pair_xors`, to store all unique `nums[x] XOR nums[y]` values where `x <= y` and `y` is less than the current `k`. This set will be updated in each iteration.
3.  Iterate `k` from `0` to `len(nums) - 1`:
    a.  Create a temporary empty set, `new_pairs_for_k`. This set will collect all `nums[i] XOR nums[k]` values for the current `k` (where `i <= k`). These are new pairs formed with `nums[k]`.
    b.  **Handle triplets where `j = k`**: Iterate `i` from `0` to `k`.
        *   Calculate `pair_xor = nums[i] XOR nums[k]`. Add this `pair_xor` to `new_pairs_for_k`.
        *   The triplet value for `(i, k, k)` is `nums[i] XOR nums[k] XOR nums[k]`, which simplifies to `nums[i]`. Add `nums[i]` to `all_triplet_xors`.
    c.  **Handle triplets where `j < k`**: Iterate through each `prev_pair_xor` in `current_pair_xors`.
        *   For each `prev_pair_xor`, calculate `triplet_xor = prev_pair_xor XOR nums[k]`. Add this `triplet_xor` to `all_triplet_xors`.
    d.  **Update `current_pair_xors`**: After processing all triplets for the current `k`, update `current_pair_xors` by adding all elements from `new_pairs_for_k` to it. This ensures `current_pair_xors` now contains all unique `nums[x] XOR nums[y]` values where `x <= y <= k`, ready for the next iteration `k+1`.
4.  Finally, return the size of `all_triplet_xors`.

## Visualization

Let's trace the process with `nums = [A, B, C, D]`.

```
Initial:
  all_triplet_xors = {}
  current_pair_xors = {}  (stores nums[x]^nums[y] for x <= y < k)

k = 0 (nums[0] = A):
  new_pairs_for_k = {}
  
  // Handle j=k: i=0
  i=0: nums[0]^nums[0] = A^A = 0. Add 0 to new_pairs_for_k.
       Triplet (0,0,0) is nums[0]^nums[0]^nums[0] = A. Add A to all_triplet_xors.
  
  // Handle j<k: current_pair_xors is empty. No triplets of this type.
  
  // Update current_pair_xors
  current_pair_xors.update(new_pairs_for_k) => current_pair_xors = {0}
  all_triplet_xors = {A}

--------------------------------------------------------------------------------

k = 1 (nums[1] = B):
  new_pairs_for_k = {}
  
  // Handle j=k: i=0, 1
  i=0: nums[0]^nums[1] = A^B. Add A^B to new_pairs_for_k.
       Triplet (0,1,1) is nums[0]^nums[1]^nums[1] = A. Add A to all_triplet_xors.
  i=1: nums[1]^nums[1] = B^B = 0. Add 0 to new_pairs_for_k.
       Triplet (1,1,1) is nums[1]^nums[1]^nums[1] = B. Add B to all_triplet_xors.
  
  // Handle j<k: current_pair_xors = {0}
  For prev_pair_xor in {0}:
    prev_pair_xor = 0: 0^nums[1] = 0^B = B. Add B to all_triplet_xors.
  
  // Update current_pair_xors
  current_pair_xors.update(new_pairs_for_k) => current_pair_xors = {0, A^B}
  all_triplet_xors = {A, B}

--------------------------------------------------------------------------------

k = 2 (nums[2] = C):
  new_pairs_for_k = {}
  
  // Handle j=k: i=0, 1, 2
  i=0: nums[0]^nums[2] = A^C. Add A^C to new_pairs_for_k.
       Triplet (0,2,2) is nums[0]^nums[2]^nums[2] = A. Add A to all_triplet_xors.
  i=1: nums[1]^nums[2] = B^C. Add B^C to new_pairs_for_k.
       Triplet (1,2,2) is nums[1]^nums[2]^nums[2] = B. Add B to all_triplet_xors.
  i=2: nums[2]^nums[2] = C^C = 0. Add 0 to new_pairs_for_k.
       Triplet (2,2,2) is nums[2]^nums[2]^nums[2] = C. Add C to all_triplet_xors.
  
  // Handle j<k: current_pair_xors = {0, A^B}
  For prev_pair_xor in {0, A^B}:
    prev_pair_xor = 0: 0^nums[2] = 0^C = C. Add C to all_triplet_xors.
    prev_pair_xor = A^B: (A^B)^nums[2] = (A^B)^C. Add (A^B)^C to all_triplet_xors.
  
  // Update current_pair_xors
  current_pair_xors.update(new_pairs_for_k) => current_pair_xors = {0, A^B, A^C, B^C}
  all_triplet_xors = {A, B, C, (A^B)^C}

... and so on for k=3.
```

## Dry Run
Let's walk through Example 1: `nums = [1, 3]`

Initial state: `all_triplet_xors = set()`, `current_pair_xors = set()`

| `k` | `nums[k]` | `i` | `nums[i]` | `pair_xor = nums[i]^nums[k]` | `new_pairs_for_k` (temp) | `current_pair_xors` (before loop over it) | `prev_pair_xor` | `triplet_xor` (`prev_pair_xor^nums[k]`) | `all_triplet_xors` (cumulative) | `current_pair_xors` (after update) |
|-----|-----------|-----|-----------|------------------------------|--------------------------|-------------------------------------------|-----------------|-----------------------------------------|-----------------------------------|------------------------------------|
| **0** | **1**     |     |           |                              | `{}`                     | `{}`                                      |                 |                                         | `{}`                              | `{}`                               |
|     |           | 0   | 1         | `1^1 = 0`                    | `{0}`                    |                                           |                 |                                         | `{1}` (from `nums[i]`)            |                                    |
|     |           |     |           |                              |                          | `{}`                                      | (empty)         |                                         | `{1}`                             | `{0}` (updated)                    |
| **1** | **3**     |     |           |                              | `{}`                     | `{0}`                                     |                 |                                         | `{1}`                             | `{0}`                              |
|     |           | 0   | 1         | `1^3 = 2`                    | `{2}`                    |                                           |                 |                                         | `{1, 3}` (from `nums[i]`)         |                                    |
|     |           | 1   | 3         | `3^3 = 0`                    | `{2, 0}`                 |                                           |                 |                                         | `{1, 3}` (from `nums[i]`)         |                                    |
|     |           |     |           |                              |                          | `{0}`                                     | `0`             | `0^3 = 3`                               | `{1, 3}`                          |                                    |
|     |           |     |           |                              |                          |                                           |                 |                                         | `{1, 3}`                          | `{0, 2}` (updated)                 |

After iterating through all `k` values, `all_triplet_xors` contains `{1, 3}`.
The final result is `len(all_triplet_xors) = 2`. This matches Example 1.

## Complexity
*   **Time Complexity**: `O(N * (N + M))`
    *   `N` is the length of `nums`.
    *   `M` is the maximum possible XOR value. Since `nums[i] <= 1500`, the maximum XOR value is less than `2^11 = 2048`. So `M` is approximately 2048.
    *   The outer loop runs `N` times (for `k`).
    *   Inside the outer loop:
        *   The loop for `i` runs `k+1` times (up to `N`).
        *   The loop iterating `current_pair_xors` runs up to `M` times (the maximum size of the set).
        *   Set operations (add, update) take `O(1)` on average for hash sets.
    *   Total time: `N * (O(N) + O(M)) = O(N^2 + N*M)`. Given `N=1500` and `M=2048`, this is `1500 * (1500 + 2048) = 1500 * 3548 ≈ 5.3 * 10^6` operations, which is efficient enough.

*   **Space Complexity**: `O(M)`
    *   `all_triplet_xors` stores up to `M` unique XOR values.
    *   `current_pair_xors` stores up to `M` unique XOR values.
    *   `new_pairs_for_k` also stores up to `M` unique XOR values.
    *   Since `M` is small (approx 2048), this is `O(1)` effectively in terms of typical competitive programming memory limits.

## Edge Cases
*   **`nums.length = 1` (e.g., `nums = [5]`)**:
    *   `k=0, nums[0]=5`.
    *   `i=0, nums[0]=5`. `new_pairs_for_k` gets `5^5=0`. `all_triplet_xors` gets `5`.
    *   `current_pair_xors` is empty.
    *   `current_pair_xors` updates to `{0}`.
    *   Result: `len({5}) = 1`. Correct, as `5 XOR 5 XOR 5 = 5` is the only triplet.
*   **All elements are the same (e.g., `nums = [X, X, X]`)**:
    *   The `nums[i]` part of the `j=k` case will always add `X` to `all_triplet_xors`.
    *   `current_pair_xors` will only ever contain `0` (since `X XOR X = 0`).
    *   The `j<k` case will add `0 XOR X = X` to `all_triplet_xors`.
    *   Result: `len({X}) = 1`. Correct.
*   **All elements are distinct (e.g., `nums = [6, 7, 8, 9]`)**:
    *   The algorithm correctly enumerates all combinations. As shown in the dry run for Example 2 in the thought process, it correctly identifies all 4 unique XOR values.

## Solution

```python
from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # Stores all unique XOR triplet values found so far.
        all_triplet_xors = set()
        
        # Stores all unique nums[x] XOR nums[y] values where x <= y < k.
        # This set is built up as k increases.
        current_pair_xors = set()

        n = len(nums)

        # Iterate k from 0 to n-1. nums[k] is the rightmost element of the triplet.
        for k in range(n):
            # new_pairs_for_k will store nums[i] XOR nums[k] for i <= k.
            # These are the new pairs formed with the current nums[k] that will
            # be added to current_pair_xors for the next iteration.
            new_pairs_for_k = set()

            # Case 1: Triplets where j = k.
            # The triplet XOR is nums[i] XOR nums[k] XOR nums[k], which simplifies to nums[i].
            # Also, populate new_pairs_for_k with all pairs involving nums[k] and nums[i] (i <= k).
            for i in range(k + 1):
                # Add nums[i] to all_triplet_xors (covers triplets (i, k, k))
                all_triplet_xors.add(nums[i])
                
                # Store nums[i] XOR nums[k] for future iterations (as part of current_pair_xors)
                new_pairs_for_k.add(nums[i] ^ nums[k])

            # Case 2: Triplets where i <= j < k.
            # The triplet XOR is (nums[i] XOR nums[j]) XOR nums[k].
            # current_pair_xors already holds all unique nums[i] XOR nums[j] where i <= j < k.
            for prev_pair_xor in current_pair_xors:
                all_triplet_xors.add(prev_pair_xor ^ nums[k])
            
            # Update current_pair_xors for the next iteration (k+1).
            # It now includes all pairs (i, j) where i <= j <= k.
            current_pair_xors.update(new_pairs_for_k)
        
        return len(all_triplet_xors)

```

## Why This Works
The solution systematically enumerates all unique XOR triplet values by iterating through the array with index `k` as the "rightmost" element of the triplet. For each `k`, it considers two exhaustive types of triplets based on the relationship between `j` and `k`:
1.  **Triplets where `j = k`**: These are of the form `nums[i] XOR nums[k] XOR nums[k]`. Due to the property `X XOR X = 0`, this simplifies to `nums[i]`. All such `nums[i]` values (for `i <= k`) are directly added to the `all_triplet_xors` set.
2.  **Triplets where `j < k`**: These are of the form `(nums[i] XOR nums[j]) XOR nums[k]`. The crucial part is that `current_pair_xors` is maintained to contain all unique `nums[x] XOR nums[y]` values where `x <= y < k`. By iterating through `current_pair_xors` and XORing each stored pair value with `nums[k]`, we efficiently generate all unique triplet values for this case.

At the end of each `k` iteration, `current_pair_xors` is updated to include all new pair XORs formed with `nums[k]` (i.e., `nums[i] XOR nums[k]` for `i <= k`). This ensures that for the next iteration `k+1`, `current_pair_xors` correctly holds all unique `nums[x] XOR nums[y]` values where `x <= y <= k`, covering all possibilities for `j < k+1`. The use of sets automatically handles the uniqueness requirement. This systematic enumeration guarantees that all valid triplets are considered exactly once, and their unique XOR values are collected.

---
<sub>Generated 2026-07-24 03:57 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
