# [3723] Maximize Sum of Squares of Digits

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-10-14 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximize-sum-of-squares-of-digits/)

**Topics:** Math, Greedy

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given two positive integers num and sum.

A positive integer n is good if it satisfies both of the following:

- The number of digits in n is exactly num.

- The sum of digits in n is exactly sum.

The score of a good integer n is the sum of the squares of digits in n.

Return a string denoting the good integer n that achieves the maximum score. If there are multiple possible integers, return the maximum ​​​​​​​one. If no such integer exists, return an empty string.

Example 1:

Input: num = 2, sum = 3

Output: "30"

Explanation:

There are 3 good integers: 12, 21, and 30.

- The score of 12 is 1^2 + 2^2 = 5.

- The score of 21 is 2^2 + 1^2 = 5.

- The score of 30 is 3^2 + 0^2 = 9.

The maximum score is 9, which is achieved by the good integer 30. Therefore, the answer is "30".

Example 2:

Input: num = 2, sum = 17

Output: "98"

Explanation:

There are 2 good integers: 89 and 98.

- The score of 89 is 8^2 + 9^2 = 145.

- The score of 98 is 9^2 + 8^2 = 145.

The maximum score is 145. The maximum good integer that achieves this score is 98. Therefore, the answer is "98".

Example 3:

Input: num = 1, sum = 10

Output: ""

Explanation:

There are no integers that have exactly 1 digit and whose digits sum to 10. Therefore, the answer is "".

Constraints:

- 1 <= num <= 2 * 10^5

- 1 <= sum <= 2 * 10^6

**Examples / sample tests:**

```
2
3
2
17
1
10
```

---

## Problem Summary
You are given a desired number of digits (`num`) and a target sum of digits (`sum`). Your task is to find a positive integer `n` that has exactly `num` digits and whose digits sum up to `sum`. Among all such valid integers, you need to find the one that maximizes the "score" (sum of squares of its digits). If there are multiple integers with the same maximum score, return the largest one. If no such integer exists, return an empty string.

## Intuition
Let's break down the problem into two parts: maximizing the **score** and maximizing the **integer** itself.

1.  **Maximizing the Score (Sum of Squares of Digits):**
    Consider two digits, `a` and `b`, whose sum is constant, say `S = a + b`. We want to maximize `a^2 + b^2`.
    Let's test some examples for `S=9`:
    *   `0 + 9`: `0^2 + 9^2 = 0 + 81 = 81`
    *   `1 + 8`: `1^2 + 8^2 = 1 + 64 = 65`
    *   `2 + 7`: `2^2 + 7^2 = 4 + 49 = 53`
    *   `3 + 6`: `3^2 + 6^2 = 9 + 36 = 45`
    *   `4 + 5`: `4^2 + 5^2 = 16 + 25 = 41`
    Notice a pattern: the sum of squares is maximized when the digits are **as far apart as possible** (e.g., `0` and `9` instead of `4` and `5`). This means to maximize the score, we should use as many `9`s as possible, and then fill the remaining sum into one digit, with the rest being `0`s.

2.  **Maximizing the Integer:**
    If multiple numbers achieve the maximum score, we need to return the largest one. To make an integer as large as possible, we should place larger digits in the more significant (leftmost) positions. For example, `98` is greater than `89`.

Combining these two insights, a **greedy approach** seems appropriate:
We want to fill the `num` digit positions from left to right. At each position, we should try to place the **largest possible digit** (up to `9`). This choice must be valid, meaning the remaining `sum` can still be formed by the remaining `num` digits. By prioritizing `9`s from left to right, we simultaneously maximize the number and, due to the property observed above, also maximize the sum of squares.

## Approach
The algorithm proceeds as follows:

1.  **Initial Validity Check**:
    *   Calculate the minimum possible sum for `num` digits (all `1`s): `min_sum = num * 1`.
    *   Calculate the maximum possible sum for `num` digits (all `9`s): `max_sum = num * 9`.
    *   If `sum` is less than `min_sum` or greater than `max_sum`, it's impossible to form such a number. Return an empty string `""`.

