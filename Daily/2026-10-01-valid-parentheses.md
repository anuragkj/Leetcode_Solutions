# [20] Valid Parentheses

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-10-01 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/valid-parentheses/)

**Topics:** String, Stack, Bracket Sequences

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.

- Open brackets must be closed in the correct order.

- Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

Constraints:

- 1 <= s.length <= 10^4

- s consists of parentheses only '()[]{}'.

**Examples / sample tests:**

```
"()"
"()[]{}"
"(]"
"([])"
"([)]"
```

---

## Problem Summary
We need to determine if a given string of parentheses (like `()`, `{}`, `[]`) is "valid". A valid string means all open brackets are closed by the *same type* of bracket, in the *correct order*, and every close bracket has a corresponding open one.

## Intuition
When we encounter an **opening bracket** (like `(`, `{`, `[`), we expect a corresponding **closing bracket** later. The key is that this closing bracket must match the *most recently opened, unmatched* bracket. For example, in `([{}])`, the `}` closes the `{`, then `]` closes `[`, and finally `)` closes `(`. This "last in, first out" (LIFO) behavior is a classic sign that a **Stack** data structure is the perfect tool for the job.

## Approach
1.  **Initialize a Stack**: Create an empty list (which will act as our stack) to store opening brackets.
2.  **Define Bracket Mappings**: Create a dictionary or hash map that maps each closing bracket to its corresponding opening bracket (e.g., `')' : '('`, `'}' : '{'`, `']' : '['`). This helps us quickly check for matches.
3.  **Iterate Through the String**: Go through each character `char` in the input string `s`.
    *   **If `char` is an Opening Bracket**: If `char` is `(`, `{`, or `[`, push it onto our stack.
    *   **If `char` is a Closing Bracket**: If `char` is `)`, `}`, or `]`:
        *   **Check for Empty Stack**: First, check if the stack is empty. If it is, it means we've encountered a closing bracket without any corresponding open bracket, so the string is **invalid**. Return `False`.
        *   **Pop and Match**: If the stack is not empty, pop the top element from the stack. This element represents the *most recently opened* bracket.
        *   Compare this popped element with the *expected* opening bracket for the current `char` (using our mapping). If they don't match (e.g., we popped `(` but the current `char` is `]`), the string is **invalid**. Return `False`.
4.  **Final Check**: After iterating through the entire string:
    *   If the stack is **empty**, it means every opening bracket found its corresponding closing bracket. The string is **valid**. Return `True`.
    *   If the stack is **not empty**, it means there are unmatched opening brackets left over. The string is **invalid**. Return `False`.

## Visualization
Let's trace `s = "([{}])"` using a stack:

```
Input: s = "([{}])"

1. Character: '('
   Stack: [] -> Push '('
   Stack: [ '(' ]

2. Character: '['
   Stack: [ '(' ] -> Push '['
   Stack: [ '(', '[' ]

3. Character: '{'
   Stack: [ '(', '[' ] -> Push '{'
   Stack: [ '(', '[', '{' ]

4. Character: '}'
   Stack: [ '(', '[', '{' ] -> Pop '{'. Is '}' the closing for '{'? Yes!
   Stack: [ '(', '[' ]

5. Character: ']'
   Stack: [ '(', '[' ] -> Pop '['. Is ']' the closing for '['? Yes!
   Stack: [ '(' ]

6. Character: ')'
   Stack: [ '(' ] -> Pop '('. Is ')' the closing for '('? Yes!
   Stack: []

End of string. Stack is empty. Result: True.
```

## Dry Run
Let's walk through Example 1: `s = "()"`

| Character | Stack State (before action) | Action                                       | Stack State (after action) | Valid? |
| :-------- | :-------------------------- | :------------------------------------------- | :------------------------- | :----- |
| `(`       | `[]`                        | Push `(`                                     | `[` `(` `]`                | `True` |
| `)`       | `[` `(` `]`                 | Pop `(`; `(` matches `)` (from `mapping`)    | `[]`                       | `True` |
| **End**   | `[]`                        | Stack is empty.                              | `[]`                       | `True` |
|           |                             | **Final Result: `True`**                     |                            |        |

## Complexity
*   **Time Complexity**: O(N), where N is the length of the input string `s`. We iterate through the string once, and each stack operation (push, pop, peek) takes constant time, O(1).
*   **Space Complexity**: O(N) in the worst case. This happens when the string consists only of opening brackets (e.g., `"((((("`). In such a scenario, all N characters would be pushed onto the stack.

## Edge Cases
*   **String with only opening brackets**: e.g., `"{[("`. The stack will not be empty at the end, correctly returning `False`.
*   **String with only closing brackets**: e.g., `")]}"`. When the first `)` is encountered, the stack will be empty, correctly returning `False`.
*   **Mismatched types**: e.g., `"{]"`. When `]` is encountered, `{` will be popped, but `]` expects `[`. The mismatch will correctly return `False`.
*   **Correct order, wrong type**: e.g., `"(]"`. Similar to above, `(` will be popped, but `]` expects `[`. Returns `False`.
*   **Nested brackets**: e.g., `"({[]})"`. Handled naturally by the LIFO property of the stack, as shown in the visualization.
*   **Empty string**: The problem constraints state `1 <= s.length`, so an empty string is not a possible input.

## Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        # Use a list as a stack.
        stack = []
        
        # Define a mapping for closing brackets to their corresponding opening brackets.
        # This allows us to quickly check if a closing bracket matches the top of the stack.
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Iterate through each character in the input string.
        for char in s:
            # If the character is an opening bracket, push it onto the stack.
            if char in ('(', '{', '['):
                stack.append(char)
            # If the character is a closing bracket.
            else:
                # If the stack is empty, it means we have a closing bracket
                # without a corresponding opening bracket. So, it's invalid.
                if not stack:
                    return False
                
                # Pop the top element from the stack. This is the most recently
                # opened bracket.
                top_element = stack.pop()
                
                # Check if the popped element matches the expected opening bracket
                # for the current closing bracket. If not, it's invalid.
                if bracket_map[char] != top_element:
                    return False
        
        # After iterating through the entire string, if the stack is empty,
        # all opening brackets have been correctly closed.
        # If the stack is not empty, there are unmatched opening brackets.
        return not stack

```

## Why This Works
This approach works because the **stack perfectly enforces the "last in, first out" (LIFO) rule** required for correctly nested parentheses. When an opening bracket is encountered, it's pushed onto the stack, signifying an expectation for a future closing bracket. When a closing bracket appears, it *must* match the *most recently opened* (i.e., the top of the stack) bracket. If it doesn't, or if there's no open bracket to match (empty stack), the sequence is invalid. Finally, if the stack is empty at the end, it guarantees that every opening bracket found its correct closing counterpart.

---
<sub>Generated 2026-10-01 06:26 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
