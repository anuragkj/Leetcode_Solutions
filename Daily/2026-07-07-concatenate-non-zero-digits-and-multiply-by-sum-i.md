# [3754] Concatenate Non-Zero Digits and Multiply by Sum I

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-07-07 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/)

**Topics:** Math

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer n.

Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero digits, x = 0.

Let sum be the sum of digits in x.

Return an integer representing the value of x * sum.

Example 1:

Input: n = 10203004

Output: 12340

Explanation:

- The non-zero digits are 1, 2, 3, and 4. Thus, x = 1234.

- The sum of digits is sum = 1 + 2 + 3 + 4 = 10.

- Therefore, the answer is x * sum = 1234 * 10 = 12340.

Example 2:

Input: n = 1000

Output: 1

Explanation:

- The non-zero digit is 1, so x = 1 and sum = 1.

- Therefore, the answer is x * sum = 1 * 1 = 1.

Constraints:

- 0 <= n <= 10^9

**Examples / sample tests:**

```
10203004
1000
```

---

## Problem Summary
This problem asks us to take an integer `n`, extract all its non-zero digits, and concatenate them in their original order to form a new integer `x`. If no non-zero digits exist, `x` is 0. Then, we calculate the sum of the digits of `x`. Finally, we return the product of `x` and this sum.

## Intuition
The core of this problem involves manipulating digits of a number. When we need to process digits individually, especially for concatenation, converting the number to a **string** is often the most straightforward approach in Python. This allows us to easily iterate through each character (digit) and build the new number `x` as a string before converting it back to an integer. Once `x` is formed, calculating its digit sum can be done using either string conversion again or by repeatedly taking the number modulo 10 and dividing by 10.

## Approach
We will follow a three-step process:

1.  **Form `x`**:
    *   Convert the input integer `n` into its string representation (`n_str`).
    *   Initialize an empty list, say `x_str_parts`, to store the characters of non-zero digits.
    *   Iterate through each character `digit_char` in `n_str`.
    *   If `digit_char` is not '0', append it to `x_str_parts`.
    *   After iterating, if `x_str_parts` is empty (meaning `n` contained only zeros or was 0 itself), set `x` to 0.
    *   Otherwise, join the characters in `x_str_parts` to form a string, and convert this string to an integer to get `x`.

2.  **Calculate `sum` of digits in `x`**:
    *   Initialize a variable `digit_sum` to 0.
    *   Create a temporary variable, say `current_x_for_sum`, and assign it the value of `x`. This is important to preserve the original `x` for the final multiplication.
    *   Use a `while` loop that continues as long as `current_x_for_sum` is greater than 0:
        *   Add the last digit of `current_x_for_sum` (obtained by `current_x_for_sum % 10`) to `digit_sum`.
        *   Remove the last digit from `current_x_for_sum` (obtained by integer division `current_x_for_sum //= 10`).
    *   If `x` was initially 0, this loop will not run, and `digit_sum` will correctly remain 0.

3.  **Return the result**:
    *   Return the product `x * digit_sum`.

## Visualization

```mermaid
graph TD
    A[Start with n] --> B{Convert n to string: n_str};
    B --> C{Initialize x_str_parts = []};
    C --> D{For each digit_char in n_str};
    D -- Is digit_char != '0'? --> E{Yes};
    E --> F[Append digit_char to x_str_parts];
    F --> D;
    D -- No --> D;
    D --> G{End loop};
    G --> H{Is x_str_parts empty?};
    H -- Yes --> I[Set x = 0];
    H -- No --> J[Join x_str_parts to form string, convert to int: x];
    I --> K[Initialize digit_sum = 0];
    J --> K;
    K --> L{Set current_x_for_sum = x};
    L --> M{While current_x_for_sum > 0};
    M -- Yes --> N[digit_sum += current_x_for_sum % 10];
    N --> O[current_x_for_sum //= 10];
    O --> M;
    M -- No --> P[Return x * digit_sum];
    P --> Q[End];
```

## Dry Run
Let's trace Example 1: `n = 10203004`

