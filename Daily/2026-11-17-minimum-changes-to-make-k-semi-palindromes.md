# [2911] Minimum Changes to Make K Semi-palindromes

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-11-17 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/)

**Topics:** Two Pointers, String, Dynamic Programming

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given a string s and an integer k, partition s into k substrings such that the letter changes needed to make each substring a semi-palindrome are minimized.

Return the minimum number of letter changes required.

A semi-palindrome is a special type of string that can be divided into palindromes based on a repeating pattern. To check if a string is a semi-palindrome:​

- Choose a positive divisor d of the string's length. d can range from 1 up to, but not including, the string's length. For a string of length 1, it does not have a valid divisor as per this definition, since the only divisor is its length, which is not allowed.

- For a given divisor d, divide the string into groups where each group contains characters from the string that follow a repeating pattern of length d. Specifically, the first group consists of characters at positions 1, 1 + d, 1 + 2d, and so on; the second group includes characters at positions 2, 2 + d, 2 + 2d, etc.

- The string is considered a semi-palindrome if each of these groups forms a palindrome.

Consider the string "abcabc":

- The length of "abcabc" is 6. Valid divisors are 1, 2, and 3.

- For d = 1: The entire string "abcabc" forms one group. Not a palindrome.

- For d = 2:

- Group 1 (positions 1, 3, 5): "acb"

- Group 2 (positions 2, 4, 6): "bac"

- Neither group forms a palindrome.

- For d = 3:

- Group 1 (positions 1, 4): "aa"

- Group 2 (positions 2, 5): "bb"

- Group 3 (positions 3, 6): "cc"

- All groups form palindromes. Therefore, "abcabc" is a semi-palindrome.

Example 1:

Input:   s = "abcac", k = 2

Output:   1

Explanation:  Divide s into "ab" and "cac". "cac" is already semi-palindrome. Change "ab" to "aa", it becomes semi-palindrome with d = 1.

Example 2:

Input:   s = "abcdef", k = 2

Output:   2

Explanation:  Divide s into substrings "abc" and "def". Each needs one change to become semi-palindrome.

Example 3:

Input:   s = "aabbaa", k = 3

Output:   0

Explanation:  Divide s into substrings "aa", "bb" and "aa". All are already semi-palindromes.

Constraints:

- 2 <= s.length <= 200

- 1 <= k <= s.length / 2

- s contains only lowercase English letters.

**Examples / sample tests:**

```
"abcac"
2
```

---

## Problem Summary
Given a string `s` and an integer `k`, we need to partition `s` into `k` non-overlapping substrings. The goal is to minimize the total number of letter changes required to make each of these `k` substrings a "semi-palindrome". A semi-palindrome is a string that can be divided into `d` groups (where `d` is a divisor of its length, `1 <= d < length`), such that each group forms a palindrome.

## Intuition
This problem asks for the minimum cost to partition a string into a fixed number of parts, where each part must satisfy a specific property. This is a classic **Dynamic Programming (DP)** problem structure.

1.  **Partitioning DP:** We can define `dp[i][j]` as the minimum number of changes to partition the suffix `s[i:]` (from index `i` to the end) into `j` semi-palindromes.
2.  **Transition:** To calculate `dp[i][j]`, we consider all possible ways to form the *first* semi-palindrome `s[i...x]`. If `s[i...x]` requires `cost` changes to become a semi-palindrome, then the total changes would be `cost + dp[x+1][j-1]` (the cost for the first part plus the minimum cost for the remaining `j-1` parts from `s[x+1:]`). We take the minimum over all valid `x`.
3.  **Semi-palindrome Cost:** The cost of making a substring `s[i...x]` a semi-palindrome itself needs to be calculated. This involves iterating through all valid divisors `d` of the substring's length. For each `d`, we form `d` groups and count the changes needed to make each group a palindrome. The minimum changes over all `d` is the cost for `s[i...x]`. Since this cost will be needed repeatedly, it's efficient to **precompute** these costs for all possible substrings.

## Approach
The solution involves two main stages:

