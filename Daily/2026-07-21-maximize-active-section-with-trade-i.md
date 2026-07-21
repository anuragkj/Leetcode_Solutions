# [3499] Maximize Active Section with Trade I

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-07-21 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximize-active-section-with-trade-i/)

**Topics:** String, Enumeration

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a binary string s of length n, where:

- '1' represents an active section.

- '0' represents an inactive section.

You can perform at most one trade to maximize the number of active sections in s. In a trade, you:

- Convert a contiguous block of '1's that is surrounded by '0's to all '0's.

- Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.

Return the maximum number of active sections in s after making the optimal trade.

Note: Treat s as if it is augmented with a '1' at both ends, forming t = '1' + s + '1'. The augmented '1's do not contribute to the final count.

Example 1:

Input: s = "01"

Output: 1

Explanation:

Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

Example 2:

Input: s = "0100"

Output: 4

Explanation:

- String "0100" → Augmented to "101001".

- Choose "0100", convert "101001" → "100001" → "111111".

- The final string without augmentation is "1111". The maximum number of active sections is 4.

Example 3:

Input: s = "1000100"

Output: 7

Explanation:

- String "1000100" → Augmented to "110001001".

- Choose "000100", convert "110001001" → "110000001" → "111111111".

- The final string without augmentation is "1111111". The maximum number of active sections is 7.

Example 4:

Input: s = "01010"

Output: 4

Explanation:

- String "01010" → Augmented to "1010101".

- Choose "010", convert "1010101" → "1000101" → "1111101".

- The final string without augmentation is "11110". The maximum number of active sections is 4.

Constraints:

- 1 <= n == s.length <= 10^5

- s[i] is either '0' or '1'

**Examples / sample tests:**

```
"01"
"0100"
"1000100"
"01010"
```

---

## Problem Summary
You are given a binary string `s` representing active ('1') and inactive ('0') sections. The goal is to maximize the total number of active sections by performing at most one trade. A trade involves converting a block of '1's (surrounded by '0's) to '0's, then converting the resulting larger block of '0's (now surrounded by '1's) to '1's.

## Intuition
The core idea is to understand the net effect of the trade. When we choose a contiguous block of '1's (say, of length $L_1$) that is surrounded by '0's (say, of lengths $L_{0,left}$ and $L_{0,right}$), the trade effectively converts the entire segment `0...0` ($L_{0,left}$) `1...1` ($L_1$) `0...0` ($L_{0,right}$) into `1...1` ($L_{0,left} + L_1 + L_{0,right}$).

The number of '1's in this segment changes from $L_1$ to $L_{0,left} + L_1 + L_{0,right}$.
The **gain** in '1's from this trade is $(L_{0,left} + L_1 + L_{0,right}) - L_1 = L_{0,left} + L_{0,right}$.
Therefore, to maximize the total number of active sections, we need to find a '1' block (surrounded by '0's) such that the sum of the lengths of its surrounding '0' blocks is maximized. If no such '1' block exists, no trade is possible, and the count remains the initial number of '1's.

The problem's note about augmenting `s` to `t = '1' + s + '1'` is crucial. It simplifies boundary conditions, ensuring that any '0' block at the start or end of `s` is considered "surrounded by '1's" and any '1' block at the start or end of `s` is considered "surrounded by '0's" if `s` itself starts/ends with '0'.

## Approach
1.  **Calculate Initial Ones:** Count the total number of '1's in the original string `s`. This will be our baseline.
2.  **Augment String:** Create an augmented string `t = '1' + s + '1'`. This helps handle edge cases where '0' or '1' blocks are at the beginning or end of `s` by providing artificial '1's as neighbors.
3.  **Group Consecutive Characters:** Iterate through the augmented string `t` and group consecutive identical characters. Store these groups as `(character, length)` pairs in a list (e.g., `[('1', 1), ('0', 2), ('1', 3), ...]`).
4.  **Find Maximum Gain:** Initialize `max_gain = 0`. Iterate through the `groups` list. We are looking for a `('1', L_1)` group that is surrounded by `('0', L_0_left)` and `('0', L_0_right)` groups.
    *   Since `t` starts and ends with '1', the `groups` list will always start with a `('1', ...)` and end with a `('1', ...)`.
    *   The groups will alternate between '1's and '0's.
    *   Therefore, any `('1', L_1)` group at index `i` (where `i > 0` and `i < len(groups) - 1`) will always have a `('0', L_0_left)` group at `i-1` and a `('0', L_0_right)` group at `i+1`.
    *   For each such `('1', L_1)` group, calculate the potential gain: `current_gain = L_0_left + L_0_right`. Update `max_gain = max(max_gain, current_gain)`.
