# [921] Minimum Add to Make Parentheses Valid

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-10-06 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

**Topics:** String, Stack, Greedy, Bracket Sequences

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

A parentheses string is valid if and only if:

- It is the empty string,

- It can be written as AB (A concatenated with B), where A and B are valid strings, or

- It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

- For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".

Return the minimum number of moves required to make s valid.

Example 1:

Input: s = "())"
Output: 1

Example 2:

Input: s = "((("
Output: 3

Constraints:

- 1 <= s.length <= 1000

- s[i] is either '(' or ')'.

**Examples / sample tests:**

```
"())"
"((("
```

---

## Problem Summary
This problem asks us to find the minimum number of parentheses we need to insert into a given string to make it a **valid parentheses string**. A valid string means every opening parenthesis `(` has a matching closing parenthesis `)`, and they are properly nested.

## Intuition
Let's think about what makes a parentheses string invalid. It's either because:
1.  We encounter a closing parenthesis `)` but there's no unmatched opening parenthesis `(` available to pair with it.
2.  We finish scanning the string, but there are still some opening parentheses `(` that never found a matching closing parenthesis `)`.

To fix these issues with the minimum number of insertions, we can use a **greedy** approach. We'll scan the string from left to right, keeping track of how many open parentheses are currently "waiting" for a match.

-   When we see an `(`, we increment our count of waiting open parentheses.
-   When we see a `)`, we try to match it.
    -   If there's an `(` waiting, we use it up (decrement the count). This `)` is validly placed.
    -   If there's *no* `(` waiting, this `)` is "superfluous". To make it valid, we *must* insert an `(` before it. This counts as one insertion.
-   After scanning the entire string, any `(` that are still waiting for a match (i.e., our count is not zero) *must* each have a `)` inserted after them. Each of these counts as one insertion.

By doing this, we always resolve imbalances as soon as they appear or are identified, ensuring we make the minimum necessary additions.

## Approach
We will use two integer variables:
1.  `unmatched_open`: To keep track of the number of opening parentheses `(` that we have encountered so far and are still waiting for a matching closing parenthesis `)`.
2.  `insertions`: To count the total number of parentheses we need to insert to make the string valid.

Here's the step-by-step algorithm:

1.  Initialize `unmatched_open = 0` and `insertions = 0`.
2.  Iterate through each `char` in the input string `s`:
    a.  If `char` is `'('`:
        Increment `unmatched_open` by 1. We've found an open parenthesis that needs a future match.
    b.  If `char` is `')'`:
        i.  Check if `unmatched_open > 0`. If true, it means there's an available `(` to match this `)`. Decrement `unmatched_open` by 1.
        ii. If `unmatched_open == 0`, it means this `)` has no `(` to match with. To make the string valid, we *must* insert an `(` before this `)`. Increment `insertions` by 1.
