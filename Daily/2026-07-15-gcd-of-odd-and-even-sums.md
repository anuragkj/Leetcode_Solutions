# [3658] GCD of Odd and Even Sums

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-07-15 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/gcd-of-odd-and-even-sums/)

**Topics:** Math, Number Theory

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer n. Your task is to compute the GCD (greatest common divisor) of two values:

-
	sumOdd: the sum of the smallest n positive odd numbers.

-
	sumEven: the sum of the smallest n positive even numbers.

Return the GCD of sumOdd and sumEven.

Example 1:

Input: n = 4

Output: 4

Explanation:

- Sum of the first 4 odd numbers sumOdd = 1 + 3 + 5 + 7 = 16

- Sum of the first 4 even numbers sumEven = 2 + 4 + 6 + 8 = 20

Hence, GCD(sumOdd, sumEven) = GCD(16, 20) = 4.

Example 2:

Input: n = 5

Output: 5

Explanation:

- Sum of the first 5 odd numbers sumOdd = 1 + 3 + 5 + 7 + 9 = 25

- Sum of the first 5 even numbers sumEven = 2 + 4 + 6 + 8 + 10 = 30

Hence, GCD(sumOdd, sumEven) = GCD(25, 30) = 5.

Constraints:

- 1 <= n <= 10​​​​​​​00

**Examples / sample tests:**

```
4
5
```

---

## Problem Summary
The task is to calculate the **greatest common divisor (GCD)** of two specific sums: `sumOdd` (the sum of the first `n` positive odd numbers) and `sumEven` (the sum of the first `n` positive even numbers), given an integer `n`.

## Intuition
Let's start by looking at the sums for small values of `n` to find a pattern:

*   **n = 1:**
    *   `sumOdd = 1`
    *   `sumEven = 2`
    *   `GCD(1, 2) = 1`
*   **n = 2:**
    *   `sumOdd = 1 + 3 = 4`
    *   `sumEven = 2 + 4 = 6`
    *   `GCD(4, 6) = 2`
*   **n = 3:**
    *   `sumOdd = 1 + 3 + 5 = 9`
    *   `sumEven = 2 + 4 + 6 = 12`
    *   `GCD(9, 12) = 3`
*   **n = 4 (Example 1):**
    *   `sumOdd = 1 + 3 + 5 + 7 = 16`
    *   `sumEven = 2 + 4 + 6 + 8 = 20`
    *   `GCD(16, 20) = 4`

Notice a pattern? The GCD seems to be exactly `n`! This is a strong hint that there's a mathematical shortcut.

Let's recall the formulas for these sums:
1.  The sum of the first `n` positive odd numbers is `n * n` (or `n^2`).
    *   `sumOdd = 1 + 3 + ... + (2n - 1) = n^2`
2.  The sum of the first `n` positive even numbers is `n * (n + 1)`.
    *   `sumEven = 2 + 4 + ... + (2n) = n * (n + 1)`

Now, the problem boils down to finding `GCD(n^2, n * (n + 1))`.
We can use a fundamental property of GCD: `GCD(a*k, b*k) = k * GCD(a, b)`.
Applying this, we can factor out `n`:
`GCD(n * n, n * (n + 1)) = n * GCD(n, n + 1)`

Finally, consider `GCD(n, n + 1)`. Any two consecutive positive integers are **coprime**, meaning their greatest common divisor is always **1**.
*   For example, `GCD(4, 5) = 1`, `GCD(9, 10) = 1`.
So, `GCD(n, n + 1) = 1`.

Substituting this back into our expression:
`n * GCD(n, n + 1) = n * 1 = n`.

Thus, the GCD of `sumOdd` and `sumEven` is simply `n`.

## Approach
1.  **Identify Sum Formulas:** Recognize or recall that the sum of the first `n` positive odd numbers (`sumOdd`) is `n * n`, and the sum of the first `n` positive even numbers (`sumEven`) is `n * (n + 1)`.
2.  **Formulate GCD Expression:** The problem then becomes computing `GCD(n * n, n * (n + 1))`.
3.  **Apply GCD Property:** Use the property `GCD(a*k, b*k) = k * GCD(a, b)` to factor out `n`. This transforms the expression to `n * GCD(n, n + 1)`.
4.  **Simplify Consecutive GCD:** Recognize that the greatest common divisor of any two consecutive positive integers (`n` and `n + 1`) is always `1`. So, `GCD(n, n + 1) = 1`.
5.  **Final Calculation:** Substitute `1` back into the expression: `n * 1 = n`.
6.  **Return Result:** The final answer is `n`.

