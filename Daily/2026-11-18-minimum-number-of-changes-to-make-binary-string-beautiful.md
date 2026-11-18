# [2914] Minimum Number of Changes to Make Binary String Beautiful

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-11-18 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/)

**Topics:** String

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 0-indexed binary string s having an even length.

A string is beautiful if it's possible to partition it into one or more substrings such that:

- Each substring has an even length.

- Each substring contains only 1's or only 0's.

You can change any character in s to 0 or 1.

Return the minimum number of changes required to make the string s beautiful.

Example 1:

Input: s = "1001"
Output: 2
Explanation: We change s[1] to 1 and s[3] to 0 to get string "1100".
It can be seen that the string "1100" is beautiful because we can partition it into "11|00".
It can be proven that 2 is the minimum number of changes needed to make the string beautiful.

Example 2:

Input: s = "10"
Output: 1
Explanation: We change s[1] to 1 to get string "11".
It can be seen that the string "11" is beautiful because we can partition it into "11".
It can be proven that 1 is the minimum number of changes needed to make the string beautiful.

Example 3:

Input: s = "0000"
Output: 0
Explanation: We don't need to make any changes as the string "0000" is beautiful already.

Constraints:

- 2 <= s.length <= 10^5

- s has an even length.

- s[i] is either '0' or '1'.

**Examples / sample tests:**

```
"1001"
"10"
"0000"
```

---

## Problem Summary
We are given a binary string `s` of even length. A string is "beautiful" if it can be partitioned into substrings, where each substring has an even length and consists of only '0's or only '1's. We need to find the minimum number of character changes required to make `s` beautiful.

## Intuition
The key to this problem lies in understanding the definition of a "beautiful" string. If a substring is beautiful, it must have an **even length** and contain **only identical characters** (e.g., "00", "11", "0000", "1111"). Notice that any such beautiful substring, like "0000", can always be further broken down into smaller beautiful units of length 2 (e.g., "00" | "00"). This implies that the fundamental building blocks of any beautiful string are pairs of identical characters, like "00" or "11".

Since the entire input string `s` has an even length, we can conceptually divide it into non-overlapping blocks of length 2: `s[0:2]`, `s[2:4]`, `s[4:6]`, and so on. For the entire string `s` to be beautiful, each of these length-2 blocks must independently be made beautiful.
For any given 2-character block `s[i]s[i+1]`:
*   If `s[i]` is already equal to `s[i+1]` (e.g., "00" or "11"), this block is already beautiful, and we need **0 changes**.
*   If `s[i]` is different from `s[i+1]` (e.g., "01" or "10"), we need to make one change to make it beautiful. For example, "01" can become "00" (change `s[i+1]`) or "11" (change `s[i]`). Both options require exactly **1 change**.
Since changes in one 2-character block do not affect other blocks, we can simply sum up the minimum changes required for each block.

## Approach
The optimal approach is a simple **greedy iteration** over the string.

1.  Initialize a `changes` counter to 0. This counter will store the total minimum changes needed.
2.  Iterate through the string `s` using an index `i`, starting from `0` and incrementing by `2` in each step. This allows us to process the string in non-overlapping pairs of characters.
3.  For each pair `s[i]` and `s[i+1]`:
    *   Compare `s[i]` and `s[i+1]`.
    *   If `s[i]` is **not equal** to `s[i+1]`, it means this pair needs one change to become "00" or "11". Increment `changes` by 1.
    *   If `s[i]` is **equal** to `s[i+1]`, this pair is already beautiful, and no changes are needed for this specific pair.
4.  After iterating through all such pairs until the end of the string, the final value of `changes` will be the minimum number of changes required.

## Visualization
Let's visualize the process with `s = "1001"`. We process the string in blocks of 2.

```
String:   1  0  0  1
Indices:  0  1  2  3

Step 1: Consider block s[0]s[1]
          [1  0] 0  1
          ^  ^
          s[0] != s[1]  -> Needs 1 change.
          Changes = 1

Step 2: Consider block s[2]s[3]
          1  0 [0  1]
                 ^  ^
                 s[2] != s[3]  -> Needs 1 change.
                 Changes = 1 + 1 = 2

End of string. Total changes = 2.
```