| Step | Variable `n_str` | Variable `x_str_parts` | Variable `x` | Variable `current_x_for_sum` | Variable `digit_sum` | Notes |
| :--- | :--------------- | :--------------------- | :----------- | :----------------------------- | :------------------- | :---- |
| 1    | "10203004"       | `[]`                   | -            | -                              | -                    | Convert `n` to string. |
| 2    | "10203004"       | `['1']`                | -            | -                              | -                    | `digit_char = '1'`, append. |
| 3    | "10203004"       | `['1']`                | -            | -                              | -                    | `digit_char = '0'`, skip. |
| 4    | "10203004"       | `['1', '2']`           | -            | -                              | -                    | `digit_char = '2'`, append. |
| 5    | "10203004"       | `['1', '2']`           | -            | -                              | -                    | `digit_char = '0'`, skip. |
| 6    | "10203004"       | `['1', '2', '3']`      | -            | -                              | -                    | `digit_char = '3'`, append. |
| 7    | "10203004"       | `['1', '2', '3']`      | -            | -                              | -                    | `digit_char = '0'`, skip. |
| 8    | "10203004"       | `['1', '2', '3']`      | -            | -                              | -                    | `digit_char = '0'`, skip. |
| 9    | "10203004"       | `['1', '2', '3', '4']` | -            | -                              | -                    | `digit_char = '4'`, append. |
| 10   | -                | `['1', '2', '3', '4']` | `1234`       | -                              | -                    | `x_str_parts` is not empty. `x = int("1234")`. |
| 11   | -                | -                      | `1234`       | `1234`                         | `0`                  | Initialize `digit_sum` and `current_x_for_sum`. |
| 12   | -                | -                      | `1234`       | `123`                          | `4`                  | `1234 % 10 = 4`. `digit_sum = 0 + 4 = 4`. `1234 //= 10 = 123`. |
| 13   | -                | -                      | `1234`       | `12`                           | `4 + 3 = 7`          | `123 % 10 = 3`. `digit_sum = 4 + 3 = 7`. `123 //= 10 = 12`. |
| 14   | -                | -                      | `1234`       | `1`                            | `7 + 2 = 9`          | `12 % 10 = 2`. `digit_sum = 7 + 2 = 9`. `12 //= 10 = 1`. |
| 15   | -                | -                      | `1234`       | `0`                            | `9 + 1 = 10`         | `1 % 10 = 1`. `digit_sum = 9 + 1 = 10`. `1 //= 10 = 0`. |
| 16   | -                | -                      | `1234`       | `0`                            | `10`                 | `current_x_for_sum` is now 0, loop ends. |
| 17   | -                | -                      | `1234`       | -                              | `10`                 | Final result: `x * digit_sum = 1234 * 10 = 12340`. |

Final Result: `12340`

## Complexity
*   **Time Complexity**: O(log N). Converting `n` to a string takes O(log N) time (where log N is the number of digits in `n`). Iterating through the digits and building `x_str_parts` takes O(log N). Converting `x_str_parts` to an integer `x` takes O(log X) time (where log X is the number of digits in `x`, which is at most log N). Calculating the sum of digits of `x` also takes O(log X) time. Since X <= N, the overall time complexity is dominated by O(log N).
*   **Space Complexity**: O(log N). Storing the string representation of `n` (`n_str`) and the list of non-zero digit characters (`x_str_parts`) each require space proportional to the number of digits in `n`, which is O(log N).

## Edge Cases
*   **`n = 0`**:
    *   `n_str` becomes "0". `x_str_parts` remains empty. `x` becomes 0.
    *   `digit_sum` for `x=0` is 0.
    *   Result: `0 * 0 = 0`. Correct.
*   **`n` contains only zeros (e.g., `n = 10000`)**:
    *   `n_str` becomes "10000". `x_str_parts` remains empty. `x` becomes 0.
    *   `digit_sum` for `x=0` is 0.
    *   Result: `0 * 0 = 0`. Correct. (Example 2 in problem statement uses `n=1000`, which has a non-zero digit. If it was `n=10000`, `x` would be 0).
*   **`n` has only one non-zero digit (e.g., `n = 1000`)**:
    *   `n_str` becomes "1000". `x_str_parts` becomes `['1']`. `x` becomes 1.
    *   `digit_sum` for `x=1` is 1.
    *   Result: `1 * 1 = 1`. Correct.
*   **`n` has all non-zero digits (e.g., `n = 123`)**:
    *   `n_str` becomes "123". `x_str_parts` becomes `['1', '2', '3']`. `x` becomes 123.
    *   `digit_sum` for `x=123` is `1+2+3 = 6`.
    *   Result: `123 * 6 = 738`. Correct.

## Solution

```python
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Convert n to a string to easily process its digits.
        n_str = str(n)

        # Step 1: Form x by concatenating non-zero digits.
        x_str_parts = []
        for digit_char in n_str:
            if digit_char != '0':
                x_str_parts.append(digit_char)

        # If no non-zero digits were found, x is 0.
        # Otherwise, join the parts and convert to an integer.
        if not x_str_parts:
            x = 0
        else:
            x = int("".join(x_str_parts))

        # Step 2: Calculate the sum of digits in x.
        digit_sum = 0
        # Use a temporary variable to calculate sum without modifying x.
        current_x_for_sum = x 
        
        # The loop correctly handles x=0 (it won't run, digit_sum remains 0).
        while current_x_for_sum > 0:
            digit_sum += current_x_for_sum % 10  # Add the last digit
            current_x_for_sum //= 10             # Remove the last digit

        # Step 3: Return x * sum.
        return x * digit_sum

```

## Why This Works
This solution works because it directly implements the problem description's steps. By converting the input number `n` to a string, we gain easy access to individual digits for filtering and concatenation. The `x_str_parts` list effectively builds the string representation of `x` by only including non-zero digits in their original order. The subsequent conversion to `int(x_str)` correctly forms the integer `x`. The `while` loop with modulo and integer division is a standard and efficient way to calculate the sum of digits of any non-negative integer. Edge cases like `n=0` or `n` containing only zeros are handled correctly by initializing `x` to 0 if `x_str_parts` remains empty, which then leads to a `digit_sum` of 0 and a final product of 0.

---
<sub>Generated 2026-07-07 04:34 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