### Stage 1: Precomputing `changes[i][j]`
This stage calculates the minimum number of letter changes required to make any substring `s[i...j]` a semi-palindrome. Let `N` be the length of `s`.
1.  Initialize a 2D array `changes` of size `N x N` with `infinity`. `changes[i][j]` will store the minimum changes for `s[i...j]`.
2.  Iterate `i` from `0` to `N-1` (start of substring).
3.  Iterate `j` from `i` to `N-1` (end of substring).
    *   Let `sub_len = j - i + 1`.
    *   **Constraint:** A semi-palindrome must have length at least 2. If `sub_len < 2`, `s[i...j]` cannot be a semi-palindrome, so `changes[i][j]` remains `infinity`.
    *   Initialize `min_changes_for_sub = infinity`.
    *   Iterate `d` from `1` to `sub_len - 1`.
        *   **Constraint:** `d` must be a positive divisor of `sub_len`. If `sub_len % d != 0`, skip this `d`.
        *   Initialize `current_d_changes = 0`.
        *   For each `group_idx` from `0` to `d-1`:
            *   This group consists of characters `s[i + group_idx], s[i + group_idx + d], s[i + group_idx + 2d], ...`.
            *   Use two pointers, `p1` starting at `i + group_idx` and `p2` starting at `i + group_idx + (sub_len // d - 1) * d` (the last character in this group).
            *   While `p1 < p2`:
                *   If `s[p1] != s[p2]`, increment `group_mismatches`.
                *   Move `p1` forward by `d`, `p2` backward by `d`.
            *   Add `group_mismatches` to `current_d_changes`.
        *   Update `min_changes_for_sub = min(min_changes_for_sub, current_d_changes)`.
    *   Set `changes[i][j] = min_changes_for_sub`.

### Stage 2: Dynamic Programming
This stage uses the precomputed `changes` table to find the overall minimum changes.
1.  Initialize a 2D array `dp` of size `(N+1) x (k+1)` with `infinity`. `dp[i][j]` stores the minimum changes for `s[i:]` into `j` parts.
2.  **Base Case:** `dp[N][0] = 0`. This means an empty suffix (`s[N:]`) requires 0 changes to be partitioned into 0 semi-palindromes.
3.  Iterate `i` from `N-1` down to `0` (start index of the current suffix).
4.  Iterate `j` from `1` to `k` (number of parts for the current suffix).
    *   **Constraint:** The remaining length `N - i` must be at least `2 * j` (since each semi-palindrome must have length at least 2). If not, `dp[i][j]` remains `infinity`.
    *   Iterate `x` from `i+1` to `N - 2 * (j-1)` (inclusive end index of the first semi-palindrome `s[i...x]`).
        *   **Constraint:** `s[i...x]` must have length at least 2, so `x >= i+1`.
        *   **Constraint:** The remaining suffix `s[x+1:]` must be able to form `j-1` semi-palindromes. Its length `N - (x+1)` must be at least `2 * (j-1)`. This implies `x <= N - 1 - 2 * (j-1)`.
        *   If `changes[i][x]` is `infinity` (meaning `s[i...x]` cannot be a semi-palindrome) or `dp[x+1][j-1]` is `infinity` (meaning the rest cannot be partitioned), skip this `x`.
        *   Update `dp[i][j] = min(dp[i][j], changes[i][x] + dp[x+1][j-1])`.
5.  The final answer is `dp[0][k]`.

## Visualization
Let's visualize the DP state and transitions for `s = "abcac", k = 2, N = 5`.

**`changes` table (simplified, only relevant values):**
`changes[i][j]` = min changes for `s[i...j]`
| Substring | `i` | `j` | `L` | `d` | Groups | Changes |
| :-------- | :-: | :-: | :-: | :-: | :----- | :------ |
| "ab"      | 0   | 1   | 2   | 1   | "ab"   | 1       |
| "abc"     | 0   | 2   | 3   | 1   | "abc"  | 1       |
| "abca"    | 0   | 3   | 4   | 1   | "abca" | 1       |
| "abcac"   | 0   | 4   | 5   | 1   | "abcac"| 2       |
| "bc"      | 1   | 2   | 2   | 1   | "bc"   | 1       |
| "bca"     | 1   | 3   | 3   | 1   | "bca"  | 1       |
| "bcac"    | 1   | 4   | 4   | 2   | "ba", "cc" | 1+0=1 |
| "ca"      | 2   | 3   | 2   | 1   | "ca"   | 1       |
| **"cac"** | **2** | **4** | **3** | **1** | **"cac"**| **0** |
| "ac"      | 3   | 4   | 2   | 1   | "ac"   | 1       |

