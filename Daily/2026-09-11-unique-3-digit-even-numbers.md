# [3483] Unique 3-Digit Even Numbers

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-09-11 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/unique-3-digit-even-numbers/)

**Topics:** Array, Hash Table, Recursion, Enumeration

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

Example 1:

Input: digits = [1,2,3,4]

Output: 12

Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

Example 2:

Input: digits = [0,2,2]

Output: 2

Explanation: The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.

Example 3:

Input: digits = [6,6,6]

Output: 1

Explanation: Only 666 can be formed.

Example 4:

Input: digits = [1,3,5]

Output: 0

Explanation: No even 3-digit numbers can be formed.

Constraints:

- 3 <= digits.length <= 10

- 0 <= digits[i] <= 9

**Examples / sample tests:**

```
[1,2,3,4]
[0,2,2]
[6,6,6]
[1,3,5]
```

---

## Problem Summary
Given an array of `digits`, the task is to count how many **distinct three-digit even numbers** can be formed. Each digit from the input array can be used only once per number, and numbers cannot have a leading zero.

## Intuition
The constraints on the input `digits` array (`length` up to 10) are very small. This suggests that we don't need an extremely complex or highly optimized algorithm. Instead, we can try a more direct approach: **enumerate all possible valid numbers** and check if they can be formed.

A three-digit number ranges from 100 to 999. An even number must end in 0, 2, 4, 6, or 8. The key challenge is to ensure we use available digits correctly, respecting their counts (e.g., if `digits = [2,2,0]`, we can form `220` because there are two `2`s). This points to using a **frequency map** (like `collections.Counter`) to track the available digits.

## Approach
The most straightforward approach for beginners, given the small constraints, is to iterate through every possible 3-digit even number and check if its digits can be formed from the input `digits`.

1.  **Count Available Digits:** First, create a frequency map (using `collections.Counter`) of the `digits` provided in the input array. This map, let's call it `available_counts`, will tell us how many copies of each digit (0-9) we have.

2.  **Initialize Counter:** Set a variable `total_distinct_numbers` to `0`. This will store our final answer.

3.  **Iterate Through Candidate Numbers:** Loop through all integers `num` from `100` up to `999` (inclusive).
    *   **Check for Evenness:** For each `num`, immediately check if it's an even number (`num % 2 == 0`). If it's odd, skip it and move to the next `num`.
    *   **Extract Digits:** If `num` is even, extract its three individual digits:
        *   `d1 = num // 100` (hundreds digit)
        *   `d2 = (num // 10) % 10` (tens digit)
        *   `d3 = num % 10` (units digit)
    *   **Count Digits for Current Number:** Create a temporary frequency map, `current_num_counts`, for these three digits (`d1`, `d2`, `d3`). For example, if `num = 220`, `current_num_counts` would be `{2: 2, 0: 1}`.
    *   **Check Feasibility:** Compare `current_num_counts` with `available_counts`. For each digit `d` and its required count `c` in `current_num_counts`:
        *   If `available_counts[d] < c`, it means we don't have enough copies of digit `d` in our input `digits` array to form `num`. In this case, `num` cannot be formed, so set a flag `can_form = False` and break this inner check.
    *   **Increment Counter:** If, after checking all three digits, `can_form` is still `True`, it means `num` can be successfully formed. Increment `total_distinct_numbers` by `1`.

4.  **Return Result:** After iterating through all numbers from 100 to 999, return the final value of `total_distinct_numbers`.

This approach naturally handles "no leading zeros" because our loop starts from 100. It handles "distinct numbers" because we iterate through distinct `num` values. It handles "each copy used once" by comparing frequency maps.

## Visualization

Let's visualize the core idea with `digits = [1,2,3,4]`.
`available_counts = {1:1, 2:1, 3:1, 4:1}`
`total_distinct_numbers = 0`