2.  **Greedy Digit Construction**:
    *   Initialize an empty list, `result_digits`, to store the digits of our number.
    *   Iterate `num` times (once for each digit position, from left to right). Let `i` be the current digit index (0-indexed).
    *   For the current position `i`, we need to determine the largest possible digit `d` (from `0` to `9`) that we can place. This digit `d` must satisfy two conditions:
        *   `0 <= d <= 9`: `d` must be a valid digit.
        *   The remaining sum (`current_sum - d`) must be achievable by the remaining `num - 1 - i` digits.
            *   The minimum sum for `num - 1 - i` digits is `0` (if all remaining digits are `0`).
            *   The maximum sum for `num - 1 - i` digits is `9 * (num - 1 - i)` (if all remaining digits are `9`).
            *   So, we need `0 <= current_sum - d <= 9 * (num - 1 - i)`.
            *   From `current_sum - d >= 0`, we get `d <= current_sum`.
            *   From `current_sum - d <= 9 * (num - 1 - i)`, we get `d >= current_sum - 9 * (num - 1 - i)`.
        *   Combining all conditions, the valid range for `d` is:
            `max(0, current_sum - 9 * (num - 1 - i)) <= d <= min(9, current_sum)`
    *   To maximize the resulting integer, we choose the **largest possible `d`** from this valid range.
    *   So, `digit_to_place = min(9, current_sum)`. (This is the upper bound).
    *   But we also need to respect the lower bound: `digit_to_place = max(digit_to_place, current_sum - 9 * (num - 1 - i))`.
    *   A simpler way to think about it: we want to place `9` if possible. If not, we try `8`, and so on, down to `0`.
        *   Start with `d = 9`.
        *   While `d` is too large (i.e., `current_sum - d` cannot be formed by the remaining `num - 1 - i` digits, specifically if `current_sum - d > 9 * (num - 1 - i)`), decrement `d`.
        *   This simplifies to: `digit_to_place = min(9, current_sum - max(0, (num - 1 - i) * 0))` is not correct.
        *   The correct logic for `digit_to_place` is:
            `digit_to_place = min(9, current_sum)`
            `digit_to_place = max(digit_to_place, current_sum - 9 * (num - (i + 1)))`
            Where `num - (i + 1)` is the count of remaining digits.
            Let `remaining_digits_count = num - 1 - i`.
            `digit_to_place = min(9, current_sum - max(0, current_sum - 9 * remaining_digits_count))`
            No, this is still confusing. Let's use the bounds directly.
            The largest digit we can place is `d_max = min(9, current_sum)`.
            The smallest digit we *must* place to ensure the remaining sum is not too large for the remaining digits is `d_min = max(0, current_sum - 9 * (num - 1 - i))`.
            We want to pick the largest possible digit. So, we pick `d_max` *unless* `d_max` is smaller than `d_min`.
            Therefore, the digit to place is `max(d_min, d_max)`? No, it's `min(9, current_sum)` but also `d >= current_sum - 9 * (num - 1 - i)`.
            So, the digit to place is `min(9, current_sum)` but also `d` must be at least `current_sum - 9 * (num - 1 - i)`.
            This means the digit is `min(9, current_sum)` but also `max(0, current_sum - 9 * (num - 1 - i))`.
            The largest digit we can place is `min(9, current_sum)` *if* `current_sum - min(9, current_sum)` can be formed by `num - 1 - i` digits.
            The correct logic is:
            `digit_to_place = min(9, current_sum)`
            `digit_to_place = max(digit_to_place, current_sum - 9 * (num - 1 - i))`
            This is the largest digit `d` such that `d <= 9` and `d` is large enough that `current_sum - d` doesn't exceed `9 * (num - 1 - i)`.
            Let's re-verify with examples.
            `num=2, sum=3`.
            `i=0`: `current_sum=3`, `remaining_digits_count = 1`.
                `digit_to_place = min(9, 3)` (this is `3`)
                `digit_to_place = max(3, 3 - 9 * 1)` (this is `max(3, -6) = 3`)
                So, `d=3`. Add `3` to `result_digits`. `current_sum = 0`.
            `i=1`: `current_sum=0`, `remaining_digits_count = 0`.
                `digit_to_place = min(9, 0)` (this is `0`)
                `digit_to_place = max(0, 0 - 9 * 0)` (this is `max(0, 0) = 0`)
                So, `d=0`. Add `0` to `result_digits`. `current_sum = 0`.
            Result: `"30"`. This works!

3.  **Final Result**:
    *   Join the digits in `result_digits` to form a string and return it.

## Visualization

Imagine `num` empty slots for digits:

