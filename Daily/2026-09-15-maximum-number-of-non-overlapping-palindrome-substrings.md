# [2472] Maximum Number of Non-overlapping Palindrome Substrings

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-09-15 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/)

**Topics:** Two Pointers, String, Dynamic Programming, Greedy

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

- The length of each substring is at least k.

- Each substring is a palindrome.

Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.

Example 2:

Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.

Constraints:

- 1 <= k <= s.length <= 2000

- s consists of lowercase English letters.

**Examples / sample tests:**

```
"abaccdbbd"
3
"adbcda"
2
```

---

## Problem Summary
Given a string `s` and an integer `k`, find the maximum number of non-overlapping substrings that are palindromes and each have a length of at least `k`.

## Intuition
This problem asks for the *maximum number* of items (palindromic substrings) under a *non-overlapping* constraint. This is a classic setup for **Dynamic Programming (DP)**. If we decide to include a palindrome `s[j...i]`, then the next palindrome must start after index `i`. This suggests building up a solution from smaller prefixes of the string.

The core idea is to iterate through the string, maintaining a DP array where `dp[x]` stores the maximum number of valid palindromes found in the prefix `s[0...x-1]`. For each character `s[i]`, we consider two possibilities for `dp[i+1]` (the answer for `s[0...i]`):
1.  We **don't** include any new palindrome ending at `s[i]`. In this case, `dp[i+1]` is simply `dp[i]`.
2.  We **do** include a palindrome `s[j...i]` that ends at `s[i]`. If this palindrome is valid (length `>= k`), then we can add `1` to the maximum count obtained from the prefix *before* this palindrome, which would be `dp[j]`.

To make this efficient, we need a fast way to find all palindromes ending at `s[i]`. The "expand around center" technique is perfect for this, as it finds all palindromes centered at `i` (odd length) or between `i` and `i+1` (even length) in `O(N)` time for each `i`.

## Approach
We will use dynamic programming combined with the "expand around center" technique for palindrome detection.

1.  **Initialize DP Array**: Create a `dp` array of size `n + 1` (where `n` is the length of `s`), initialized with zeros. `dp[x]` will store the maximum number of non-overlapping palindromic substrings of length at least `k` found in the prefix `s[0...x-1]`. `dp[0]` will be 0, representing an empty prefix.

2.  **Iterate Through String**: Loop `i` from `0` to `n-1` (representing the current character `s[i]`).
    *   **Default DP Update**: At the beginning of each iteration `i`, set `dp[i+1] = dp[i]`. This accounts for the case where we don't pick any new palindrome ending at `s[i]`. The maximum count for `s[0...i]` is at least the maximum count for `s[0...i-1]`.

    *   **Expand for Odd-Length Palindromes**: Consider `s[i]` as the center of an odd-length palindrome.
        *   Initialize `left = i` and `right = i`.
        *   While `left >= 0`, `right < n`, and `s[left] == s[right]`:
            *   Calculate `current_len = right - left + 1`.
            *   If `current_len >= k`:
                *   This means `s[left...right]` is a valid palindrome.
                *   The number of palindromes if we include this one would be `1` (for `s[left...right]`) plus the maximum palindromes we could find in the string *before* `s[left]`. This previous count is stored in `dp[left]`.
                *   Update `dp[right+1] = max(dp[right+1], dp[left] + 1)`. Note `dp[right+1]` corresponds to the prefix `s[0...right]`.
            *   Decrement `left` and increment `right` to expand outwards.

    *   **Expand for Even-Length Palindromes**: Consider `s[i]` and `s[i+1]` as the centers of an even-length palindrome.
        *   Initialize `left = i` and `right = i + 1`.
        *   While `left >= 0`, `right < n`, and `s[left] == s[right]`:
            *   Calculate `current_len = right - left + 1`.
            *   If `current_len >= k`:
                *   Update `dp[right+1] = max(dp[right+1], dp[left] + 1)`.
            *   Decrement `left` and increment `right`.

3.  **Return Result**: After iterating through all characters, `dp[n]` will hold the maximum number of non-overlapping palindromic substrings for the entire string `s`.

## Visualization

Let's trace `s = "abaccdbbd"`, `k = 3`. `n = 9`.
`dp` array of size `n+1 = 10`, initialized to `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`.

