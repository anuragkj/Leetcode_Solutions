# [3518] Smallest Palindromic Rearrangement II

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-07-29 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/)

**Topics:** Hash Table, Math, String, Combinatorics, Counting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a palindromic string s and an integer k.

Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.

Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.

Example 1:

Input: s = "abba", k = 2

Output: "baab"

Explanation:

- The two distinct palindromic rearrangements of "abba" are "abba" and "baab".

- Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".

Example 2:

Input: s = "aa", k = 2

Output: ""

Explanation:

- There is only one palindromic rearrangement: "aa".

- The output is an empty string since k = 2 exceeds the number of possible rearrangements.

Example 3:

Input: s = "bacab", k = 1

Output: "abcba"

Explanation:

- The two distinct palindromic rearrangements of "bacab" are "abcba" and "bacab".

- Lexicographically, "abcba" comes before "bacab". Since k = 1, the output is "abcba".

Constraints:

- 1 <= s.length <= 10^4

- s consists of lowercase English letters.

- s is guaranteed to be palindromic.

- 1 <= k <= 10^6

**Examples / sample tests:**

```
"abba"
2
"aa"
2
"bacab"
1
```

---

## Problem Summary
Given a palindromic string `s` and an integer `k`, the task is to find the `k`-th lexicographically smallest distinct palindromic permutation of `s`. If there are fewer than `k` such permutations, an empty string `""` should be returned.

## Intuition
The core idea revolves around the properties of palindromes and lexicographical ordering.
1.  **Palindrome Symmetry:** A palindrome is symmetric. If its length is `N`, we only need to construct the first `N // 2` characters. The remaining characters (the second half) are determined by mirroring the first half. If `N` is odd, there's a single middle character that doesn't have a pair.
2.  **Lexicographical Ordering:** To find the `k`-th smallest string, we employ a **greedy approach**. We build the string character by character from left to right. At each position, we try to place the smallest possible character ('a', then 'b', etc.).
3.  **Counting Permutations (Combinatorics):** When considering a character `c` for the current position, we need to determine how many distinct palindromic permutations can be formed if `c` is fixed at this position. This count is crucial:
    *   If `k` is less than or equal to this count, it means the `k`-th permutation starts with `c` (or an earlier character if `k` was reduced). We fix `c` and move to the next position.
    *   If `k` is greater than this count, it means the `k`-th permutation does *not* start with `c`. We subtract this count from `k` and try the next lexicographically larger character.
    The number of distinct permutations of a multiset of characters (e.g., `n1` of char A, `n2` of char B, etc., totaling `N` characters) is given by the multinomial coefficient formula: `N! / (n1! * n2! * ... * nk!)`.

## Approach
1.  **Character Frequency Analysis:**
    *   Count the occurrences of each character in the input string `s`.
    *   Identify the `middle_char`: If `s.length` is odd, exactly one character will have an odd count; this character will be the center of the palindrome.
    *   Calculate `half_counts`: For each character, store `count // 2`. These `half_counts` represent the characters available for constructing the first `N // 2` positions of the palindrome.

2.  **Precompute Factorials:**
    *   The maximum number of characters in the first half is `s.length // 2`, which can be up to `5000`.
    *   Precompute factorials up to `s.length // 2` to efficiently calculate multinomial coefficients. Store them in an array `factorials[i] = i!`.

3.  **Greedy Construction of the First Half:**
    *   Initialize an empty list `first_half_chars` to store the characters of the first half.
    *   Initialize `current_total_chars` as the sum of all `half_counts`.
    *   Iterate `half_len = s.length // 2` times (for each position in the first half):
        *   For each position, iterate through characters `c` from 'a' to 'z':
            *   If `half_counts[c]` is greater than 0 (meaning `c` is available):
                *   **Temporarily decrement** `half_counts[c]` and `current_total_chars`.
                *   **Calculate `perms`:** Use the `multinomial_coefficient` formula (with the updated `half_counts` and `current_total_chars`) to find how many distinct permutations can be formed for the *remaining* `half_len - current_position` slots.
                *   **Compare `k` with `perms`:**
                    *   If `k <= perms`: This means the `k`-th permutation falls within the branch starting with `c`. Append `c` to `first_half_chars`, mark `c` as chosen, and break from the inner loop (move to the next position).
                    *   Else (`k > perms`): The `k`-th permutation is not in this branch. Subtract `perms` from `k`. **Backtrack:** Increment `half_counts[c]` and `current_total_chars` back to their previous values. Continue to the next character.
        *   If no character was chosen for the current position (meaning `k` was too large for any valid prefix), return `""`.

