# [3718] Smallest Missing Multiple of K

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-08-25 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/smallest-missing-multiple-of-k/)

**Topics:** Array, Hash Table

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given an integer array nums and an integer k, return the smallest positive multiple of k that is missing from nums.

A multiple of k is any positive integer divisible by k.

Example 1:

Input: nums = [8,2,3,4,6], k = 2

Output: 10

Explanation:

The multiples of k = 2 are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from nums is 10.

Example 2:

Input: nums = [1,4,7,10,15], k = 5

Output: 5

Explanation:

The multiples of k = 5 are 5, 10, 15, 20... and the smallest multiple missing from nums is 5.

Constraints:

- 1 <= nums.length <= 100

- 1 <= nums[i] <= 100

- 1 <= k <= 100

**Examples / sample tests:**

```
[8,2,3,4,6]
2
[1,4,7,10,15]
5
```

---

## Problem Summary
Given an array of integers `nums` and an integer `k`, the task is to find the **smallest positive multiple of `k`** that is **not present** in the `nums` array.

## Intuition
The problem asks for the *smallest* missing multiple. This immediately suggests we should check multiples of `k` in **increasing order**: `k`, `2k`, `3k`, and so on. For each multiple, we need to quickly determine if it exists in the `nums` array. A **hash set** (Python's `set`) is the perfect data structure for this, as it allows for **average O(1) time complexity** lookups.

## Approach
1.  **Create a Hash Set**: Convert the input list `nums` into a hash set (let's call it `num_set`). This allows for very fast checking of whether a number is present in `nums`.
2.  **Iterate Through Multiples**: Start with the first positive multiple of `k`, which is `k` itself.
3.  **Check for Presence**: For each multiple `m = i * k` (where `i` starts from 1 and increments), check if `m` is present in `num_set`.
4.  **Return First Missing**: The very first multiple `m` that is **not found** in `num_set` is our answer. Return this value immediately. Since the problem guarantees `nums[i]` are positive, and `k` is positive, we will always find a positive multiple.

## Visualization

Let's trace with `nums = [8,2,3,4,6]` and `k = 2`.

```
1. Input:
   nums = [8, 2, 3, 4, 6]
   k    = 2

2. Convert nums to a hash set for quick lookups:
   num_set = {2, 3, 4, 6, 8}
   
3. Start checking positive multiples of k (which is 2):

   - Check 1 * k = 2:
     Is 2 in num_set?  YES (Found)
     
   - Check 2 * k = 4:
     Is 4 in num_set?  YES (Found)
     
   - Check 3 * k = 6:
     Is 6 in num_set?  YES (Found)
     
   - Check 4 * k = 8:
     Is 8 in num_set?  YES (Found)
     
   - Check 5 * k = 10:
     Is 10 in num_set? NO  <-- This is the first missing multiple!
     
4. Return 10.
```

## Dry Run

Let's walk through **Example 1**: `nums = [8,2,3,4,6]`, `k = 2`.

1.  **Initialization**:
    *   `num_set = set(nums)` which becomes `{2, 3, 4, 6, 8}`.
    *   We'll use a counter `i` starting from 1 to generate multiples.

| Iteration | `i` | `current_multiple = i * k` | `current_multiple` in `num_set`? | Action                               |
| :-------- | :-- | :------------------------- | :------------------------------- | :----------------------------------- |
| 1         | 1   | `1 * 2 = 2`                | `True`                           | Continue to next multiple            |
| 2         | 2   | `2 * 2 = 4`                | `True`                           | Continue to next multiple            |
| 3         | 3   | `3 * 2 = 6`                | `True`                           | Continue to next multiple            |
| 4         | 4   | `4 * 2 = 8`                | `True`                           | Continue to next multiple            |
| 5         | 5   | `5 * 2 = 10`               | `False`                          | `10` is missing! Return `10`.        |

**Final Result**: 10

## Complexity

*   **Time Complexity**: O(N + M/k).
    *   Creating the `num_set` takes O(N) time, where N is the length of `nums`.
    *   The loop iterates `M/k` times, where `M` is the smallest missing multiple. In the worst case, `M` can be up to `max(nums) + k` (e.g., if `nums` contains all multiples up to its maximum value). Given the constraints (`nums[i] <= 100`, `k <= 100`), `M` will be at most `100 + 100 = 200`. So, the loop runs at most `200/1 = 200` times. Each lookup in a hash set is O(1) on average. Thus, the loop part is effectively O(C) where C is a small constant.
    *   Overall, it's O(N + C), which simplifies to **O(N)**.
*   **Space Complexity**: O(N).
    *   We store all elements of `nums` in a hash set, which requires space proportional to the number of unique elements in `nums`.

## Edge Cases

*   **`k` itself is the smallest missing multiple**:
    *   `nums = [2, 4, 6], k = 2`
    *   `num_set = {2, 4, 6}`.
    *   `1 * 2 = 2` (in set).
    *   `2 * 2 = 4` (in set).
    *   `3 * 2 = 6` (in set).
    *   `4 * 2 = 8` (not in set). Output: 8. (Wait, this example is wrong, `k` itself is not missing here. Let's fix it.)
    *   Correct example: `nums = [4, 6, 8], k = 2`
    *   `num_set = {4, 6, 8}`.
    *   `1 * 2 = 2` (not in set). Output: 2.
    *   The solution correctly handles this by starting the check from `1 * k`.
*   **All multiples up to a certain point are present**:
    *   `nums = [2, 4, 6, 8], k = 2`
    *   `num_set = {2, 4, 6, 8}`.
    *   The loop will proceed through 2, 4, 6, 8, find them all, and then correctly identify 10 as the first missing multiple.
*   **`k = 1`**:
    *   `nums = [1, 2, 4], k = 1`
    *   `num_set = {1, 2, 4}`.
    *   `1 * 1 = 1` (in set).
    *   `2 * 1 = 2` (in set).
    *   `3 * 1 = 3` (not in set). Output: 3.
    *   The solution works for `k=1` as well.
*   **`nums` contains values not multiples of `k`**:
    *   `nums = [8, 2, 3, 4, 6], k = 2` (Example 1)
    *   The number `3` is in `nums` but is not a multiple of `k=2`. The hash set will contain `3`, but our iteration only checks multiples of `k`, so `3` is simply ignored by the check logic, which is correct.

## Solution

```python
from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Step 1: Convert the input list nums into a hash set for O(1) average time lookups.
        num_set = set(nums)
        
        # Step 2: Start checking positive multiples of k.
        # Multiples are k, 2*k, 3*k, ...
        # We can use a counter 'i' starting from 1.
        i = 1
        while True:
            current_multiple = i * k
            
            # Step 3: Check if the current multiple is present in our hash set.
            if current_multiple not in num_set:
                # Step 4: If it's not in the set, this is the smallest missing multiple.
                # Return it immediately.
                return current_multiple
            
            # If the current_multiple was found, increment 'i' to check the next multiple.
            i += 1

```

## Why This Works

This approach works because it systematically checks all positive multiples of `k` in **strictly increasing order**. By using a **hash set**, each check for presence is extremely fast (average O(1)). The moment we encounter a multiple that is *not* in the `num_set`, we know it must be the **smallest** such missing multiple, because we have already verified that all smaller positive multiples of `k` *were* present in `nums`. The problem constraints guarantee that `k` is positive and `nums` contains positive integers, so we will always find a positive missing multiple.

---
<sub>Generated 2026-08-25 02:04 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