```
[ _ ] [ _ ] [ _ ] ... [ _ ]
```

We fill them from left to right:

**Step 1: First digit (index 0)**
*   `current_sum = sum`
*   `remaining_digits_count = num - 1`
*   Calculate `d_min = max(0, current_sum - 9 * remaining_digits_count)`
    *   This is the smallest digit we *must* place to ensure the remaining sum can be formed by the remaining digits (even if they are all `9`s).
*   Calculate `d_max = min(9, current_sum)`
    *   This is the largest digit we *can* place without exceeding `9` or `current_sum`.
*   The digit to place is `d = min(d_max, current_sum - d_min)`? No.
*   The digit to place is `d = min(d_max, current_sum - (num - 1 - i) * 0)`
*   The digit `d` must be `min(9, current_sum)` AND `d >= current_sum - 9 * (num - 1 - i)`.
*   So, we pick `d = min(9, current_sum)`. If this `d` is too small, i.e., `current_sum - d > 9 * (num - 1 - i)`, then we must pick a larger `d`.
*   The largest possible digit `d` at the current position `i` is `min(9, current_sum)`.
*   However, this `d` must also be large enough such that the remaining sum `current_sum - d` can be formed by the remaining `num - 1 - i` digits. The maximum sum for these remaining digits is `9 * (num - 1 - i)`.
*   So, `current_sum - d <= 9 * (num - 1 - i)`. This implies `d >= current_sum - 9 * (num - 1 - i)`.
*   Therefore, the digit we place is `d = min(9, max(0, current_sum - 9 * (num - 1 - i)))` is for smallest number.
*   The digit we place is `d = min(9, current_sum - max(0, current_sum - 9 * (num - 1 - i)))` is for largest number.

Let's simplify the `digit_to_place` calculation:
We want to place the largest possible digit `d` at the current position.
`d` must be `0 <= d <= 9`.
`d` must also be such that `current_sum - d` can be formed by `remaining_digits_count` digits.
This means `0 <= current_sum - d <= 9 * remaining_digits_count`.
From `current_sum - d >= 0`, we get `d <= current_sum`.
From `current_sum - d <= 9 * remaining_digits_count`, we get `d >= current_sum - 9 * remaining_digits_count`.
So, `d` must be in the range `[max(0, current_sum - 9 * remaining_digits_count), min(9, current_sum)]`.
To maximize the number, we pick the **largest value** from this range.
Thus, `digit_to_place = min(9, current_sum)`.
But this `digit_to_place` must also be at least `max(0, current_sum - 9 * remaining_digits_count)`.
So, `digit_to_place = min(9, current_sum)`
`digit_to_place = max(digit_to_place, current_sum - 9 * remaining_digits_count)`
This is the correct logic.

```
Initial: num = N, sum = S
Digits: [ _ ] [ _ ] [ _ ] ... [ _ ]  (N slots)

Loop for i from 0 to N-1 (current digit position):
  remaining_digits_count = N - 1 - i

  # Calculate the largest possible digit 'd' for the current slot:
  # 1. 'd' cannot be greater than 9.
  # 2. 'd' cannot be greater than the current remaining 'sum'.
  # 3. 'd' must be large enough so that the 'current_sum - d'
  #    can be formed by the 'remaining_digits_count' digits.
  #    (i.e., current_sum - d <= 9 * remaining_digits_count)
  #    This implies d >= current_sum - 9 * remaining_digits_count.

  d = min(9, current_sum)
  d = max(d, current_sum - 9 * remaining_digits_count)

  Add d to result_digits
  current_sum -= d

Final: Join result_digits to form the string.
```

## Dry Run

**Example 1: `num = 2, sum = 3`**

1.  **Initial Validity Check**:
    *   `min_sum = 2 * 1 = 2`
    *   `max_sum = 2 * 9 = 18`
    *   `2 <= 3 <= 18`. Valid.

