# [3513] Number of Unique XOR Triplets I

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-07-23 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/number-of-unique-xor-triplets-i/)

**Topics:** Array, Math, Bit Manipulation

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums of length n, where nums is a permutation of the numbers in the range [1, n].

A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.

Return the number of unique XOR triplet values from all possible triplets (i, j, k).

Example 1:

Input: nums = [1,2]

Output: 2

Explanation:

The possible XOR triplet values are:

- (0, 0, 0) → 1 XOR 1 XOR 1 = 1

- (0, 0, 1) → 1 XOR 1 XOR 2 = 2

- (0, 1, 1) → 1 XOR 2 XOR 2 = 1

- (1, 1, 1) → 2 XOR 2 XOR 2 = 2

The unique XOR values are {1, 2}, so the output is 2.

Example 2:

Input: nums = [3,1,2]

Output: 4

Explanation:

The possible XOR triplet values include:

- (0, 0, 0) → 3 XOR 3 XOR 3 = 3

- (0, 0, 1) → 3 XOR 3 XOR 1 = 1

- (0, 0, 2) → 3 XOR 3 XOR 2 = 2

- (0, 1, 2) → 3 XOR 1 XOR 2 = 0

The unique XOR values are {0, 1, 2, 3}, so the output is 4.

Constraints:

- 1 <= n == nums.length <= 10^5

- 1 <= nums[i] <= n

- nums is a permutation of integers from 1 to n.

**Examples / sample tests:**

```
[1,2]
[3,1,2]
```

---

## Problem Summary
You are given an integer array `nums` of length `n`, which is a permutation of numbers from `1` to `n`. The goal is to find the total count of **unique** values that can be obtained by taking the XOR sum of three elements `nums[i] XOR nums[j] XOR nums[k]`, where indices `i, j, k` can be the same or different, as long as `i <= j <= k`.

## Intuition
The problem asks for the number of unique XOR sums of three elements from `nums`, allowing repetition. Since `nums` is a permutation of `[1, n]`, the actual values we can pick from are simply the integers `1, 2, ..., n`.

The `i <= j <= k` constraint means we can pick the same element multiple times from the array. Let's analyze the types of XOR sums possible:
*   **Picking the same element three times:** `nums[x] ^ nums[x] ^ nums[x] = nums[x]`. This implies that all numbers from `1` to `n` are guaranteed to be possible XOR sums.
*   **Picking one element twice and another once:** `nums[x] ^ nums[x] ^ nums[y] = nums[y]` (for `x != y`). This again confirms that all numbers from `1` to `n` are possible XOR sums.
*   **Picking three distinct elements:** `nums[x] ^ nums[y] ^ nums[z]`. These can produce new values, including `0` (e.g., `1^2^3 = 0` if `n >= 3`).

The core insight comes from the official hints: for `n >= 3`, the set of unique XOR sums of three elements from `{1, ..., n}` (with replacement) covers *all* integers from `0` up to `2^(K+1) - 1`. Here, `K` is the index of the most significant bit (MSB) of `n` (i.e., `floor(log2(n))`). This is a powerful mathematical property of XOR sums over a sufficiently dense set of integers. For smaller `n` (1 or 2), this property doesn't fully hold, so these cases must be handled separately.

## Approach
The solution relies on recognizing and applying a specific mathematical property of XOR sums over the set of integers `[1, n]`.

1.  **Handle Base Cases:**
    *   If `n` (the length of `nums`) is `1`:
        *   `nums = [1]`. The only possible triplet is `nums[0] ^ nums[0] ^ nums[0] = 1 ^ 1 ^ 1 = 1`.
        *   The set of unique XOR values is `{1}`.
        *   Return `1`.
    *   If `n` is `2`:
        *   `nums = [1, 2]`.
        *   Possible XOR sums: `1^1^1=1`, `1^1^2=2`, `1^2^2=1`, `2^2^2=2`.
        *   The set of unique XOR values is `{1, 2}`.
        *   Return `2`.

