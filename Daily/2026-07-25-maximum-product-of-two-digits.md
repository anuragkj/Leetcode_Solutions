# [3536] Maximum Product of Two Digits

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-07-25 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximum-product-of-two-digits/)

**Topics:** Math, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.

Example 1:

Input: n = 31

Output: 3

Explanation:

- The digits of n are [3, 1].

- The possible products of any two digits are: 3 * 1 = 3.

- The maximum product is 3.

Example 2:

Input: n = 22

Output: 4

Explanation:

- The digits of n are [2, 2].

- The possible products of any two digits are: 2 * 2 = 4.

- The maximum product is 4.

Example 3:

Input: n = 124

Output: 8

Explanation:

- The digits of n are [1, 2, 4].

- The possible products of any two digits are: 1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8.

- The maximum product is 8.

Constraints:

- 10 <= n <= 10^9

**Examples / sample tests:**

```
31
22
124
```

---

## Problem Summary
Given a positive integer `n`, the task is to find the largest possible product that can be formed by multiplying any two digits present in `n`. Digits can be reused if they appear multiple times in `n`.

## Intuition
To maximize the product of two positive numbers, we should choose the two largest available numbers. Since digits are always non-negative (0-9), this principle holds true. For example, if we have digits `[1, 2, 4]`, the largest two are `4` and `2`, and their product `4 * 2 = 8` is greater than `1 * 2 = 2` or `1 * 4 = 4`. This means we need to **extract all digits** from the given integer `n`, **identify the two largest digits** among them, and then **multiply them**.

## Approach
The optimal approach involves iterating through the digits of `n` and keeping track of the two largest digits encountered so far.

1.  **Initialize two variables:**
    *   `max1` to store the largest digit found (initialize to 0).
    *   `max2` to store the second largest digit found (initialize to 0).
    These initial values work because all digits are non-negative (0-9), so any actual digit will be greater than or equal to 0.

2.  **Extract digits iteratively:**
    *   Use a `while` loop that continues as long as `n` is greater than 0.
    *   In each iteration:
        a.  Get the **last digit** of `n` using the modulo operator: `digit = n % 10`.
        b.  **Compare `digit` with `max1` and `max2`**:
            *   If `digit` is **greater than `max1`**: This means we've found a new largest digit. The old `max1` now becomes the new `max2`, and `digit` becomes the new `max1`. So, `max2 = max1`, then `max1 = digit`.
            *   Else (if `digit` is not greater than `max1`), but `digit` is **greater than `max2`**: This means `digit` is not the absolute largest, but it's larger than our current second largest. So, `max2 = digit`.
        c.  **Remove the last digit** from `n` using integer division: `n = n // 10`.

3.  **Return the product:**
    *   Once the loop finishes (when `n` becomes 0), `max1` will hold the largest digit and `max2` will hold the second largest digit from the original `n`.
    *   Return `max1 * max2`.

## Visualization

Let's trace the process for `n = 124`:

```
Initial State:
max1 = 0
max2 = 0
n    = 124

Iteration 1:
  digit = 124 % 10 = 4
  n     = 124 // 10 = 12

  Is 4 > max1 (0)? Yes.
    max2 = max1 (0)  => max2 = 0
    max1 = 4         => max1 = 4

  Current State: max1=4, max2=0, n=12

Iteration 2:
  digit = 12 % 10 = 2
  n     = 12 // 10 = 1

  Is 2 > max1 (4)? No.
  Is 2 > max2 (0)? Yes.
    max2 = 2         => max2 = 2

  Current State: max1=4, max2=2, n=1

Iteration 3:
  digit = 1 % 10 = 1
  n     = 1 // 10 = 0

  Is 1 > max1 (4)? No.
  Is 1 > max2 (2)? No.

  Current State: max1=4, max2=2, n=0

Loop Ends (n is 0)

Final Result: max1 * max2 = 4 * 2 = 8
```

## Dry Run
Let's walk through Example 1: `n = 31`

Initial state: `max1 = 0`, `max2 = 0`

| Step | `n` | `digit` (`n % 10`) | `digit > max1`? | `digit > max2`? (if prev false) | Action                               | `max1` | `max2` |
| :--- | :-- | :----------------- | :-------------- | :------------------------------ | :----------------------------------- | :----- | :----- |
| Start| 31  |                    |                 |                                 | Initial                              | 0      | 0      |
| 1    | 31  | 1                  | Yes (1 > 0)     | (skipped)                       | `max2 = max1` (0), `max1 = 1`        | 1      | 0      |
|      | 3   |                    |                 |                                 | `n = 31 // 10 = 3`                   |        |        |
| 2    | 3   | 3                  | Yes (3 > 1)     | (skipped)                       | `max2 = max1` (1), `max1 = 3`        | 3      | 1      |
|      | 0   |                    |                 |                                 | `n = 3 // 10 = 0`                    |        |        |
| End  | 0   |                    |                 |                                 | Loop terminates                      |        |        |

Final `max1 = 3`, `max2 = 1`.
Result: `max1 * max2 = 3 * 1 = 3`. This matches the example output.

## Complexity
*   **Time Complexity:** O(log N). The number of iterations in the `while` loop is proportional to the number of digits in `n`. For an integer `n`, the number of digits is `floor(log10(n)) + 1`. Since `n` is at most `10^9`, it has at most 10 digits. This makes the operation count very small and effectively constant.
*   **Space Complexity:** O(1). We only use a few constant-size variables (`max1`, `max2`, `digit`, `n`) regardless of the input `n`.

## Edge Cases
*   **`n` with two identical digits (e.g., `n = 22`):** The logic correctly handles this. The first `2` sets `max1 = 2, max2 = 0`. The second `2` is not greater than `max1` (2), but it is greater than `max2` (0), so `max2` becomes `2`. The final product is `2 * 2 = 4`.
*   **`n` containing zero (e.g., `n = 105`):** If `0` is one of the two largest digits (e.g., `n=10`), the product will correctly be `0`. If `0` is not among the two largest, it will be ignored by the comparison logic. For `n=105`, `max1` becomes `5`, `max2` becomes `1`, and `0` is ignored, resulting in `5 * 1 = 5`.
*   **Minimum `n` (10):** The smallest `n` is `10`. The digits are `1` and `0`. `max1` becomes `1`, `max2` becomes `0`. The product is `1 * 0 = 0`. This is correct.

## Solution

```python
class Solution:
    def maxProduct(self, n: int) -> int:
        max1 = 0  # Stores the largest digit found
        max2 = 0  # Stores the second largest digit found

        # Iterate through the digits of n
        while n > 0:
            digit = n % 10  # Get the last digit

            if digit > max1:
                # If current digit is greater than the largest found so far,
                # the old max1 becomes the new max2, and current digit becomes max1.
                max2 = max1
                max1 = digit
            elif digit > max2:
                # If current digit is not the largest, but is greater than the
                # second largest found so far, it becomes the new max2.
                max2 = digit

            n //= 10  # Remove the last digit (integer division)

        # The product of the two largest digits found
        return max1 * max2

```

## Why This Works
This solution works because to maximize the product of two non-negative numbers (which digits are), we must select the two largest available numbers. By iterating through each digit of `n` and maintaining `max1` and `max2` as the largest and second largest digits encountered *so far*, we guarantee that by the end of the process, `max1` will hold the absolute largest digit in `n` and `max2` will hold the absolute second largest digit in `n`. Multiplying these two values then correctly yields the maximum possible product as required by the problem.

---
<sub>Generated 2026-07-25 03:50 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
