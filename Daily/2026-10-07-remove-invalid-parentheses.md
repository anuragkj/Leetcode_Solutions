# [301] Remove Invalid Parentheses

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-10-07 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/remove-invalid-parentheses/)

**Topics:** String, Backtracking, Breadth-First Search

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]

Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

Example 3:

Input: s = ")("
Output: [""]

Constraints:

- 1 <= s.length <= 25

- s consists of lowercase English letters and parentheses '(' and ')'.

- There will be at most 20 parentheses in s.

**Examples / sample tests:**

```
"()())()"
"(a)())()"
")("
```

---

## Problem Summary
Given a string containing parentheses and letters, the goal is to find all possible valid parentheses strings by removing the **minimum** number of invalid parentheses. We need to return a list of these unique, valid strings.

## Intuition
This problem asks for *all* solutions that achieve a *minimum* number of removals. This pattern strongly suggests a **Breadth-First Search (BFS)** approach. BFS explores states level by level, guaranteeing that the first time we find a valid string, it must have been achieved with the minimum number of removals.

Here's the core idea:
1.  Start with the original string. This is level 0.
2.  At level 1, generate all possible strings by removing *one* parenthesis from the strings at level 0.
3.  At level 2, generate all possible strings by removing *two* parentheses (one from each string at level 1).
4.  Continue this process. The first level at which we encounter *any* valid parentheses string means we've found the minimum number of removals. We then collect *all* valid strings at that specific level and stop the search.
5.  To avoid redundant work and cycles, we'll use a `set` to keep track of all strings we've already visited.

## Approach
We will implement a BFS algorithm using a queue and a helper function to check string validity.

1.  **`is_valid(s: str)` Helper Function**:
    *   This function takes a string `s` and returns `True` if it's a valid parentheses string, `False` otherwise.
    *   Initialize a `balance` counter to 0.
    *   Iterate through each character `char` in `s`:
        *   If `char` is `'('`, increment `balance`.
        *   If `char` is `')'`, decrement `balance`.
        *   If `balance` ever drops below 0, it means we have an unmatched closing parenthesis, so the string is immediately invalid. Return `False`.
    *   After iterating through the entire string, if `balance` is 0, all parentheses are matched, and the string is valid. Return `True`. Otherwise, return `False`. (Note: Non-parenthesis characters are ignored by this logic, which is correct).

2.  **BFS Algorithm**:
    *   Initialize a `queue` (using `collections.deque` for efficient `popleft`) and add the input string `s` to it.
    *   Initialize a `visited` set and add `s` to it to prevent processing the same string multiple times.
    *   Initialize an `ans` list to store the valid strings found.
    *   Initialize a `found_valid` boolean flag to `False`. This flag will become `True` once we find the first valid string, signaling that we've reached the minimum removal level.

    *   **Main BFS Loop (`while queue`):**
        *   Get the `level_size` (number of strings currently in the queue) to process all strings at the current level before moving to the next.
        *   **Inner Loop (`for _ in range(level_size)`):**
            *   Dequeue `current_string` from the front of the `queue`.
            *   **Check Validity**: Call `is_valid(current_string)`.
                *   If `True`:
                    *   Add `current_string` to `ans`.
                    *   Set `found_valid = True`.
            *   **Pruning**: If `found_valid` is now `True` (meaning we've found at least one valid string at this level), we **must not** generate children for `current_string`. We only collect valid strings at this minimum removal level and stop exploring deeper. Use `continue` to skip to the next string in the current level.
            *   **Generate Children (if `found_valid` is still `False`):**
                *   Iterate `i` from `0` to `len(current_string) - 1`.
                *   If `current_string[i]` is a parenthesis (`'('` or `')'`):
                    *   Create `next_string` by removing `current_string[i]` (i.e., `current_string[:i] + current_string[i+1:]`).
                    *   If `next_string` has not been `visited`:
                        *   Add `next_string` to `visited`.
                        *   Enqueue `next_string`.
        *   **Level Completion Check**: After processing all strings at the current level (inner loop finishes), if `found_valid` is `True`, it means we have collected all valid strings with the minimum number of removals. Break out of the main BFS loop.

    *   Return the `ans` list.

## Visualization
Let's visualize the BFS for `s = "()())()"`.
`is_valid("()())()")` is `False` (balance goes to -1).

```
Level 0:
                                "()())()"
                                   | (is_valid? No)
                                   V
----------------------------------------------------------------------------------------------------------------
Level 1 (Remove 1 parenthesis):
(Strings generated by removing one char from "()())()")

  "()())"   "())()"   "()())"   "()())"   "()())"   "()()()"   "()())"
  (rem s[0]) (rem s[1]) (rem s[2]) (rem s[3]) (rem s[4]) (rem s[5]) (rem s[6])
     |          |          |          |          |          |          |
     V          V          V          V          V          V          V
(is_valid? No) (is_valid? No) (is_valid? No) (is_valid? No) (is_valid? No) (is_valid? Yes!) (is_valid? No)
                                                                |
                                                                V
                                                        Add "()()()" to ans.
                                                        Set found_valid = True.

(Continue processing other nodes at Level 1. For each, if it's valid, add to ans.
 If found_valid is True, DO NOT generate children for the next level.)

Example: When processing "())()":
  is_valid("())()") -> No
  Since found_valid is True, we skip generating children for "())()".

Example: When processing "(())()":
  is_valid("(())()") -> Yes!
  Add "(())()" to ans.
  found_valid is already True.
  Since found_valid is True, we skip generating children for "(())()".

After processing all nodes at Level 1:
  ans = ["()()()", "(())()"]
  found_valid = True.

----------------------------------------------------------------------------------------------------------------
Level 2:
(No strings are added to the queue for Level 2 because `found_valid` was True
 after processing Level 1, and the BFS loop breaks.)
```

## Dry Run
Let's trace `s = "()())()"`:

**Helper: `is_valid(t)`**
*   `is_valid("()())()")`: `bal=1,0,1,0,-1` -> `False`
*   `is_valid("()()()")`: `bal=1,0,1,0,1,0` -> `True`
*   `is_valid("(())()")`: `bal=1,2,1,0,1,0` -> `True`
*   `is_valid("()())")`: `bal=1,0,1,0,-1` -> `False`

**BFS Trace:**

| Level | Queue (before level)

---
<sub>Generated 2026-10-07 06:22 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