**`dp` table (size `(N+1) x (k+1)` = `6 x 3`):**
`dp[i][j]` = min changes for `s[i:]` into `j` parts.
Initially all `inf`, except `dp[5][0] = 0`.

```
i \ j | 0     1     2
--------------------------
0     | inf   inf   inf
1     | inf   inf   inf
2     | inf   inf   inf
3     | inf   inf   inf
4     | inf   inf   inf
5     | 0     inf   inf  (Base case: dp[N][0] = 0)
```

**DP Calculation for `j=1` (1 part):**
*   `i=3` (`s[3:]`="ac"): `x=4`. `dp[3][1] = changes[3][4] + dp[5][0] = 1 + 0 = 1`.
*   `i=2` (`s[2:]`="cac"): `x=4`. `dp[2][1] = changes[2][4] + dp[5][0] = 0 + 0 = 0`.
*   `i=1` (`s[1:]`="bcac"): `x=4`. `dp[1][1] = changes[1][4] + dp[5][0] = 1 + 0 = 1`.
*   `i=0` (`s[0:]`="abcac"): `x=4`. `dp[0][1] = changes[0][4] + dp[5][0] = 2 + 0 = 2`.

```
i \ j | 0     1     2
--------------------------
0     | inf   2     inf
1     | inf   1     inf
2     | inf   0     inf
3     | inf   1     inf
4     | inf   inf   inf
5     | 0     inf   inf
```

**DP Calculation for `j=2` (2 parts):**
*   `i=1` (`s[1:]`="bcac"): `N-i=4 >= 2*2`. `x` from `1+1=2` to `5-1-2*(2-1)+1 = 3`. So `x` from `2` to `3`.
    *   `x=2`: `s[1...2]`="bc". `changes[1][2]=1`. `dp[3][1]=1`.
        `dp[1][2] = min(inf, changes[1][2] + dp[3][1]) = 1 + 1 = 2`.
    *   `x=3`: `s[1...3]`="bca". `changes[1][3]=1`. `dp[4][1]=inf`. Skip.
*   `i=0` (`s[0:]`="abcac"): `N-i=5 >= 2*2`. `x` from `0+1=1` to `5-1-2*(2-1)+1 = 3`. So `x` from `1` to `3`.
    *   `x=1`: `s[0...1]`="ab". `changes[0][1]=1`. `dp[2][1]=0`.
        `dp[0][2] = min(inf, changes[0][1] + dp[2][1]) = 1 + 0 = 1`.
    *   `x=2`: `s[0...2]`="abc". `changes[0][2]=1`. `dp[3][1]=1`.
        `dp[0][2] = min(1, changes[0][2] + dp[3][1]) = min(1, 1 + 1) = 1`.
    *   `x=3`: `s[0...3]`="abca". `changes[0][3]=1`. `dp[4][1]=inf`. Skip.

```
i \ j | 0     1     2
--------------------------
0     | inf   2     1    <-- Final Answer dp[0][2] = 1
1     | inf   1     2
2     | inf   0     inf
3     | inf   1     inf
4     | inf   inf   inf
5     | 0     inf   inf
```

## Dry Run
Let's walk through Example 1: `s = "abcac", k = 2`. `N = 5`.

**1. Precompute `changes[i][j]`:**
(See "Visualization" section for a detailed table. Key values used in DP are shown below.)
*   `changes[0][1]` ("ab"): 1
*   `changes[0][2]` ("abc"): 1
*   `changes[1][2]` ("bc"): 1
*   `changes[2][4]` ("cac"): 0
*   `changes[3][4]` ("ac"): 1

**2. Initialize `dp` table:**
`dp` table of size `(6 x 3)` initialized to `infinity`.
`dp[5][0] = 0`.

**3. DP Calculation:**

