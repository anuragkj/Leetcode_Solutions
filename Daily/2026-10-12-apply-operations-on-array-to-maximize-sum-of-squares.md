# [2897] Apply Operations on Array to Maximize Sum of Squares

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-10-12 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/)

**Topics:** Array, Hash Table, Greedy, Bit Manipulation

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 0-indexed integer array nums and a positive integer k.

You can do the following operation on the array any number of times:

- Choose any two distinct indices i and j and simultaneously update the values of nums[i] to (nums[i] AND nums[j]) and nums[j] to (nums[i] OR nums[j]). Here, OR denotes the bitwise OR operation, and AND denotes the bitwise AND operation.

You have to choose k elements from the final array and calculate the sum of their squares.

Return the maximum sum of squares you can achieve.

Since the answer can be very large, return it modulo 10^9 + 7.

Example 1:

Input: nums = [2,6,5,8], k = 2
Output: 261
Explanation: We can do the following operations on the array:
- Choose i = 0 and j = 3, then change nums[0] to (2 AND 8) = 0 and nums[3] to (2 OR 8) = 10. The resulting array is nums = [0,6,5,10].
- Choose i = 2 and j = 3, then change nums[2] to (5 AND 10) = 0 and nums[3] to (5 OR 10) = 15. The resulting array is nums = [0,6,0,15].
We can choose the elements 15 and 6 from the final array. The sum of squares is 15^2 + 6^2 = 261.
It can be shown that this is the maximum value we can get.

Example 2:

Input: nums = [4,5,4,7], k = 3
Output: 90
Explanation: We do not need to apply any operations.
We can choose the elements 7, 5, and 4 with a sum of squares: 7^2 + 5^2 + 4^2 = 90.
It can be shown that this is the maximum value we can get.

Constraints:

- 1 <= k <= nums.length <= 10^5

- 1 <= nums[i] <= 10^9

**Examples / sample tests:**

```
[2,6,5,8]
2
[4,5,4,7]
3
```

---

## Problem Summary
You are given an array `nums` and an integer `k`. You can perform an operation any number of times: choose two distinct indices `i, j` and update `nums[i]` to `(nums[i] AND nums[j])` and `nums[j]` to `(nums[i] OR nums[j])`. The goal is to choose `k` elements from the final array such that the sum of their squares is maximized, returning the result modulo `10^9 + 7`.

## Intuition
The key to this problem lies in understanding the bitwise operation: `(a, b) -> (a AND b, a OR b)`.
Let's analyze what happens to the bits:
1.  **Sum Invariant:** Notice that `(a AND b) + (a OR b) = a + b`. The sum of the two numbers involved in the operation remains constant.
2.  **Bit Distribution:** Consider a specific bit position `p`.
    *   If bit `p` is set in both `a` and `b`, it remains set in both `a AND b` and `a OR b`.
    *   If bit `p` is set in `a` but not `b`, it becomes 0 in `a AND b` and 1 in `a OR b`. This is like "transferring" the bit from `a` to `b`.
    *   If bit `p` is set in `b` but not `a`, it becomes 0 in `a AND b` and 1 in `a OR b`. This is like "transferring" the bit from `b` to `a`.
    *   If bit `p` is not set in either `a` or `b`, it remains not set in both.

This means that for any given bit position `p`, the **total count of numbers in the array that have bit `p` set remains invariant** throughout any number of operations. For example, if `a` has bit `p` and `b` doesn't, after the operation, `a` loses bit `p` and `b` gains it. The total count of numbers with bit `p` set (which was 1) remains 1.

This powerful property implies that we can effectively **pool all set bits from all numbers in the initial array and then redistribute them arbitrarily** among the `nums.length` elements. To maximize the sum of squares of `k` chosen elements, we should make these `k` elements as large as possible. Therefore, we should use the available bits to construct `k` numbers that are as large as possible.