5.  **Calculate Final Result:** The maximum number of active sections will be `initial_ones + max_gain`. If no valid trade was possible (e.g., `max_gain` remains 0), this correctly returns the initial count.

## Visualization
Let's visualize the process with `s = "0100"`.

1.  **Original string `s`:**
    ```
    s = "0 1 0 0"
    ```
    Initial '1's = 1.

2.  **Augmented string `t`:**
    ```
    t = "1 0 1 0 0 1"
          ^       ^
          |       |
      Augmented '1's
    ```

3.  **Group consecutive characters in `t`:**
    ```
    Index: 0 1 2 3 4 5
    Char:  1 0 1 0 0 1
    Groups:
    [ ('1', 1),  ('0', 1),  ('1', 1),  ('0', 2),  ('1', 1) ]
      ^          ^          ^          ^          ^
      groups[0]  groups[1]  groups[2]  groups[3]  groups[4]
    ```

4.  **Iterate through groups to find max gain:**
    *   `i = 0`: `groups[0]` is `('1', 1)`. This is an augmented '1'. (Loop starts from `i=1`).
    *   `i = 1`: `groups[1]` is `('0', 1)`. Not a '1' block. Skip.
    *   `i = 2`: `groups[2]` is `('1', 1)`. This is the '1' block from `s[1]`.
        *   Left neighbor `groups[1]` is `('0', 1)`. So, `L_0_left = 1`.
        *   Right neighbor `groups[3]` is `('0', 2)`. So, `L_0_right = 2`.
        *   `current_gain = L_0_left + L_0_right = 1 + 2 = 3`.
        *   `max_gain = max(0, 3) = 3`.
    *   `i = 3`: `groups[3]` is `('0', 2)`. Not a '1' block. Skip.
    *   `i = 4`: `groups[4]` is `('1', 1)`. This is an augmented '1'. (Loop ends before `i=4`).

5.  **Final Result:** `initial_ones + max_gain = 1 + 3 = 4`.

## Dry Run
Let's walk through **Example 1: `s = "01"`**

| Step | `s` | `initial_ones` | `t` | `groups` | `i` | `groups[i]` | `L_0_left` | `L_0_right` | `current_gain` | `max_gain` | Notes |
| :--- | :-- | :------------- | :-- | :------- | :-- | :---------- | :--------- | :---------- | :------------- | :--------- | :---- |
| 1    | "01" | 1              |     |          |     |             |            |             |                | 0          | Count '1's in `s` |
| 2    |     |                | "1011" |          |     |             |            |             |                |            | Augment `s` to `t` |
| 3    |     |                |     | `[('1',1), ('0',1), ('1',2)]` | | | | | | | Group `t` |
| 4    |     |                |     |          | 1   | `('0',1)`   |            |             |                | 0          | `groups[1]` is '0', skip |
| 5    |     |                |     |          |     |             |            |             |                | 0          | Loop ends (`range(1, len(groups) - 1)` is `range(1, 2)`). |
| 6    |     |                |     |          |     |             |            |             |                | 0          | Final `max_gain` is 0. |
| 7    |     |                |     |          |     |             |            |             |                |            | Result = `initial_ones + max_gain = 1 + 0 = 1`. |

**Final Result for `s = "01"`: 1**

## Complexity
*   **Time Complexity:** **O(N)**.
    *   Calculating `initial_ones` takes O(N).
    *   Augmenting the string `t` takes O(N).
    *   Grouping consecutive characters using `itertools.groupby` takes O(N) as it iterates through the string once.
    *   Iterating through the `groups` list takes O(N) in the worst case (e.g., "010101...").
*   **Space Complexity:** **O(N)**.
    *   Storing the augmented string `t` takes O(N) space.
    *   Storing the `groups` list takes O(N) space in the worst case (e.g., "010101...", where the number of groups is proportional to N).

## Edge Cases
*   **`s` contains all '1's (e.g., "111")**: `initial_ones` will be `n`. `t` will be all '1's. `groups` will contain only one `('1', n+2)` element. The loop for `max_gain` will not run, `max_gain` remains 0. Result `n + 0 = n`. Correct, as no trade can increase '1's.
*   **`s` contains all '0's (e.g., "000")**: `initial_ones` will be 0. `t` will be `10...01`. `groups` will be `[('1',1), ('0',n), ('1',1)]`. The loop for `max_gain` will not find any `('1', ...)` group at index `i` (only `groups[0]` and `groups[2]` are '1's, which are skipped by loop bounds). `max_gain` remains 0. Result `0 + 0 = 0`. Correct.
*   **`s` has length 1 (e.g., "0" or "1")**:
    *   `s = "0"`: `initial_ones = 0`. `t = "101"`. `groups = [('1',1), ('0',1), ('1',1)]`. Loop for `max_gain` will not find a valid '1' block. `max_gain = 0`. Result `0`. Correct.
    *   `s = "1"`: `initial_ones = 1`. `t = "111"`. `groups = [('1',3)]`. Loop for `max_gain` will not run. `max_gain = 0`. Result `1`. Correct.