| `j` (parts) | `i` (start index) | `x` (end index of first part) | `s[i...x]` | `changes[i][x]` | `dp[x+1][j-1]` | `changes[i][x] + dp[x+1][j-1]` | `dp[i][j]` (current) | `dp[i][j]` (new) |
| :---------- | :---------------- | :---------------------------- | :--------- | :-------------- | :------------- | :------------------------------ | :------------------- | :--------------- |
| **1**       |                   |                               |            |                 |                |                                 |                      |                  |
|             | 4                 | (skip: `N-i < 2*j`)           |            |                 |                |                                 | `inf`                | `inf`            |
|             | 3                 | 4                             | "ac"       | 1               | `dp[5][0]=0`   | 1 + 0 = 1                       | `inf`                | `1`              |
|             | 2                 | 4                             | "cac"      | 0               | `dp[5][0]=0`   | 0 + 0 = 0                       | `inf`                | `0`              |
|             | 1                 | 4                             | "bcac"     | 1               | `dp[5][0]=0`   | 1 + 0 = 1                       | `inf`                | `1`              |
|             | 0                 | 4                             | "abcac"    | 2               | `dp[5][0]=0`   | 2 + 0 = 2                       | `inf`                | `2`              |
| **2**       |                   |                               |            |                 |                |                                 |                      |                  |
|             | 4,3,2             | (skip: `N-i < 2*j`)           |            |                 |                |                                 | `inf`                | `inf`            |
|             | 1                 | 2                             | "bc"       | 1               | `dp[3][1]=1`   | 1 + 1 = 2                       | `inf`                | `2`              |
|             |                   | 3                             | "bca"      | 1               | `dp[4][1]=inf` | (skip)                          | `2`                  | `2`              |
|             | 0                 | 1                             | "ab"       | 1               | `dp[2][1]=0`   | 1 + 0 = 1                       | `inf`                | `1`              |
|             |                   | 2                             | "abc"      | 1               | `dp[3][1]=1`   | 1 + 1 = 2                       | `1`                  | `min(1,2)=1`     |
|             |                   | 3                             | "abca"     | 1               | `dp[4][1]=inf` | (skip)                          | `1`                  | `1`              |

**Final Result:** `dp[0][2] = 1`.

## Complexity
*   **Time Complexity:** `O(N^3 * tau(N) + N^3)`
    *   **Precomputation (`changes` table):** There are `O(N^2)` substrings. For each substring of length `L`, we iterate through its divisors `d`. The number of divisors `tau(L)` is small (e.g., `tau(192) = 14`). For each `d`, checking all groups takes `O(L)` time. So, calculating `changes[i][j]` takes `O(L * tau(L))`. Total: `O(N^2 * N * tau(N)) = O(N^3 * tau(N))`.
    *   **DP Calculation (`dp` table):** There are `O(N * k)` states. Each state `dp[i][j]` involves iterating `x` from `O(N)` possible split points. So, `O(N * k * N) = O(N^2 * k)`. Since `k <= N/2`, this is `O(N^3)`.
    *   Overall, dominated by precomputation: `O(N^3 * tau(N))`. Given `N <= 200`, `200^3 * 18` (max `tau(N)` for `N <= 200`) is roughly `1.44 * 10^8`, which is acceptable.
*   **Space Complexity:** `O(N^2)`
    *   `changes` table: `O(N^2)`.
    *   `dp` table: `O(N * k)`. Since `k <= N/2`, this is `O(N^2)`.
    *   Overall: `O(N^2)`. Given `N <= 200`, `200^2 = 40000`, which is acceptable.

## Edge Cases
*   **`s.length < 2 * k`**: The problem constraints `1 <= k <= s.length / 2` ensure that `s.length >= 2 * k`. This means there are always enough characters to form `k` semi-palindromes, each of minimum length 2. The DP's `N - i < 2 * j` check handles cases where a suffix is too short for the required number of parts.
*   **`k = 1`**: The solution correctly calculates `dp[0][1]`, which will be `changes[0][N-1]`, the minimum changes for the entire string `s` to be a semi-palindrome.
*   **`s` is already a semi-palindrome (or can be made with 0 changes)**: If `s` can be partitioned into `k` semi-palindromes with 0 changes, `changes[i][j]` for relevant substrings will be 0, and the DP will correctly sum these to 0.
*   **`s` contains all identical characters (e.g., "aaaaa")**: All substrings will require 0 changes to be semi-palindromes (as any group of identical characters is a palindrome). The solution will correctly return 0.

## Solution