The strategy is:
1.  Count how many times each bit position (e.g., `2^0`, `2^1`, `2^2`, etc.) is set across *all* numbers in the initial `nums` array.
2.  Initialize `k` numbers to zero.
3.  For each bit position `p` (from `2^0` up to `2^29` since `nums[i] <= 10^9 < 2^30`):
    *   If we have `C` instances of bit `p` available (from our count in step 1), we can set bit `p` in `C` of our `k` target numbers.
    *   To maximize the sum of squares, we should distribute these `C` bits among the `k` numbers we are building. The most effective way to do this is to add `2^p` to the first `min(k, C)` numbers. This ensures the `k` numbers are built to be as large as possible.
4.  Once all bits are distributed, calculate the sum of squares of these `k` numbers, modulo `10^9 + 7`.

## Approach
1.  **Initialize Modulo Constant:** Set `MOD = 10^9 + 7`.
2.  **Count Bit Frequencies:**
    *   Create an array, `bit_counts`, of size 30 (to cover bit positions 0 through 29, as `10^9` fits within 30 bits). Initialize all counts to 0.
    *   Iterate through each `num` in the input `nums` array.
    *   For each `num`, iterate `p` from 0 to 29. If the `p`-th bit of `num` is set (i.e., `(num >> p) & 1` is true), increment `bit_counts[p]`.
3.  **Construct `k` Final Numbers:**
    *   Create an array, `final_nums`, of size `k`, initialized with all zeros. These will be the `k` numbers we select.
    *   Iterate `p` from 0 to 29 (representing bit values `2^0` to `2^29`).
    *   Let `power_of_2 = (1 << p)`.
    *   Let `current_bit_count = bit_counts[p]`.
    *   Iterate `i` from 0 to `k-1`:
        *   If `current_bit_count > 0`:
            *   Add `power_of_2` to `final_nums[i]`.
            *   Decrement `current_bit_count`.
        *   Else (if `current_bit_count` is 0):
            *   Break from this inner loop, as there are no more `p`-th bits to distribute.
4.  **Calculate Sum of Squares:**
    *   Initialize `total_sum_squares = 0`.
    *   Iterate through each `val` in `final_nums`.
    *   Calculate `val_squared = (val * val) % MOD`.
    *   Add `val_squared` to `total_sum_squares`, taking modulo: `total_sum_squares = (total_sum_squares + val_squared) % MOD`.
5.  **Return `total_sum_squares`.**

## Visualization

```mermaid
graph TD
    A[Input nums: [2, 6, 5, 8], k=2] --> B{Count Set Bits for Each Position};

    subgraph Bit Counting
        B --> C1[num=2 (0010_2): bit_counts[1]++ (1)];
        B --> C2[num=6 (0110_2): bit_counts[1]++ (2), bit_counts[2]++ (1)];
        B --> C3[num=5 (0101_2): bit_counts[0]++ (1), bit_counts[2]++ (2)];
        B --> C4[num=8 (1000_2): bit_counts[3]++ (1)];
    end

    C1 & C2 & C3 & C4 --> D{Resulting bit_counts:};
    D --> D0[bit_counts[0] = 1];
    D --> D1[bit_counts[1] = 2];
    D --> D2[bit_counts[2] = 2];
    D --> D3[bit_counts[3] = 1];
    D --> D_other[Other bit_counts = 0];

    D0 & D1 & D2 & D3 & D_other --> E{Construct k=2 numbers};

    subgraph Number Construction (final_nums = [0, 0])
        E --> F0[p=0 (bit 2^0): count_0=1];
        F0 --> G0_1[final_nums[0] += 2^0 (now [1, 0])];
        G0_1 --> F1[p=1 (bit 2^1): count_1=2];
        F1 --> G1_1[final_nums[0] += 2^1 (now [3, 0])];
        G1_1 --> G1_2[final_nums[1] += 2^1 (now [3, 2])];
        G1_2 --> F2[p=2 (bit 2^2): count_2=2];
        F2 --> G2_1[final_nums[0] += 2^2 (now [7, 2])];
        G2_1 --> G2_2[final_nums[1] += 2^2 (now [7, 6])];
        G2_2 --> F3[p=3 (bit 2^3): count_3=1];
        F3 --> G3_1[final_nums[0] += 2^3 (now [15, 6])];
    end

    G3_1 --> H[Final final_nums = [15, 6]];
    H --> I{Calculate Sum of Squares (mod 10^9 + 7)};
    I --> J[15^2 + 6^2 = 225 + 36 = 261];
    J --> K[Output: 261];
```

