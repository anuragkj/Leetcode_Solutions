# [3720] Lexicographically Smallest Permutation Greater Than Target

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-08-27 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/)

**Topics:** Hash Table, String, Greedy, Counting, Enumeration

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

Example 1:

Input: s = "abc", target = "bba"

Output: "bca"

Explanation:

- The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".

- The lexicographically smallest permutation that is strictly greater than target is "bca".

Example 2:

Input: s = "leet", target = "code"

Output: "eelt"

Explanation:

- The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".

- The lexicographically smallest permutation that is strictly greater than target is "eelt".

Example 3:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

- The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".

- None of them is lexicographically strictly greater than target. Therefore, the answer is "".

Constraints:

- 1 <= s.length == target.length <= 300

- s and target consist of only lowercase English letters.

**Examples / sample tests:**

```
"abc"
"bba"
"leet"
"code"
"baba"
"bbaa"
```

---

## Problem Summary
Find the lexicographically smallest permutation of string `s` that is strictly greater than string `target`. Both strings have the same length and consist of lowercase English letters. If no such permutation exists, return an empty string.

## Intuition
To find the **lexicographically smallest** string that is **strictly greater** than `target`, we want to keep its prefix as similar to `target` as possible. This means we try to match `target[i]` at each position `i` from left to right.

However, at some point, we *must* make our permutation `P` strictly greater than `target`. This happens at the *first* position `i` where `P[i] > target[i]`, while `P[j] == target[j]` for all `j < i`. To keep `P` as small as possible:
1.  We want to make this "bump" (where `P[i] > target[i]`) as far to the right as possible.
2.  When we make the bump at position `i`, we want to choose the *smallest possible character* `c` from the remaining characters of `s` such that `c > target[i]`.
3.  Once `P[0...i-1]` is fixed to `target[0...i-1]` and `P[i]` is fixed to `c`, the rest of the string `P[i+1:]` must be filled with the *remaining available characters* from `s` in **sorted ascending order** to ensure the overall string is lexicographically smallest.

Our strategy will be to iterate from left to right, considering two options at each position `i`:
*   **Option A (Bump):** Try to place a character `c` at `ans[i]` such that `c > target[i]`. If successful, this forms a candidate solution. We find the *smallest* such `c` and construct the candidate `target[0...i-1] + c + sorted_remaining_chars`. We keep track of the overall smallest candidate found across all `i` and `c`.
*   **Option B (Match):** Try to place `target[i]` at `ans[i]`. This keeps our prefix small, allowing for a potential bump at a later position `j > i`. If `target[i]` is not available, we cannot continue this path, and any solution must have come from an earlier "bump".

## Approach
The algorithm proceeds as follows:

1.  **Initialize:**
    *   Create a frequency array `s_counts` (size 26) to store the counts of each character in `s`.
    *   Initialize `min_greater_perm = ""` to store the best (smallest) valid permutation found so far. This will be our final answer.
    *   Initialize `current_prefix_chars = []` to build the prefix of the permutation we are currently considering.

2.  **Iterate through positions:** Loop `i` from `0` to `n-1` (where `n` is the length of `s` and `target`).

3.  **At each position `i`:**
    *   Get `target_char_code = ord(target[i]) - ord('a')`.

    *   **Strategy 1: Try to make `ans[i]` strictly greater than `target[i]` (the "bump" strategy):**
        *   Iterate `c_code` from `target_char_code + 1` up to `25` (representing 'z').
        *   If `s_counts[c_code] > 0` (meaning character `chr(ord('a') + c_code)` is available):
            *   This `c_code` represents the **smallest character `c`** that is greater than `target[i]` and available.
            *   **Construct a candidate permutation:**
                *   Temporarily decrement `s_counts[c_code]` to reflect using `c`.
                *   Build a `suffix_chars` list by appending all remaining characters in `s_counts` in sorted ascending order.
                *   Form the full `candidate` string: `"".join(current_prefix_chars) + chr(ord('a') + c_code) + "".join(suffix_chars)`.
                *   Restore `s_counts[c_code]` (important for subsequent iterations of `i`).
            *   **Update `min_greater_perm`:** If `min_greater_perm` is empty or `candidate` is lexicographically smaller than `min_greater_perm`, update `min_greater_perm = candidate`.
            *   **Break:** Since we found the *smallest* `c` that can make `ans[i] > target[i]` (given `ans[0...i-1]` matches `target[0...i-1]`), any larger `c` would result in a lexicographically larger candidate. So, we `break` from this inner `c_code` loop and proceed to Strategy 2.

    *   **Strategy 2: Try to make `ans[i]` equal to `target[i]` (the "match" strategy):**
        *   If `s_counts[target_char_code] > 0` (meaning `target[i]` is available):
            *   Append `target[i]` to `current_prefix_chars`.
            *   Decrement `s_counts[target_char_code]`.
            *   Continue to the next position `i+1`.
        *   Else (if `target[i]` is not available):
            *   We cannot match `target[i]` at this position. This means any valid permutation must have made its first "bump" at an earlier position `j < i`. All such possibilities have already been considered and `min_greater_perm` updated.
            *   Therefore, we `break` from the main `for i` loop, as no further matching or bumping at `i` or beyond will yield a valid solution with `target[0...i-1]` as prefix.

