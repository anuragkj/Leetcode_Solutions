# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-08-28 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/)

**Topics:** Two Pointers, String, Enumeration

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given two strings s and target, each of length n, consisting of lowercase English letters.

Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

Example 1:

Input: s = "baba", target = "abba"

Output: "baab"

Explanation:

- The palindromic permutations of s (in lexicographical order) are "abba" and "baab".

- The lexicographically smallest permutation that is strictly greater than target is "baab".

Example 2:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

- The palindromic permutations of s (in lexicographical order) are "abba" and "baab".

- None of them is lexicographically strictly greater than target. Therefore, the answer is "".

Example 3:

Input: s = "abc", target = "abb"

Output: ""

Explanation:

s has no palindromic permutations. Therefore, the answer is "".

Example 4:

Input: s = "aac", target = "abb"

Output: "aca"

Explanation:

- The only palindromic permutation of s is "aca".

- "aca" is strictly greater than target. Therefore, the answer is "aca".

Constraints:

- 1 <= n == s.length == target.length <= 300

- s and target consist of only lowercase English letters.

**Examples / sample tests:**

```
"baba"
"abba"
"baba"
"bbaa"
"abc"
"abb"
"aac"
"abb"
```

---

## Problem Summary
Given two strings `s` and `target` of equal length `n`, find the lexicographically smallest string that is a palindromic permutation of `s` and is strictly greater than `target`. If no such string exists, return an empty string.

## Intuition
To find the lexicographically smallest palindromic permutation that is strictly greater than `target`, we can use a **backtracking** approach. A palindrome is determined by its first half (and a potential middle character for odd-length strings). We'll build the first half character by character, from left to right.

The key observations are:
1.  **Palindromic Permutation Condition:** A string can form a palindrome if and only if at most one character has an odd count. If `n` is even, all character counts must be even. If `n` is odd, exactly one character can have an odd count, which will be the middle character.
2.  **Lexicographical Smallest:** To ensure the resulting palindrome is lexicographically smallest, we should try placing the smallest possible characters ('a', then 'b', etc.) at each position of the first half. The first valid palindrome we construct will be the answer.
3.  **"Strictly Greater Than Target":** This condition is crucial. When building the first half, we maintain a flag (`is_greater`).
    *   If the prefix of our current palindrome is already strictly greater than the corresponding prefix of `target`, then we can greedily pick the smallest available characters for the remaining positions to ensure the overall palindrome is as small as possible.
    *   If the prefix of our current palindrome is equal to the corresponding prefix of `target`, we must pick a character for the current position that is greater than or equal to `target`'s character at that position. If we pick a character strictly greater, `is_greater` becomes `True`. If we pick an equal character, `is_greater` remains `False`, and we continue comparing.
    *   If we pick a character smaller than `target`'s character (when `is_greater` is `False`), that path is invalid and we prune it.

## Approach
1.  **Pre-processing:**
    *   Count the frequencies of all characters in `s` using a `collections.Counter`.
    *   Identify characters with odd counts. If there's more than one, or if `n` is even and there's any odd count, no palindromic permutation is possible. Return `""`.
    *   If `n` is odd, store the single character with an odd count as `middle_char` and decrement its count by one (it will be placed in the center, not part of the paired characters).
    *   Convert the character counts to a list of 26 integers (`counts_arr`) for efficient indexing.

