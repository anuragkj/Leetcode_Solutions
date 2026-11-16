# [2243] Calculate Digit Sum of a String

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-11-16 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/calculate-digit-sum-of-a-string/)

**Topics:** String, Simulation

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a string s consisting of digits and an integer k.

A round can be completed if the length of s is greater than k. In one round, do the following:

- Divide s into consecutive groups of size k such that the first k characters are in the first group, the next k characters are in the second group, and so on. Note that the size of the last group can be smaller than k.

- Replace each group of s with a string representing the sum of all its digits. For example, "346" is replaced with "13" because 3 + 4 + 6 = 13.

- Merge consecutive groups together to form a new string. If the length of the string is greater than k, repeat from step 1.

Return s after all rounds have been completed.

Example 1:

Input: s = "11111222223", k = 3
Output: "135"
Explanation:
- For the first round, we divide s into groups of size 3: "111", "112", "222", and "23".
  ​​​​​Then we calculate the digit sum of each group: 1 + 1 + 1 = 3, 1 + 1 + 2 = 4, 2 + 2 + 2 = 6, and 2 + 3 = 5.
  So, s becomes "3" + "4" + "6" + "5" = "3465" after the first round.
- For the second round, we divide s into "346" and "5".
  Then we calculate the digit sum of each group: 3 + 4 + 6 = 13, 5 = 5.
  So, s becomes "13" + "5" = "135" after second round.
Now, s.length <= k, so we return "135" as the answer.

Example 2:

Input: s = "00000000", k = 3
Output: "000"
Explanation:
We divide s into "000", "000", and "00".
Then we calculate the digit sum of each group: 0 + 0 + 0 = 0, 0 + 0 + 0 = 0, and 0 + 0 = 0.
s becomes "0" + "0" + "0" = "000", whose length is equal to k, so we return "000".

Constraints:

- 1 <= s.length <= 100

- 2 <= k <= 100

- s consists of digits only.

**Examples / sample tests:**

```
"11111222223"
3
"00000000"
3
```

---

## Problem Summary
You are given a string `s` consisting of digits and an integer `k`. The goal is to repeatedly transform `s` until its length is no longer greater than `k`. In each round of transformation, `s` is divided into consecutive groups of size `k` (the last group might be smaller). Each group is then replaced by the string representation of the sum of its digits. Finally, these new sum strings are merged to form the `s` for the next round.

## Intuition
The problem explicitly describes a **simulation** process. We need to follow the rules given step-by-step, repeating the transformation rounds until the condition (`len(s) > k`) is no longer met. This means our core logic will be a loop that continues as long as `s` is longer than `k`. Inside this loop, we'll implement the three main steps of a single round: **grouping**, **summing digits**, and **merging** the results.

## Approach
The optimal approach is a direct simulation of the process described:

1.  **Main Loop**: Start a `while` loop that continues as long as `len(s)` is strictly greater than `k`. This is the condition for performing another round.
2.  **Initialize for New Round**: Inside the `while` loop, create an empty list, let's call it `next_s_parts`. This list will temporarily store the string representations of the digit sums for each group in the current round.
3.  **Group and Sum**: Iterate through the current string `s` to form groups of size `k`.
    *   Use a `for` loop with `range(0, len(s), k)`. The loop variable `i` will represent the starting index of each group.
    *   For each `i`, extract the `group` using string slicing: `s[i : i + k]`. Python's slicing handles the end gracefully, so `s[i : i + k]` will correctly take fewer than `k` characters if `i + k` goes beyond the string's end.
    *   Calculate the sum of digits for this `group`:
        *   Initialize `current_group_sum = 0`.
        *   Iterate through each character `char_digit` in the `group`.
        *   Convert `char_digit` to an integer using `int(char_digit)` and add it to `current_group_sum`.
    *   Convert `current_group_sum` back to a string using `str(current_group_sum)` and append it to the `next_s_parts` list.
4.  **Merge for Next Round**: After the `for` loop finishes (meaning all groups have been processed), join all the strings in `next_s_parts` together to form the new `s` for the next iteration of the `while` loop: `s = "".join(next_s_parts)`.
5.  **Return Result**: Once the `while` loop condition `len(s) > k` becomes false (i.e., `len(s) <= k`), the process is complete. Return the final `s`.

## Visualization

Let's trace Example 1: `s = "11111222223"`, `k = 3`

```
Initial s: "11111222223", k = 3

Round 1: (len(s) = 11 > k = 3)
  Divide s into groups of size k=3:
  "111"  "112"  "222"  "23"
    |      |      |      |
    v      v      v      v
  Calculate digit sums:
  (1+1+1) (1+1+2) (2+2+2) (2+3)
    |      |      |      |
    v      v      v      v
  Sums (as strings):
   "3"    "4"    "6"    "5"
    \----------------------/
             |
             v
  Merge to form new s:
           "3465"

Round 2: (len(s) = 4 > k = 3)
  Divide s into groups of size k=3:
  "346"  "5"
    |      |
    v      v
  Calculate digit sums:
  (3+4+6) (5)
    |      |
    v      v
  Sums (as strings):
   "13"   "5"
    \-------/
        |
        v
  Merge to form new s:
       "135"

End: (len(s) = 3 <= k = 3)
Return "135"
```