4.  **Return:** After the loop finishes, `min_greater_perm` will hold the lexicographically smallest permutation of `s` that is strictly greater than `target`, or `""` if none was found. Return `min_greater_perm`.

## Visualization

Let's trace `s = "abc"`, `target = "bba"`:

```
s_counts = {'a':1, 'b':1, 'c':1}
min_greater_perm = ""
current_prefix_chars = []

i = 0: target[0] = 'b' (char_code = 1)
  +--------------------------------------------------------------------------------+
  | Current state:                                                                 |
  |   current_prefix_chars = []                                                    |
  |   s_counts = {'a':1, 'b':1, 'c':1}                                             |
  |   min_greater_perm = ""                                                        |
  +--------------------------------------------------------------------------------+
  | Strategy 1 (Bump): Try ans[0] > 'b'                                            |
  |   Smallest char c > 'b' available in s_counts: 'c' (c_code = 2)                |
  |   - Temporarily s_counts['c']--  => {'a':1, 'b':1, 'c':0}                      |
  |   - Remaining chars sorted: ['a', 'b']                                         |
  |   - Candidate: "" + 'c' + "ab" = "cab"                                         |
  |   - Restore s_counts['c']++    => {'a':1, 'b':1, 'c':1}                        |
  |   - min_greater_perm is "", so update: min_greater_perm = "cab"                |
  |   - Break from c_code loop (found smallest 'c' for this 'i')                   |
  +--------------------------------------------------------------------------------+
  | Strategy 2 (Match): Try ans[0] == 'b'                                          |
  |   target[0] = 'b'. s_counts['b'] > 0. Yes.                                     |
  |   - current_prefix_chars.append('b') => ['b']                                  |
  |   - s_counts['b']--                  => {'a':1, 'b':0, 'c':1}                 |
  |   - Continue to next i                                                         |
  +--------------------------------------------------------------------------------+

i = 1: target[1] = 'b' (char_code = 1)
  +--------------------------------------------------------------------------------+
  | Current state:                                                                 |
  |   current_prefix_chars = ['b']                                                 |
  |   s_counts = {'a':1, 'b':0, 'c':1}                                             |
  |   min_greater_perm = "cab"                                                     |
  +--------------------------------------------------------------------------------+
  | Strategy 1 (Bump): Try ans[1] > 'b'                                            |
  |   Smallest char c > 'b' available in s_counts: 'c' (c_code = 2)                |
  |   - Temporarily s_counts['c']--  => {'a':1, 'b':0, 'c':0}                      |
  |   - Remaining chars sorted: ['a']                                              |
  |   - Candidate: "b" + 'c' + "a" = "bca"                                         |
  |   - Restore s_counts['c']++    => {'a':1, 'b':0, 'c':1}                        |
  |   - "bca" < "cab". Update: min_greater_perm = "bca"                            |
  |   - Break from c_code loop                                                     |
  +--------------------------------------------------------------------------------+
  | Strategy 2 (Match): Try ans[1] == 'b'                                          |
  |   target[1] = 'b'. s_counts['b'] > 0. No (s_counts['b'] is 0).                 |
  |   - Cannot match. Break from main loop.                                        |
  +--------------------------------------------------------------------------------+

Loop ends. Return min_greater_perm.

Final Result: "bca"
```

## Dry Run
Let's walk through Example 1: `s = "abc"`, `target = "bba"`

