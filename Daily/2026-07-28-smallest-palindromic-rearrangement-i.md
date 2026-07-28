# [3517] Smallest Palindromic Rearrangement I

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-07-28 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/smallest-palindromic-rearrangement-i/)

**Topics:** String, Sorting, Counting Sort

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a palindromic string s.

Return the lexicographically smallest palindromic permutation of s.

Example 1:

Input: s = "z"

Output: "z"

Explanation:

A string of only one character is already the lexicographically smallest palindrome.

Example 2:

Input: s = "babab"

Output: "abbba"

Explanation:

Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.

Example 3:

Input: s = "daccad"

Output: "acddca"

Explanation:

Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.

Constraints:

- 1 <= s.length <= 10^5

- s consists of lowercase English letters.

- s is guaranteed to be palindromic.

**Examples / sample tests:**

```
"z"
"babab"
"daccad"
```

---

## Problem Summary
Given a string `s` that is guaranteed to be a palindrome, the task is to rearrange its characters to form a new palindrome that is lexicographically the smallest possible.

## Intuition
A **palindrome** reads the same forwards and backward. This means it's symmetric: its first half mirrors its second half. For example, in "racecar", "rac" is the first half, and "car" (reverse of "rac") is the second half, with 'e' in the middle.

To make a string **lexicographically smallest**, we want the smallest characters ('a', then 'b', etc.) to appear as early as possible in the string.

Combining these ideas: to make the *entire palindrome* lexicographically smallest, we must make its **first half** lexicographically smallest. If the first half is "abc...", then the entire palindrome will start with "abc...", which is the smallest possible prefix given the available characters.

Since the input `s` is already a palindrome, we know that all its characters appear an even number of times, except possibly one character if the string's length is odd. This single odd-count character must be placed in the exact middle of our resulting palindrome. All other characters must form pairs, with one character from each pair going into the first half and the other into the second (reversed) half.

## Approach
The optimal approach involves counting character frequencies and then constructing the palindrome greedily:

1.  **Count Character Frequencies**: First, count how many times each character ('a' through 'z') appears in the input string `s`. A frequency map (like `collections.Counter` in Python or an array of size 26) is suitable for this.