## Dry Run
Let's walk through Example 1: `s = "11111222223"`, `k = 3`

| Round | `s` (start)         | `len(s) > k`? | `i` (group start) | `group` | `current_group_sum` | `str(current_group_sum)` | `next_s_parts` (after group) | `s` (end of round) |
| :---- | :------------------ | :------------ | :---------------- | :------ | :------------------ | :----------------------- | :--------------------------- | :----------------- |
| 1     | "11111222223"       | True          | 0                 | "111"   | 3                   | "3"                      | `["3"]`                      |                    |
|       |                     |               | 3                 | "112"   | 4                   | "4"                      | `["3", "4"]`                 |                    |
|       |                     |               | 6                 | "222"   | 6                   | "6"                      | `["3", "4", "6"]`            |                    |
|       |                     |               | 9                 | "23"    | 5                   | "5"                      | `["3", "4", "6", "5"]`       | "3465"             |
| 2     | "3465"              | True          | 0                 | "346"   | 13                  | "13"                     | `["13"]`                     |                    |
|       |                     |               | 3                 | "5"     | 5                   | "5"                      | `["13", "5"]`                | "135"              |
| Final | "135"               | False         |                   |         |                     |                          |                              | "135"              |

Final Result: "135"

## Complexity
*   **Time Complexity**: `O(N * R)`, where `N` is the initial length of `s` and `R` is the number of rounds. In each round, we iterate through the current string `s` once, which takes `O(current_len(s))` time. The length of `s` decreases rapidly. For `k > 2`, the length of `s` strictly decreases in each round. For `k = 2`, the length can stay the same for a round (e.g., "99" -> "18"), but eventually, single-digit sums will appear, leading to a length reduction. Given `N <= 100`, `R` is a very small constant (at most a few rounds), making the total time complexity effectively `O(N)`.
*   **Space Complexity**: `O(N)`. In each round, we create `next_s_parts` which stores the sum strings. The total length of these strings when joined can be up to `N` (the initial length of `s`). This space is reused in subsequent rounds.

## Edge Cases
*   **`s.length <= k` initially**: The `while len(s) > k` loop condition will be false from the start. The function will immediately return the original `s`. This is correct as no rounds are needed.
*   **`s` consists of all zeros**: E.g., `s = "00000000", k = 3`.
    *   Round 1: "000", "000", "00" -> "0", "0", "0" -> "000".
    *   Now `len("000")` is `3`, which is not `> k=3`. The loop terminates, returning "000". Correct.
*   **`k` is large, equal to `s.length`**: E.g., `s = "12345", k = 5`.
    *   `len(s) = 5`, `k = 5`. `len(s) > k` is false. Returns "12345". Correct.

## Solution

```python
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # The simulation continues as long as the length of s is greater than k.
        while len(s) > k:
            # This list will store the sum of digits for each group, as strings.
            next_s_parts = []
            
            # Iterate through the string s to form groups of size k.
            # The range(start, stop, step) function is perfect for this.
            # 'i' will be the starting index of each group.
            for i in range(0, len(s), k):
                # Extract the current group.
                # s[i : i + k] handles the last group being smaller than k automatically.
                group = s[i : i + k]
                
                # Calculate the sum of digits for the current group.
                current_group_sum = 0
                for char_digit in group:
                    current_group_sum += int(char_digit)
                
                # Convert the sum back to a string and add it to our parts list.
                next_s_parts.append(str(current_group_sum))
            
            # Merge all the sum strings to form the new 's' for the next round.
            # Using "".join() is efficient for concatenating many strings in Python.
            s = "".join(next_s_parts)
            
        # Once the loop finishes, len(s) is no longer greater than k.
        # This means len(s) <= k, so we return the final string s.
        return s

```

## Why This Works
This solution works because it directly implements the problem's rules as a simulation. The `while` loop correctly controls the rounds, ensuring they continue only when `s` is longer than `k`. Inside the loop, string slicing (`s[i : i + k]`) accurately divides `s` into groups, including handling the potentially shorter last group. The inner loop correctly calculates the sum of digits for each group, and `str()` converts these sums back into strings. Finally, `"".join()` efficiently merges these sum strings to form the `s` for the next round. The process is guaranteed to terminate because the length of `s` either strictly decreases or eventually decreases (for `k=2`, the length might stay the same for a round, but eventually, sums will be single digits, reducing length) until it is less than or equal to `k`.

---
<sub>Generated 2026-11-16 07:09 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
