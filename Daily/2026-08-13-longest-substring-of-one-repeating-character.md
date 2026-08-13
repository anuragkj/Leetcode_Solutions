# [2213] Longest Substring of One Repeating Character

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-08-13 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/longest-substring-of-one-repeating-character/)

**Topics:** Array, String, Segment Tree, Ordered Set

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

The i^th query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the i^th query is performed.

Example 1:

Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
Output: [3,3,4]
Explanation:
- 1^st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2^nd query updates s = "bbbccc".
  The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3^rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].

Example 2:

Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
Output: [2,3]
Explanation:
- 1^st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
- 2^nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].

Constraints:

- 1 <= s.length <= 10^5

- s consists of lowercase English letters.

- k == queryCharacters.length == queryIndices.length

- 1 <= k <= 10^5

- queryCharacters consists of lowercase English letters.

- 0 <= queryIndices[i] < s.length

**Examples / sample tests:**

```
"babacc"
"bcb"
[1,3,3]
"abyzz"
"aa"
[2,1]
```

---

## Problem Summary
You are given an initial string `s` and a series of `k` queries. Each query specifies an index and a new character to update in `s`. After each update, you must find and return the length of the **longest substring consisting of only one repeating character** in the modified string `s`.

## Intuition
The problem asks us to perform **point updates** on a string and, after each update, query for a global property (the maximum length of a repeating character substring). A naive approach of rebuilding the string and re-scanning it after each query would be `O(K * N)`, which is too slow for `N, K = 10^5`. This pattern strongly suggests using a **Segment Tree**.

A standard segment tree node usually stores information like sum, min, or max for its range. Here, we need more complex information to correctly combine results from child nodes:
1.  **`max_len`**: The longest repeating character substring within this segment. This is our primary target.
2.  **`left_char` / `right_char`**: The characters at the very beginning and end of the segment. These are crucial for checking if a repeating substring can extend across the boundary when merging two child nodes.
3.  **`prefix_len`**: The length of the longest repeating character substring starting from the leftmost character of the segment.
4.  **`suffix_len`**: The length of the longest repeating character substring ending at the rightmost character of the segment.
5.  **`total_len`**: The total length of the segment. Useful for `prefix_len` and `suffix_len` calculations.

The **key insight** is how to **merge** two child nodes (`left_node` and `right_node`) into a parent node. The `max_len` of the parent could come from:
*   The `max_len` of the left child.
*   The `max_len` of the right child.
*   A new repeating substring formed by combining the `suffix_len` of the left child and the `prefix_len` of the right child, *if* `left_node.right_char` is equal to `right_node.left_char`.

## Approach
1.  **Initialize `s` as a list of characters**: Strings in Python are immutable, so converting `s` to a `list` allows for `O(1)` character updates.
2.  **Define a `Node` class**: This class will encapsulate all the information needed for each segment tree node: `max_len`, `left_char`, `right_char`, `prefix_len`, `suffix_len`, and `total_len`.
    ```python
    class Node:
        def __init__(self, max_len=0, left_char='', right_char='', prefix_len=0, suffix_len=0, total_len=0):
            self.max_len = max_len
            self.left_char = left_char
            self.right_char = right_char
            self.prefix_len = prefix_len
            self.suffix_len = suffix_len
            self.total_len = total_len
    ```
3.  **Implement a `merge` function**: This function takes two `Node` objects (representing the left and right children) and returns a new `Node` object for their parent.
    *   `total_len`, `left_char`, `right_char` are straightforward combinations.
    *   `max_len` is `max(left_node.max_len, right_node.max_len)`. If `left_node.right_char == right_node.left_char`, we also consider `left_node.suffix_len + right_node.prefix_len`.
    *   `prefix_len` is `left_node.total_len + right_node.prefix_len` if the entire `left_node` is a single repeating character and it matches `right_node.left_char`. Otherwise, it's just `left_node.prefix_len`.
    *   `suffix_len` is symmetric to `prefix_len`.
4.  **Build the Segment Tree**:
    *   Create an array `tree` of size `4 * N` (where `N` is `len(s)`) to store `Node` objects.
    *   Recursively build the tree:
        *   **Base Case**: If `tl == tr` (a leaf node representing a single character), create a `Node` with `max_len=1`, `prefix_len=1`, `suffix_len=1`, `total_len=1`, and `left_char`/`right_char` set to that character.
        *   **Recursive Step**: Divide the segment `[tl, tr]` into two halves `[tl, tm]` and `[tm+1, tr]`. Recursively build the left and right children, then merge their results using the `merge` function to populate the current node.
5.  **Implement the `update` function**:
    *   When a character at `pos` changes to `new_char`:
        *   Recursively traverse the tree to find the leaf node corresponding to `pos`.
        *   Update this leaf node with the `new_char` (creating a new `Node(1, new_char, new_char, 1, 1, 1)`).
        *   As the recursion unwinds, re-merge the parent nodes along the path from the updated leaf to the root, ensuring all aggregated values are correct.
