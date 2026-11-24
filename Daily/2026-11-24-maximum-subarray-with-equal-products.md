# [3411] Maximum Subarray With Equal Products

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-11-24 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximum-subarray-with-equal-products/)

**Topics:** Array, Math, Sliding Window, Enumeration, Number Theory

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an array of positive integers nums.

An array arr is called product equivalent if prod(arr) == lcm(arr) * gcd(arr), where:

- prod(arr) is the product of all elements of arr.

- gcd(arr) is the GCD of all elements of arr.

- lcm(arr) is the LCM of all elements of arr.

Return the length of the longest product equivalent subarray of nums.

Example 1:

Input: nums = [1,2,1,2,1,1,1]

Output: 5

Explanation:

The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1, 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.

Example 2:

Input: nums = [2,3,4,5,6]

Output: 3

Explanation:

The longest product equivalent subarray is [3, 4, 5].

Example 3:

Input: nums = [1,2,3,1,4,5,1]

Output: 5

Constraints:

- 2 <= nums.length <= 100

- 1 <= nums[i] <= 10

**Examples / sample tests:**

```
[1,2,1,2,1,1,1]
[2,3,4,5,6]
[1,2,3,1,4,5,1]
```

---

## Problem Summary
The goal is to find the longest contiguous subarray within a given array `nums` that satisfies a specific "product equivalent" condition. This condition states that the product of all elements in the subarray must equal the product of their least common multiple (LCM) and greatest common divisor (GCD).

## Intuition
The core of this problem lies in understanding the mathematical property `prod(arr) == lcm(arr) * gcd(arr)`. Let's break down numbers into their prime factorizations. For any number `x = p1^a * p2^b * ...`, its prime factors `p1, p2, ...` have certain exponents `a, b, ...`.

For a subarray `arr = [x1, x2, ..., xk]`, let's consider a single prime `p`. Let the exponents of `p` in `x1, x2, ..., xk` be `e1, e2, ..., ek`.
Then:
- The exponent of `p` in `prod(arr)` is `sum(e1, e2, ..., ek)`.
- The exponent of `p` in `lcm(arr)` is `max(e1, e2, ..., ek)`.
- The exponent of `p` in `gcd(arr)` is `min(e1, e2, ..., ek)`.

For `prod(arr) == lcm(arr) * gcd(arr)` to hold, the exponents for each prime `p` must satisfy:
`sum(e1, e2, ..., ek) == max(e1, e2, ..., ek) + min(e1, e2, ..., ek)`

Let's sort the exponents for a prime `p`: `e_{(1)} <= e_{(2)} <= ... <= e_{(k)}`.
Then `min(e_i) = e_{(1)}` and `max(e_i) = e_{(k)}`.
The condition becomes: `e_{(1)} + e_{(2)} + ... + e_{(k)} == e_{(1)} + e_{(k)}`.
This simplifies to: `e_{(2)} + e_{(3)} + ... + e_{(k-1)} == 0`.

Since all exponents `e_i` must be non-negative (as `nums` contains positive integers), this implies that `e_{(2)} = 0`, `e_{(3)} = 0`, ..., `e_{(k-1)} = 0`.
This is a very strong condition! It means that for any prime `p`, at most two numbers in the subarray can have a non-zero exponent for `p`. In other words, at most two numbers in the subarray can be divisible by `p`. All other numbers in the subarray (if any) must not be divisible by `p`.

Given the constraint `nums[i] <= 10`, the only primes we need to consider are 2, 3, 5, and 7.
So, the problem transforms into finding the longest subarray `arr` such that for each prime `p` in {2, 3, 5, 7}, the exponents of `p` in `arr` satisfy `e_{(2)} = ... = e_{(k-1)} = 0`.

This is a classic **sliding window** problem. We can maintain a window `[left, right]` and for each prime, track the exponents of numbers within this window. When the condition is violated, we shrink the window from the `left`.

## Approach
1.  **Precomputation:** Since `nums[i]` is small (up to 10), we can precompute the prime factorization (specifically, the exponents for primes 2, 3, 5, 7) for each number from 1 to 10. This will speed up exponent retrieval.
    *   Example: `PRECOMPUTED_EXPS[6]` would be `{2: 1, 3: 1, 5: 0, 7: 0}`.

2.  **Sliding Window Initialization:**
    *   Initialize `max_len = 0` to store the length of the longest valid subarray.
    *   Initialize `left = 0` as the left pointer of the sliding window.
    *   Create a dictionary `prime_exponents_lists`. For each prime `p` in {2, 3, 5, 7}, this dictionary will store a list of all `p`-exponents for numbers currently within the window `[left, right]`.
        *   Example: If the window is `[2, 4, 6]`, then `prime_exponents_lists[2]` would be `[1, 2, 1]` (exponents of 2 in 2, 4, and 6 respectively).

3.  **Window Expansion (Right Pointer):**
    *   Iterate `right` from `0` to `len(nums) - 1`.
    *   For each `nums[right]`:
        *   Retrieve its precomputed prime exponents.
        *   For each prime `p`, append the exponent of `p` from `nums[right]` to `prime_exponents_lists[p]`. This effectively adds `nums[right]` to the window.