2.  **Greedy Digit Construction**:
    *   `result_digits = []`
    *   `current_sum = 3`

    **Iteration 1 (i = 0, first digit):**
    *   `remaining_digits_count = num - 1 - i = 2 - 1 - 0 = 1`
    *   `d = min(9, current_sum) = min(9, 3) = 3`
    *   `d = max(d, current_sum - 9 * remaining_digits_count) = max(3, 3 - 9 * 1) = max(3, -6) = 3`
    *   Place `d = 3`.
    *   `result_digits = ["3"]`
    *   `current_sum = 3 - 3 = 0`

    **Iteration 2 (i = 1, second digit):**
    *   `remaining_digits_count = num - 1 - i = 2 - 1 - 1 = 0`
    *   `d = min(9, current_sum) = min(9, 0) = 0`
    *   `d = max(d, current_sum - 9 * remaining_digits_count) = max(0, 0 - 9 * 0) = max(0, 0) = 0`
    *   Place `d = 0`.
    *   `result_digits = ["3", "0"]`
    *   `current_sum = 0 - 0 = 0`

3.  **Final Result**:
    *   Join `result_digits`: `"30"`.

This matches Example 1's output.

## Complexity

*   **Time Complexity**: O(`num`)
    We iterate `num` times (once for each digit). Inside the loop, operations are constant time.
*   **Space Complexity**: O(`num`)
    We store `num` digits in the `result_digits` list.

## Edge Cases

*   **`num = 1, sum = 10`**:
    *   `min_sum = 1 * 1 = 1`, `max_sum = 1 * 9 = 9`.
    *   `sum = 10` is `> max_sum`. The initial validity check correctly returns `""`.
*   **`num = 1, sum = 1`**:
    *   `min_sum = 1`, `max_sum = 9`. `1 <= 1 <= 9`. Valid.
    *   `i=0`: `current_sum=1`, `remaining_digits_count=0`.
        *   `d = min(9, 1) = 1`
        *   `d = max(1, 1 - 9 * 0) = max(1, 1) = 1`
        *   `result_digits = ["1"]`. `current_sum = 0`.
    *   Returns `"1"`. Correct.
*   **`num = 5, sum = 45`**: (All nines)
    *   `min_sum = 5`, `max_sum = 45`. `5 <= 45 <= 45`. Valid.
    *   The loop will repeatedly place `9`s:
        *   `i=0`: `d=9`, `current_sum=36`.
        *   `i=1`: `d=9`, `current_sum=27`.
        *   `i=2`: `d=9`, `current_sum=18`.
        *   `i=3`: `d=9`, `current_sum=9`.
        *   `i=4`: `d=9`, `current_sum=0`.
    *   Returns `"99999"`. Correct.
*   **`num = 5, sum = 1`**: (One and zeros)
    *   `min_sum = 5`. `sum = 1` is `< min_sum`. The initial validity check correctly returns `""`.
    *   Wait, the problem states "A positive integer n is good if it satisfies...". A positive integer cannot have leading zeros unless it's just "0". But the number of digits is `num`. So `10000` is a 5-digit number.
    *   My initial check `min_sum = num * 1` is for digits `1-9`. If `0` is allowed, then `min_sum` for `num` digits is `1` (for the first digit) + `0` for the rest, so `1`.
    *   The problem statement says "A positive integer n is good". A positive integer cannot start with `0`. So the first digit must be `1-9`.
    *   Let's adjust the initial validity check:
        *   `min_sum = 1 + 0 * (num - 1)` (first digit 1, rest 0s) = `1`.
        *   `max_sum = 9 * num`.
        *   If `sum < 1` (not possible by constraints `sum >= 1`) or `sum > 9 * num`, return `""`.
        *   Also, if `num > 1` and `sum < 1 + 0 * (num - 1)` (i.e. `sum < 1`), this is covered.
        *   The constraint `1 <= num` and `1 <= sum` means we always need at least one digit and a positive sum.
        *   The smallest `num`-digit number is `10...0` (`num-1` zeros), which sums to `1`.
        *   The largest `num`-digit number is `99...9` (`num` nines), which sums to `9*num`.
        *   So the range `[1, 9*num]` for `sum` is correct.
        *   Let's re-check `num=5, sum=1`.
            *   `min_sum = 1` (for `10000`). `max_sum = 45`.
            *   `1 <= 1 <= 45`. Valid.
            *   `i=0`: `current_sum=1`, `remaining_digits_count=4`.
                *   `d = min(9, 1) = 1`
                *   `d = max(1, 1 - 9 * 4) = max(1, 1 - 36) = max(1, -35) = 1`
                *   Place `d = 1`. `result_digits = ["1"]`. `current_sum = 0`.
            *   `i=1`: `current_sum=0`, `remaining_digits_count=3`.
                *   `d = min(9, 0) = 0`
                *   `d = max(0, 0 - 9 * 3) = max(0, -27) = 0`
                *   Place `d = 0`. `result_digits = ["1", "0"]`. `current_sum = 0`.
            *   ... (rest are `0`s)
            *   Returns `"10000"`. Correct.

