# [1021] Remove Outermost Parentheses

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-10-08 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/remove-outermost-parentheses/)

**Topics:** String, Stack, Bracket Sequences

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

- For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

Example 3:

Input: s = "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

Constraints:

- 1 <= s.length <= 10^5

- s[i] is either '(' or ')'.

- s is a valid parentheses string.

**Examples / sample tests:**

```
"(()())(())"
"(()())(())(()(()))"
"()()"
```

---

## Problem Summary
The task is to take a valid parentheses string, decompose it into its "primitive" components, and then remove the outermost parentheses from each of these primitive parts. The modified parts are then concatenated to form the final result.

## Intuition
A **primitive valid parentheses string** is one that cannot be split into two smaller, non-empty valid parentheses strings. For example, "()" is primitive, but "(())()" is not (it can be split into "(())" + "()").

The key observation for identifying primitive strings is using a **balance counter**.
1.  When we encounter an opening parenthesis `'('`, we increment the balance.
2.  When we encounter a closing parenthesis `')'`, we decrement the balance.

For any valid parentheses string:
*   The balance starts at 0.
*   The balance never drops below 0.
*   The balance ends at 0.

For a *primitive* valid parentheses string, the balance will only return to 0 *exactly at its very end*. It will be `> 0` for all characters in between its first `'('` and its last `')'`.

This gives us a simple rule:
*   We want to remove the **first `'('`** of each primitive string. This is the `'('` that causes the balance to go from `0` to `1`.
*   We want to remove the **last `')'`** of each primitive string. This is the `')'` that causes the balance to go from `1` to `0`.
*   All other parentheses are "inner" parentheses and should be kept.

So, we can iterate through the string, maintain a `balance` counter, and append characters to our result based on this rule.

## Approach
We will use a single pass through the input string and a `balance` counter to keep track of the current nesting level.

1.  Initialize an empty list, `result_chars`, to store the characters that will form our final string. Using a list is efficient for appending characters, and we'll join it into a string at the end.
2.  Initialize an integer `balance` to `0`. This counter will track the number of open parentheses minus the number of closed parentheses encountered so far.
3.  Iterate through each `char` in the input string `s`:
    a.  **If `char` is `'('`**:
        i.  Before incrementing `balance`, check if `balance` is currently greater than `0`. If it is, it means we are already *inside* a primitive string (i.e., this `'('` is not the very first character of a new primitive string). In this case, append `'('` to `result_chars`.
        ii. After checking, increment `balance` by `1`.
    b.  **If `char` is `')'`**:
        i.  Before checking `balance`, decrement `balance` by `1`.
        ii. After decrementing, check if `balance` is currently greater than `0`. If it is, it means we are still *inside* a primitive string (i.e., this `')'` is not the very last character of the current primitive string). In this case, append `')'` to `result_chars`.
4.  Finally, join all characters in `result_chars` to form a single string and return it.

## Visualization

Let's visualize the process with `s = "(()())"`:

```
Input: s = " ( ( ) ( ) ) "
Balance:     0 1 2 1 2 1 0  (Balance after processing each char)
Output:        ( ) ( )      (Characters kept)

Detailed step-by-step:

char:      (      (      )      (      )      )
-------------------------------------------------------------------
balance_before: 0      1      2      1      2      1
action:    bal++  bal++  bal--  bal++  bal--  bal--
balance_after:  1      2      1      2      1      0
append_char?: NO     YES    YES    YES    YES    NO
result_chars: []   ['(']  ['(', ')'] ['(', ')', '('] ['(', ')', '(', ')'] ['(', ')', '(', ')']
```
The first `'('` is skipped because `balance` was `0` before it.
The last `')'` is skipped because `balance` became `0` after it.
All intermediate characters are kept.

## Dry Run

Let's trace Example 1: `s = "(()())(())"`

`result_chars = []`
`balance = 0`