## Dry Run
Let's trace Example 1: `s = "1001"`

| Step | `i` | `s[i]` | `s[i+1]` | `s[i] == s[i+1]`? | `changes` (before update) | `changes` (after update) | Notes |
| :--- | :-- | :----- | :------- | :---------------- | :------------------------ | :----------------------- | :---- |
| 1    | -   | -      | -        | -                 | 0                         | 0                        | Initialize `changes` |
| 2    | 0   | '1'    | '0'      | False             | 0                         | 1                        | `s[0]` ('1') != `s[1]` ('0'). Increment `changes`. |
| 3    | 2   | '0'    | '1'      | False             | 1                         | 2                        | `s[2]` ('0') != `s[3]` ('1'). Increment `changes`. |
| 4    | 4   | -      | -        | -                 | 2                         | 2                        | `i` reaches `s.length` (4). Loop ends. |

Final Result: `changes = 2`.

## Complexity
*   **Time Complexity:** O(N), where N is the length of the string `s`. We iterate through the string once, checking each character pair.
*   **Space Complexity:** O(1). We only use a single counter variable, regardless of the input string's length.

## Edge Cases
*   **Smallest possible string:** `s = "00"` or `s = "11"`.
    *   `s = "00"`: `s[0] == s[1]`, `changes` remains 0. Correct.
    *   `s = "11"`: `s[0] == s[1]`, `changes` remains 0. Correct.
*   **String with all identical characters:** `s = "0000"` or `s = "1111"`.
    *   `s = "0000"`: `s[0] == s[1]`, `s[2] == s[3]`. `changes` remains 0. Correct.
*   **String with alternating characters:** `s = "0101"` or `s = "1010"`.
    *   `s = "0101"`: `s[0] != s[1]` (1 change), `s[2] != s[3]` (1 change). Total `changes = 2`. Correct.
*   **Long strings:** The approach iterates linearly, so it handles `N=10^5` efficiently within typical time limits.

## Solution
```python
class Solution:
    def minChanges(self, s: str) -> int:
        """
        Calculates the minimum number of changes required to make a binary string beautiful.
        A string is beautiful if it can be partitioned into substrings, where each substring
        has an even length and consists of only '0's or only '1's.
        
        The core idea is that any beautiful string can be broken down into pairs of identical
        characters (e.g., "00" or "11"). Since the input string has an even length, we can
        process it in non-overlapping blocks of two characters. For each block, if the two
        characters are different, one change is needed to make them identical.
        """
        
        n = len(s)
        changes = 0
        
        # Iterate through the string in steps of 2
        # This allows us to consider each non-overlapping pair (s[i], s[i+1])
        for i in range(0, n, 2):
            # If the characters in the current pair are different,
            # we need to make one change to make them identical ('00' or '11').
            # For example, "01" can become "00" (change s[i+1]) or "11" (change s[i]).
            # Both options require exactly one change.
            if s[i] != s[i+1]:
                changes += 1
                
        return changes

```

## Why This Works
This approach works because the problem's definition of a "beautiful" string implicitly reduces to making every adjacent pair of characters identical. A beautiful string can be partitioned into segments like "00", "11", "0000", "1111", etc. Any segment of even length consisting of identical characters (e.g., "1111") can always be further broken down into units of `length 2` (e.g., "11" | "11"). Since the original string `s` has an even length, it can be perfectly divided into non-overlapping pairs `(s[0], s[1])`, `(s[2], s[3])`, and so on. To make the entire string beautiful, each of these `length 2` pairs must become beautiful. A `length 2` pair is beautiful if and only if its two characters are identical ("00" or "11"). Therefore, we simply count how many pairs `s[i]s[i+1]` are *not* identical, as each such pair requires exactly one change to become beautiful. The minimum changes for each pair are independent, so summing them up gives the global minimum.

---
<sub>Generated 2026-11-18 07:52 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