2.  **Handle General Case (`n >= 3`):**
    *   For `n >= 3`, it's a known property (as stated in the hints) that we can generate all integers from `0` up to `2^(K+1) - 1`, where `K` is the index of the most significant bit (MSB) of `n`.
    *   The index of the MSB of `n` can be found using `n.bit_length() - 1`. Let `K = n.bit_length() - 1`.
        *   For example:
            *   If `n = 3` (binary `11`), `3.bit_length()` is `2`. So `K = 2 - 1 = 1`.
            *   If `n = 4` (binary `100`), `4.bit_length()` is `3`. So `K = 3 - 1 = 2`.
            *   If `n = 7` (binary `111`), `7.bit_length()` is `3`. So `K = 3 - 1 = 2`.
    *   The range of unique XOR values is `[0, 2^(K+1) - 1]`.
    *   The total count of numbers in this range is `(2^(K+1) - 1) - 0 + 1`, which simplifies to `2^(K+1)`.
    *   This value can be calculated efficiently using a left bit shift: `1 << (K + 1)`.

## Visualization
This problem's solution is based on a mathematical property, so a traditional algorithm diagram isn't applicable. Instead, we can visualize the range of numbers covered by the XOR sums.

Let `K = n.bit_length() - 1` (the index of the most significant bit of `n`).

**Case: n = 1**
`nums = [1]`
Possible XORs: `1^1^1 = 1`
Unique values: `{1}`
Count: 1

**Case: n = 2**
`nums = [1, 2]`
Possible XORs: `1^1^1=1`, `1^1^2=2`, `1^2^2=1`, `2^2^2=2`
Unique values: `{1, 2}`
Count: 2

**Case: n = 3**
`nums = [1, 2, 3]` (or any permutation like `[3,1,2]`)
`n = 3` (binary `11_2`). `K = 3.bit_length() - 1 = 2 - 1 = 1`.
The property states we can generate all numbers in `[0, 2^(K+1) - 1] = [0, 2^(1+1) - 1] = [0, 2^2 - 1] = [0, 3]`.
This range includes `{0, 1, 2, 3}`.
Count: `2^(K+1) = 2^(1+1) = 2^2 = 4`.

```
n=3, K=1
Range of values: [0, 2^(K+1)-1] = [0, 3]
    
0   1   2   3
^   ^   ^   ^
|   |   |   |
-----------------> Number Line
All values in this range are reachable.
Total count = 4.
```

**Case: n = 7**
`nums = [1, 2, 3, 4, 5, 6, 7]`
`n = 7` (binary `111_2`). `K = 7.bit_length() - 1 = 3 - 1 = 2`.
The property states we can generate all numbers in `[0, 2^(K+1) - 1] = [0, 2^(2+1) - 1] = [0, 2^3 - 1] = [0, 7]`.
This range includes `{0, 1, 2, 3, 4, 5, 6, 7}`.
Count: `2^(K+1) = 2^(2+1) = 2^3 = 8`.

```
n=7, K=2
Range of values: [0, 2^(K+1)-1] = [0, 7]
    
0   1   2   3   4   5   6   7
^   ^   ^   ^   ^   ^   ^   ^
|   |   |   |   |   |   |   |
---------------------------------> Number Line
All values in this range are reachable.
Total count = 8.
```

## Dry Run

Let's walk through **Example 1: `nums = [1, 2]`**

1.  **Input:** `nums = [1, 2]`
2.  **Determine `n`:** `n = len(nums) = 2`.
3.  **Check Base Cases:**
    *   Is `n == 1`? No, `2 != 1`.
    *   Is `n == 2`? Yes, `2 == 2`.
4.  **Apply `n=2` logic:** The function returns `2`.

**Final Result for Example 1:** `2`.

---

Let's walk through **Example 2: `nums = [3, 1, 2]`**

1.  **Input:** `nums = [3, 1, 2]`
2.  **Determine `n`:** `n = len(nums) = 3`.
3.  **Check Base Cases:**
    *   Is `n == 1`? No, `3 != 1`.
    *   Is `n == 2`? No, `3 != 2`.
4.  **Apply General Case (`n >= 3`) logic:**
    *   Calculate `K = n.bit_length() - 1`.
        *   `n = 3`.
        *   Binary representation of `3` is `11_2`.
        *   `3.bit_length()` (number of bits needed) is `2`.
        *   `K = 2 - 1 = 1`.
    *   Calculate the result: `1 << (K + 1)`.
        *   `K + 1 = 1 + 1 = 2`.
        *   `1 << 2` is `2^2 = 4`.
