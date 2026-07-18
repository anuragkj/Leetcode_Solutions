# [1979] Find Greatest Common Divisor of Array

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-07-18 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)

**Topics:** Array, Math, Number Theory

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

Example 1:

Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.

Example 2:

Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.

Example 3:

Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.

Constraints:

- 2 <= nums.length <= 1000

- 1 <= nums[i] <= 1000

**Examples / sample tests:**

```
[2,5,6,9,10]
[7,5,6,8,3]
[3,3]
```

---

## Problem Summary
Given an array of integers, the task is to find the **smallest number** and the **largest number** within that array. Then, we need to calculate and return the **greatest common divisor (GCD)** of these two identified numbers.

## Intuition
The problem breaks down into two main parts:
1.  **Finding the smallest and largest numbers**: This is a standard operation. We can iterate through the array once, keeping track of the minimum and maximum values seen so far. Python's built-in `min()` and `max()` functions can do this efficiently.
2.  **Calculating the Greatest Common Divisor (GCD)**: The GCD of two numbers is the largest positive integer that divides both numbers without leaving a remainder. For example, GCD(10, 2) is 2, because 2 divides both 10 (10/2=5) and 2 (2/2=1), and no larger number does.
    *   A straightforward way to find the GCD of two numbers, say `a` and `b`, is to start checking from the **smaller** of the two numbers, downwards to 1. The **first number** we find that divides both `a` and `b` evenly will be their GCD. This is because a common divisor cannot be larger than the smaller of the two numbers, and by checking downwards, we guarantee finding the *greatest* one first.

## Approach
1.  **Find Minimum and Maximum**: Iterate through the input array `nums` to find its smallest element (`min_val`) and its largest element (`max_val`). Alternatively, use Python's built-in `min(nums)` and `max(nums)` for conciseness and efficiency.
2.  **Implement GCD Function**: Create a helper function, say `_gcd(a, b)`, that takes two integers `a` and `b` and returns their greatest common divisor.
    *   Inside `_gcd(a, b)`:
        *   Determine the **upper limit** for checking divisors. This limit is the smaller of `a` and `b` (e.g., `limit = min(a, b)`).
        *   Loop downwards from `limit` to `1` (inclusive). Let the current number in the loop be `i`.
        *   In each iteration, check if `i` divides both `a` and `b` evenly. This means `a % i == 0` AND `b % i == 0`.
        *   If both conditions are true, `i` is a common divisor. Since we are iterating downwards, the *first* `i` we find that satisfies this condition will be the **greatest common divisor**. Return `i` immediately.
        *   (Optional, but good practice) If the loop finishes without finding any common divisor (which should only happen if `a` or `b` is 0, but problem constraints state `nums[i] >= 1`), return 1, as 1 is always a common divisor for positive integers.
3.  **Call and Return**: In the main `findGCD` method, call the `_gcd` helper function with `min_val` and `max_val` as arguments, and return its result.

## Visualization

Let's visualize the GCD finding process for `min_val = 2` and `max_val = 10`.

```mermaid
graph TD
    A[Start: nums = [2,5,6,9,10]] --> B{Find min and max}
    B --> C[min_val = 2]
    B --> D[max_val = 10]
    C & D --> E{Calculate GCD(min_val, max_val)}
    E --> F[GCD_Helper(a=2, b=10)]

    subgraph GCD_Helper(a, b)
        F --> G[limit = min(a, b) = 2]
        G --> H{Loop i from limit (2) down to 1}
        H --> I{i = 2}
        I --> J{Is 2 % 2 == 0 AND 10 % 2 == 0?}
        J -- Yes --> K[Return 2]
        J -- No --> L{i = 1}
        L --> M{Is 2 % 1 == 0 AND 10 % 1 == 0?}
        M -- Yes --> N[Return 1]
        N -- No --> O[End Loop]
    end

    K --> P[Result: 2]
    P --> Q[End]
```

## Dry Run
Let's walk through **Example 1: `nums = [2,5,6,9,10]`**