## Dry Run
Let's walk through **Example 1**: `nums = [2, 6, 5, 8]`, `k = 2`.
`MOD = 10^9 + 7`.

1.  **Initialize `bit_counts` (size 30) to all zeros.**
    `bit_counts = [0, 0, ..., 0]`

2.  **Populate `bit_counts`:**
    *   `num = 2 (0010_2)`: `bit_counts[1]` becomes 1.
    *   `num = 6 (0110_2)`: `bit_counts[1]` becomes 2, `bit_counts[2]` becomes 1.
    *   `num = 5 (0101_2)`: `bit_counts[0]` becomes 1, `bit_counts[2]` becomes 2.
    *   `num = 8 (1000_2)`: `bit_counts[3]` becomes 1.

    **Relevant `bit_counts` after this step:**
    `bit_counts[0] = 1`
    `bit_counts[1] = 2`
    `bit_counts[2] = 2`
    `bit_counts[3] = 1`
    (All other `bit_counts[p]` remain 0)

3.  **Initialize `final_nums` (size `k=2`) to all zeros.**
    `final_nums = [0, 0]`

4.  **Construct `final_nums` by distributing bits:**

| `p` | `1 << p` | `bit_counts[p]` (start) | `i` | `final_nums[i]` (before) | Operation (`final_nums[i] += (1 << p)`) | `final_nums[i]` (after) | `bit_counts[p]` (end) | `final_nums` state |
| :-- | :------- | :---------------------- | :-- | :----------------------- | :--------------------------------------- | :---------------------- | :-------------------- | :----------------- |
| 0   | 1        | 1                       | 0   | 0                        | `0 + 1`                                  | 1                       | 0                     | `[1, 0]`           |
|     |          |                         | 1   | -                        | (break, `bit_counts[0]` is 0)            | -                       | -                     |                    |
| 1   | 2        | 2                       | 0   | 1                        | `1 + 2`                                  | 3                       | 1                     | `[3, 0]`           |
|     |          |                         | 1   | 0                        | `0 + 2`                                  | 2                       | 0                     | `[3, 2]`           |
| 2   | 4        | 2                       | 0   | 3                        | `3 + 4`                                  | 7                       | 1                     | `[7, 2]`           |
|     |          |                         | 1   | 2                        | `2 + 4`                                  | 6                       | 0                     | `[7, 6]`           |
| 3   | 8        | 1                       | 0   | 7                        | `7 + 8`                                  | 15                      | 0                     | `[15, 6]`          |
|     |          |                         | 1   | -                        | (break, `bit_counts[3]` is 0)            | -                       | -                     |                    |
| ... | ...      | 0                       | ... | ...                      | (break for all remaining `p`)            | ...                     | ...                   | `[15, 6]`          |

5.  **Calculate Sum of Squares:**
    `total_sum_squares = 0`
    *   For `val = 15`:
        `val_squared = (15 * 15) % MOD = 225 % MOD = 225`.
        `total_sum_squares = (0 + 225) % MOD = 225`.
    *   For `val = 6`:
        `val_squared = (6 * 6) % MOD = 36 % MOD = 36`.
        `total_sum_squares = (225 + 36) % MOD = 261`.

**Final Result:** `261`.

## Complexity
*   **Time Complexity:** `O(N * log(max_val) + k * log(max_val))`
    *   Counting bits: `N` numbers, each up to `10^9` (approx `2^30`), so `log(max_val)` bits to check. This is `O(N * log(max_val))`.
    *   Constructing `k` numbers: `log(max_val)` bit positions, for each we iterate up to `k` times. This is `O(k * log(max_val))`.
    *   Calculating sum of squares: Iterate `k` numbers. This is `O(k)`.
    *   Since `k <= N`, the dominant term is `O(N * log(max_val))`. Given `N=10^5` and `log(max_val) approx 30`, this is roughly `3 * 10^6` operations, which is efficient.
