# [3870] Count Commas in Range

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-09-08 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/count-commas-in-range/)

**Topics:** Math

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer n.

Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.

In standard formatting:

- A comma is inserted after every three digits from the right.

- Numbers with fewer than 4 digits contain no commas.

Example 1:

Input: n = 1002

Output: 3

Explanation:

The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

Example 2:

Input: n = 998

Output: 0

Explanation:

All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

Constraints:

- 1 <= n <= 10^5

**Examples / sample tests:**

```
1002
998
```

---

## Problem Summary
Given an integer `n`, we need to calculate the total count of commas used when writing all numbers from 1 to `n` (inclusive) in standard number formatting. Standard formatting places a comma after every three digits from the right, but only for numbers with four or more digits.

## Intuition
The key to solving this problem efficiently lies in understanding how commas are placed and the given constraints.
1.  **Comma Rule:** A comma is inserted after every three digits from the right. Numbers with fewer than 4 digits (e.g., 1, 99, 999) have **no commas**.
2.  **Constraint:** The input `n` is between 1 and 10^5 (100,000).
3.  **Combining Rules:**
    *   Numbers from 1 to 999 have 0 commas.
    *   Numbers from 1,000 to 99,999 (inclusive) are 4, 5, or 6-digit numbers. For example, 1,000, 10,000, 100,000. All these numbers have exactly **one comma**.
    *   Numbers 100,000 and above (up to 10^5) still only have one comma (e.g., 100,000).
    *   Numbers 1,000,000 and above would have two commas, but `n` never reaches this high (max `n` is 100,000).

Therefore, for any `n` up to 100,000, the only numbers that contribute commas are those from 1,000 up to `n`. Each of these numbers contributes exactly one comma.

## Approach
The optimal approach is a simple conditional check based on the observation above:

1.  Initialize a variable `total_commas` to 0.
2.  **Check the range of `n`**:
    *   If `n` is less than 1000 (i.e., `n < 1000`), then all numbers from 1 to `n` have fewer than four digits. According to the rules, none of them will contain any commas. In this case, the `total_commas` is 0.
    *   If `n` is 1000 or greater (i.e., `n >= 1000`), then all numbers from 1000 up to `n` (inclusive) will each contain exactly one comma.
        *   The count of such numbers is `n - 1000 + 1`.
        *   Since each of these numbers contributes 1 comma, the `total_commas` will be exactly `n - 1000 + 1`.
3.  Return the calculated `total_commas`.

## Visualization

```
Number Line:
1           999       1000      ...      n
|-------------|---------|------------------|
  0 commas      1 comma (for each number in this range)

Example: n = 1002
1           999       1000      1001      1002
|-------------|---------|---------|---------|
  0 commas      1 comma   1 comma   1 comma
                (for 1,000) (for 1,001) (for 1,002)

Total commas = 3
```

## Dry Run

Let's walk through Example 1: `n = 1002`

| Step | Condition (`n < 1000`?) | Calculation (`n - 1000 + 1`) | `total_commas` | Notes                                                              |
| :--- | :---------------------- | :--------------------------- | :------------- | :----------------------------------------------------------------- |
| 1    | `1002 < 1000` is **False** | `1002 - 1000 + 1`            |                | `n` is 1000 or greater, so numbers from 1000 to `n` contribute.    |
| 2    |                         | `2 + 1`                      | `3`            | Each number from 1000 to 1002 (1000, 1001, 1002) has one comma.    |
| 3    |                         |                              | `3`            | Final result.                                                      |

Final Result: `3`

Let's walk through Example 2: `n = 998`

| Step | Condition (`n < 1000`?) | Calculation (`n - 1000 + 1`) | `total_commas` | Notes                                                              |
| :--- | :---------------------- | :--------------------------- | :------------- | :----------------------------------------------------------------- |
| 1    | `998 < 1000` is **True** |                              | `0`            | `n` is less than 1000, so no numbers have commas. Return 0 directly. |

Final Result: `0`

## Complexity

*   **Time Complexity:** O(1)
    *   The solution involves a single comparison and a simple arithmetic operation, regardless of the value of `n`.
*   **Space Complexity:** O(1)
    *   The solution uses a constant amount of extra space for variables.

## Edge Cases

*   **`n = 1` (minimum constraint):**
    *   `1 < 1000` is true. Returns 0. Correct, "1" has no commas.
*   **`n = 999` (just before 1000):**
    *   `999 < 1000` is true. Returns 0. Correct, "999" has no commas.
*   **`n = 1000` (first number with a comma):**
    *   `1000 < 1000` is false. Calculates `1000 - 1000 + 1 = 1`. Returns 1. Correct, "1,000" has one comma.
*   **`n = 100000` (maximum constraint):**
    *   `100000 < 1000` is false. Calculates `100000 - 1000 + 1 = 99001`. Returns 99001. Correct, all numbers from 1000 to 100000 each have one comma.

## Solution

```python
class Solution:
    def countCommas(self, n: int) -> int:
        # Numbers less than 1000 (1-999) have no commas.
        # Numbers from 1000 up to 100,000 (the max 'n') each have exactly one comma.
        # For example: 1,000; 10,000; 100,000.

        if n < 1000:
            # If n is less than 1000, no numbers in the range [1, n] will have commas.
            return 0
        else:
            # If n is 1000 or greater, all numbers from 1000 up to n (inclusive)
            # will each contribute one comma.
            # The count of such numbers is (n - 1000 + 1).
            # Since each contributes 1 comma, the total is simply this count.
            return n - 1000 + 1

```

## Why This Works

This solution works because the problem constraints (`1 <= n <= 10^5`) simplify the comma counting rule significantly. Within this range, numbers either have **zero commas** (for 1 to 999) or **exactly one comma** (for 1000 to 100,000). There are no numbers that would require two or more commas. By identifying this clear threshold at 1000, we can directly calculate the count of numbers that contribute one comma each, which is simply the size of the range `[1000, n]`. If `n` is below this threshold, no numbers contribute, resulting in zero commas. This approach correctly partitions the problem space and provides an O(1) solution.

---
<sub>Generated 2026-09-08 05:05 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