4.  **Window Shrinking (Left Pointer):**
    *   After adding `nums[right]`, the window `[left, right]` might no longer be product equivalent.
    *   Use a `while` loop to check if the current window is valid using the `is_window_product_equivalent` helper function (described below).
    *   If the window is *not* valid:
        *   Retrieve the precomputed prime exponents for `nums[left]`.
        *   For each prime `p`, remove the corresponding exponent from `prime_exponents_lists[p]`. (Python's `list.remove(value)` removes the *first occurrence* of `value`, which is exactly what we need since we add/remove elements in order).
        *   Increment `left` to shrink the window.

5.  **Update Maximum Length:**
    *   Once the `while` loop finishes, the current window `[left, right]` is guaranteed to be product equivalent.
    *   Update `max_len = max(max_len, right - left + 1)`.

6.  **Return Result:** After iterating through all `right` positions, `max_len` will hold the length of the longest product equivalent subarray.

### Helper Function: `is_window_product_equivalent()`
This function checks if the current window (represented by `prime_exponents_lists`) satisfies the condition: `sum(e_i) == max(e_i) + min(e_i)` for all primes.
*   For each prime `p` in {2, 3, 5, 7}:
    *   Get `exps_p = prime_exponents_lists[p]`.
    *   If `exps_p` is empty, it means no numbers in the window are divisible by `p`, so the condition is trivially met for this prime. Continue to the next prime.
    *   Calculate `sum_exps = sum(exps_p)`, `min_exps = min(exps_p)`, `max_exps = max(exps_p)`.
    *   If `sum_exps != min_exps + max_exps`, then the window is not product equivalent. Return `False`.
*   If all primes satisfy the condition, return `True`.

## Visualization

Let's trace `nums = [1,2,1,2,1,1,1]` with the sliding window.
`PRIMES = [2,3,5,7]`
`PRECOMPUTED_EXPS[1]={2:0,..}, PRECOMPUTED_EXPS[2]={2:1,..}`

```
nums = [1, 2, 1, 2, 1, 1, 1]
        ^                    
        left=0, right=-1, max_len=0
        prime_exponents_lists = {2:[], 3:[], 5:[], 7:[]}

right = 0, nums[0] = 1:
  add(1) -> prime_exponents_lists[2] = [0]
  is_valid() -> True (sum=0, min=0, max=0 for p=2)
  max_len = max(0, 0-0+1) = 1
  Window: [1]
          ^
          left=0

right = 1, nums[1] = 2:
  add(2) -> prime_exponents_lists[2] = [0, 1]
  is_valid() -> True (sum=1, min=0, max=1 for p=2)
  max_len = max(1, 1-0+1) = 2
  Window: [1, 2]
          ^  ^
          left=0

right = 2, nums[2] = 1:
  add(1) -> prime_exponents_lists[2] = [0, 1, 0]
  is_valid() -> True (sum=1, min=0, max=1 for p=2)
  max_len = max(2, 2-0+1) = 3
  Window: [1, 2, 1]
          ^     ^
          left=0

right = 3, nums[3] = 2:
  add(2) -> prime_exponents_lists[2] = [0, 1, 0, 1]
  is_valid() -> False (for p=2: sum=2, min=0, max=1. 2 != 0+1)
  
  WHILE not is_valid():
    remove(nums[left=0]=1) -> prime_exponents_lists[2] = [1, 0, 1] (removed first 0)
    left = 1
    Window: [2, 1, 2]
             ^     ^
             left=1
    is_valid() -> False (for p=2: sum=2, min=0, max=1. 2 != 0+1)

    remove(nums[left=1]=2) -> prime_exponents_lists[2] = [0, 1] (removed first 1)
    left = 2
    Window: [1, 2]
                ^  ^
                left=2
    is_valid() -> True (for p=2: sum=1, min=0, max=1)
  
  max_len = max(3, 3-2+1) = max(3, 2) = 3
  
right = 4, nums[4] = 1:
  add(1) -> prime_exponents_lists[2] = [0, 1, 0]
  is_valid() -> True
  max_len = max(3, 4-2+1) = max(3, 3) = 3
  Window: [1, 2, 1]
                ^     ^
                left=2

right = 5, nums[5] = 1:
  add(1) -> prime_exponents_lists[2] = [0, 1, 0, 0]
  is_valid() -> True
  max_len = max(3, 5-2+1) = max(3, 4) = 4
  Window: [1, 2, 1, 1]
                ^        ^
                left=2

right = 6, nums[6] = 1:
  add(1) -> prime_exponents_lists[2] = [0, 1, 0, 0, 0]
  is_valid() -> True
  max_len = max(4, 6-2+1) = max(4, 5) = 5
  Window: [1, 2, 1, 1, 1]
                ^           ^
                left=2

End of loop. Return max_len = 5.
```

## Dry Run
Let's walk through Example 1: `nums = [1,2,1,2,1,1,1]`

| `right` | `nums[right]` | `prime_exponents_lists[2]` (simplified) | `is_valid()` | `left` (after shrink) | `Current Window` | `Current Length` | `max_len` |
| :------ | :------------ | :-------------------------------------- | :----------- | :-------------------- | :--------------- | :--------------- | :-------- |
| -       | -             | `[]`                                    | -            | 0                     | `[]`             | 0                | 0         |
| 0       | 1             | `[0]`                                   | True         | 0                     | `[1]`            | 1                | 1         |
| 1       | 2             | `[0, 1]`                                | True         | 0                     | `[1,2]`          | 2                | 2         |
| 2       | 1             | `[0, 1, 0]`                             | True         | 0                     | `[1,2,1]`        | 3                | 3         |
| 3       | 2             | `[0, 1, 0, 1]`                          | False        |                       | `[1,2,1,2]`      | -                | 3         |
|         | **Shrink**    | `[1, 0, 1]` (removed `nums[0]=1`'s 0)  | False        | 1                     | `[2,1,2]`        | -                | 3         |
|         | **Shrink**    | `[0, 1]` (removed `nums[1]=2`'s 1)     | True         | 2                     | `[1,2]`          | 2                | 3         |
| 4       | 1             | `[0, 1, 0]`                             | True         | 2                     | `[1,2,1]`        | 3                | 3         |
| 5       | 1             | `[0, 1, 0, 0]`                          | True         | 2                     | `[1,2,1,1]`      | 4                | 4         |
| 6       | 1             | `[0, 1, 0, 0, 0]`                       | True         | 2                     | `[1,2,1,1,1]`    | 5                | 5         |

Final Result: `max_len = 5`. This matches the example output.

## Complexity
*   **Time Complexity:** `O(N^2)`
    *   The outer loop iterates `N` times (for `right`).
    *   Inside the outer loop, `add_to_window` takes `O(NumPrimes)` time (constant, 4 primes).
    *   The `while` loop for shrinking the window runs at most `N` times in total across all `right` iterations (amortized `O(N)` for `left` pointer movement).
    *   Inside the `while` loop, `remove_from_window` takes `O(NumPrimes * K)` where `K` is the current window size (up to `N`), because `list.remove()` can take `O(K)` time.
    *   `is_window_product_equivalent` takes `O(NumPrimes * K)` time, as it iterates through primes and then through `K` exponents for each prime.
    *   Therefore, the worst-case time complexity is `O(N * (NumPrimes + NumPrimes * N))`, which simplifies to `O(N^2)` since `NumPrimes` is a constant.
    *   Given `N <= 100`, `N^2 = 10000`, which is perfectly acceptable.

*   **Space Complexity:** `O(N)`
    *   `prime_exponents_lists` stores lists of exponents. In the worst case, each list can contain up to `N` elements (e.g., if all numbers are divisible by 2). Since there are `NumPrimes` such lists, the total space is `O(NumPrimes * N)`, which simplifies to `O(N)`.
    *   `PRECOMPUTED_EXPS` stores a constant number of dictionaries (10 entries), each of constant size (4 primes), so it's `O(1)`.

## Edge Cases
1.  **All 1s:** `nums = [1, 1, 1, 1]`.
    *   All numbers have 0 exponents for all primes. `prime_exponents_lists` will contain lists of zeros.
    *   `is_window_product_equivalent()` will always return `True` (sum=0, min=0, max=0).
    *   The window will never shrink. `max_len` will become `len(nums)`. Correct.

2.  **All same non-1 numbers:** `nums = [2, 2, 2]`.
    *   `[2]` is valid (`max_len=1`).
    *   `[2, 2]` is valid (`p=2` exponents `[1,1]`, sum=2, min=1, max=1. `2 == 1+1`. `max_len=2`).
    *   `[2, 2, 2]` is invalid (`p=2` exponents `[1,1,1]`, sum=3, min=1, max=1. `3 != 1+1`).
    *   The window shrinks to `[2, 2]`. `max_len` remains 2. Correct.

3.  **Minimum length array:** `nums = [2, 3]`.
    *   `right=0, num=2`: `[2]`. `p2_exps=[1]`. Valid. `max_len=1`.
    *   `right=1, num=3`: `[2,3]`. `p2_exps=[1,0]`, `p3_exps=[0,1]`. Valid. `max_len=2`.
    *   Correct.

The solution handles these cases correctly due to the robust mathematical condition and the sliding window mechanism.

## Solution

```python
import collections
from typing import List

class Solution:
    # Precompute prime exponents for numbers 1 to 10.
    # This map stores for each number `n`, a dictionary of its prime exponents.
    # E.g., PRECOMPUTED_EXPS[6] = {2: 1, 3: 1, 5: 0, 7: 0}
    PRECOMPUTED_EXPS = {}
    PRIMES = [2, 3, 5, 7]

    @classmethod
    def _precompute_exponents(cls):
        """
        Precomputes prime exponents for numbers 1-10.
        This method is called once to populate PRECOMPUTED_EXPS.
        """
        if not cls.PRECOMPUTED_EXPS: # Only precompute once
            for i in range(1, 11):
                exps = {p: 0 for p in cls.PRIMES}
                temp = i

---
<sub>Generated 2026-11-24 10:20 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
