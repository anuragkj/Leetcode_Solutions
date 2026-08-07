# [3348] Smallest Divisible Digit Product II

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-08-07 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/smallest-divisible-digit-product-ii/)

**Topics:** Math, String, Backtracking, Greedy, Number Theory

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a string num which represents a positive integer, and an integer t.

A number is called zero-free if none of its digits are 0.

Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return "-1".

Example 1:

Input: num = "1234", t = 256

Output: "1488"

Explanation:

The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

Example 2:

Input: num = "12355", t = 50

Output: "12355"

Explanation:

12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

Example 3:

Input: num = "11111", t = 26

Output: "-1"

Explanation:

No number greater than 11111 has the product of its digits divisible by 26.

Constraints:

- 2 <= num.length <= 2 * 10^5

- num consists only of digits in the range ['0', '9'].

- num does not contain leading zeros.

- 1 <= t <= 10^14

**Examples / sample tests:**

```
"1234"
256
"12355"
50
"11111"
26
```

---

This problem asks us to find the smallest "zero-free" number (no digit 0) greater than or equal to a given number `num`, such that the product of its digits is divisible by `t`.

## Problem Summary
Find the smallest positive integer `X` that is zero-free (contains no '0' digits) and `X >= num`, such that the product of `X`'s digits is divisible by `t`. Return `"-1"` if no such number exists.

## Intuition
The core idea revolves around finding the smallest number, which implies two priorities:
1.  **Fewer digits are better.** A number with `L` digits is always smaller than a number with `L+1` digits (for `L > 0`).
2.  **Lexicographical smallest.** If two numbers have the same number of digits, the one with smaller digits at more significant positions is smaller (e.g., `123` < `132`).

The divisibility condition `product(digits) % t == 0` is tricky. Since digits are 1-9, their prime factors can only be 2, 3, 5, 7. If `t` has any other prime factor (e.g., 11), it's impossible to satisfy the condition, so we can immediately return `"-1"`. Otherwise, we need to ensure the product of digits collectively provides enough factors of 2, 3, 5, and 7 to cover `t`'s prime factorization.

We can approach this by trying to construct the smallest possible number `X` in a greedy fashion:
-   First, try to find an `X` with the same number of digits as `num` (`N`).
-   If no such `X` exists, try to find an `X` with `N+1` digits. This will be the smallest `N+1` digit number that satisfies the condition.

To find the smallest `N`-digit number `X >= num`:
We iterate through `num` from left to right (most significant digit to least significant). At each position `i`:
1.  **Try to change `num[i]` to a larger digit `d`**: If we pick a `d > num[i]` (or `d >= 1` if `num[i]` is '0'), then the prefix `num[0...i-1] + d` is already greater than `num[0...i]`. This means all subsequent digits (from `i+1` to `N-1`) can be chosen as `1`s to make the number as small as possible, and then we append the necessary digits to satisfy `t`'s remaining prime factor requirements. This is a greedy strategy for the suffix.
2.  **Keep `num[i]`**: If `num[i]` is not '0', we can keep it and continue to the next position `i+1`, accumulating its prime factors. If `num[i]` is '0', we *must* change it (or a previous digit), as the number must be zero-free.

This approach ensures we find the lexicographically smallest `N`-digit number `X >= num` by trying changes at the earliest possible position `i` and using the smallest possible digit `d` at that position, followed by the smallest possible suffix.

## Approach
The solution involves several helper functions and a main logic flow:

1.  **Precompute Prime Factors for Digits (1-9):**
    Create a map `prime_factors_map` where `prime_factors_map[d]` stores the prime factorization of digit `d` (e.g., `prime_factors_map[

---
<sub>Generated 2026-08-07 03:33 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