4.  **Construct the Full Palindrome:**
    *   Join `first_half_chars` to form `first_half_str`.
    *   Create `second_half_str` by reversing `first_half_str`.
    *   If `s.length` is odd, the result is `first_half_str + middle_char + second_half_str`.
    *   If `s.length` is even, the result is `first_half_str + second_half_str`.

## Visualization
The process can be visualized as traversing a decision tree. At each level (position), we choose a character. Each branch represents a choice, and we calculate how many permutations can be formed from that choice.

```mermaid
graph TD
    A[Start: k=2, half_counts={a:1, b:1}] --> B{Pos 0: Choose char}
    B --> C1[Try 'a': temp_counts={a:0, b:1}]
    C1 --> C1a{Calculate perms for remaining (1 char 'b'): 1}
    C1a --> C1b[k=2 > 1. k = 2-1=1. Backtrack 'a']
    B --> C2[Try 'b': temp_counts={a:1, b:0}]
    C2 --> C2a{Calculate perms for remaining (1 char 'a'): 1}
    C2a --> C2b[k=1 <= 1. Fix 'b'. Prefix="b"]
    C2b --> D{Pos 1: Choose char, current_counts={a:1, b:0}}
    D --> E1[Try 'a': temp_counts={a:0, b:0}]
    E1 --> E1a{Calculate perms for remaining (0 chars): 1}
    E1a --> E1b[k=1 <= 1. Fix 'a'. Prefix="ba"]
    E1b --> F[End: First half="ba"]
    F --> G[Result: "baab"]
```

## Dry Run
Example 1: `s = "abba", k = 2`

*   `n = 4`, `half_len = 2`, `middle_char = ''`
*   Initial `char_counts = {'a': 2, 'b': 2}`
*   Initial `half_counts = [1, 1, 0, ..., 0]` (for 'a', 'b', others)
*   `factorials = [1, 1, 2]` (up to `half_len = 2`)

| Step | `pos` | `char_to_try` | `half_counts` (before try) | `current_total_chars` (before try) | `half_counts` (after decrement) | `current_total_chars` (after decrement) | `perms` | `k` (before check) | `k <= perms`? | Action | `first_half_chars` | `k` (after action) |
| :--- | :--- | :------------ | :-------------------------- | :--------------------------------- | :------------------------------ | :-------------------------------------- | :------ | :----------------- | :------------ | :----- | :----------------- | :----------------- |
| 1    | 0    | 'a'           | `[1,1,0...]`                | 2                                  | `[0,1,0...]`                    | 1                                       | 1       | 2                  | No (2 > 1)    | `k = 2-1=1`. Backtrack 'a'. | `[]`               | 1                  |
| 2    | 0    | 'b'           | `[1,1,0...]`                | 2                                  | `[1,0,0...]`                    | 1                                       | 1       | 1                  | Yes (1 <= 1)  | Fix 'b'.           | `['b']`            | 1                  |
| 3    | 1    | 'a'           | `[1,0,0...]`                | 1                                  | `[0,0,0...]`                    | 0                                       | 1       | 1                  | Yes (1 <= 1)  | Fix 'a'.           | `['b', 'a']`       | 1                  |
| 4    | -    | -             | `[0,0,0...]`                | 0                                  | -                               | -                                       | -       | -                  | -             | Done building first half. | `['b', 'a']`       | 1                  |

Final result:
`first_half_str = "ba"`
`second_half_str = "ab"`
`middle_char = ""`
Result: `"ba" + "" + "ab" = "baab"`

## Complexity
*   **Time Complexity:** `O(N * C^2)` where `N` is `s.length` and `C` is the size of the alphabet (26 for lowercase English letters).
    *   Counting frequencies: `O(N)`.
    *   Precomputing factorials: `O(N)`.
    *   Building the first half: `half_len` iterations (`O(N)`). In each iteration, we try `C` characters. For each character, `calculate_permutations` iterates `C` times (over `half_counts`) and performs constant-time factorial lookups. So, `O(N * C * C) = O(N * C^2)`. Since `C` is a constant (26), this simplifies to `O(N)`.
*   **Space Complexity:** `O(N)`
    *   `char_counts`, `half_counts`: `O(C) = O(1)`.
    *   `factorials` array: `O(N)` (stores up to `N/2` factorials).
    *   `first_half_chars`: `O(N)` (stores `N/2` characters).

