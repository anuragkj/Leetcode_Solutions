# [1614] Maximum Nesting Depth of the Parentheses

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-09-28 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)

**Topics:** String, Stack, Bracket Sequences

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation:

Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

Input: s = "(1)+((2))+(((3)))"

Output: 3

Explanation:

Digit 3 is inside of 3 nested parentheses in the string.

Example 3:

Input: s = "()(())((()()))"

Output: 3

Constraints:

- 1 <= s.length <= 100

- s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.

- It is guaranteed that parentheses expression s is a VPS.

**Examples / sample tests:**

```
"(1+(2*3)+((8)/4))+1"
"(1)+((2))+(((3)))"
"()(())((()()))"
```

---

## Problem Summary
Given a string `s` that is guaranteed to be a **Valid Parentheses String (VPS)**, the goal is to find its **nesting depth**. This depth is defined as the maximum number of open parentheses encountered before a matching closing parenthesis.

## Intuition
Imagine you're walking along the string, keeping track of how many open parentheses you've seen that haven't been closed yet.
*   Every time you see an **opening parenthesis `(`**, you go one level deeper into the nesting. So, your current depth increases.
*   Every time you see a **closing parenthesis `)`**, you come out one level. So, your current depth decreases.
*   Any other character (digits, operators) doesn't change the nesting level.

Our task is to find the **highest depth** we ever reached during this walk. We'll need a variable to track the `current_depth` and another to store the `max_depth` seen so far.

## Approach
The most straightforward way to solve this is to iterate through the string character by character and maintain two variables:
1.  `current_depth`: Tracks the nesting level at the current position.
2.  `max_depth`: Stores the highest `current_depth` encountered throughout the scan.

Here are the concrete steps:

1.  Initialize `max_depth` to `0`. This will store our final answer.
2.  Initialize `current_depth` to `0`. This tracks the depth as we scan.
3.  Iterate through each `char` in the input string `s`:
    a.  If `char` is an opening parenthesis `(`:
        i.  Increment `current_depth` by 1.
        ii. Update `max_depth = max(max_depth, current_depth)`. We do this because an opening parenthesis signifies entering a new, potentially deeper, level.
    b.  If `char` is a closing parenthesis `)`:
        i.  Decrement `current_depth` by 1.
    c.  If `char` is any other character (digit or operator):
        i.  Do nothing, as these characters do not affect the nesting depth.
4.  After iterating through all characters in the string, `max_depth` will hold the maximum nesting depth. Return `max_depth`.

## Visualization
Let's visualize the process with a simple example: `s = "((1+(2)))"`

```
String:   (   (   1   +   (   2   )   )   )
          ^   ^               ^       ^   ^   ^
          |   |               |       |   |   |
current_depth:
Initial:  0
'(':      1   (max_depth = 1)
'(':      2   (max_depth = 2)
'1':      2
'+':      2
'(':      3   (max_depth = 3)
'2':      3
')':      2
')':      1
')':      0

Final max_depth = 3
```

## Dry Run
Let's walk through Example 1: `s = "(1+(2*3)+((8)/4))+1"`

| Char | `current_depth` (before) | Action                               | `current_depth` (after) | `max_depth` |
| :--- | :----------------------- | :----------------------------------- | :---------------------- | :---------- |
| `(`  | 0                        | `current_depth++`                    | 1                       | `max(0,1)=1`|
| `1`  | 1                        | Skip                                 | 1                       | 1           |
| `+`  | 1                        | Skip                                 | 1                       | 1           |
| `(`  | 1                        | `current_depth++`                    | 2                       | `max(1,2)=2`|
| `2`  | 2                        | Skip                                 | 2                       | 2           |
| `*`  | 2                        | Skip                                 | 2                       | 2           |
| `3`  | 2                        | Skip                                 | 2                       | 2           |
| `)`  | 2                        | `current_depth--`                    | 1                       | 2           |
| `+`  | 1                        | Skip                                 | 1                       | 2           |
| `(`  | 1                        | `current_depth++`                    | 2                       | `max(2,2)=2`|
| `(`  | 2                        | `current_depth++`                    | 3                       | `max(2,3)=3`|
| `8`  | 3                        | Skip                                 | 3                       | 3           |
| `)`  | 3                        | `current_depth--`                    | 2                       | 3           |
| `/`  | 2                        | Skip                                 | 2                       | 3           |
| `4`  | 2                        | Skip                                 | 2                       | 3           |
| `)`  | 2                        | `current_depth--`                    | 1                       | 3           |
| `)`  | 1                        | `current_depth--`                    | 0                       | 3           |
| `+`  | 0                        | Skip                                 | 0                       | 3           |
| `1`  | 0                        | Skip                                 | 0                       | 3           |

The final result is `max_depth = 3`.

## Complexity
*   **Time Complexity**: O(N), where N is the length of the string `s`. We iterate through the string exactly once.
*   **Space Complexity**: O(1). We only use a few constant-space variables (`current_depth`, `max_depth`) regardless of the input string's length.

## Edge Cases
*   **String with no parentheses**: `s = "1+2*3"`.
    *   `current_depth` remains 0, `max_depth` remains 0. Correctly returns 0.
*   **String with only one level of parentheses**: `s = "(a+b)"`.
    *   `current_depth` goes `0 -> 1 -> 0`. `max_depth` becomes 1. Correctly returns 1.
*   **String with multiple independent groups at same depth**: `s = "()(())((()()))"`.
    *   `current_depth` will fluctuate, but `max_depth` will correctly capture the highest point (3 in this case).
*   **Minimum length string**: `s = "()"`.
    *   `current_depth` goes `0 -> 1 -> 0`. `max_depth` becomes 1. Correctly returns 1.

The solution handles all these cases naturally because it simply tracks the current nesting level and updates the maximum seen.

## Solution

```python
class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        current_depth = 0

        # Iterate through each character in the string
        for char in s:
            if char == '(':
                # An opening parenthesis increases the current depth
                current_depth += 1
                # Update max_depth if current_depth is higher
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                # A closing parenthesis decreases the current depth
                current_depth -= 1
            # Other characters (digits, operators) do not affect depth, so we skip them

        return max_depth

```

## Why This Works
This approach works because `current_depth` accurately models the **net count of open parentheses** encountered so far. Each `(` increases the nesting level, and each `)` decreases it. By taking the `max` of `current_depth` every time we encounter an opening parenthesis, we ensure that `max_depth` always stores the highest nesting level reached at any point in the string. The problem guarantees that `s` is a Valid Parentheses String (VPS), which means `current_depth` will never go negative and will always return to 0 by the end of a fully balanced expression.

---
<sub>Generated 2026-09-28 05:45 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