```python
import math

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # --- Stage 1: Precompute changes[i][j] ---
        # changes[i][j] stores the minimum letter changes to make s[i...j] a semi-palindrome.
        # Initialize with infinity, as some substrings might not be valid semi-palindromes
        # (e.g., length < 2).
        changes = [[math.inf] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                sub_len = j - i + 1
                
                # A semi-palindrome must have length at least 2.
                if sub_len < 2:
                    continue
                
                min_changes_for_sub = math.inf
                
                # Iterate through possible divisors 'd' of sub_len.
                # 'd' can range from 1 up to, but not including, the string's length.
                for d in range(1, sub_len):
                    if sub_len % d == 0: # 'd' must be a divisor of sub_len
                        current_d_changes = 0
                        
                        # Divide the substring s[i...j] into 'd' groups.
                        # Each group_idx from 0 to d-1 corresponds to characters
                        # at positions (i + group_idx), (i + group_idx + d), etc.
                        for group_idx in range(d):
                            group_mismatches = 0
                            
                            # Pointers for the current group.
                            # p1 starts at the first character of the group.
                            # p2 starts at the last character of the group.
                            p1 = i + group_idx
                            p2 = i + group_idx + (sub_len // d - 1) * d
                            
                            # Check if the group forms a palindrome.
                            while p1 < p2:
                                if s[p1] != s[p2]:
                                    group_mismatches += 1
                                p1 += d
                                p2 -= d
                            current_d_changes += group_mismatches
                        
                        min_changes_for_sub = min(min_changes_for_sub, current_d_changes)
                
                changes[i][j] = min_changes_for_sub

        # --- Stage 2: Dynamic Programming ---
        # dp[i][j] = minimum changes to partition suffix s[i:] into j semi-palindromes.
        # dp table size (n+1) x (k+1)
        dp = [[math.inf] * (k + 1) for _ in range(n + 1)]

        # Base case: 0 changes for an empty suffix (s[n:]) with 0 parts.
        dp[n][0] = 0

        # Iterate 'i' from n-1 down to 0 (start index of the current suffix).
        for i in range(n - 1, -1, -1):
            # Iterate 'j_parts' from 1 to k (number of semi-palindromes to form).
            for j_parts in range(1, k + 1):
                # Optimization: If remaining length (n - i) is less than 2 * j_parts,
                # it's impossible to form j_parts semi-palindromes (each needs length >= 2).
                if n - i < 2 * j_parts:
                    continue

                # Iterate 'x' as the inclusive end index of the first semi-palindrome s[i...x].
                # The first part s[i...x] must have length >= 2, so x >= i+1.
                # The remaining suffix s[x+1:] must form j_parts - 1 semi-palindromes.
                # Its length (n - (x+1)) must be at least 2 * (j_parts - 1).
                # This implies x+1 <= n - 2 * (j_parts - 1)
                # So, x <= n - 1 - 2 * (j_parts - 1).
                for x in range(i + 1, n - 2 * (j_parts - 1) + 1):
                    # Check if s[i...x] can be a semi-palindrome and if the rest can be partitioned.
                    if changes[i][x] == math.inf or dp[x + 1][j_parts - 1] == math.inf:
                        continue
                    
                    # Update dp[i][j_parts] with the minimum cost.
                    dp[i][j_parts] = min(dp[i][j_parts], changes[i][x] + dp[x + 1][j_parts - 1])
        
        return dp[0][k]

```

## Why This Works
This solution correctly finds the minimum changes by leveraging **Dynamic Programming**, which is suitable for optimization problems exhibiting **optimal substructure** and **overlapping subproblems**.

1.  **Optimal Substructure:** The problem of partitioning `s[i:]` into `j` semi-palindromes can be optimally solved by finding the optimal first semi-palindrome `s[i...x]` and then optimally solving the subproblem of partitioning the remaining `s[x+1:]` into `j-1` semi-palindromes. The total minimum changes for `s[i:]` will be the sum of changes for `s[i...x]` and the minimum changes for `s[x+1:]`.
2.  **Overlapping Subproblems:** The costs for making various substrings semi-palindromes (`changes[i][j]`) and the minimum changes for partitioning suffixes into a certain number of parts (`dp[i][j]`) are reused multiple times. Precomputing these values in tables avoids redundant calculations, leading to an efficient solution.

The precomputation stage exhaustively checks all valid divisor patterns for every possible substring to find its absolute minimum changes to become a semi-palindrome. The DP stage then systematically builds up the solution from smaller subproblems (suffixes with fewer parts) to larger ones (longer suffixes with more parts), ensuring that when `dp[i][j]` is computed, all necessary `changes[i][x]` and `dp[x+1][j-1]` values are already finalized and optimal. This guarantees that `dp[0][k]` will hold the overall minimum changes for the entire string `s` into `k` semi-palindromes.

---
<sub>Generated 2026-11-17 08:23 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