```
Loop num from 100 to 999:

num = 100 (even)
  d1=1, d2=0, d3=0
  current_num_counts = {1:1, 0:2}
  Check:
    - For digit 1: available_counts[1]=1 >= current_num_counts[1]=1 (OK)
    - For digit 0: available_counts[0]=0 < current_num_counts[0]=2 (FAIL!)
  -> can_form = False. Skip 100.

num = 102 (even)
  d1=1, d2=0, d3=2
  current_num_counts = {1:1, 0:1, 2:1}
  Check:
    - For digit 1: available_counts[1]=1 >= current_num_counts[1]=1 (OK)
    - For digit 0: available_counts[0]=0 < current_num_counts[0]=1 (FAIL!)
  -> can_form = False. Skip 102.

... (many numbers skipped) ...

num = 124 (even)
  d1=1, d2=2, d3=4
  current_num_counts = {1:1, 2:1, 4:1}
  Check:
    - For digit 1: available_counts[1]=1 >= current_num_counts[1]=1 (OK)
    - For digit 2: available_counts[2]=1 >= current_num_counts[2]=1 (OK)
    - For digit 4: available_counts[4]=1 >= current_num_counts[4]=1 (OK)
  -> can_form = True.
  -> total_distinct_numbers = 1.

num = 132 (even)
  d1=1, d2=3, d3=2
  current_num_counts = {1:1, 3:1, 2:1}
  Check: (all OK)
  -> can_form = True.
  -> total_distinct_numbers = 2.

... (continue until 999) ...
```

## Dry Run
Let's trace `digits = [0,2,2]`

| `num` | `num % 2` | `d1, d2, d3` | `current_num_counts` | `available_counts` | `can_form` | `total_distinct_numbers` | Notes                                                              |
| :---- | :-------- | :----------- | :------------------- | :----------------- | :--------- | :----------------------- | :----------------------------------------------------------------- |
|       |           |              |                      | `{0:1, 2:2}`       |            | `0`                      | Initial state                                                      |
| `100` | `0`       | `1,0,0`      | `{1:1, 0:2}`         |                    | `False`    | `0`                      | `available_counts[1]=0 < current_num_counts[1]=1`                |
| `102` | `0`       | `1,0,2`      | `{1:1, 0:1, 2:1}`    |                    | `False`    | `0`                      | `available_counts[1]=0 < current_num_counts[1]=1`                |
| ...   |           |              |                      |                    |            |                          | Many numbers skipped (e.g., due to missing digit `1`, `3`, etc.) |
| `200` | `0`       | `2,0,0`      | `{2:1, 0:2}`         |                    | `False`    | `0`                      | `available_counts[0]=1 < current_num_counts[0]=2`                |
| `202` | `0`       | `2,0,2`      | `{2:2, 0:1}`         |                    | `True`     | `1`                      | `available_counts[2]=2 >= current_num_counts[2]=2` (OK) <br> `available_counts[0]=1 >= current_num_counts[0]=1` (OK) |
| `204` | `0`       | `2,0,4`      | `{2:1, 0:1, 4:1}`    |                    | `False`    | `1`                      | `available_counts[4]=0 < current_num_counts[4]=1`                |
| `220` | `0`       | `2,2,0`      | `{2:2, 0:1}`         |                    | `True`     | `2`                      | `available_counts[2]=2 >= current_num_counts[2]=2` (OK) <br> `available_counts[0]=1 >= current_num_counts[0]=1` (OK) |
| `222` | `0`       | `2,2,2`      | `{2:3}`              |                    | `False`    | `2`                      | `available_counts[2]=2 < current_num_counts[2]=3`                |
| ...   |           |              |                      |                    |            |                          | Loop continues until 999                                           |
Final Result: `2`

