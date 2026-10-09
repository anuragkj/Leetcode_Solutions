# [1541] Minimum Insertions to Balance a Parentheses String

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-10-09 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/)

**Topics:** String, Stack, Greedy, Bracket Sequences

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

- Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.

- Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.

In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

- For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.

Example 1:

Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

Example 2:

Input: s = "())"
Output: 0
Explanation: The string is already balanced.

Example 3:

Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.

Constraints:

- 1 <= s.length <= 10^5

- s consists of '(' and ')' only.

**Examples / sample tests:**

```
"(()))"
"())"
"))())("
```

---

## Problem Summary
The goal is to balance a parentheses string where each `(` must be matched by two consecutive `))`. We need to find the minimum number of `(` or `)` insertions required to achieve this balance.

## Intuition
This problem is a variation of classic bracket balancing. We can process the string from left to right, keeping track of **unmatched open parentheses**. When we encounter a closing parenthesis, we try to match it. The key challenge is that a single `(` requires *two* `)` characters. This suggests a greedy approach:
1. Maintain a `balance` counter for currently open `(` that are waiting for their `))`.
2. Maintain an `insertions` counter for the total characters added.
3. When we see an `(`, we increment `balance`.
4. When we see a `)`, we need to form a `))` pair.
   - If the next character is also `)`, we have a `))`.
   - If the next character is not `)` (or we're at the end of the string), we have a single `)`. We must insert another `)` to form a `))`. This costs 1 insertion.
5. Once we have a `))` (either found or formed by insertion), we try to match it:
   - If `balance > 0`, it means we have an open `(` that this `))` can close. So, we decrement `balance`.
   - If `balance == 0`, it means there's no open `(` to match this `))`. We must insert an `(` to match it. This costs 1 insertion.
6. After iterating through the entire string, any remaining `balance > 0` means we have `(` that were never closed. Each such `(` needs a `))`, which costs 2 insertions.

## Approach
We'll use a single pass (iterating through the string) with two variables: `open_needed` to track unmatched open parentheses, and `insertions` to count the total characters added.

1. **Initialize:**
   - `open_needed = 0`: Represents the number of `(` characters that are currently open and require a `))`.
   - `insertions = 0`: Represents the total number of characters (`(` or `)`) inserted.
   - `i = 0`: Our pointer to iterate through the string `s`.

2. **Iterate through the string `s` using a `while` loop:**
   - **If `s[i] == '('`:**
     - Increment `open_needed` (we've encountered an opening parenthesis).
     - Move to the next character: `i += 1`.
   - **If `s[i] == ')'`:**
     - **Check for a `))` pair:**
       - If `i + 1 < len(s)` AND `s[i+1] == ')'`: We found a complete `))` pair.
         - Advance `i` by 2 (to consume both `)` characters).
       - Else (it's a single `)`):
         - We need to insert one `)` to form a `))`. Increment `insertions`.
         - Advance `i` by 1 (to consume the single `)`).
     - **Match the `))` (either found or formed):**
       - If `open_needed > 0`: This `))` can match an existing `(`. Decrement `open_needed`.
       - Else (`open_needed == 0`): There's no `(` to match this `))`. We must insert an `(` to match it. Increment `insertions`.

3. **After the loop:**

---
<sub>Generated 2026-10-09 06:35 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
