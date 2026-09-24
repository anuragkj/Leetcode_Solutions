# [3550] Smallest Index With Digit Sum Equal to Index

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-09-24 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/)

**Topics:** Array, Math

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums.

Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

If no such index exists, return -1.

Example 1:

Input: nums = [1,3,2]

Output: 2

Explanation:

- For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.

Example 2:

Input: nums = [1,10,11]

Output: 1

Explanation:

- For nums[1] = 10, the sum of digits is 1 + 0 = 1, which is equal to index i = 1.

- For nums[2] = 11, the sum of digits is 1 + 1 = 2, which is equal to index i = 2.

- Since index 1 is the smallest, the output is 1.

Example 3:

Input: nums = [1,2,3]

Output: -1

Explanation:

- Since no index satisfies the condition, the output is -1.

Constraints:

- 1 <= nums.length <= 100

- 0 <= nums[i] <= 1000

**Examples / sample tests:**

```
[1,3,2]
[1,10,11]
[1,2,3]
```

---

## Problem Summary
We need to find the smallest index `i` in a given integer array `nums` such that the sum of the digits of the number `nums[i]` is exactly equal to `i`. If no such index exists after checking all possibilities, we should return -1.

## Intuition
The problem asks for the **smallest** index that satisfies a specific condition. This is a strong hint to **iterate through the array from the beginning (index 0) upwards**. As soon as we find an index `i` that meets the criteria, we can immediately return it because any subsequent matching index would necessarily be larger. The core operation for each element will be to **calculate the sum of its digits**.

## Approach
1.  **Define a helper function `get_digit_sum(num)`:** This function will take an integer `num` and return the sum of its digits.
    *   If `num` is 0, its digit sum is 0.
    *   For any positive `num`, initialize `digit_sum = 0`.
    *   Repeatedly:
        *   Add the last digit (`num % 10`) to `digit_sum`.
        *   Remove the last digit (`num //= 10`).
    *   Continue until `num` becomes 0.
    *   Return `digit_sum`.

2.  **Iterate through the `nums` array:** Use a `for` loop with an index `i` ranging from `0` up to `len(nums) - 1`.

3.  **Check the condition for each index `i`:**
    *   Get the current number: `current_num = nums[i]`.
    *   Calculate its digit sum using our helper function: `s = get_digit_sum(current_num)`.
    *   Compare `s` with the current index `i`.

4.  **Return if condition met:** If `s == i`, we have found an index that satisfies the condition. Since we are iterating from `0` upwards, this `i` is guaranteed to be the **smallest** such index. So, `return i` immediately.

5.  **Handle no match:** If the loop completes without finding any matching index (i.e., we never returned `i`), it means no such index exists in the array. In this case, `return -1`.

## Visualization

Let's trace with `nums = [1, 10, 11]`

```
nums = [ 1,  10,  11 ]
Indices:  0    1     2

Start loop from i = 0:
  i = 0:
    nums[0] = 1
    Digit Sum(1) = 1
    Is 1 == 0? No.

  i = 1:
    nums[1] = 10
    Digit Sum(10) = 1 + 0 = 1
    Is 1 == 1? Yes!
    
    Condition met at i=1.
    Since we iterate from smallest index, this is the smallest.
    
    Return 1.
```

## Dry Run

Let's walk through **Example 1: `nums = [1,3,2]`**

| `i` | `nums[i]` | `current_num` | `digit_sum` calculation | `digit_sum` | `digit_sum == i`? | Action       |
| :-- | :-------- | :------------ | :---------------------- | :---------- | :---------------- | :----------- |
| 0   | 1         | 1             | `1 % 10 = 1`            | 1           | `1 == 0`? **No**  | Continue loop |
| 1   | 3         | 3             | `3 % 10 = 3`            | 3           | `3 == 1`? **No**  | Continue loop |
| 2   | 2         | 2             | `2 % 10 = 2`            | 2           | `2 == 2`? **Yes** | **Return 2** |

The final result is **2**.

## Complexity

*   **Time Complexity:** O(N \* log(max\_num)).
    *   We iterate through the `nums` array once, which has `N` elements.
    *   For each element `nums[i]`, we calculate its digit sum. The number of operations for `get_digit_sum` is proportional to the number of digits in `nums[i]`. Since `nums[i]` can be up to 1000, it has at most 4 digits (`log10(1000)` is 3, plus one for the first digit).
    *   Therefore, the digit sum calculation is a constant small factor (at most 4 operations) for each element.
    *   Effectively, for the given constraints, this is very close to O(N).

*   **Space Complexity:** O(1).
    *   We only use a few constant extra variables (like `digit_sum`, `current_num`, `i`, `n`). We do not use any data structures that grow with the input size.

## Edge Cases

*   **No matching index:** `nums = [1,2,3]` should correctly return -1. Our loop will complete without finding a match, and the final `-1` will be returned.
*   **First element matches:** `nums = [0, 5, 10]` should return 0. Our loop starts at `i=0`, `nums[0]=0`, `digit_sum(0)=0`. Since `0 == 0`, it correctly returns 0 immediately.
*   **`nums[i]` is 0:** Handled by `get_digit_sum(0)` returning 0.
*   **`nums[i]` is a single digit:** `nums = [1, 3, 2]`. `nums[0]=1`, `digit_sum(1)=1`. `nums[1]=3`, `digit_sum(3)=3`. `nums[2]=2`, `digit_sum(2)=2`. All handled correctly.
*   **Multiple matches, smallest returned:** `nums = [1, 10, 11]`. `i=1` (`nums[1]=10`, sum=1) matches. `i=2` (`nums[2]=11`, sum=2) also matches. Our approach returns 1 because it's found first due to iteration order.

## Solution

```python
from typing import List

class Solution:
    def _get_digit_sum(self, num: int) -> int:
        """
        Helper function to calculate the sum of digits of a non-negative integer.
        Example: _get_digit_sum(123) -> 1 + 2 + 3 = 6
                 _get_digit_sum(0)   -> 0
        """
        if num == 0:
            return 0
        
        digit_sum = 0
        current_num = num
        while current_num > 0:
            digit_sum += current_num % 10  # Add the last digit
            current_num //= 10             # Remove the last digit
        return digit_sum

    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Iterate through the array using index 'i'
        for i in range(n):
            # Calculate the sum of digits for the number at the current index
            current_num_digit_sum = self._get_digit_sum(nums[i])
            
            # Check if the calculated digit sum is equal to the current index 'i'
            if current_num_digit_sum == i:
                # If it is, we've found the smallest such index
                # because we are iterating from i = 0 upwards.
                return i
        
        # If the loop completes, it means no such index was found in the array
        return -1

```

## Why This Works

This approach works because it systematically checks every possible index starting from `0` and proceeding upwards. The problem asks for the **smallest** index satisfying the condition. By iterating in increasing order of indices and returning immediately upon finding the first match, we guarantee that the returned index is indeed the smallest one that satisfies the criteria. If the loop finishes without returning any index, it correctly implies that no such index exists in the array, and -1 is returned.

---
<sub>Generated 2026-09-24 05:14 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