*   **`s` has only one '1' block, but it's at an end (e.g., "100" or "001")**:
    *   `s = "100"`: `initial_ones = 1`. `t = "11001"`. `groups = [('1',2), ('0',2), ('1',1)]`. Loop for `max_gain` will not find a valid '1' block (only `groups[0]` and `groups[2]` are '1's, which are skipped). `max_gain = 0`. Result `1`. Correct.
    *   `s = "001"`: `initial_ones = 1`. `t = "10011"`. `groups = [('1',1), ('0',2), ('1',2)]`. Similar to above, `max_gain = 0`. Result `1`. Correct.

## Solution
```python
import itertools

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        
        # Step 1: Calculate initial number of '1's
        initial_ones = s.count('1')
        
        # If all '1's or all '0's, no trade can increase the count.
        # This is an optimization, but the general logic handles it too.
        if initial_ones == n or initial_ones == 0:
            return initial_ones
            
        # Step 2: Augment the string with '1's at both ends
        # This simplifies boundary conditions for '0' and '1' blocks.
        t = '1' + s + '1'
        
        # Step 3: Group consecutive identical characters in 't'
        # Example: "101001" -> [('1', 1), ('0', 1), ('1', 1), ('0', 2), ('1', 1)]
        groups = []
        for char, group_iter in itertools.groupby(t):
            groups.append((char, len(list(group_iter))))
            
        # Step 4: Find the maximum gain from a single trade
        # A trade involves picking a '1' block surrounded by '0's.
        # The gain is the sum of lengths of the surrounding '0' blocks.
        max_gain = 0
        
        # Iterate through the groups. We are looking for a '1' block (groups[i])
        # that has a '0' block to its left (groups[i-1]) and to its right (groups[i+1]).
        # The augmented '1's at the ends of 't' ensure that groups[0] and groups[len(groups)-1]
        # are always '1's. So we only need to consider '1' blocks in between.
        # These '1' blocks will always be at even indices (0-indexed) in the 'groups' list
        # if the list starts with a '1' block.
        # Since t starts with '1', groups[0] is ('1', ...).
        # So, '1' blocks are at indices 0, 2, 4, ...
        # '0' blocks are at indices 1, 3, 5, ...
        # We need a '1' block (groups[i]) where i > 0 and i < len(groups) - 1.
        # This means i must be an even index, and it must be at least 2.
        # The loop range `range(1, len(groups) - 1)` ensures we have left and right neighbors.
        for i in range(1, len(groups) - 1):
            current_char, current_len = groups[i]
            
            # If the current group is a '1' block (which means it's a candidate for the first step of the trade)
            if current_char == '1':
                # Its left neighbor (groups[i-1]) must be a '0' block.
                # Its right neighbor (groups[i+1]) must be a '0' block.
                # Due to the alternating nature of groups in 't', this is guaranteed if current_char is '1'
                # and i is not 0 or len(groups)-1.
                L_0_left = groups[i-1][1]
                L_0_right = groups[i+1][1]
                
                # The gain from this trade is the sum of the lengths of the surrounding '0' blocks.
                max_gain = max(max_gain, L_0_left + L_0_right)
                
        # Step 5: The maximum number of active sections is the initial count plus the maximum gain.
        return initial_ones + max_gain

```

## Why This Works
The solution works by accurately modeling the trade's effect. The augmentation `t = '1' + s + '1'` ensures that any '0' block at the ends of `s` is considered "surrounded by '1's" and any '1' block at the ends of `s` is considered "surrounded by '0's" if `s` itself starts/ends with '0'. By grouping consecutive characters, we efficiently identify all alternating blocks of '0's and '1's. The crucial insight is that converting a `0...0` ($L_{0,left}$) `1...1` ($L_1$) `0...0` ($L_{0,right}$) segment to all '1's results in a net gain of $L_{0,left} + L_{0,right}$ ones. By iterating through all '1' blocks that are surrounded by '0's (which are precisely the `('1', L_1)` groups with `('0', L_0_left)` and `('0', L_0_right)` neighbors in the `groups` list, excluding the augmented '1's), we find the maximum possible gain. Adding this maximum gain to the initial count of '1's yields the optimal result.

---
<sub>Generated 2026-07-21 03:58 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