| Step | Action | `nums` | `min_val` | `max_val` | `i` (in GCD) | `min_val % i == 0` | `max_val % i == 0` | Result |
| :--- | :----- | :----- | :-------- | :-------- | :----------- | :----------------- | :----------------- | :----- |
| 1    | Initialize | `[2,5,6,9,10]` | -         | -         | -            | -                  | -                  | -      |
| 2    | Find `min_val` | `[2,5,6,9,10]` | `2`       | -         | -            | -                  | -                  | -      |
| 3    | Find `max_val` | `[2,5,6,9,10]` | `2`       | `10`      | -            | -                  | -                  | -      |
| 4    | Call `_gcd(2, 10)` | - | `2`       | `10`      | -            | -                  | -                  | -      |
| 5    | `_gcd`: `limit = min(2, 10)` | - | `2`       | `10`      | `2`          | -                  | -                  | -      |
| 6    | `_gcd`: Loop `i = 2` | - | `2`       | `10`      | `2`          | `2 % 2 == 0` (True) | `10 % 2 == 0` (True) | -      |
| 7    | `_gcd`: Both true, return `i` | - | `2`       | `10`      | `2`          | True               | True               | `2`    |
| 8    | Final Result | - | -         | -         | -            | -                  | -                  | `2`    |

The final result is **2**.

## Complexity
*   **Time Complexity**: O(N + M)
    *   Finding the minimum and maximum elements in `nums` takes O(N) time, where N is the number of elements in `nums`.
    *   The GCD calculation iterates from `min_val` down to 1. In the worst case, `min_val` can be up to 1000 (as per constraints `nums[i] <= 1000`). So, this part takes O(min_val) time.
    *   Overall, the time complexity is dominated by these two steps, resulting in O(N + min_val). Given N <= 1000 and `min_val` <= 1000, this is very efficient.
*   **Space Complexity**: O(1)
    *   We only use a few variables to store `min_val`, `max_val`, and loop counters. This amount of space does not grow with the input size.

## Edge Cases
*   **`nums` with identical elements**: E.g., `nums = [3,3]`.
    *   `min_val` will be 3, `max_val` will be 3.
    *   `_gcd(3, 3)` will correctly return 3. (Loop `i=3`: `3%3==0` and `3%3==0`, return 3).
*   **`nums` where min and max are coprime (GCD is 1)**: E.g., `nums = [7,5,6,8,3]`.
    *   `min_val` will be 3, `max_val` will be 8.
    *   `_gcd(3, 8)` will iterate:
        *   `i=3`: `3%3==0` (True), `8%3!=0` (False).
        *   `i=2`: `3%2!=0` (False).
        *   `i=1`: `3%1==0` (True), `8%1==0` (True). Return 1.
    *   The solution correctly handles this by finding 1 as the GCD.
*   **Smallest possible `nums.length` (2 elements)**: E.g., `nums = [4, 6]`.
    *   `min_val` will be 4, `max_val` will be 6.
    *   `_gcd(4, 6)` will correctly return 2.
*   **Constraints on `nums[i]` (1 to 1000)**: All numbers are positive, so GCD will always be at least 1. The brute-force GCD approach works perfectly for positive integers.

## Solution

```python
from typing import List

class Solution:
    def _gcd(self, a: int, b: int) -> int:
        """
        Helper function to calculate the greatest common divisor of two positive integers.
        Uses the brute-force method by checking divisors downwards from min(a, b).
        """
        # The GCD cannot be greater than the smaller of the two numbers.
        # We iterate downwards from this limit to find the largest common divisor first.
        limit = min(a, b)
        for i in range(limit, 0, -1): # Iterate from limit down to 1
            if a % i == 0 and b % i == 0:
                return i
        return 1 # Should not be reached for positive a, b as 1 always divides both.

    def findGCD(self, nums: List[int]) -> int:
        # Step 1: Find the smallest number in the array.
        min_val = min(nums)
        
        # Step 2: Find the largest number in the array.
        max_val = max(nums)
        
        # Step 3: Calculate and return the GCD of the smallest and largest numbers.
        return self._gcd(min_val, max_val)

```

## Why This Works
This solution works because it correctly identifies the two numbers required by the problem (the smallest and largest in the array) using standard `min()` and `max()` operations. The core of the solution lies in the `_gcd` helper function. By iterating downwards from the smaller of the two numbers (`limit`) to 1, the very first number `i` that divides both `a` and `b` evenly is guaranteed to be the **greatest** common divisor. Any larger number would have been found earlier in the downward iteration, and any smaller common divisor is not the *greatest*. This systematic check ensures correctness for all positive integer inputs.

---
<sub>Generated 2026-07-18 03:42 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