3.  After the loop finishes (we've processed all characters in `s`):
    Any remaining value in `unmatched_open` represents `(` that never found a `)` to match them. Each of these requires a `)` to be inserted *after* them. Add the value of `unmatched_open` to `insertions`.
4.  Return the final value of `insertions`.

## Visualization

Let's trace `s = "())"` with `unmatched_open` and `insertions`.

Initial state: `unmatched_open = 0`, `insertions = 0`

```
String: " (   )   ) "
         ^
         |
         Current character

1. Character: '('
   - unmatched_open becomes 1.
   - insertions remains 0.
   State: unmatched_open = 1, insertions = 0
   (
   ^

2. Character: ')'
   - unmatched_open is 1 (> 0), so it matches.
   - unmatched_open becomes 0.
   - insertions remains 0.
   State: unmatched_open = 0, insertions = 0
   ( )
     ^

3. Character: ')'
   - unmatched_open is 0. No '(' to match.
   - We need to insert an '('.
   - insertions becomes 1.
   - unmatched_open remains 0.
   State: unmatched_open = 0, insertions = 1
   ( ) )
       ^

End of string.
Remaining unmatched_open = 0. Add this to insertions.
Final insertions = 1.
```

## Dry Run

Let's walk through Example 1: `s = "())"`

| Character | `unmatched_open` (before) | `insertions` (before) | Action                                                               | `unmatched_open` (after) | `insertions` (after) |
| :-------- | :------------------------ | :-------------------- | :------------------------------------------------------------------- | :----------------------- | :------------------- |
| `(`       | 0                         | 0                     | `char == '('`: Increment `unmatched_open`                            | 1                        | 0                    |
| `)`       | 1                         | 0                     | `char == ')'`: `unmatched_open > 0`, decrement `unmatched_open`      | 0                        | 0                    |
| `)`       | 0                         | 0                     | `char == ')'`: `unmatched_open == 0`, increment `insertions`         | 0                        | 1                    |
| **End Loop** |                           |                       | Add remaining `unmatched_open` to `insertions` (`0 + 1`)             |                          | 1                    |

Final Result: `1`

## Complexity

*   **Time Complexity**: O(N)
    We iterate through the input string `s` exactly once, where N is the length of the string. Each character processing takes constant time.
*   **Space Complexity**: O(1)
    We only use a few integer variables (`unmatched_open`, `insertions`) to store state, regardless of the input string's length.

## Edge Cases

*   **Empty String `s = ""`**:
    `unmatched_open` and `insertions` will both remain 0. The loop won't run. `insertions += unmatched_open` will be `0 + 0 = 0`. Correct, an empty string is valid.
*   **Already Valid String `s = "()()"`**:
    `(`: `unmatched_open = 1`, `insertions = 0`
    `)`: `unmatched_open = 0`, `insertions = 0`
    `(`: `unmatched_open = 1`, `insertions = 0`
    `)`: `unmatched_open = 0`, `insertions = 0`
    End: `insertions += 0`. Final `insertions = 0`. Correct.
*   **String with only opening parentheses `s = "((("`**:
    `(`: `unmatched_open = 1`, `insertions = 0`
    `(`: `unmatched_open = 2`, `insertions = 0`
    `(`: `unmatched_open = 3`, `insertions = 0`
    End: `insertions += 3`. Final `insertions = 3`. Correct, three `)` are needed.
*   **String with only closing parentheses `s = ")))"`**:
    `)`: `unmatched_open = 0`, `insertions = 1` (needs `(`)
    `)`: `unmatched_open = 0`, `insertions = 2` (needs `(`)
    `)`: `unmatched_open = 0`, `insertions = 3` (needs `(`)
    End: `insertions += 0`. Final `insertions = 3`. Correct, three `(` are needed.

## Solution

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # unmatched_open counts the number of open parentheses '('
        # that are currently waiting for a matching closing parenthesis ')'.
        unmatched_open = 0
        
        # insertions counts the total number of parentheses we need to insert
        # to make the string valid.
        insertions = 0

        # Iterate through each character in the input string
        for char in s:
            if char == '(':
                # If we see an opening parenthesis, it needs a future match.
                # Increment the count of unmatched open parentheses.
                unmatched_open += 1
            else:  # char == ')'
                # If we see a closing parenthesis:
                if unmatched_open > 0:
                    # If there's an unmatched open parenthesis available,
                    # this ')' can successfully close it.
                    # Decrement the count of unmatched open parentheses.
                    unmatched_open -= 1
                else:
                    # If there are no unmatched open parentheses, this ')'
                    # is "superfluous" and has nothing to pair with.
                    # To make it valid, we must insert an opening parenthesis
                    # before it. Increment our total insertions count.
                    insertions += 1
        
        # After iterating through the entire string, any remaining
        # unmatched_open parentheses still need a closing parenthesis ')'.
        # Each of these requires one insertion.
        insertions += unmatched_open
        
        # The total number of insertions required is our answer.
        return insertions

```

## Why This Works

This greedy approach works because it addresses imbalances locally and optimally. When we encounter an `(` we simply note its presence, as it *must* be closed by a `)` later. When we encounter a `)`, we prioritize matching it with the *earliest possible* available `(` (implicitly, by decrementing `unmatched_open`). If no `(` is available, we *must* insert one immediately before the current `)` to make it valid. This is the minimum possible action at that point. Similarly, any `(` left unmatched at the end *must* be closed by an inserted `)`. By only adding parentheses when absolutely necessary to resolve an immediate or final imbalance, we guarantee the minimum number of insertions.

---
<sub>Generated 2026-10-06 06:46 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