2.  **Backtracking Function (`solve`):**
    *   Define `solve(idx, current_first_half_list, current_counts, is_greater)`:
        *   `idx`: The current index we are trying to fill in the first half (from `0` to `n // 2 - 1`).
        *   `current_first_half_list`: A list of characters representing the first half built so far.
        *   `current_counts`: The remaining available character counts (passed by reference, so changes are reflected and then backtracked).
        *   `is_greater`: A boolean flag indicating if the palindrome built so far is already lexicographically strictly greater than `target`'s prefix.

    *   **Base Case:** If `idx == n // 2` (the first half is complete):
        *   Construct the full palindrome: `P = "".join(current_first_half_list) + middle_char + "".join(current_first_half_list[::-1])`.
        *   If `P > target`, return `P`. Otherwise, return `""` (indicating this path didn't yield a valid result).

    *   **Recursive Step:**
        *   Determine `start_char_code`:
            *   If `is_greater` is `True`, we can pick any character from 'a' onwards (`start_char_code = 0`).
            *   If `is_greater` is `False`, we must pick a character `char >= target[idx]`. So, `start_char_code = ord(target[idx]) - ord('a')`.
        *   Iterate `char_code` from `start_char_code` to `25` (representing 'a' to 'z'):
            *   Let `char = chr(ord('a') + char_code)`.
            *   **Check Availability:** If `current_counts[char_code] < 2`, we don't have a pair of this character, so skip to the next `char_code`.
            *   **Make Choice:**
                *   Decrement `current_counts[char_code]` by 2 (one for `idx`, one for `n-1-idx`).
                *   Update `new_is_greater = is_greater or (char > target[idx])`.
                *   Append `char` to `current_first_half_list`.
                *   Recursively call `solve(idx + 1, current_first_half_list, current_counts, new_is_greater)`.
                *   **Backtrack:** Remove `char` from `current_first_half_list` and increment `current_counts[char_code]` by 2.
                *   If the recursive call `result` is not `""` (meaning a valid palindrome was found), return `result` immediately (since we iterate characters in lexicographical order, this is the smallest valid one).

    *   If the loop finishes without finding a solution, return `""`.

3.  **Initial Call:** Call `solve(0, [], counts_arr, False)` and return its result.

## Visualization
Let's visualize the backtracking for `s = "baba"`, `target = "abba"`. `n=4`, `first_half_len=2`. `counts={'a':2, 'b':2}`. `middle_char=''`.

```
solve(idx=0, first_half=[], counts={'a':2,'b':2}, is_greater=False)
  |
  +-- Try char='a' (target[0]='a'):
  |   (char 'a' is NOT > target[0] 'a', so new_is_greater remains False)
  |   counts: {'a':0,'b':2}
  |   first_half: ['a']
  |   solve(idx=1, first_half=['a'], counts={'a':0,'b':2}, is_greater=False)
  |     |
  |     +-- Try char='a': (counts['a'] < 2) -> SKIP
  |     +-- Try char='b' (target[1]='b'):
  |     |   (char 'b' is NOT > target[1] 'b', so new_is_greater remains False)
  |     |   counts: {'a':0,'b':0}
  |     |   first_half: ['a','b']
  |     |   solve(idx=2, first_half=['a','b'], counts={'a':0,'b':0}, is_greater=False)
  |     |     |
  |     |     +-- BASE CASE: idx == first_half_len (2)
  |     |     |   P = "ab" + "" + "ba" = "abba"
  |     |     |   Is "abba" > "abba"? No. Return "".
  |     |   (Backtrack: pop 'b', counts['b']+=2)
  |     |
  |     +-- No other chars for idx=1. Return "".
  |   (Backtrack: pop 'a', counts['a']+=2)
  |
  +-- Try char='b' (target[0]='a'):
  |   (char 'b' IS > target[0] 'a', so new_is_greater becomes True)
  |   counts: {'a':2,'b':0}
  |   first_half: ['b']
  |   solve(idx=1, first_half=['b'], counts={'a':2,'b':0}, is_greater=True)  <-- is_greater is now True!
  |     |
  |     +-- Try char='a': (is_greater is True, so target[1] comparison is skipped)
  |     |   counts: {'a':0,'b':0}
  |     |   first_half: ['b','a']
  |     |   solve(idx=2, first_half=['b','a'], counts={'a':0,'b':0}, is_greater=True)
  |     |     |
  |     |     +-- BASE CASE: idx == first_half_len (2)
  |     |     |   P = "ba" + "" + "ab" = "baab"
  |     |     |   Is "baab" > "abba"? Yes! Return "baab".
  |     |   (Result "baab" is propagated up)
  |     |
  |     +-- Return "baab".
  |
  +-- Return "baab".
```

## Dry Run
**Example 1:** `s = "baba"`, `target = "abba"`

**Initial State:**
*   `n = 4`, `first_half_len = 2`
*   `char_counts = {'a': 2, 'b': 2}`
*   `odd_count_char = ''` (since `n` is even, all counts must be even)
*   `counts_arr = [2, 2, 0, ..., 0]` (for 'a', 'b', ...)

**Call:** `solve(idx=0, current_first_half_list=[], current_counts=[2,2,...], is_greater=False)`

| `idx` | `current_first_half_list` | `current_counts` (relevant) | `is_greater` | `char` (tried) | `target[idx]` | `new_is_greater` | `Result` |
| :---- | :------------------------ | :-------------------------- | :----------- | :------------- | :------------ | :--------------- | :------- |
| 0     | `[]`                      | `{'a':2, 'b':2}`            | `False`      | `'a'`          | `'a'`         | `False`          |          |
| 1     | `['a']`                   | `{'a':0, 'b':2}`            | `False`      | `'a'`          | `'b'`         | (skip: `counts['a']<2`) |          |
| 1     | `['a']`                   | `{'a':0, 'b':2}`            | `False`      | `'b'`          | `'b'`         | `False`          |          |
| 2     | `['a', 'b']`              | `{'a':0, 'b':0}`            | `False`      | (Base Case)    |               |                  | `""` (`"abba"` not `>` `"abba"`) |
| 1     | `['a']`                   | `{'a':0, 'b':2}`            | `False`      | (loop ends)    |               |                  | `""`     |
| 0     | `[]`                      | `{'a':2, 'b':2}`            | `False`      | `'b'`          | `'a'`         | `True`           |          |
| 1     | `['b']`                   | `{'a':2, 'b':0}`            | `True`       | `'a'`          | (ignored)     | `True`           |          |
| 2     | `['b', 'a']`              | `{'a':0, 'b':0}`            | `True`       | (Base Case)    |               |                  | `"baab"` (`"baab"` `>` `"abba"`) |
| 1     | `['b']`                   | `{'a':2, 'b':0}`            | `True`       | (loop ends)    |               |                  | `"baab"` |
| 0     | `[]`                      | `{'a':2, 'b':2}`            | `False`      | (loop ends)    |               |                  | `"baab"` |

**Final Result:** `"baab"`

## Complexity
*   **Time Complexity:** `O(N * 26)`. The recursion depth is `N/2`. At each level, we iterate through at most 26 possible characters. The `is_greater` flag allows for significant pruning: once `is_greater` becomes `True`, subsequent choices are greedy (picking the smallest available character), effectively reducing the remaining search to `O((N/2 - idx) * 26)`. The string concatenation and comparison at the base case take `O(N)` time, but this happens only once for the first valid result found. Thus, the overall time complexity is dominated by the `N/2` levels * 26 choices, which is `O(N * 26)`.
*   **Space Complexity:** `O(N)` for the recursion stack depth (up to `N/2`) and `O(N)` for storing `current_first_half_list`. The `counts_arr` takes `O(26)` space.

## Edge Cases
*   **No palindromic permutation possible:**
    *   `s = "abc", target = "abb"`: `s` has three characters with odd counts (`a:1, b:1, c:1`). The initial check correctly returns `""`.
    *   `s = "ab", target = "aa"`: `n=2` (even), but `a:1, b:1` (two odd counts). The initial check correctly returns `""`.
*   **Only one palindromic permutation, but not greater than target:**
    *   `s = "baba", target = "bbaa"`: Palindromic permutations are "abba" and "baab". Neither is strictly greater than "bbaa". The base case `P > target` correctly returns `""` for all paths.
*   **Only one palindromic permutation, and it is greater than target:**
    *   `s = "aac", target = "abb"`: The only palindromic permutation is "aca". "aca" > "abb". The solution will find "aca" and return it.
*   **`n = 1`:**
    *   `s = "a", target = "a"`: `n=1`, `first_half_len=0`. `odd_count_char='a'`. `solve(0,...)` immediately hits base case. `P="a"`. `"a" > "a"` is `False`. Returns `""`. Correct.
    *   `s = "b", target = "a"`: `n=1`, `first_half_len=0`. `odd_count_char='b'`. `solve(0,...)` immediately hits base case. `P="b"`. `"b" > "a"` is `True`. Returns `"b"`. Correct.

## Solution

```python
import collections

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        
        # 1. Pre-process: Count characters and check for palindromic permutation possibility
        char_counts = collections.Counter(s)
        
        odd_count_char = ''
        odd_count_chars_list = []
        for char_code in range(26):
            char = chr(ord('a') + char_code)
            if char_counts[char] % 2 != 0:
                odd_count_chars_list.append(char)
        
        # Rule 1: At most one character can have an odd count
        if len(odd_count_chars_list) > 1:
            return "" 
        
        # Rule 2: If string length is even, all character counts must be even
        if n % 2 == 0 and len(odd_count_chars_list) > 0:
            return ""
            
        # If string length is odd, the single odd-count character becomes the middle character
        if n % 2 != 0 and len(odd_count_chars_list) == 1:
            odd_count_char = odd_count_chars_list[0]
            char_counts[odd_count_char] -= 1 # This char is used for the middle, so its count for pairs is now even
        
        # Convert counts to a list for easier indexing (0-25 for 'a'-'z')
        # All remaining counts in counts_arr must be even.
        counts_arr = [char_counts[chr(ord('a') + i)] for i in range(26)]
        
        first_half_len = n // 2
        
        # 2. Backtracking function to build the first half
        # idx: current position to fill in the first half
        # current_first_half_list: characters chosen for the first half so far
        # current_counts: mutable list of remaining character counts
        # is_greater: True if the current prefix is already lexicographically greater than target's prefix
        def solve(idx: int, current_first_half_list: list[str], current_counts: list[int], is_greater: bool) -> str:
            if idx == first_half_len:
                # Base case: The first half is complete
                first_half_str = "".join(current_first_half_list)
                palindrome = first_half_str + odd_count_char + first_half_str[::-1]
                
                if palindrome > target:
                    return palindrome
                else:
                    return "" # This palindrome is not strictly greater than target
            
            # Determine the starting character code for iteration
            # If we are already greater, we can pick any character ('a' onwards)
            # If not, we must pick a character >= target[idx]
            start_char_code = 0
            if not is_greater:
                start_char_code = ord(target[idx]) - ord('a')
            
            for char_code in range(start_char_code, 26):
                char = chr(ord('a') + char_code)
                
                # Check if we have at least two of this character for a pair
                if current_counts[char_code] >= 2:
                    current_counts[char_code] -= 2 # Use two characters
                    
                    # Update is_greater flag for the next recursive call
                    # It becomes True if it was already True, or if current char is > target[idx]
                    new_is_greater = is_greater or (char > target[idx])
                    
                    current_first_half_list.append(char) # Add char to the first half
                    
                    # Recurse for the next position
                    result = solve(idx + 1, current_first_half_list, current_counts, new_is_greater)
                    
                    current_first_half_list.pop() # Backtrack: remove char
                    current_counts[char_code] += 2 # Backtrack: restore counts
                    
                    if result != "": # If a valid palindrome is found, return it immediately
                        return result # This is the lexicographically smallest due to iteration order
            
            return "" # No valid palindrome found from this path
        
        # Initial call to the backtracking function
        return solve(0, [], counts_arr, False)

```

## Why This Works
The solution works by systematically exploring potential first halves of palindromes in **lexicographical order**. By iterating through characters from 'a' to 'z' at each position `idx` and returning the *first* valid result found, we guarantee that the returned string is the lexicographically smallest. The `is_greater` flag is crucial for pruning the search space:
1.  It ensures that we only consider paths that can lead to a string strictly greater than `target`.
2.  Once `is_greater` becomes `True`, we can greedily pick the smallest available characters for the remaining positions, as the "strictly greater" condition is already met, and we want the overall palindrome to be as small as possible. This greedy selection significantly reduces the number of branches explored, making the `O(N * 26)` complexity feasible for `N=300`. The initial character count check and `middle_char` handling ensure that only valid palindromic permutations are ever constructed.

---
<sub>Generated 2026-08-28 12:05 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
