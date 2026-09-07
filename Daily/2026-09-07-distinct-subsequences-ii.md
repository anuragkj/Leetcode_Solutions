# [940] Distinct Subsequences II

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-09-07 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/distinct-subsequences-ii/)

**Topics:** String, Dynamic Programming

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 10^9 + 7.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.

Example 1:

Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".

Example 2:

Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".

Example 3:

Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".

Constraints:

- 1 <= s.length <= 2000

- s consists of lowercase English letters.

**Examples / sample tests:**

```
"abc"
"aba"
"aaa"
```

---

## Problem Summary
This problem asks us to count the total number of **distinct non-empty subsequences** of a given string `s`. Since the count can be very large, we need to return the result modulo `10^9 + 7`.

## Intuition
Let's think about how the number of distinct subsequences changes as we process the string character by character. Suppose we have processed the prefix `s[0...i-1]` and know the total number of distinct subsequences formed so far. When we encounter a new character `s[i]`, what happens?

1.  All distinct subsequences formed from `s[0...i-1]` are still valid.
2.  We can form **new** distinct subsequences by:
    *   Taking `s[i]` itself as a single-character subsequence.
    *   Appending `s[i]` to every distinct subsequence formed from `s[0...i-1]`.

If there were `X` distinct subsequences from `s[0...i-1]`, then by adding `s[i]`, we potentially add `X + 1` new subsequences (the `+1` is for `s[i]` itself). This would make the total `X + (X + 1) = 2X + 1`.

However, this simple `2X + 1` rule overcounts if `s[i]` has appeared before. For example, if `s = "aba"`:
*   After "a": {"a"} (1 subsequence)
*   After "ab": {"a", "b", "ab"} (3 subsequences)
*   After "aba":
    *   Previous: {"a", "b", "ab"}
    *   New by appending 'a': {"aa", "ba", "aba"}
    *   New single 'a': {"a"}
    *   Combining these: {"a", "b", "ab", "aa", "ba", "aba"}. Notice "a" and "aba" are duplicated if we just blindly add.