| Step | `i` | `target[i]` | `s_counts` (before) | `current_prefix_chars` (before) | `min_greater_perm` (before) | Action (Strategy 1: Bump) | Action (Strategy 2: Match) | `s_counts` (after) | `current_prefix_chars` (after) | `min_greater_perm` (after) |
| :--- | :-: | :---------- | :------------------ | :------------------------------ | :-------------------------- | :------------------------ | :------------------------- | :----------------- | :----------------------------- | :------------------------- |
| Init |   |             | `{'a':1,'b':1,'c':1}` | `[]`                            | `""`                        |                           |                            | `{'a':1,'b':1,'c':1}` | `[]`                           | `""`                       |
| 1    | 0 | 'b'         | `{'a':1,'b':1,'c':1}` | `[]`                            | `""`                        | Find 'c' > 'b': 'c'. <br> Candidate: "cab". <br> `min_greater_perm = "cab"`. Break. | `target[0]` ('b') available. <br> Add 'b' to prefix. | `{'a':1,'b':0,'c':1}` | `['b']`                        | `"cab"`                    |
| 2    | 1 | 'b'         | `{'a':1,'b':0,'c':1}` | `['b']`                         | `"cab"`                     | Find 'c' > 'b': 'c'. <br> Candidate: "bca". <br> "bca" < "cab", so `min_greater_perm = "bca"`. Break. | `target[1]` ('b') NOT available. <br> Break main loop. | `{'a':1,'b':0,'c':1}` | `['b']`                        | `"bca"`                    |

Final Result: `"bca"`

## Complexity
*   **Time Complexity:** `O(N^2)`
    *   The outer loop runs `N` times (for `i` from `0` to `n-1`).
    *   Inside the outer loop:
        *   The inner loop for `c_code` runs at most 26 times. It breaks after finding the first suitable character.
        *   Building `suffix_chars` involves iterating through 26 character counts and extending a list, which takes `O(N)` time in total (as `sum(s_counts)` is `N`).
        *   String concatenation `"".join(...)` takes `O(N)` time.
        *   String comparison `candidate < min_greater_perm` takes `O(N)` time.
        *   The "match" strategy takes `O(1)` time.
    *   Thus, each iteration of the outer loop takes `O(26 + N) = O(N)` time.
    *   Total time complexity: `N * O(N) = O(N^2)`. Given `N <= 300`, `300^2 = 90,000` operations, which is efficient enough.

*   **Space Complexity:** `O(N)`
    *   `s_counts` array: `O(26)` (constant space).
    *   `current_prefix_chars` list: `O(N)` in the worst case (stores up to `N` characters).
    *   `suffix_chars` list: `O(N)` in the worst case.
    *   `min_greater_perm` string: `O(N)` in the worst case.
    *   Total space complexity: `O(N)`.

## Edge Cases
*   **No solution exists:** If `s` cannot form any permutation strictly greater than `target` (e.g., `s = "baba", target = "bbaa"`), `min_greater_perm` will remain `""` throughout the process, and `""` will be returned. This is handled correctly because if `target[i]` is not available and no `c > target[i]` is available, the loop breaks, and `min_greater_perm` is returned as is.
*   **`s` is already sorted and greater than `target`:** The algorithm will correctly find the smallest `i` where `ans[i] > target[i]` and construct the minimal permutation.
*   **`s` contains duplicate characters:** The frequency array `s_counts` correctly handles duplicate characters by tracking their counts.
*   **`s` is a permutation of `target`:** The algorithm still correctly identifies the smallest permutation of `s` that is *strictly* greater than `target`. If `s` itself is `target`, it will find the next permutation. If `s` is lexicographically smaller than `target`, it will find the smallest greater one.

## Solution

```python
import collections

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        
        # Use a frequency array for characters 'a' through 'z' for efficiency.
        # s_counts[0] for 'a', s_counts[1] for 'b', ..., s_counts[25] for 'z'.
        s_counts = [0] * 26
        for char_s in s:
            s_counts[ord(char_s) - ord('a')] += 1
        
        # This variable will store the lexicographically smallest permutation found
        # that is strictly greater than `target`.
        # Initialized to an empty string, which is the required return value
        # if no such permutation exists.
        min_greater_perm = "" 
        
        # `current_prefix_chars` stores the characters that form the prefix
        # of our candidate permutation, which currently matches `

---
<sub>Generated 2026-08-27 10:12 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