6.  **Process Queries**:
    *   Initialize an empty list `ans` to store results.
    *   For each query `i` from `0` to `k-1`:
        *   Update the character in `s_list` at `queryIndices[i]` to `queryCharacters[i]`.
        *   Call the `update` function on the segment tree.
        *   The answer for the current query is `tree[1].max_len` (the `max_len` of the root node, which represents the entire string).
        *   Append this result to `ans`.
7.  **Return `ans`**.

## Visualization
Let's illustrate the `merge` logic for two nodes: `Left Child` and `Right Child` combining to form a `Parent Node`.

```mermaid
graph TD
    subgraph Parent Node (e.g., "aaabb")
        P_max_len["max_len: 4"]
        P_left_char["left_char: 'a'"]
        P_right_char["right_char: 'b'"]
        P_prefix_len["prefix_len: 4"]
        P_suffix_len["suffix_len: 2"]
        P_total_len["total_len: 5"]
    end

    subgraph Left Child ("aaab")
        L_max_len["max_len: 3"]
        L_left_char["left_char: 'a'"]
        L_right_char["right_char: 'a'"]
        L_prefix_len["prefix_len: 3"]
        L_suffix_len["suffix_len: 3"]
        L_total_len["total_len: 3"]
    end

    subgraph Right Child ("abb")
        R_max_len["max_len: 2"]
        R_left_char["left_char: 'a'"]
        R_right_char["right_char: 'b'"]
        R_prefix_len["prefix_len: 1"]
        R_suffix_len["suffix_len: 2"]
        R_total_len["total_len: 2"]
    end

    L_max_len -- contributes --> P_max_len
    R_max_len -- contributes --> P_max_len
    L_right_char -- 'a' == 'a' --> R_left_char
    L_suffix_len -- (3) + (1) --> R_prefix_len
    L_suffix_len -- (combined length 4) --> P_max_len
    L_prefix_len -- (extends) --> P_prefix_len
    R_suffix_len -- (is) --> P_suffix_len
    L_total_len -- (sum) --> P_total_len
    R_total_len -- (sum) --> P_total_len

    style P_max_len fill:#f9f,stroke:#333,stroke-width:2px
    style P_prefix_len fill:#f9f,stroke:#333,stroke-width:2px
    style P_suffix_len fill:#f9f,stroke:#333,stroke-width:2px
```
In this example:
*   `Left Child` covers "aaab", `Right Child` covers "abb".
*   `Parent Node` covers "aaabb".
*   `L.right_char` ('a') matches `R.left_char` ('a'). This means a repeating substring can span the merge point.
*   `P.max_len` becomes `max(L.max_len=3, R.max_len=2, L.suffix_len + R.prefix_len = 3 + 1 = 4) = 4`.
*   `P.prefix_len`: Since `L.prefix_len == L.total_len` (3 == 3) and characters match, `P.prefix_len = L.total_len + R.prefix_len = 3 + 1 = 4`.
*   `P.suffix_len`: `R.suffix_len == R.total_len` (2 == 2) is false (string "abb" is not all 'b'). So, `P.suffix_len = R.suffix_len = 2`.

## Dry Run
Let's trace Example 1: `s = "babacc"`, `queryCharacters = "bcb"`, `queryIndices = [1,3,3]`

| Query | `s` (after update) | `root.max_len` | Explanation |
| :---- | :----------------- | :------------- | :---------- |
| Initial | "babacc"           | 2              | The longest repeating substring is "cc" (length 2). |
| 1: `s[1] = 'b'` | "bbbacc"           | 3              | `s[1]` changes from 'a' to 'b'. The string becomes "bbbacc". The longest repeating substring is "bbb" (length 3). |
| 2: `s[3] = 'c'` | "bbbccc"           | 3              | `s[3]` changes from 'a' to 'c'. The string becomes "bbbccc". The longest repeating substrings are "bbb" and "ccc" (both length 3). |
| 3: `s[3] = 'b'` | "bbbbcc"           | 4              | `s[3]` changes from 'c' to 'b'. The string becomes "bbbbcc". The longest repeating substring is "bbbb" (length 4). |
| Final Result |                    | `[3, 3, 4]`    |             |

## Complexity
*   **Time Complexity**: `O(N + K log N)`
    *   Building the segment tree takes `O(N)` time, where `N` is the length of `s`.
    *   Each of the `K` queries involves an `update` operation, which takes `O(log N)` time (due to traversing a path from leaf to root).
*   **Space Complexity**: `O(N)`
    *   The segment tree requires `O(N)` space to store its nodes (typically `4N` for an array-based implementation).
    *   The `s_list` also takes `O(N)` space.

## Edge Cases
*   **String with all identical characters**: E.g., `s = "aaaaa"`. The `max_len` for the root node will correctly be `N`. The `prefix_len` and `suffix_len` will also be `N`.
*   **String with alternating characters**: E.g., `s = "ababab"`. The `max_len` for the root node will correctly be `1`. The `prefix_len` and `suffix_len` will also be `1` for most nodes.
*   **Single character string**: E.g., `s = "a"`. The leaf node logic correctly initializes `max_len=1`.
*   **Queries at the same index**: The problem example `queryIndices = [1,3,3]` demonstrates this. Each query updates the string from its *current* state, which the segment tree handles naturally by modifying the relevant leaf node and propagating changes.
*   **Constraints**: `1 <= s.length <= 10^5` means `s` is never empty.

