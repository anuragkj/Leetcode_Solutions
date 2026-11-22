# [2124] Check if All A's Appears Before All B's

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-11-22 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/)

**Topics:** String

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

Example 1:

Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.

Example 2:

Input: s = "abab"
Output: false
Explanation:
There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.

Example 3:

Input: s = "bbb"
Output: true
Explanation:
There are no 'a's, hence, every 'a' appears before every 'b' and we return true.

Constraints:

- 1 <= s.length <= 100

- s[i] is either 'a' or 'b'.

**Examples / sample tests:**

```
"aaabbb"
"abab"
"bbb"
```

---

## Problem Summary
Given a string composed solely of 'a's and 'b's, determine if all occurrences of 'a' appear strictly before all occurrences of 'b'. This means you should never find an 'a' after a 'b'.

## Intuition
Imagine scanning the string from left to right. If you haven't encountered any 'b's yet, finding an 'a' is perfectly fine. However, the moment you encounter your **first 'b'**, a critical change happens: from that point onwards, you **must not** see any more 'a's. If you do find an 'a' after you've already seen at least one 'b', then the condition "every 'a' appears before every 'b'" is violated. If you scan the entire string and this violation never occurs, then the condition holds true.

## Approach
We can solve this by iterating through the string once and keeping track of whether we've already encountered a 'b'.

1.  Initialize a boolean flag, let's call it `found_b`, to `False`. This flag will tell us if we have seen any 'b's so far.
2.  Iterate through each character (`char`) in the input string `s` from left to right.
3.  Inside the loop:
    *   If `char` is `'b'`:
        *   Set `found_b` to `True`. This marks that we have now entered the "b-zone" of the string.
    *   If `char` is `'a'`:
        *   Check if `found_b` is already `True`.
        *   If `found_b` is `True`, it means we've just found an 'a' *after* having already seen at least one 'b'. This violates the problem's condition. In this case, we can immediately return `False`.
4.  If the loop completes without ever returning `False`, it means we never found an 'a' after a 'b'. Therefore, all 'a's appeared before all 'b's (or there were no 'a's after 'b's), so we return `True`.

## Visualization
Let's trace the `found_b` flag as we iterate through an example string `s = "abab"`.

```
String: "a b a b"
Index:   0 1 2 3

Initial state: found_b = False

Iteration 0: char = 'a' (at index 0)
  Is char 'b'? No.
  Is char 'a'? Yes.
    Is found_b True? No (it's False).
  found_b remains False.
  
  String: "a b a b"
           ^
           |
           Current char
           found_b = False

Iteration 1: char = 'b' (at index 1)
  Is char 'b'? Yes.
    Set found_b = True.
  
  String: "a b a b"
             ^
             |
             Current char
             found_b = True

Iteration 2: char = 'a' (at index 2)
  Is char 'b'? No.
  Is char 'a'? Yes.
    Is found_b True? Yes (it's True!).
    This means we found an 'a' AFTER a 'b'.
    VIOLATION! Return False immediately.

  String: "a b a b"
               ^
               |
               Current char
               found_b = True (VIOLATION!)
```

## Dry Run
Let's walk through `s = "aaabbb"` (Example 1) using our approach.

| Index | Character | `found_b` (before) | Action                                    | `found_b` (after) | Result |
| :---- | :-------- | :----------------- | :---------------------------------------- | :---------------- | :----- |
|       |           | `False`            | (Initial state)                           | `False`           |        |
| 0     | `'a'`     | `False`            | `char` is 'a', `found_b` is `False`. OK.  | `False`           |        |
| 1     | `'a'`     | `False`            | `char` is 'a', `found_b` is `False`. OK.  | `False`           |        |
| 2     | `'a'`     | `False`            | `char` is 'a', `found_b` is `False`. OK.  | `False`           |        |
| 3     | `'b'`     | `False`            | `char` is 'b'. Set `found_b = True`.      | `True`            |        |
| 4     | `'b'`     | `True`             | `char` is 'b'. `found_b` already `True`.  | `True`            |        |
| 5     | `'b'`     | `True`             | `char` is 'b'. `found_b` already `True`.  | `True`            |        |
|       |           | `True`             | (Loop finished)                           | `True`            | `True` |

The loop completes, and we return `True`.

## Complexity
*   **Time Complexity**: O(N), where N is the length of the string `s`. We iterate through the string at most once.
*   **Space Complexity**: O(1). We only use a single boolean variable (`found_b`) regardless of the input string's length.

## Edge Cases
*   **String with only 'a's (e.g., `"aaa"`)**: `found_b` will always remain `False`. The loop completes, and `True` is returned. Correct.
*   **String with only 'b's (e.g., `"bbb"`)**: `found_b` will become `True` at the first 'b' and stay `True`. No 'a's are encountered, so `False` is never returned. The loop completes, and `True` is returned. Correct (Example 3).
*   **String with a single character (e.g., `"a"`, `"b"`)**: Both cases correctly return `True` as no 'a' appears after a 'b'.
*   **String with `ba` pattern (e.g., `"ba"`)**: `found_b` becomes `True` at 'b'. Then 'a' is encountered while `found_b` is `True`, immediately returning `False`. Correct.
*   **String with `ab` pattern (e.g., `"ab"`)**: `found_b` remains `False` at 'a'. Then `found_b` becomes `True` at 'b'. The loop completes, returning `True`. Correct.

## Solution

```python
class Solution:
    def checkString(self, s: str) -> bool:
        # This flag tracks if we have encountered any 'b' character yet.
        # Initially, we haven't seen any 'b's.
        found_b = False 

        # Iterate through each character in the string from left to right.
        for char in s:
            if char == 'b':
                # If we find a 'b', we set our flag to True.
                # This means we've now entered the "b-zone" of the string.
                found_b = True
            elif char == 'a':
                # If we find an 'a':
                # We need to check if we've already been in the "b-zone".
                if found_b:
                    # If found_b is True, it means we found an 'a' AFTER
                    # we had already seen at least one 'b'.
                    # This violates the condition that all 'a's must appear
                    # before all 'b's. So, we can immediately return False.
                    return False
        
        # If the loop completes without ever returning False, it means
        # we never found an 'a' after a 'b'.
        # Therefore, the condition is met, and we return True.
        return True

```

## Why This Works
This approach works because it directly implements the problem's core condition: "every 'a' appears before every 'b'". By using the `found_b` flag, we establish an invariant: once `found_b` becomes `True`, we are in a segment of the string where only 'b's are allowed. If an 'a' is encountered while `found_b` is `True`, it means an 'a' has appeared after a 'b', violating the invariant and the problem's condition. If we traverse the entire string without violating this invariant, it guarantees that all 'a's indeed appeared before all 'b's.

---
<sub>Generated 2026-11-22 07:19 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