| `char` | `balance` (before op) | Operation | `balance` (after op) | Append? | `result_chars` |
| :----- | :-------------------- | :-------- | :------------------- | :------ | :------------- |
| `(`    | 0                     | `balance++` | 1                    | No (`balance` was 0) | `[]` |
| `(`    | 1                     | `balance++` | 2                    | Yes (`balance` was >0) | `['(']` |
| `)`    | 2                     | `balance--` | 1                    | Yes (`balance` is >0) | `['(', ')']` |
| `(`    | 1                     | `balance++` | 2                    | Yes (`balance` was >0) | `['(', ')', '(']` |
| `)`    | 2                     | `balance--` | 1                    | Yes (`balance` is >0) | `['(', ')', '(', ')']` |
| `)`    | 1                     | `balance--` | 0                    | No (`balance` is 0) | `['(', ')', '(', ')']` |
| `(`    | 0                     | `balance++` | 1                    | No (`balance` was 0) | `['(', ')', '(', ')']` |
| `(`    | 1                     | `balance++` | 2                    | Yes (`balance` was >0) | `['(', ')', '(', ')', '(']` |
| `)`    | 2                     | `balance--` | 1                    | Yes (`balance` is >0) | `['(', ')', '(', ')', '(', ')']` |
| `)`    | 1                     | `balance--` | 0                    | No (`balance` is 0) | `['(', ')', '(', ')', '(', ')']` |

Final `result_chars` is `['(', ')', '(', ')', '(', ')']`.
Joining them gives `"()()()"`. This matches Example 1 output.

## Complexity

*   **Time Complexity**: O(N), where N is the length of the input string `s`. We iterate through the string exactly once. Appending to a list and joining at the end are both efficient operations.
*   **Space Complexity**: O(N), where N is the length of the input string `s`. In the worst case (e.g., `s = "((()))"`), we might keep almost all characters in `result_chars`.

## Edge Cases

*   `s = "()"`: This is a single primitive string.
    *   `(`: `balance` goes from 0 to 1. Not appended.
    *   `)`: `balance` goes from 1 to 0. Not appended.
    *   Result: `""`. Correct.
*   `s = "()()"`: Two primitive strings.
    *   `(`: bal 0->1, not appended.
    *   `)`: bal 1->0, not appended.
    *   `(`: bal 0->1, not appended.
    *   `)`: bal 1->0, not appended.
    *   Result: `""`. Correct.
*   `s = "(())"`: A single primitive string.
    *   `(`: bal 0->1, not appended.
    *   `(`: bal 1->2, appended. `result_chars = ['(']`
    *   `)`: bal 2->1, appended. `result_chars = ['(', ')']`
    *   `)`: bal 1->0, not appended.
    *   Result: `"()"`. Correct.

The solution handles these cases correctly because the logic precisely identifies and discards the outermost parentheses of each primitive component.

## Solution

```python
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result_chars = []  # Use a list to efficiently build the result string
        balance = 0        # Counter for the current balance of parentheses

        for char in s:
            if char == '(':
                # If balance > 0, it means we are inside a primitive string
                # and this '(' is not the very first character of a new primitive.
                # So, we should keep it.
                if balance > 0:
                    result_chars.append(char)
                balance += 1
            else:  # char == ')'
                # Decrement balance first, as this ')' closes an open parenthesis.
                balance -= 1
                # If balance > 0 after decrementing, it means we are still inside
                # a primitive string, and this ')' is not the very last character.
                # So, we should keep it.
                if balance > 0:
                    result_chars.append(char)
        
        # Join the list of characters to form the final string
        return "".join(result_chars)

```

## Why This Works

This approach works because the `balance` counter precisely tracks the nesting level within the valid parentheses string. A primitive string begins when the `balance` goes from `0` to `1` (the first `'('`) and ends when the `balance` goes from `1` to `0` (the last `')'`). By appending a character only when `balance` is strictly greater than `0` (for `'('` *before* incrementing, or for `')'` *after* decrementing), we effectively skip these boundary characters (the outermost parentheses of each primitive string) while retaining all inner characters. This correctly implements the problem's requirement to remove only the outermost parentheses of each primitive decomposition.

---
<sub>Generated 2026-10-08 06:33 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