*   **Space Complexity:** `O(k + log(max_val))`
    *   `bit_counts` array: `O(log(max_val))` (constant size, 30 elements).
    *   `final_nums` array: `O(k)`.
    *   Since `k <= N`, this simplifies to `O(N)`. Given `N=10^5`, this is `10^5` integers, which is acceptable.

## Edge Cases
*   **`k = 1`**: The solution correctly builds one number by accumulating all available bits into `final_nums[0]`.
*   **`k = nums.length`**: The solution will distribute bits among all `nums.length` numbers, constructing the largest possible values for each.
*   **All `nums[i]` are 0**: `bit_counts` will be all zeros. `final_nums` will remain all zeros. The sum of squares will be 0, which is correct.
*   **`nums[i]` are large (up to `10^9`)**: The use of `BIT_COUNT_MAX = 30` correctly handles numbers up to `2^30 - 1`. Python's arbitrary-precision integers handle `val * val` without overflow before the modulo operation.
*   **All `nums[i]` are identical**: `bit_counts` will reflect this. The `k` numbers constructed will also be identical to the original number if `k <= N`.

## Solution

```python
import collections
from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Maximum number of bits needed for nums[i] up to 10^9.
        # 2^29 = 536,870,912
        # 2^30 = 1,073,741,824
        # So, numbers up to 10^9 require bits from 0 to 29 (total 30 bits).
        BIT_COUNT_MAX = 30 
        
        # Step 1: Count the occurrences of each set bit position across all numbers.
        # bit_counts[p] will store how many numbers in 'nums' have the p-th bit set.
        bit_counts = [0] * BIT_COUNT_MAX
        
        for num in nums:
            for p in range(BIT_COUNT_MAX):
                if (num >> p) & 1:  # Check if the p-th bit is set in 'num'
                    bit_counts[p] += 1
        
        # Step 2: Construct 'k' numbers by distributing the collected bits.
        # To maximize the sum of squares, we want to make the 'k' numbers as large as possible.
        # We achieve this by adding the value of each bit (2^p) to the first 'count_p'
        # numbers in our 'final_nums' array. This greedily builds the largest possible numbers.
        final_nums = [0] * k
        
        for p in range(BIT_COUNT_MAX):
            power_of_2 = (1 << p)  # Calculate 2^p
            current_bit_count = bit_counts[p]
            
            # Distribute 'current_bit_count' instances of the p-th bit (value 2^p)
            # among the 'k' numbers we are constructing.
            # We can set the p-th bit in at most 'k' numbers, and at most 'current_bit_count' times.
            # So, we set it in min(k, current_bit_count) numbers.
            for i in range(k):
                if current_bit_count > 0:
                    final_nums[i] += power_of_2
                    current_bit_count -= 1
                else:
                    # If we run out of p-th bits, stop distributing for this bit position.
                    break
        
        # Step 3: Calculate the sum of squares of the constructed 'k' numbers, modulo MOD.
        total_sum_squares = 0
        for val in final_nums:
            # Calculate (val * val) % MOD.
            # Python's integers handle arbitrary size, so val * val won't overflow
            # before the modulo operation, even if val is large (e.g., 10^9).
            val_squared = (val * val) % MOD
            total_sum_squares = (total_sum_squares + val_squared) % MOD
            
        return total_sum_squares

```

## Why This Works
The core reason this approach works is the **invariant property of the bitwise operation**. When `(a, b)` are transformed into `(a AND b, a OR b)`, the multiset of set bits across `a` and `b` is preserved. Specifically, for any bit position `p`, the total count of numbers in the array that have bit `p` set remains constant. This means we can effectively "pool" all set bits from the entire initial array and then redistribute them arbitrarily among the `nums.length` elements. To maximize the sum of squares of `k` chosen elements, we must make these `k` elements as large as possible. Our greedy strategy of iterating through each bit position and adding `2^p` to `min(k, bit_counts[p])` of our target numbers ensures that we construct the `k` largest possible numbers that can be formed from the available bits, thereby maximizing their sum of squares.

---
<sub>Generated 2026-10-12 06:24 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