5.  **Return:** `4`.

**Final Result for Example 2:** `4`.

## Complexity
*   **Time Complexity:** `O(1)`. The solution involves a few comparisons and bit manipulation operations (`len()`, `.bit_length()`, `<<`), all of which take constant time regardless of the input size `n`.
*   **Space Complexity:** `O(1)`. No additional data structures are used that scale with the input size `n`.

## Edge Cases
*   **`n = 1`:** `nums = [1]`. This is handled by the `n == 1` base case, returning `1`. This is correct as `1^1^1 = 1` is the only possible XOR sum.
*   **`n = 2`:** `nums = [1, 2]`. This is handled by the `n == 2` base case, returning `2`. This is correct as the unique XOR sums are `{1, 2}`.
*   **`n = 3`:** `nums = [1, 2, 3]` (or any permutation). This falls into the general case. `3.bit_length() - 1 = 1`. The result is `1 << (1+1) = 4`. This is correct, as shown in Example 2.
*   **`n` is a power of 2 (e.g., `n=4`):** `nums = [1, 2, 3, 4]`. This falls into the general case. `4.bit_length() - 1 = 2`. The result is `1 << (2+1) = 8`. This is correct, as the range `[0, 7]` has 8 unique values.
*   **Maximum `n` (`n = 10^5`):** `10^5` in binary is `11000011010100000_2`. `100000.bit_length()` is `17`. So `K = 17 - 1 = 16`. The result is `1 << (16+1) = 1 << 17 = 131072`. This calculation is constant time and fits within standard integer types.

The solution correctly handles all specified constraints and edge cases.

## Solution
```python
from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        # Base cases for n = 1 and n = 2.
        # The general mathematical property for XOR sums (described below)
        # does not fully apply to these small values of n.
        if n == 1:
            # If nums = [1], the only possible triplet is (0,0,0) -> nums[0]^nums[0]^nums[0] = 1^1^1 = 1.
            # The set of unique XOR values is {1}.
            return 1
        elif n == 2:
            # If nums = [1, 2], the possible XOR sums are:
            # 1^1^1 = 1
            # 1^1^2 = 2
            # 1^2^2 = 1
            # 2^2^2 = 2
            # The set of unique XOR values is {1, 2}.
            return 2
        else:
            # For n >= 3, a known property (as hinted in the problem) states that
            # all integers from 0 up to (2^(K+1) - 1) can be formed as XOR sums
            # of three elements from the set {1, ..., n} (with replacement).
            # Here, K is the index of the most significant bit (MSB) of n.
            
            # K can be calculated as n.bit_length() - 1.
            # For example:
            # n = 3 (binary 11) -> bit_length = 2 -> K = 1
            # n = 4 (binary 100) -> bit_length = 3 -> K = 2
            # n = 7 (binary 111) -> bit_length = 3 -> K = 2
            
            msb_index = n.bit_length() - 1
            
            # The range of unique XOR values is [0, 2^(msb_index + 1) - 1].
            # The total count of numbers in this contiguous range is:
            # (maximum_value - minimum_value + 1)
            # = (2^(msb_index + 1) - 1) - 0 + 1
            # = 2^(msb_index + 1)
            
            # This can be computed efficiently using a left bit shift: 1 << (exponent).
            return 1 << (msb_index + 1)

```

## Why This Works
The solution leverages a specific mathematical property related to XOR sums. For a set of integers `S = {1, 2, ..., n}`, if `n` is sufficiently large (specifically, `n >= 3`), it's possible to generate all non-negative integers up to a certain maximum value by taking XOR sums of three elements from `S` (with replacement). This maximum value is `2^(K+1) - 1`, where `K` is the index of the most significant bit of `n`. This property arises from the fact that the set `{1, 2, ..., n}`, when `n >= 3`, contains enough "basis" elements (like `1, 2, 3`) to form a generating set for all numbers up to the next power of two beyond `n`. The base cases `n=1` and `n=2` are too small for this general property to hold, as their limited elements restrict the possible XOR sums, so they are handled separately by direct observation of their unique XOR values.

---
<sub>Generated 2026-07-23 03:57 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
