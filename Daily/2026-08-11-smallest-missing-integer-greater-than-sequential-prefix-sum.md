# [2996] Smallest Missing Integer Greater Than Sequential Prefix Sum

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-08-11 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/)

**Topics:** Array, Hash Table, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 0-indexed array of integers nums.

A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.

Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.

Example 1:

Input: nums = [1,2,3,2,5]
Output: 6
Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

Example 2:

Input: nums = [3,4,5,1,12,14,13]
Output: 15
Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.

Constraints:

- 1 <= nums.length <= 50

- 1 <= nums[i] <= 50

**Examples / sample tests:**

```
[1,2,3,2,5]
[3,4,5,1,12,14,13]
```

---

## Problem Summary
Given an array `nums`, first find the sum of its **longest sequential prefix**. A prefix `nums[0...i]` is sequential if `nums[j] = nums[j-1] + 1` for all `1 <= j <= i`. Then, find the **smallest integer `x`** that is **missing from `nums`** and is **greater than or equal to** this calculated prefix sum.

## Intuition
This problem can be broken down into two distinct parts:

1.  **Finding the sum of the longest sequential prefix**: We need to iterate through the array from left to right. We maintain a running sum. As long as the current number `nums[i]` is exactly one greater than the previous number `nums[i-1]`, we continue adding it to our sum. The moment this condition breaks (or we reach the end of the array), the current running sum is the sum of the longest sequential prefix.

2.  **Finding the smallest missing integer `x`**: Once we have the `prefix_sum`, we need to start checking numbers from `prefix_sum` upwards (`prefix_sum`, `prefix_sum + 1`, `prefix_sum + 2`, ...). For each number, we ask: "Is this number present in the original `nums` array?" The very first number we check that is *not* in `nums` is our answer. To efficiently check for presence in `nums`, a **hash set** (or `set` in Python) is the perfect data structure, as it allows for average O(1) lookups.

## Approach
Here's the step-by-step algorithm:

1.  **Calculate the longest sequential prefix sum**:
    *   Initialize `prefix_sum = nums[0]`. This handles the base case where the prefix is just `nums[0]`.
    *   Iterate through `nums` starting from the second element (index `1`) up to the end of the array.
    *   In each iteration `i`:
        *   Check if `nums[i] == nums[i-1] + 1`.
        *   If true, it means the sequential prefix continues. Add `nums[i]` to `prefix_sum`.
        *   If false, the sequential prefix has ended. Break out of this loop; `prefix_sum` now holds the correct value.

2.  **Prepare for efficient lookups**:
    *   Create a **hash set** (e.g., `num_set`) and populate it with all unique elements from the input `nums` array. This allows for very fast `O(1)` average-time checks for whether a number exists in `nums`.

3.  **Find the smallest missing integer**:
    *   Initialize a variable `x` with the `prefix_sum` calculated in step 1.
    *   Enter a loop that continues as long as `x` is found in `num_set`:
        *   Increment `x` by 1.
    *   Once the loop terminates (meaning `x` is *not* in `num_set`), `x` is our answer. Return `x`.

## Visualization

Let's illustrate with `nums = [1,2,3,2,5]`

**Part 1: Finding the Longest Sequential Prefix Sum**

```
nums = [ 1,  2,  3,  2,  5 ]
         ^
prefix_sum = 1

i = 1: nums[1] = 2
       nums[1] == nums[0] + 1  (2 == 1 + 1) ? Yes!
       prefix_sum = 1 + 2 = 3
       
nums = [ 1,  2,  3,  2,  5 ]
             ^
prefix_sum = 3

i = 2: nums[2] = 3
       nums[2] == nums[1] + 1  (3 == 2 + 1) ? Yes!
       prefix_sum = 3 + 3 = 6

nums = [ 1,  2,  3,  2,  5 ]
                 ^
prefix_sum = 6

i = 3: nums[3] = 2
       nums[3] == nums[2] + 1  (2 == 3 + 1) ? No! (2 != 4)
       Break loop.

Final prefix_sum = 6
```

**Part 2: Finding the Smallest Missing Integer >= `prefix_sum`**

```
nums = [1,2,3,2,5]
num_set = {1, 2, 3, 5}  (unique elements from nums)
prefix_sum = 6

Start checking from x = prefix_sum:

x = 6
Is 6 in num_set? No.

Result: 6
```

## Dry Run
Let's walk through Example 1: `nums = [1,2,3,2,5]`