The initial validity check should be:
`if sum < 1 or sum > 9 * num: return ""`
This covers all cases.

## Solution

```python
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # 1. Initial Validity Check
        # The smallest possible sum for a 'num'-digit positive integer is 1
        # (e.g., 10...0 for num > 1, or 1 for num = 1).
        # The largest possible sum for a 'num'-digit integer is 9 * num (e.g., 99...9).
        # The problem states 'num' is positive, so a 'num'-digit number must have its first digit >= 1.
        # The minimum sum is 1 (for 10...0).
        # The maximum sum is 9*num (for 99...9).
        # If sum is outside this range, no such number exists.
        if sum < 1 or sum > 9 * num:
            return ""

        result_digits = []
        
        # 2. Greedy Digit Construction
        # Iterate 'num' times to determine each digit from left to right.
        for i in range(num):
            # 'remaining_digits_count' is the number of digits we still need to place
            # after the current one.
            remaining_digits_count = num - 1 - i

            # Determine the largest possible digit 'd' for the current position.
            # 'd' must satisfy:
            # a) 0 <= d <= 9 (it's a single digit)
            # b) d <= current_sum (we can't use more sum than available)
            # c) current_sum - d <= 9 * remaining_digits_count
            #    (the remaining sum must be achievable by the remaining digits,
            #     even if they are all 9s)
            #    This implies d >= current_sum - 9 * remaining_digits_count

            # Combine these conditions to find the largest valid 'd':
            # The upper bound for 'd' is min(9, current_sum).
            # The lower bound for 'd' is max(0, current_sum - 9 * remaining_digits_count).
            # To maximize the number, we pick the largest possible digit 'd'.
            # So, we start with the highest possible digit (9) and adjust downwards
            # if it violates the remaining sum constraint.
            
            # Start with the largest possible digit (9) or current_sum if it's smaller.
            digit_to_place = min(9, sum)
            
            # Adjust 'digit_to_place' if it's too small to satisfy the lower bound
            # (i.e., if placing 'digit_to_place' leaves too much sum for the remaining digits
            #  to handle, even if they are all 9s).
            # This ensures that sum - digit_to_place <= 9 * remaining_digits_count.
            digit_to_place = max(digit_to_place, sum - 9 * remaining_digits_count)

            # For the first digit, it cannot be 0 for a positive integer with 'num' digits.
            # (Unless num is 1 and sum is 0, but sum is >= 1).
            # If num > 1 and it's the first digit (i == 0), digit_to_place must be at least 1.
            # However, our logic for `sum - 9 * remaining_digits_count` will naturally handle this.
            # E.g., if num=2, sum=1.
            # i=0: remaining_digits_count=1. digit_to_place = max(min(9,1), 1 - 9*1) = max(1, -8) = 1. Correct.
            # So, no special handling for the first digit being non-zero is needed.

            result_digits.append(str(digit_to_place))
            sum -= digit_to_place

        # 3. Final Result
        return "".join(result_digits)

```

## Why This Works

This greedy approach works because it addresses both objectives simultaneously: maximizing the sum of squares and maximizing the integer itself.
1.  **Maximizing the Sum of Squares**: The sum of squares `d_1^2 + d_2^2 + ... + d_n^2` for a fixed total sum `d_1 + ... + d_n = S` is maximized when the digits are as **extreme** as possible (e.g., `0`s and `9`s). By always trying to place the largest possible digit (`9`, then `8`, etc.) at each step, our algorithm naturally prioritizes using larger digits, which contribute more to the sum of squares. This implicitly leads to a distribution of digits that favors `9`s and `0`s (and one "remainder" digit if `sum` is not a multiple of `9`).
2.  **Maximizing the Integer**: By iterating from left to right (most significant to least significant digit) and placing the largest valid digit at each position, we ensure that the resulting number is the largest possible among all numbers that satisfy the constraints and achieve the maximum score. The conditions `d <= 9`, `d <= current_sum`, and `d >= current_sum - 9 * remaining_digits_count` ensure that the chosen digit is valid and leaves a solvable subproblem for the remaining digits.

---
<sub>Generated 2026-10-14 05:16 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