## Visualization
```mermaid
graph TD
    A[Start with n] --> B{Calculate sumOdd and sumEven};
    B --> C1[sumOdd = 1 + 3 + ... + (2n-1)];
    B --> C2[sumEven = 2 + 4 + ... + (2n)];
    C1 --> D1[sumOdd = n * n];
    C2 --> D2[sumEven = n * (n + 1)];
    D1 & D2 --> E{Find GCD(sumOdd, sumEven)};
    E --> F[GCD(n * n, n * (n + 1))];
    F --> G{Factor out n using GCD(ak, bk) = k * GCD(a, b)};
    G --> H[n * GCD(n, n + 1)];
    H --> I{Property: GCD(x, x+1) = 1};
    I --> J[n * 1];
    J --> K[Result: n];
```

## Dry Run
Let's walk through **Example 1: `n = 4`**

| Step | `n` | `sumOdd` (Formula) | `sumEven` (Formula) | `GCD(sumOdd, sumEven)` Calculation | Result |
| :--- | :-- | :----------------- | :------------------ | :--------------------------------- | :----- |
| 1    | 4   | `4 * 4 = 16`       | `4 * (4 + 1) = 20`  | `GCD(16, 20)`                      |        |
| 2    |     |                    |                     | `GCD(4 * 4, 4 * 5)`                |        |
| 3    |     |                    |                     | `4 * GCD(4, 5)`                    |        |
| 4    |     |                    |                     | `4 * 1`                            |        |
| 5    |     |                    |                     |                                    | **4**  |

The final result is 4, which matches the example output.

## Complexity
*   **Time Complexity:** O(1)
    *   The solution involves a direct return of the input `n`. No loops, recursive calls, or complex operations are performed.
*   **Space Complexity:** O(1)
    *   No additional data structures are used. The memory usage is constant, regardless of the input `n`.

## Edge Cases
*   **`n = 1` (Minimum Constraint):**
    *   `sumOdd = 1`
    *   `sumEven = 2`
    *   `GCD(1, 2) = 1`. Our solution returns `n = 1`. Correct.
*   **`n = 1000` (Maximum Constraint):**
    *   `sumOdd = 1000 * 1000 = 1,000,000`
    *   `sumEven = 1000 * 1001 = 1,001,000`
    *   `GCD(1,000,000, 1,001,000) = 1000 * GCD(1000, 1001) = 1000 * 1 = 1000`. Our solution returns `n = 1000`. Correct.

The solution correctly handles the minimum and maximum constraints, demonstrating its robustness for all valid inputs.

## Solution

```python
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # The sum of the first n positive odd numbers (sumOdd) is n * n.
        # For example:
        # n=1: 1 = 1*1
        # n=2: 1+3 = 4 = 2*2
        # n=3: 1+3+5 = 9 = 3*3
        # So, sumOdd = n * n

        # The sum of the first n positive even numbers (sumEven) is n * (n + 1).
        # For example:
        # n=1: 2 = 1*(1+1)
        # n=2: 2+4 = 6 = 2*(2+1)
        # n=3: 2+4+6 = 12 = 3*(3+1)
        # So, sumEven = n * (n + 1)

        # We need to compute GCD(sumOdd, sumEven)
        # This translates to GCD(n * n, n * (n + 1))

        # Using the GCD property: GCD(a*k, b*k) = k * GCD(a, b)
        # We can factor out 'n' from both terms:
        # GCD(n * n, n * (n + 1)) = n * GCD(n, n + 1)

        # A fundamental property of GCD is that for any positive integer x,
        # GCD(x, x + 1) = 1 (i.e., any two consecutive integers are coprime).
        # Therefore, GCD(n, n + 1) = 1.

        # Substituting this back into our expression:
        # n * GCD(n, n + 1) = n * 1 = n

        # The final result is simply n.
        return n

```

## Why This Works
This solution works because it leverages well-known mathematical properties. First, the sums of the first `n` odd and even numbers simplify to `n^2` and `n*(n+1)` respectively. Second, the **greatest common divisor (GCD)** has a distributive property: `GCD(a*k, b*k) = k * GCD(a, b)`. Applying this, we factor out `n` from `GCD(n^2, n*(n+1))` to get `n * GCD(n, n+1)`. Finally, a crucial property of consecutive integers is that their GCD is always `1` (e.g., `GCD(4, 5) = 1`). Therefore, `GCD(n, n+1)` simplifies to `1`, making the entire expression `n * 1 = n`.

---
<sub>Generated 2026-07-15 03:46 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