## Solution

```python
from typing import List

class Node:
    """
    Represents a node in the segment tree.
    Stores information about a segment of the string.
    """
    def __init__(self, max_len=0, left_char='', right_char='', prefix_len=0, suffix_len=0, total_len=0):
        self.max_len = max_len          # Longest repeating char substring in this segment
        self.left_char = left_char      # Character at the leftmost index of the segment
        self.right_char = right_char    # Character at the rightmost index of the segment
        self.prefix_len = prefix_len    # Length of longest repeating char prefix
        self.suffix_len = suffix_len    # Length of longest repeating char suffix
        self.total_len = total_len      # Total length of the segment

class Solution:
    def longestRepeating(self, s: str, queryCharacters: List[str], queryIndices: List[int]) -> List[int]:
        n = len(s)
        s_list = list(s) # Convert string to list for mutable updates
        tree = [None] * (4 * n) # Segment tree array

        def merge(left_node: Node, right_node: Node) -> Node:
            """
            Merges two child nodes to create a parent node.
            This is the core logic of the segment tree for this problem.
            """
            res = Node()
            res.total_len = left_node.total_len + right_node.total_len
            res.left_char = left_node.left_char
            res.right_char = right_node.right_char

            # Calculate max_len:
            # It can be from left child, right child, or span across the merge point.
            res.max_len = max(left_node.max_len, right_node.max_len)
            if left_node.right_char == right_node.left_char:
                res.max_len = max(res.max_len, left_node.suffix_len + right_node.prefix_len)

            # Calculate prefix_len:
            # If the entire left segment is one repeating char and it matches
            # the start of the right segment, the prefix can extend.
            if left_node.prefix_len == left_node.total_len and left_node.right_char == right_node.left_char:
                res.prefix_len = left_node.total_len + right_node.prefix_len
            else:
                res.prefix_len = left_node.prefix_len

            # Calculate suffix_len: (Symmetric to prefix_len)
            # If the entire right segment is one repeating char and it matches
            # the end of the left segment, the suffix can extend.
            if right_node.suffix_len == right_node.total_len and left_node.right_char == right_node.left_char:
                res.suffix_len = right_node.total_len + left_node.suffix_len
            else:
                res.suffix_len = right_node.suffix_len
            
            return res

        def build(v: int, tl: int, tr: int):
            """
            Builds the segment tree recursively.
            v: current node index in tree array
            tl, tr: current segment range [tl, tr]
            """
            if tl == tr: # Leaf node
                char = s_list[tl]
                tree[v] = Node(1, char, char, 1, 1, 1)
            else:
                tm = (tl + tr) // 2
                build(2 * v, tl, tm) # Build left child
                build(2 * v + 1, tm + 1, tr) # Build right child
                tree[v] = merge(tree[2 * v], tree[2 * v + 1]) # Merge children

        def update(v: int, tl: int, tr: int, pos: int, new_char: str):
            """
            Updates a character at a specific position and propagates changes up the tree.
            v: current node index
            tl, tr: current segment range [tl, tr]
            pos: index to update
            new_char: new character value
            """
            if tl == tr: # Leaf node found
                s_list[pos] = new_char # Update the actual string list
                tree[v] = Node(1, new_char, new_char, 1, 1, 1)
            else:
                tm = (tl + tr) // 2
                if pos <= tm: # Update in left child
                    update(2 * v, tl, tm, pos, new_char)
                else: # Update in right child
                    update(2 * v + 1, tm + 1, tr, pos, new_char)
                tree[v] = merge(tree[2 * v], tree[2 * v + 1]) # Re-merge parent

        # 1. Build the initial segment tree
        build(1, 0, n - 1)

        # 2. Process queries
        results = []
        for i in range(len(queryCharacters)):
            pos = queryIndices[i]
            char = queryCharacters[i]
            update(1, 0, n - 1, pos, char)
            results.append(tree[1].max_len) # The root node (tree[1]) holds the answer for the entire string

        return results

```

## Why This Works
This solution works because the **Segment Tree** efficiently maintains and updates aggregated information about substrings. Each node in the tree stores not just the maximum repeating character substring length (`max_len`), but also critical boundary information (`left_char`, `right_char`, `prefix_len`, `suffix_len`). The carefully designed `merge` function ensures that when two child segments are combined, all possibilities for the longest repeating substring in the parent segment are considered: those fully contained within either child, and crucially, those that **span the boundary** between the children. Point updates are efficient (`O(log N)`) because only the nodes on the path from the updated leaf to the root need to be recomputed. After each update, the root node (`tree[1]`) accurately reflects the `max_len` for the entire string, providing the correct answer in `O(1)` time.

---
<sub>Generated 2026-08-13 03:10 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