```
String s:  a b a c c d b b d
Indices:   0 1 2 3 4 5 6 7 8

DP array (dp[x] = max palindromes in s[0...x-1]):
dp: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  (size n+1)

Iteration i=2 (s[2] = 'a'):
1. Default: dp[3] = dp[2] = 0
2. Expand for odd-length palindromes centered at i=2:
   - (2,2) "a": length 1. Not >= k.
   - (1,3) "bac": s[1] != s[3]. Stop.
   - (0,2) "aba": length 3. >= k.
     prev_count = dp[0] = 0.
     Update dp[3] = max(dp[3], dp[0] + 1) = max(0, 0 + 1) = 1.
dp: [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
             ^
             dp[3] now 1

... (intermediate steps, dp[4] to dp[8] will become 1 from default updates) ...

Iteration i=8 (s[8] = 'd'):
1. Default: dp[9] = dp[8] = 1 (assuming dp[8] was 1 from previous steps)
2. Expand for odd-length palindromes centered at i=8:
   - (8,8) "d": length 1. Not >= k.
   - (7,9) (out of bounds)
   - (6,8) "dbd": s[6] != s[8] ('b' != 'd'). Stop.
3. Expand for even-length palindromes centered between i=8 and i+1=9:
   - (8,9) (out of bounds)
   - (7,8) "bd": s[7] != s[8] ('b' != 'd'). Stop.
   - (6,9) (out of bounds)
   - (5,8) "dbbd": s[5] == s[8] ('d' == 'd') AND s[6] == s[7] ('b' == 'b'). Length 4. >= k.
     prev_count = dp[5] = 1.
     Update dp[9] = max(dp[9], dp[5] + 1) = max(1, 1 + 1) = 2.
dp: [0, 0, 0, 1, 1, 1, 1, 1, 1, 2]
                               ^
                               dp[9] now 2

Final Answer: dp[n] = dp[9] = 2
```

## Dry Run
Let's walk through Example 1: `s = "abaccdbbd"`, `k = 3`.
`n = 9`. `dp` array of size `10`, initialized to `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`.

| `i` | `s[i]` | `dp[i+1]` init | Palindrome (left, right) | `s[left...right]` | Length | `>= k`? | `prev_count` (`dp[left]`) | `dp[right+1]` update | `dp` array state (after current `i`) |
| :-- | :----- | :------------- | :----------------------- | :---------------- | :----- | :------ | :------------------------- | :-------------------- | :----------------------------------- |
| 0   | 'a'    | `dp[1]=dp[0]=0`| (0,0)                    | "a"               | 1      | No      |                            |                       | `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`     |
| 1   | 'b'    | `dp[2]=dp[1]=0`| (1,1)                    | "b"               | 1      | No      |                            |                       | `[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`     |
| 2   | 'a'    | `dp[3]=dp[2]=0`| (2,2)                    | "a"               | 1      | No      |                            |                       |                                      |
|     |        |                | (0,2)                    | "aba"             | 3      | Yes     | `dp[0]=0`                  | `dp[3]=max(0, 0+1)=1` | `[0, 0, 0, 1, 0, 0, 0, 0, 0, 0]`     |
| 3   | 'c'    | `dp[4]=dp[3]=1`| (3,3)                    | "c"               | 1      | No      |                            |                       | `[0, 0, 0, 1, 1, 0, 0, 0, 0, 0]`     |
| 4   | 'c'    | `dp[5]=dp[4]=1`| (4,4)                    | "c"               | 1      | No      |                            |                       |                                      |
|     |        |                | (3,4)                    | "cc"              | 2      | No      |                            |                       | `[0, 0, 0, 1, 1, 1, 0, 0, 0, 0]`     |
| 5   | 'd'    | `dp[6]=dp[5]=1`| (5,5)                    | "d"               | 1      | No      |                            |                       | `[0, 0, 0, 1, 1, 1, 1, 0, 0, 0]`     |
| 6   | 'b'    | `dp[7]=dp[6]=1`| (6,6)                    | "b"               | 1      | No      |                            |                       | `[0, 0, 0, 1, 1, 1, 1, 1, 0, 0]`     |
| 7   | 'b'    | `dp[8]=dp[7]=1`| (7,7)                    | "b"               | 1      | No      |                            |                       |                                      |
|     |        |                | (6,7)                    | "bb"              | 2      | No      |                            |                       | `[0, 0, 0, 1, 1, 1, 1, 1, 1, 0]`     |
| 8   | 'd'    | `dp[9]=dp[8]=1`| (8,8)                    | "d"               | 1      | No      |                            |                       |                                      |
|     |        |                | (5,8)                    | "dbbd"            | 4      | Yes     | `dp[5]=1`                  | `dp[9]=max(1, 1+1)=2` | `[0, 0, 0, 1, 1, 1, 1, 1, 1, 2]`     |