## Edge Cases
*   **`k = 1`:** The solution correctly finds the lexicographically smallest permutation by always picking the first character `c` for which `k <= perms` is true.
*   **`k` is too large:** If `k` exceeds the total number of possible distinct palindromic permutations, the `found_char_for_pos` flag will remain `False` for some position, and the function will return `""`.
*   **`s.length = 1` (e.g., "a", `k=1`):** `half_len` will be 0, so the loop for building the first half won't run. `middle_char` will be 'a'. `first_half_str` will be `""`. The result will be `"" + 'a' + "" = "a"`, which is correct.
*   **All characters are the same (e.g., "aaaaa", `k=1`):** The logic will correctly pick 'a' for all positions in the first half, resulting in "aaaaa".

## Solution

```python
import collections
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        
        # 1. Count character frequencies
        char_counts = collections.Counter(s)
        
        # 2. Determine half counts and middle character
        # half_counts will store the number of times each character
        # can appear in the first half of the palindrome.
        half_counts = [0] * 26 
        middle_char = ''
        
        for i in range(26):
            char = chr(ord('a') + i)
            count = char_counts[char]
            
            # If a character has an odd count, it must be the middle character
            # (only one such character is possible in a palindrome)
            if count % 2 == 1:
                middle_char = char
            
            # For the first half, we use half of the total count for each character
            half_counts[i] = count // 2
            
        # The length of the first half we need to construct
        half_len = n // 2
        
        # Precompute factorials for multinomial coefficient calculation
        # Max value for N in N! is half_len, which can be up to 5000.
        # Python's math.factorial handles large numbers automatically.
        factorials = [1] * (half_len + 1)
        for i in range(1, half_len + 1):
            factorials[i] = factorials[i-1] * i
            
        # Helper function to calculate the number of distinct permutations
        # for a multiset of characters.
        # total_chars: the sum of counts in current_counts (N in N! / (n1!n2!...))
        # current_counts: a list of 26 integers representing counts of 'a' through 'z'
        def calculate_permutations(current_counts, total_chars):
            if total_chars == 0:
                return 1 # An empty string has 1 permutation (itself)
            
            res = factorials[total_chars]
            for count in current_counts:
                res //= factorials[count] # Integer division
            return res

        # 3. Build the first half of the palindrome greedily
        first_half_chars = []
        current_total_chars = sum(half_counts) # Sum of counts in half_counts
        
        # Iterate for each position in the first half
        for _ in range(half_len):
            found_char_for_pos = False
            # Try characters 'a' through 'z' in lexicographical order
            for i in range(26): 
                if half_counts[i] > 0: # If we have this character available
                    # Temporarily decrement its count and the total count
                    half_counts[i] -= 1
                    current_total_chars -= 1
                    
                    # Calculate how many distinct palindromic permutations
                    # can be formed if we fix this character at the current position
                    perms = calculate_permutations(half_counts, current_total_chars)
                    
                    if k <= perms:
                        # If k falls within this branch, this is the character we want
                        first_half_chars.append(chr(ord('a') + i))
                        found_char_for_pos = True
                        break # Move to the next position in the first half
                    else:
                        # k is larger than the number of permutations in this branch.
                        # Subtract these permutations from k and backtrack (undo the temporary decrement).
                        k -= perms
                        half_counts[i] += 1
                        current_total_chars += 1
            
            if not found_char_for_pos:
                # If we tried all characters for the current position and couldn't find one
                # that satisfies k, it means k is too large.
                return ""
        
        # 4. Construct the full palindrome
        first_half_str = "".join(first_half_chars)
        second_half_str = first_half_str[::-1] # Reverse the first half
        
        if n % 2 == 1:
            # If n is odd, insert the middle character
            return first_half_str + middle_char + second_half_str
        else:
            # If n is even, no middle character
            return first_half_str + second_half_str

```

## Why This Works
This approach works because it systematically constructs the `k`-th lexicographically smallest palindrome by making locally optimal, greedy choices. By building only the first half and using `half_counts`, we ensure that the resulting string will always be a valid palindrome. The core principle is to iterate through characters 'a' to 'z' for each position. For each candidate character, we calculate the number of distinct permutations that can be formed if that character is chosen. If `k` falls within this count, we commit to that character; otherwise, we reduce `k` and move to the next character. This process effectively prunes the search space, guaranteeing that we find the `k`-th smallest permutation without explicitly generating all of them. The `k` value acts as a rank that is continuously updated to reflect the relative rank within the remaining possibilities.

---
<sub>Generated 2026-07-29 03:52 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