| Step | Variable / State | Description |
| :--- | :--------------- | :---------- |
| **1. Find Longest Sequential Prefix Sum** | | |
| 1.1 | `prefix_sum = 1` | Initialize `prefix_sum` with `nums[0]`. |
| 1.2 | `i = 1` | Start loop from index 1. |
| 1.2.1 | `nums[1] = 2`, `nums[0] = 1` | Check `nums[1] == nums[0] + 1` (2 == 1 + 1)? Yes. |
| 1.2.2 | `prefix_sum = 1 + 2 = 3` | Add `nums[1]` to `prefix_sum`. |
| 1.3 | `i = 2` | Next iteration. |
| 1.3.1 | `nums[2] = 3`, `nums[1] = 2` | Check `nums[2] == nums[1] + 1` (3 == 2 + 1)? Yes. |
| 1.3.2 | `prefix_sum = 3 + 3 = 6` | Add `nums[2]` to `prefix_sum`. |
| 1.4 | `i = 3` | Next iteration. |
| 1.4.1 | `nums[3] = 2`, `nums[2] = 3` | Check `nums[3] == nums[2] + 1` (2 == 3 + 1)? No (2 != 4). |
| 1.4.2 | Loop breaks | The longest sequential prefix ends. |
| **2. Prepare for Lookups** | | |
| 2.1 | `num_set = {1, 2, 3, 5}` | Create a set of unique elements from `nums`. |
| **3. Find Smallest Missing Integer** | | |
| 3.1 | `x = 6` | Initialize `x` with the `prefix_sum`. |
| 3.2 | `x = 6` | Is `6` in `num_set`? No. |
| 3.3 | Loop terminates | `x` is not found, so it's the smallest missing integer. |
| **Final Result** | `6` | Return `x`. |

## Complexity
*   **Time Complexity**: `O(N)`
    *   Calculating the `prefix_sum` involves a single pass through `nums`, which takes `O(N)` time.
    *   Creating the `num_set` from `nums` takes `O(N)` time on average.
    *   Finding the smallest missing integer `x` involves checking `x`, `x+1`, `x+2`, ... against the `num_set`. In the worst case, `x` might be `prefix_sum + N` (if `prefix_sum` and the next `N-1` integers are all present in `nums`). Each check is `O(1)` on average. So, this step takes `O(N)` time on average.
    *   Overall, the dominant operations are linear with respect to `N`, so the total time complexity is `O(N)`.
*   **Space Complexity**: `O(N)`
    *   The `num_set` stores up to `N` unique elements from `nums`. This requires `O(N)` space.

## Edge Cases
*   **`nums` has only one element**: E.g., `[5]`.
    *   `prefix_sum` will be `5`. `num_set` will be `{5}`.
    *   `x` starts at `5`. `5` is in `num_set`. `x` becomes `6`.
    *   `6` is not in `num_set`. Return `6`. Correct.
*   **All elements form a sequential prefix**: E.g., `[1,2,3,4]`.
    *   `prefix_sum` will be `10`. `num_set` will be `{1,2,3,4}`.
    *   `x` starts at `10`. `10` is not in `num_set`. Return `10`. Correct.
*   **`prefix_sum` is already the smallest missing integer**: E.g., `[1,2,3,5]`.
    *   `prefix_sum` will be `6`. `num_set` will be `{1,2,3,5}`.
    *   `x` starts at `6`. `6` is not in `num_set`. Return `6`. Correct.
*   **`prefix_sum` and subsequent numbers are present**: E.g., `[1,2,3,6,7,8]`.
    *   `prefix_sum` will be `6`. `num_set` will be `{1,2,3,6,7,8}`.
    *   `x` starts at `6`. `6` is in `num_set`. `x` becomes `7`.
    *   `7` is in `num_set`. `x` becomes `8`.
    *   `8` is in `num_set`. `x` becomes `9`.
    *   `9` is not in `num_set`. Return `9`. Correct.
*   **Duplicate numbers in `nums`**: E.g., `[1,2,3,2,5]`.
    *   The `set` automatically handles duplicates, storing only unique values, which is exactly what we need for efficient presence checks.

## Solution

```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Part 1: Calculate the sum of the longest sequential prefix
        # Initialize prefix_sum with the first element
        prefix_sum = nums[0]
        
        # Iterate from the second element
        for i in range(1, len(nums)):
            # Check if the current element continues the sequential prefix
            if nums[i] == nums[i-1] + 1:
                prefix_sum += nums[i]
            else:
                # If the sequence breaks, stop and use the current prefix_sum
                break
        
        # Part 2: Find the smallest integer x missing from nums
        # such that x >= prefix_sum
        
        # Create a hash set for O(1) average-time lookups
        num_set = set(nums)
        
        # Start checking from prefix_sum
        x = prefix_sum
        
        # Increment x until we find a number not present in num_set
        while x in num_set:
            x += 1
            
        return x

```

## Why This Works
The solution correctly identifies the **longest sequential prefix sum** by iterating through the array and accumulating the sum only as long as the sequential property holds. This ensures `prefix_sum` is the exact target value. Then, by creating a **hash set** of all numbers in `nums`, we can efficiently check for the presence of any integer in `O(1)` average time. Starting from `prefix_sum`, we increment `x` one by one and query the hash set. The first value of `x` that is *not* found in the set is guaranteed to be the **smallest missing integer** that is greater than or equal to `prefix_sum`, as we checked all preceding integers in increasing order.

---
<sub>Generated 2026-08-11 02:36 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