## Complexity
*   **Time Complexity:**
    *   Creating `available_counts` using `collections.Counter(digits)` takes `O(N)` time, where `N` is the length of the `digits` array. Given `N <= 10`, this is very fast.
    *   The main loop iterates from `100` to `999`, which is a fixed `900` iterations.
    *   Inside the loop, extracting digits, creating `current_num_counts` (for 3 digits), and comparing frequency maps (at most 3 distinct digits) all take constant time, `O(1)`.
    *   Therefore, the total time complexity is dominated by the fixed number of iterations, making it **O(1)** (constant time relative to the problem's constraints, as `N` is small and the loop range is fixed).
*   **Space Complexity:**
    *   `available_counts` stores frequencies for at most 10 distinct digits (0-9). This requires `O(1)` space.
    *   `current_num_counts` stores frequencies for at most 3 distinct digits. This also requires `O(1)` space.
    *   The total space complexity is **O(1)**.

## Edge Cases
*   **`digits = [1,3,5]` (No even digits):** The `available_counts` will not contain any even digits. When checking any candidate `num` that is even, its units digit `d3` will be even. The check `available_counts[d3] < current_num_counts[d3]` will always be true (since `available_counts[d3]` will be 0 and `current_num_counts[d3]` will be at least 1). Thus, `can_form` will always be `False`, and the function will correctly return `0`.
*   **`digits = [0,2,2]` (Leading zero, duplicate digits):** The approach naturally handles this. The loop starts from 100, so no leading zeros are formed. Duplicate digits like `2` are handled by `collections.Counter`, which correctly tracks that two `2`s are available.
*   **`digits = [6,6,6]` (All same digits):** `available_counts` will be `{6:3}`. When `num = 666` is checked, `current_num_counts` will be `{6:3}`. Since `available_counts[6]` is `3`, which is `>= current_num_counts[6]`, `666` is correctly counted once.
*   **`digits.length < 3`:** The problem constraints state `3 <= digits.length`, so this case is not possible.

## Solution

```python
from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # Step 1: Create a frequency map of the available digits.
        # This allows us to quickly check if we have enough copies of each digit.
        available_counts = Counter(digits)
        
        # Step 2: Initialize a counter for the distinct valid numbers found.
        total_distinct_numbers = 0
        
        # Step 3: Iterate through all possible 3-digit numbers.
        # A 3-digit number ranges from 100 to 999.
        # The loop implicitly handles the "no leading zeros" constraint
        # because numbers below 100 are not 3-digit numbers.
        for num in range(100, 1000):
            # Constraint: The number must be even.
            if num % 2 != 0:
                continue # Skip odd numbers
            
            # Extract the individual digits of the current number.
            d1 = num // 100         # Hundreds digit
            d2 = (num // 10) % 10   # Tens digit
            d3 = num % 10           # Units digit
            
            # Create a temporary frequency map for the digits of the current number.
            current_num_counts = Counter([d1, d2, d3])
            
            # Step 4: Check if the current number can be formed using the available digits.
            # We need to ensure that for each digit required by 'num', we have enough
            # copies in our 'available_counts'.
            can_form = True
            for digit, count_needed in current_num_counts.items():
                if available_counts[digit] < count_needed:
                    can_form = False
                    break # Not enough copies of this digit, so 'num' cannot be formed.
            
            # If 'can_form' is still True, it means we successfully formed this number.
            # Since we iterate through distinct 'num' values, 'total_distinct_numbers'
            # will correctly count distinct valid numbers.
            if can_form:
                total_distinct_numbers += 1
                
        # Step 5: Return the total count of distinct valid numbers.
        return total_distinct_numbers

```

## Why This Works
This solution works by **exhaustively checking every single 3-digit even number** (from 100 to 998). For each candidate number, it precisely determines if its constituent digits can be formed using the provided `digits` array. This is done by comparing the frequency of each digit required by the candidate number against the frequency of digits available in the input. The use of `collections.Counter` efficiently handles the "each copy of a digit can only be used once" rule. Since we iterate through all distinct 3-digit even numbers, and only increment our counter if a number can be formed, we naturally arrive at the correct count of **distinct** valid numbers. The small, fixed range of 3-digit numbers (900 total) makes this exhaustive check extremely efficient and well within typical time limits.

---
<sub>Generated 2026-09-11 05:05 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