2.  **Identify the Middle Character**: Iterate through the character counts. If any character has an **odd** frequency, it must be the **middle character** of the final palindrome. Store this character. Since `s` is guaranteed to be a palindrome, there will be at most one such character. If all characters have even frequencies, there is no middle character (or it's an empty string).

3.  **Construct the First Half**: Initialize an empty list to build the first half of the palindrome. Iterate through characters from 'a' to 'z' (in alphabetical order). For each character `c` with count `freq[c]`:
    *   Append `c` to the `first_half_chars` list `freq[c] // 2` times. This ensures we use half of each character's total count for the first half, prioritizing smaller characters.

4.  **Assemble the Result**:
    *   Convert the `first_half_chars` list into a string, let's call it `first_half_str`.
    *   The second half of the palindrome is simply the reverse of `first_half_str`. Let's call it `second_half_str`.
    *   The final lexicographically smallest palindrome is formed by concatenating: `first_half_str` + `middle_char` + `second_half_str`.

## Visualization

Imagine building the palindrome by taking characters from the available pool and placing them into the first half, then mirroring that first half to complete the structure.

Let's use `s = "daccad"` as an example:

1.  **Count Characters**:
    `'a': 2`
    `'c': 2`
    `'d': 2`

2.  **Identify Middle Character**:
    All character counts are even. So, `middle_char = ""` (empty string).

3.  **Construct First Half**:
    We iterate 'a' through 'z'. For each character, we take `count // 2` instances:
    - For 'a': `2 // 2 = 1` time. Add 'a'.
    - For 'b': `0 // 2 = 0` times.
    - For 'c': `2 // 2 = 1` time. Add 'c'.
    - For 'd': `2 // 2 = 1` time. Add 'd'.
    ... (and so on for 'e' through 'z', which have 0 counts)

    This builds our `first_half`:
    `first_half = "a" + "c" + "d" = "acd"`

    ```
    Available Chars:  [a, a, c, c, d, d]
                       ^  ^  ^  ^  ^  ^
                       |  |  |  |  |  |
                       V  V  V  V  V  V
    First Half:      [a] [c] [d]
                     /           \
                    /             \
                   /               \
    Palindrome:  "a" "c" "d"  [middle]  "d" "c" "a"
                 <--------------------------------->
                      Lexicographically Smallest Palindrome
    ```

4.  **Assemble**:
    `first_half_str = "acd"`
    `middle_char = ""`
    `second_half_str = "acd"[::-1] = "dca"`

    `Result = first_half_str + middle_char + second_half_str`
    `Result = "acd" + "" + "dca" = "acddca"`

## Dry Run

Let's trace Example 3: `s = "daccad"`

| Step | Action                                  | `char_counts`                               | `middle_char` | `first_half_chars` | `first_half_str` | `second_half_str` | `result`   |
| :--- | :-------------------------------------- | :------------------------------------------ | :------------ | :----------------- | :--------------- | :---------------- | :--------- |
| 1    | Initialize & Count Frequencies          | `{'a': 2, 'c': 2, 'd': 2}`                  | `""`          | `[]`               | `""`             | `""`              | `""`       |
| 2    | Identify Middle Char (iterate 'a' to 'z') |                                             |               |                    |                  |                   |            |
|      | `char = 'a'`, count = 2 (even)          | `{'a': 2, 'c': 2, 'd': 2}`                  | `""`          | `[]`               |                  |                   |            |
|      | `char = 'b'`, count = 0 (even)          | `{'a': 2, 'c': 2, 'd': 2}`                  | `""`          | `[]`               |                  |                   |            |
|      | `char = 'c'`, count = 2 (even)          | `{'a': 2, 'c': 2, 'd': 2}`                  | `""`          | `[]`               |                  |                   |            |
|      | `char = 'd'`, count = 2 (even)          | `{'a': 2, 'c': 2, 'd': 2}`                  | `""`          | `[]`               |                  |                   |            |
|      | ... (rest of chars 'e' to 'z' are 0)    |                                             |               |                    |                  |                   |            |
|      | **Middle Char Final**                   |                                             | `""`          |                    |                  |                   |            |
| 3    | Construct First Half (iterate 'a' to 'z') |                                             |               |                    |                  |                   |            |
|      | `char = 'a'`, `count = 2`. Add `2//2=1` 'a'. | `{'a': 2, 'c': 2, 'd': 2}`                  | `""`          | `['a']`            |                  |                   |            |
|      | `char = 'b'`, `count = 0`. Add `0//2=0` 'b'. | `{'a': 2, 'c': 2, 'd': 2}`                  | `""`          | `['a']`            |                  |                   |            |
|      | `char = 'c'`, `count = 2`. Add `2//2=1` 'c'. | `{'a': 2, 'c': 2, 'd': 2}`                  | `""`          | `['a', 'c']`       |                  |                   |            |
|      | `char = 'd'`, `count = 2`. Add `2//2=1` 'd'. | `{'a': 2, 'c': 2, 'd': 2}`                  | `""`          | `['a', 'c', 'd']`  |                  |                   |            |
|      | ... (rest of chars 'e' to 'z' are 0)    |                                             |               |                    |                  |                   |            |
|      | **First Half String**                   |                                             |               |                    | `"acd"`          |                   |            |
| 4    | Assemble Final Palindrome               |                                             |               |                    | `"acd"`          | `"dca"`           | `"acddca"` |

**Final Result:** `"acddca"`

## Complexity

*   **Time Complexity**: O(N + K), where N is the length of the input string `s` and K is the size of the alphabet (26 for lowercase English letters).
    *   Counting character frequencies takes O(N) time.
    *   Iterating through the alphabet (26 characters) to find the middle character and construct the first half takes O(K) time.
    *   Joining the list of characters for the first half takes O(N) time in the worst case (if all characters are unique).
    *   String reversal and concatenation take O(N) time.
    *   Overall, the dominant factor is N.

*   **Space Complexity**: O(N + K).
    *   The frequency map (e.g., `collections.Counter`) takes O(K) space (at most 26 entries).
    *   The list `first_half_chars` can store up to N/2 characters, and the final result string takes O(N) space.
    *   Overall, the dominant factor is N.

## Edge Cases

*   **Single character string**: `s = "z"`
    *   `char_counts = {'z': 1}`. `middle_char = 'z'`. `first_half_chars = []`.
    *   Result: `"" + "z" + "" = "z"`. Correct.
*   **String with all same characters**: `s = "aaaaa"`
    *   `char_counts = {'a': 5}`. `middle_char = 'a'`. `first_half_chars = ['a', 'a']`.
    *   Result: `"aa" + "a" + "aa" = "aaaaa"`. Correct.
*   **Even length string with no middle character**: `s = "abba"`
    *   `char_counts = {'a': 2, 'b': 2}`. `middle_char = ""`. `first_half_chars = ['a', 'b']`.
    *   Result: `"ab" + "" + "ba" = "abba"`. Correct.

## Solution

```python
import collections

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # 1. Count character frequencies
        # collections.Counter is efficient for this.
        char_counts = collections.Counter(s)

        # 2. Identify the middle character (if any)
        # A palindrome can have at most one character with an odd count.
        # This character will be placed in the very center.
        middle_char = ""
        # Iterate through characters 'a' to 'z' to ensure consistent order
        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            if char_counts[char] % 2 == 1:
                middle_char = char
                # For a valid palindrome, there's at most one such character.
                # We could break here, but iterating 26 times is negligible.
                
        # 3. Construct the first half of the palindrome
        # To make the overall palindrome lexicographically smallest,
        # its first half must be lexicographically smallest.
        # We achieve this by appending characters in alphabetical order,
        # using half of their total counts.
        first_half_chars = []
        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            # Add char (count // 2) times to the first half
            # For example, if 'a' appears 4 times, we use 2 'a's in the first half.
            # If 'a' appears 5 times, we use 2 'a's in the first half (the 5th 'a' is the middle_char).
            first_half_chars.extend([char] * (char_counts[char] // 2))
        
        # Convert the list of characters to a string for the first half
        first_half_str = "".join(first_half_chars)

        # 4. Assemble the final palindrome
        # The second half is simply the reverse of the first half.
        second_half_str = first_half_str[::-1]
        
        # Concatenate the parts: first half + middle char (if any) + reversed first half
        return first_half_str + middle_char + second_half_str

```

## Why This Works

This approach works because it directly addresses the two core requirements: forming a **palindrome** and making it **lexicographically smallest**. A palindrome is inherently symmetric, meaning its first half dictates its second half. By constructing the first half using characters in **alphabetical order** and taking exactly half of each character's total count (excluding the single middle character if present), we guarantee that the prefix of the resulting string is the smallest possible. The remaining characters (those not used in the first half or as the middle character) are then used to form the mirror image, ensuring the entire string is a valid palindrome and, by extension, the lexicographically smallest one possible.

---
<sub>Generated 2026-07-28 03:48 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
