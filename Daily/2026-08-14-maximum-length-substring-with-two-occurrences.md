# [3090] Maximum Length Substring With Two Occurrences

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-08-14 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/)

**Topics:** Hash Table, String, Sliding Window

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".

Constraints:

- 2 <= s.length <= 100

- s consists only of lowercase English letters.

**Examples / sample tests:**

```
"bcbbbcba"
"aaaa"
```

---

## Problem Summary
Find the longest possible substring within a given string `s` such that no character appears more than twice in that substring.

## Intuition
This problem asks for the **maximum length** of a **substring** that satisfies a certain condition (character counts). This is a classic indicator for the **sliding window** technique. We can maintain a window `s[left...right]` and expand it by moving the `right` pointer. If the window becomes invalid (any character count exceeds two), we shrink it by moving the `left` pointer until it's valid again. We keep track of the maximum valid window length encountered.

## Approach
1.  Initialize `max_length = 0` to store the longest valid substring found.
2.  Initialize `left = 0` as the left boundary of our sliding window.
3.  Use a **hash map** (dictionary in Python, `char_counts`) to store the frequency of each character within the current window `s[left...right]`.
4.  Iterate with a `right` pointer from `0` to `len(s) - 1`:
    a.  Add the character `s[right]` to our window by incrementing its count in `char_counts`.
    b.  **Check for violation**: If the count of `s[right]` (the character just added) becomes greater than 2, the window is now invalid.
    c.  **Shrink the window**: While `char_counts[s[right]]` is greater than 2:
        i.  Remove the character `s[left]` from the window by decrementing its count in `char_counts`.
        ii. Move the `left` pointer one position to the right (`left += 1`).
        This process continues until the window becomes valid again (i.e., `s[right]`'s count is no longer greater than 2).
    d.  After ensuring the window `s[left...right]` is valid, update `max_length = max(max_length, right - left + 1)`.
5.  After the `right` pointer has traversed the entire string, return `max_length`.

## Visualization
Let's trace `s = "bcbbbcba"` with `L` (left pointer), `R` (right pointer), `Counts` (character frequencies), and `MaxLen` (maximum length).

```
s: b c b b b c b a
   ^
   L
   ^
   R
Counts: {}
MaxLen: 0

Step 1: R moves to 0 ('b')
s: b c b b b c b a
   ^
   L
   ^
   R
Counts: {'b': 1}
MaxLen: 1 (R-L+1 = 0-0+1)

Step 2: R moves to 1 ('c')
s: b c b b b c b a
   ^ ^
   L R
Counts: {'b': 1, 'c': 1}
MaxLen: 2 (R-L+1 = 1-0+1)

Step 3: R moves to 2 ('b')
s: b c b b b c b a
   ^   ^
   L   R
Counts: {'b': 2, 'c': 1}
MaxLen: 3 (R-L+1 = 2-0+1)

Step 4: R moves to 3 ('b')
s: b c b b b c b a
   ^     ^
   L     R
Counts: {'b': 3, 'c': 1}  <- 'b' count > 2!
   Shrink window:
   s[L] = 'b', decrement 'b' count. L moves.
s: b c b b b c b a
     ^   ^
     L   R
Counts: {'b': 2, 'c': 1}  <- Valid again!
MaxLen: 3 (R-L+1 = 3-1+1)

Step 5: R moves to 4 ('b')
s: b c b b b c b a
     ^       ^
     L       R
Counts: {'b': 3, 'c': 1}  <- 'b' count > 2!
   Shrink window:
   s[L] = 'c', decrement 'c' count. L moves.
s: b c b b b c b a
       ^     ^
       L     R
Counts: {'b': 3}          <- 'b' count > 2!
   Shrink window:
   s[L] = 'b', decrement 'b' count. L moves.
s: b c b b b c b a
         ^   ^
         L   R
Counts: {'b': 2}          <- Valid again!
MaxLen: 3 (R-L+1 = 4-3+1)

... and so on until R reaches the end.
```

## Dry Run
Let's walk through `s = "bcbbbcba"` (Example 1) using the approach.

| `right` | `s[right]` | `char_counts` (after `s[right]` added) | `char_counts[s[right]] > 2`? | `s[left]` (if shrink) | `char_counts` (after shrinking) | `left` (after shrinking) | `max_length` | `Current Substring` |
| :------ | :--------- | :------------------------------------- | :--------------------------- | :-------------------- | :----------------------------------- | :----------------------- | :----------- | :------------------ |
| 0       | 'b'        | {'b': 1}                               | No                           | -                     | {'b': 1}                             | 0                        | 1            | "b"                 |
| 1       | 'c'        | {'b': 1, 'c': 1}                       | No                           | -                     | {'b': 1, 'c': 1}                     | 0                        | 2            | "bc"                |
| 2       | 'b'        | {'b': 2, 'c': 1}                       | No                           | -                     | {'b': 2, 'c': 1}                     | 0                        | 3            | "bcb"               |
| 3       | 'b'        | {'b': 3, 'c': 1}                       | Yes ('b': 3)                 | 'b'                   | {'b': 2, 'c': 1}                     | 1                        | 3            | "cbb"               |
| 4       | 'b'        | {'b': 3, 'c': 1}                       | Yes ('b': 3)                 | 'c'                   | {'b': 3}                             | 2                        | 3            | "bbb" (still invalid) |
|         |            |                                        | Yes ('b': 3)                 | 'b'                   | {'b': 2}                             | 3                        | 3            | "bb"                |
| 5       | 'c'        | {'b': 2, 'c': 1}                       | No                           | -                     | {'b': 2, 'c': 1}                     | 3                        | 3            | "bbc"               |
| 6       | 'b'        | {'b': 3, 'c': 1}                       | Yes ('b': 3)                 | 'b'                   | {'b': 2, 'c': 1}                     | 4                        | 3            | "bcba"              |
| 7       | 'a'        | {'b': 2, 'c': 1, 'a': 1}               | No                           | -                     | {'b': 2, 'c': 1, 'a': 1}             | 4                        | 4            | "bcba"              |

The final `max_length` returned is 4.

## Complexity
*   **Time Complexity**: O(N), where N is the length of the string `s`. Both `left` and `right` pointers traverse the string at most once. Each character is added to `char_counts` once and removed from `char_counts` at most once.
*   **Space Complexity**: O(1). The `char_counts` dictionary stores at most 26 entries (for lowercase English letters), which is a constant amount of space regardless of the input string's length.

## Edge Cases
*   **String with all unique characters** (e.g., "abcde"): The `while` loop condition `char_counts[s[right]] > 2` will never be met. `max_length` will simply become `len(s)`.
*   **String with all identical characters** (e.g., "aaaa"):
    *   `s[0]`='a', `counts={'a':1}`, `max_length=1`.
    *   `s[1]`='a', `counts={'a':2}`, `max_length=2`.
    *   `s[2]`='a', `counts={'a':3}`. `char_counts['a'] > 2` is true. `left` moves, `counts['a']` becomes 2. `max_length` remains 2.
    The solution correctly handles this, returning 2.
*   **Minimum length string** (e.g., `s = "aa"` or `s = "ab"`): The logic holds, returning 2 for "aa" and 2 for "ab".

## Solution
```python
import collections

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # char_counts will store the frequency of each character in the current window
        char_counts = collections.defaultdict(int)
        
        # left pointer of the sliding window
        left = 0
        
        # max_length will store the maximum length of a valid substring found
        max_length = 0

        # Iterate with the right pointer to expand the window
        for right in range(len(s)):
            # Add the current character s[right] to the window
            char_counts[s[right]] += 1

            # If the count of the character just added exceeds 2,
            # the window is now invalid. Shrink it from the left.
            while char_counts[s[right]] > 2:
                # Remove the character at the left pointer from the window
                char_counts[s[left]] -= 1
                # Move the left pointer to the right
                left += 1
            
            # After ensuring the window is valid, update the maximum length
            # The current valid substring length is (right - left + 1)
            max_length = max(max_length, right - left + 1)
        
        # Return the maximum length found
        return max_length

```

## Why This Works
This sliding window approach works because it maintains an **invariant**: the window `s[left...right]` always represents the longest possible valid substring ending at `right`. When we expand the window by moving `right`, we add `s[right]`. If this addition violates the condition (i.e., `s[right]`'s count exceeds 2), we *minimally* shrink the window from the `left` until the condition is restored. By doing so, we ensure that for every `right` position, `s[left...right]` is the longest valid substring ending at `right`. The maximum of these lengths across all `right` positions will be the overall maximum length substring satisfying the condition.

---
<sub>Generated 2026-08-14 03:09 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