The key insight to handle duplicates is: if the current character `s[i]` (let's call it `c`) has appeared before, say at index `j` (`s[j] == c`), then any subsequence that was formed *ending with* `s[j]` will be duplicated by a subsequence formed *ending with* `s[i]` if they share the same prefix. We need to subtract these duplicates.

Specifically, the number of distinct subsequences that *ended with* the previous occurrence of `c` (at `s[j]`) is exactly the number of subsequences we need to subtract to avoid overcounting.

This leads to a Dynamic Programming approach where we keep track of two things:
1.  `dp[char_code]`: The number of distinct subsequences ending with `char_code` using the prefix processed so far.
2.  `total_distinct_subsequences`: The sum of all `dp` values, representing the total count of distinct non-empty subsequences.

## Approach
We will use a dynamic programming approach with an array to store counts for each character.

1.  **Initialization**:
    *   Create an array `dp` of size 26 (for 'a' through 'z'), initialized to all zeros. `dp[char_idx]` will store the count of distinct subsequences ending with `chr(ord('a') + char_idx)`.
    *   Initialize `total_distinct_subsequences = 0`. This variable will keep track of the sum of all values in `dp`, which is our running total of distinct subsequences.
    *   Define `MOD = 10^9 + 7` for modulo operations.

2.  **Iteration**:
    *   Iterate through each character `c` in the input string `s`.
    *   For each `c`:
        a.  Calculate its `char_idx = ord(c) - ord('a')`.
        b.  Store the current count of subsequences ending with `c`: `prev_count_for_c = dp[char_idx]`. This is crucial for handling duplicates.
        c.  Calculate the `new_count_for_c`: This is `(1 + total_distinct_subsequences) % MOD`.
            *   The `1` accounts for the single-character subsequence `c` itself.
            *   `total_distinct_subsequences` accounts for all previously formed distinct subsequences, to which we can append `c` to form new ones (e.g., if "a" and "b" were formed, and `c` is 'c', we get "ac", "bc").
        d.  Update `dp[char_idx] = new_count_for_c`. This replaces the old count for `c` with the newly calculated one.
        e.  Update `total_distinct_subsequences`:
            `total_distinct_subsequences = (total_distinct_subsequences + new_count_for_c - prev_count_for_c + MOD) % MOD`.
            *   We add `new_count_for_c` because these are the new distinct subsequences ending with `c`.
            *   We subtract `prev_count_for_c` to remove the count of subsequences that ended with a *previous* occurrence of `c`. These are the duplicates that `new_count_for_c` now covers.
            *   Adding `MOD` before taking the final modulo ensures the result remains positive even if `total_distinct_subsequences + new_count_for_c - prev_count_for_c` is negative.

3.  **Result**:
    *   After iterating through all characters in `s`, `total_distinct_subsequences` will hold the final count of distinct non-empty subsequences. Return this value.

## Visualization

Let's visualize the process for `s = "aba"`:

**Initial State:**
`dp = [0, 0, ..., 0]` (26 zeros)
`total_distinct_subsequences = 0`

---

**Processing 'a' (s[0]):**
*   `char_idx` for 'a' is 0.
*   `prev_count_for_a = dp[0] = 0`.
*   `new_count_for_a = (1 + total_distinct_subsequences) % MOD = (1 + 0) % MOD = 1`.
*   `dp[0] = 1`.
*   `total_distinct_subsequences = (0 + 1 - 0 + MOD) % MOD = 1`.

**State after 'a':**
`dp = [1, 0, 0, ..., 0]` (dp[0] for 'a' is 1)
`total_distinct_subsequences = 1`
Subsequences: {"a"}

---

**Processing 'b' (s[1]):**
*   `char_idx` for 'b' is 1.
*   `prev_count_for_b = dp[1] = 0`.
*   `new_count_for_b = (1 + total_distinct_subsequences) % MOD = (1 + 1) % MOD = 2`.
*   `dp[1] = 2`.
*   `total_distinct_subsequences = (1 + 2 - 0 + MOD) % MOD = 3`.

**State after 'b':**
`dp = [1, 2, 0, ..., 0]` (dp[0] for 'a' is 1, dp[1] for 'b' is 2)
`total_distinct_subsequences = 3`
Subsequences: {"a"}, {"b", "ab"}

---

**Processing 'a' (s[2]):**
*   `char_idx` for 'a' is 0.
*   `prev_count_for_a = dp[0] = 1`.
*   `new_count_for_a = (1 + total_distinct_subsequences) % MOD = (1 + 3) % MOD = 4`.
*   `dp[0] = 4`.
*   `total_distinct_subsequences = (3 + 4 - 1 + MOD) % MOD = 6`.

**State after 'a':**
`dp = [4, 2, 0, ..., 0]` (dp[0] for 'a' is 4, dp[1] for 'b' is 2)
`total_distinct_subsequences = 6`
Subsequences: {"a", "aa", "ba", "aba"}, {"b", "ab"}

---

**Final Result:** `total_distinct_subsequences = 6`.

## Dry Run

Let's trace `s = "aba"` with the detailed steps. `MOD = 10^9 + 7`.

| Char | `char_idx` | `prev_count_for_char` | `total_distinct_subsequences` (before update) | `new_count_for_char` (`1 + total`) | `dp` array (relevant parts) | `total_distinct_subsequences` (after update) |
| :--- | :--------- | :-------------------- | :-------------------------------------------- | :--------------------------------- | :-------------------------- | :------------------------------------------- |
| **Initial** |            |                       | 0                                             |                                    | `dp['a']=0, dp['b']=0`      | 0                                            |
| 'a'    | 0          | `dp[0]` = 0           | 0                                             | `(1 + 0) % MOD` = 1                | `dp['a']=1`                 | `(0 + 1 - 0 + MOD) % MOD` = 1                |
| 'b'    | 1          | `dp[1]` = 0           | 1                                             | `(1 + 1) % MOD` = 2                | `dp['a']=1, dp['b']=2`      | `(1 + 2 - 0 + MOD) % MOD` = 3                |
| 'a'    | 0          | `dp[0]` = 1           | 3                                             | `(1 + 3) % MOD` = 4                | `dp['a']=4, dp['b']=2`      | `(3 + 4 - 1 + MOD) % MOD` = 6                |

**Final Result:** 6

## Complexity

*   **Time Complexity**: O(N), where N is the length of the string `s`. We iterate through the string once, and each character processing involves constant time operations (array access, arithmetic).
*   **Space Complexity**: O(1). We use a `dp` array of fixed size 26 (for lowercase English letters) and a few constant variables, regardless of the input string length.

## Edge Cases

*   **`s.length = 1` (e.g., "a")**:
    *   The loop runs once. `total_distinct_subsequences` becomes 1. Correct, as "a" is the only distinct subsequence.
*   **All characters are the same (e.g., "aaa")**:
    *   "a": `total=1`
    *   "aa": `prev_a=1`, `new_a=(1+1)=2`, `total=(1+2-1)=2`
    *   "aaa": `prev_a=2`, `new_a=(1+2)=3`, `total=(2+3-2)=3`
    *   The result is `N`, which is correct for "aaa" -> {"a", "aa", "aaa"}.
*   **All characters are distinct (e.g., "abc")**:
    *   "a": `total=1`
    *   "ab": `total=3`
    *   "abc": `total=7`
    *   The result is `2^N - 1`, which is correct.

The solution correctly handles these cases due to the robust duplicate handling mechanism.

## Solution

```python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        # dp[char_idx] stores the number of distinct subsequences ending with
        # the character chr(ord('a') + char_idx), using the prefix of s processed so far.
        dp = [0] * 26 
        
        # total_distinct_subsequences stores the sum of all values in dp,
        # representing the total number of distinct non-empty subsequences found so far.
        total_distinct_subsequences = 0
        
        for char_code in s:
            char_idx = ord(char_code) - ord('a')
            
            # prev_count_for_char is the number of distinct subsequences ending with char_code
            # *before* processing the current char_code.
            prev_count_for_char = dp[char_idx]
            
            # new_count_for_char represents all distinct subsequences that *will* end with
            # the current char_code. This includes:
            # 1. The char_code itself (e.g., "a").
            # 2. All previously formed distinct subsequences (total_distinct_subsequences)
            #    with the current char_code appended (e.g., if "b" and "ab" were formed,
            #    and current char is 'a', new subsequences are "ba", "aba").
            new_count_for_char = (1 + total_distinct_subsequences) % MOD
            
            # Update dp for the current char_code. This effectively replaces the old count
            # with the new, more comprehensive count for subsequences ending with this character.
            dp[char_idx] = new_count_for_char
            
            # Update the total_distinct_subsequences.
            # We add new_count_for_char because these are the newly formed distinct subsequences
            # ending with char_code.
            # We subtract prev_count_for_char because these were subsequences ending with char_code
            # that were already counted (due to a previous occurrence of char_code). These are
            # the duplicates that new_count_for_char now covers, so we remove their old contribution.
            # Adding MOD before taking modulo handles potential negative results from subtraction
            # (e.g., if new_count_for_char < prev_count_for_char, which can happen if total_distinct_subsequences
            # was very small and prev_count_for_char was large, or due to modulo arithmetic).
            total_distinct_subsequences = (total_distinct_subsequences + new_count_for_char - prev_count_for_char + MOD) % MOD
            
        return total_distinct_subsequences

```

## Why This Works

The solution works by maintaining a running count of all distinct non-empty subsequences (`total_distinct_subsequences`) and, for each character, the count of distinct subsequences ending with that specific character (`dp[char_idx]`). When a new character `c` is processed, it effectively "doubles" the existing set of subsequences (by appending `c` to them) and adds `c` itself. This gives `2 * total_distinct_subsequences + 1` potential new subsequences. However, if `c` has appeared before, say at index `j`, then any subsequence `X + s[j]` (where `X` is a subsequence formed before `s[j]`) would be identical to `X + s[i]`. The `prev_count_for_c` variable precisely captures the number of distinct subsequences that ended with the *previous* occurrence of `c`. By subtracting this `prev_count_for_c`, we correctly remove the duplicated subsequences, ensuring that `total_distinct_subsequences` always holds the unique count. The `new_count_for_c` then updates the `dp` array to reflect the new total of subsequences ending with `c`, which now includes all valid subsequences ending with the current `c`.

---
<sub>Generated 2026-09-07 05:08 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