Final result: `dp[9] = 2`.

## Complexity
*   **Time Complexity**: `O(N^2)`. The outer loop iterates `N` times (for `i` from `0` to `n-1`). Inside this loop, the two `while` loops (for odd and even length palindromes) expand outwards. In the worst case, each `while` loop can run `O(N)` times. Thus, the total time complexity is `N * O(N) = O(N^2)`. Given `N <= 2000`, `N^2` is `4 * 10^6`, which is efficient enough.
*   **Space Complexity**: `O(N)`. We use a `dp` array of size `N+1`.

## Edge Cases
*   **`k = 1`**: Any single character is a palindrome. The solution will correctly count `N` palindromes if `N >= 1`.
*   **`k > n`**: No substring can have length `k`. The `current_len >= k` condition will never be met, and `dp` will remain all zeros. The result will be `0`, which is correct.
*   **No palindromes of length `k`**: For example, `s = "adbcda", k = 2`. The `current_len >= k` condition will not be met for any palindrome found, or no palindromes will be found. The `dp` array will remain all zeros, resulting in `0`, which is correct.
*   **String with all identical characters**: E.g., `s = "aaaaa", k = 2`. The algorithm will correctly identify many palindromes and maximize the count. For `k=2`, it would find `aa`, `aaaa`, etc.
*   **String is itself a palindrome**: E.g., `s = "racecar", k = 3`. The algorithm will find "racecar" and correctly update the DP.

## Solution

```python
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        # dp[i] stores the maximum number of non-overlapping palindrome substrings
        # of length at least k in the prefix s[0...i-1].
        # dp array size n+1 to handle dp[0] for empty prefix and dp[n] for full string.
        dp = [0] * (n + 1)

        # Iterate through each character of the string.
        # 'i' represents the current character's index (s[i]).
        # We are calculating dp[i+1], which is for the prefix s[0...i].
        for i in range(n):
            # Option 1: Don't pick any new palindrome ending at s[i].
            # The maximum count for s[0...i] is at least the count for s[0...i-1].
            dp[i+1] = dp[i]

            # Option 2 & 3: Find palindromes ending at s[i] and update dp[i+1].
            # We use "expand around center" to find all palindromes.

            # Case A: Odd-length palindromes centered at s[i]
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                current_len = right - left + 1
                if current_len >= k:
                    # If s[left...right] is a valid palindrome,
                    # we can potentially include it.
                    # The previous count comes from dp[left] (max palindromes in s[0...left-1]).
                    prev_count = dp[left]
                    # Update dp[right+1] (max palindromes in s[0...right])
                    # with the possibility of including this palindrome.
                    dp[right+1] = max(dp[right+1], prev_count + 1)
                
                # Expand outwards
                left -= 1
                right += 1

            # Case B: Even-length palindromes centered between s[i] and s[i+1]
            # (Note: s[i+1] might be out of bounds, handled by 'right < n')
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                current_len = right - left + 1
                if current_len >= k:
                    # Same logic as for odd-length palindromes
                    prev_count = dp[left]
                    dp[right+1] = max(dp[right+1], prev_count + 1)
                
                # Expand outwards
                left -= 1
                right += 1
        
        # The final answer is the maximum count for the entire string s[0...n-1].
        return dp[n]

```

## Why This Works
This solution correctly finds the maximum number of non-overlapping palindromic substrings by using **dynamic programming** with an optimal substructure and overlapping subproblems. The `dp[x]` state accurately stores the maximum count for the prefix `s[0...x-1]`. By iterating through each character `s[i]` and considering all valid palindromes `s[left...right]` that *end* at `s[i]` (i.e., `right == i`), we ensure that we explore all possible ways to extend the solution. The update `dp[right+1] = max(dp[right+1], dp[left] + 1)` correctly enforces the **non-overlapping** constraint: if we choose `s[left...right]`, the `dp[left]` term ensures that any previously counted palindromes must lie entirely to the left of `s[left]`. The `dp[i+1] = dp[i]` step ensures that the maximum count is always carried forward, even if no new palindrome ending at `s[i]` improves the count. This comprehensive approach guarantees optimality.

---
<sub>Generated 2026-09-15 05:13 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
