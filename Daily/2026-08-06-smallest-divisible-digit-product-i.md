# [3345] Smallest Divisible Digit Product I

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-08-06 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/smallest-divisible-digit-product-i/)

**Topics:** Math, Enumeration

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.

Example 1:

Input: n = 10, t = 2

Output: 10

Explanation:

The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.

Example 2:

Input: n = 15, t = 3

Output: 16

Explanation:

The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.

Constraints:

- 1 <= n <= 100

- 1 <= t <= 10

**Examples / sample tests:**

```
10
2
15
3
```

---

## Problem Summary
Given two integers `n` and `t`, find the smallest number `x` such that `x` is greater than or equal to `n`, and the product of the digits of `x` is perfectly divisible by `t`.

## Intuition
The problem asks for the **smallest number** `x` starting from `n` that satisfies a specific condition. This immediately suggests a **brute-force** approach: start checking `n`, then `n+1`, then `n+2`, and so on, until we find the first number whose digit product is divisible by `t`.

The key to why this brute-force approach is efficient enough lies in the **constraints**: `n` is at most 100, and `t` is at most 10. These are very small numbers.
- If a number contains the digit `0` (e.g., 10, 20, 100), its digit product will be `0`. Since `0` is divisible by any non-zero integer `t` (and `t >= 1`), any such number will satisfy the condition.
- Given `n <= 100`, the largest number we might need to check is `100` itself (e.g., if `n=99` and `t=7`, `99`'s product is `81` (not div by 7), but `100`'s product is `0` (div by 7)).
- The official hint confirms this: "You have to check at most 10 numbers." This means the answer will never be much larger than `n`, making a simple iterative check very fast.

## Approach
1.  **Helper Function `get_digit_product(num)`:**
    *   This function will take an integer `num` and return the product of its digits.
    *   Initialize `product = 1`.
    *   Convert `num` to a string to easily iterate through its individual digits.
    *   For each character `char_digit` in the string:
        *   Convert `char_digit` back to an integer `digit`.
        *   **Crucially:** If `digit` is `0`, immediately return `0`. This is because any product involving `0` is `0`.
        *   Otherwise, multiply `product` by `digit`.
    *   After iterating through all digits, return the final `product`.

2.  **Main Logic (Iterative Search):**
    *   Initialize a variable `current_num` with the input value `n`.
    *   Start an infinite `while True` loop (or a loop that continues until a return statement is hit).
    *   Inside the loop:
        *   Call `get_digit_product(current_num)` to get the product of its digits.
        *   Check if `digit_product % t == 0`.
        *   If the condition is true (the digit product is divisible by `t`), then `current_num` is the smallest number we're looking for. **Return `current_num`**.
        *   If the condition is false, increment `current_num` by `1` and continue to the next iteration of the loop to check the next number.

## Visualization

```mermaid
graph TD
    A[Start] --> B{Initialize current_num = n};
    B --> C{Call get_digit_product(current_num)};
    C --> D{Is digit_product % t == 0?};
    D -- Yes --> E[Return current_num];
    D -- No --> F[Increment current_num by 1];
    F --> C;
```

## Dry Run
Let's walk through **Example 1: `n = 10, t = 2`**

| `current_num` | `str(current_num)` | `digit_product` calculation | `digit_product` | `digit_product % t` (`% 2`) | Condition `== 0`? | Action |
| :------------ | :----------------- | :-------------------------- | :-------------- | :-------------------------- | :---------------- | :----- |
| 10            | "10"               | `1 * 0` (due to '0')        | 0               | `0 % 2 = 0`                 | True              | Return 10 |

Final Result: `10`

Let's walk through **Example 2: `n = 15, t = 3`**

| `current_num` | `str(current_num)` | `digit_product` calculation | `digit_product` | `digit_product % t` (`% 3`) | Condition `== 0`? | Action |
| :------------ | :----------------- | :-------------------------- | :-------------- | :-------------------------- | :---------------- | :----- |
| 15            | "15"               | `1 * 5`                     | 5               | `5 % 3 = 2`                 | False             | Increment `current_num` |
| 16            | "16"               | `1 * 6`                     | 6               | `6 % 3 = 0`                 | True              | Return 16 |

Final Result: `16`

## Complexity
*   **Time Complexity:** O(D \* K), where D is the number of digits in `current_num` and K is the number of iterations. Given `n <= 100`, `current_num` will have at most 3 digits (e.g., 100). The number of iterations `K` is very small (at most 10, as per problem hints and analysis). Therefore, both D and K are tiny constants, making the overall time complexity effectively **O(1)**.
*   **Space Complexity:** O(D) for storing the string representation of `current_num` inside the `get_digit_product` helper. Since `current_num` has at most 3 digits, this is also effectively **O(1)** constant space.

## Edge Cases
*   **`n` itself satisfies the condition:** The solution correctly checks `n` first. If its digit product is divisible by `t`, `n` is returned immediately. (e.g., `n=10, t=2` returns `10`).
*   **`t=1`:** Any integer's digit product is divisible by `1`. The solution will return `n` immediately, as `digit_product % 1 == 0` is always true. (e.g., `n=15, t=1` returns `15`).
*   **Numbers containing `0`:** If `current_num` contains a `0` (e.g., `10`, `20`, `100`), `get_digit_product` correctly returns `0`. Since `0` is divisible by any `t >= 1`, such numbers will always satisfy the condition, ensuring a quick termination of the search. (e.g., `n=99, t=7` checks `99` (prod `81`, not div by `7`), then `100` (prod `0`, div by `7`), returns `100`).
*   **Single-digit `n`:** The logic works correctly for single-digit numbers, treating them like any other number. (e.g., `n=5, t=3` checks `5` (prod `5`, not div by `3`), then `6` (prod `6`, div by `3`), returns `6`).

## Solution

```python
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def get_digit_product(num: int) -> int:
            """
            Calculates the product of the digits of a given number.
            If any digit is 0, the product is 0.
            """
            # For this problem's constraints (n >= 1), num will always be >= 1.
            # However, handling num == 0 is good practice for a general utility.
            if num == 0:
                return 0
            
            product = 1
            # Convert the number to a string to easily iterate through its digits
            s_num = str(num)
            
            for char_digit in s_num:
                digit = int(char_digit)
                if digit == 0:
                    # If any digit is 0, the entire product becomes 0.
                    # This is a crucial optimization as 0 is divisible by any t (t >= 1).
                    return 0 
                product *= digit
            return product

        current_num = n
        while True:
            # Calculate the product of digits for the current number
            digit_product = get_digit_product(current_num)
            
            # Check if the digit product is divisible by t
            if digit_product % t == 0:
                # If it is, we've found the smallest number that satisfies the condition
                return current_num
            
            # If not divisible, increment and check the next number
            current_num += 1

```

## Why This Works
This solution correctly finds the smallest number `x >= n` because it systematically checks numbers in increasing order, starting from `n`. The first number encountered that satisfies the condition (its digit product is divisible by `t`) is guaranteed to be the smallest. The problem's tight constraints (`n <= 100`, `t <= 10`) ensure that this brute-force search is extremely efficient. The maximum number of iterations is very small (at most 10 checks), and the numbers themselves are small (at most 3 digits), making the overall execution time constant and negligible. The special handling of the digit `0` in the `get_digit_product` function correctly identifies numbers whose product is `0`, which is always divisible by any `t >= 1`, further optimizing the search for common cases like `10`, `20`, or `100`.

---
<sub>Generated 2026-08-06 03:51 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
