# [3841] Palindromic Path Queries in a Tree

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-10-29 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/palindromic-path-queries-in-a-tree/)

**Topics:** Array, String, Divide and Conquer, Bit Manipulation, Tree, Depth-First Search, Binary Indexed Tree, Segment Tree

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an undirected tree with n nodes labeled 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [u_i, v_i] indicates an undirected edge between nodes u_i and v_i.

You are also given a string s of length n consisting of lowercase English letters, where s[i] represents the character assigned to node i.

You are also given a string array queries, where each queries[i] is either:

- "update u_i c": Change the character at node u_i to c. Formally, update s[u_i] = c.

- "query u_i v_i": Determine whether the string formed by the characters on the unique path from u_i to v_i (inclusive) can be rearranged into a palindrome.

Return a boolean array answer, where answer[j] is true if the j^th query of type "query u_i v_i"​​​​​​​ can be rearranged into a palindrome, and false otherwise.

Example 1:

Input: n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]

Output: [true,false]

Explanation:

- "query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.

- "update 1 b": Update node 1 to 'b', now s = "abc".

- "query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.

Thus, answer = [true, false].

Example 2:

Input: n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]

Output: [false,false,true]

Explanation:

- "query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form a palindrome. Thus, answer[0] = false.

- "update 0 b": Update node 0 to 'b', now s = "bbca".

- "query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.

- "update 3 a": Update node 3 to 'a', s = "bbca".

- "query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form "bab", a palindrome. Thus, answer[2] = true.

Thus, answer = [false, false, true].

Constraints:

- 1 <= n == s.length <= 5 * 10^4

- edges.length == n - 1

- edges[i] = [u_i, v_i]

- 0 <= u_i, v_i <= n - 1

- s consists of lowercase English letters.

- The input is generated such that edges represents a valid tree.

- 1 <= queries.length <= 5 * 10^4​​​​​​​

- queries[i] = "update u_i c" or

- queries[i] = "query u_i v_i"

- 0 <= u_i, v_i <= n - 1

- c is a lowercase English letter.

**Examples / sample tests:**

```
3
[[0,1],[1,2]]
"aac"
["query 0 2","update 1 b","query 0 2"]
4
[[0,1],[0,2],[0,3]]
"abca"
["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]
```

---

## Problem Summary

Given an undirected tree of $n$ nodes where each node contains a lowercase letter, handle two types of queries:
1. **Update**: Change the character at node $u$.
2. **Query**: Determine if the characters along the unique simple path between nodes $u$ and $v$ can be rearranged to form a palindrome.

---

## Intuition

A string can be rearranged into a palindrome if and only if **at most one character has an odd frequency**.

Since there are only 26 lowercase English letters, we can represent the character frequencies as a **26-bit bitmask**, where bit $k$ is $1$ if letter $k$ appears an odd number of times, and $0$ if it appears an even number of times.

Because each node on the path between $u$ and $v$ is visited exactly once, the path parity mask is the **XOR sum** of the bitmasks of all nodes on that path. 

Crucially, XOR is self-inverting ($x \oplus x = 0$). If $P(x)$ is the XOR sum from the root to node $x$:
$$\text{PathXOR}(u, v) = P(u) \oplus P(v) \oplus \text{val}(\text{LCA}(u, v))$$
All common ancestors above $\text{LCA}(u, v)$ cancel out completely, and $\text{LCA}(u, v)$ (which gets cancelled by $P(u) \oplus P(v)$) is XORed back in once.

When a node $u$'s character changes by $\Delta = \text{mask}_{\text{new}} \oplus \text{mask}_{\text{old}}$, $P(x)$ changes by $\Delta$ for every node $x$ in $u$'s subtree. In a DFS entry/exit order, a subtree is a contiguous range $[tin[u], tout[u]]$. 

Thus:
- **Subtree update**: Range XOR update on $[tin[u], tout[u]]$.
- **Path query**: Point queries of $P(u)$ and $P(v)$, plus $\text{LCA}(u, v)$.
A standard **Binary Indexed Tree (Fenwick Tree)** easily supports range XOR updates and point queries in $O(\log n)$.

---

## Approach

1. **Tree Flattening & LCA Precomputation**:
   - Run an iterative DFS/BFS to compute node depths and binary lifting tables `up[k][u]` for $O(\log n)$ LCA queries.
   - Record discovery intervals $[tin[u], tout[u]]$ for each node's subtree.
2. **Fenwick Tree Initialization**:
   - Maintain a Binary Indexed Tree over indices $1 \dots n$ supporting range updates and point queries via a difference array.
   - For each node $u$, range-update $[tin[u], tout[u]]$ with $1 \ll (\text{ord}(s[u]) - \text{ord}(\text{'a'}))$.
3. **Processing Queries**:
   - **`update u c`**:
     - Compute $\Delta = (1 \ll (c - \text{'a'})) \oplus (1 \ll (s[u] - \text{'a'}))$.
     - Range-update $[tin[u], tout[u]]$ with $\Delta$ in the BIT.
     - Update $s[u] = c$.
   - **`query u v`**:
     - Query $P(u)$ and $P(v)$ via prefix XOR in the BIT.
     - Find $l = \text{LCA}(u, v)$.
     - Path mask is $M = P(u) \oplus P(v) \oplus (1 \ll (s[l] - \text{'a'}))$.
     - Path forms a palindrome $\iff M \ \& \ (M - 1) == 0$ (at most one bit set).

---

## Visualization

```
Tree:                  DFS Order / Array intervals:
     0 ('a')           node 0: [1, 3]
    /                  node 1: [2, 3]
   1 ('a')             node 2: [3, 3]
  /
 2 ('c')

Path 0 -> 2:
  P(2) = val(0) ^ val(1) ^ val(2)
  P(0) = val(0)
  LCA(0, 2) = 0
  PathXOR = P(0) ^ P(2) ^ val(0)
          = val(0) ^ val(1) ^ val(2)
          = 'a' ^ 'a' ^ 'c' = 'c' (mask has 1 bit set -> True)
```

---

## Dry Run

### Example 1: `n = 3, edges = [[0,1],[1,2]], s = "aac"`
- Character masks: $0 \to \text{'a'} (1)$, $1 \to \text{'a'} (1)$, $2 \to \text{'c'} (4)$.
- Root-to-node XOR values initially: $P(0) = 1$, $P(1) = 0$, $P(2) = 4$.

| Operation | Target / Nodes | Computation | State / Output |
| :--- | :--- | :--- | :--- |
| `query 0 2` | $u=0, v=2, \text{LCA}=0$ | $P(0) \oplus P(2) \oplus \text{val}(0) = 1 \oplus 4 \oplus 1 = 4$ | $4 \ \& \ 3 == 0 \implies$ **`true`** |
| `update 1 b`| $u=1, c=\text{'b'}$ | $\Delta = \text{mask}('a') \oplus \text{mask}('b') = 1 \oplus 2 = 3$. Subtree of 1 is $\{1, 2\}$. | $P(1) \to 3, P(2) \to 7$ |
| `query 0 2` | $u=0, v=2, \text{LCA}=0$ | $P(0) \oplus P(2) \oplus \text{val}(0) = 1 \oplus 7 \oplus 1 = 7$ | $7 \ \& \ 6 = 6 \neq 0 \implies$ **`false`** |

Final result: `[true, false]`.

---

## Complexity

- **Time Complexity**: $O((n + q) \log n)$ — Precomputing LCA and DFS order takes $O(n \log n)$. Each update takes $O(\log n)$ (two BIT point updates). Each query takes $O(\log n)$ (LCA via binary lifting and two BIT prefix queries).
- **Space Complexity**: $O(n \log n)$ — Storing the tree adjacency list, DFS intervals, Fenwick tree, and the binary lifting table $\text{up}[\log n][n]$.

---

## Edge Cases

- **$u = v$ (Path of length 1)**: $P(u) \oplus P(u) \oplus \text{val}(u) = \text{val}(u)$, which has exactly 1 bit set $\to$ always `True`.
- **$n = 1$**: Handled properly; tree has 0 edges and depth 0, queries on single node work seamlessly.
- **Deep / Skewed Trees**: Implemented using an iterative DFS to prevent Python's `RecursionError`.

---

## Solution

```python
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Iterative DFS to compute depths, parent, tin, tout
        LOG = (n).bit_length() + 1
        up = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n

        timer = 0
        visited = [False] * n
        stack = [(0, 0, False)]  # (u, p, processed)

        while stack:
            u, p, processed = stack.pop()
            if not processed:
                visited[u] = True
                up[0][u] = p
                timer += 1
                tin[u] = timer
                stack.append((u, p, True))
                for v in adj[u]:
                    if v != p and not visited[v]:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, False))
            else:
                tout[u] = timer

        # Binary lifting table for LCA
        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]

        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if (diff >> k) & 1:
                    u = up[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]
            return up[0][u]

        # Fenwick Tree (Binary Indexed Tree) for range XOR update, point query
        # Difference array size is n + 2
        bit = [0] * (n + 2)

        def bit_add(idx: int, val: int):
            while idx <= n + 1:
                bit[idx] ^= val
                idx += idx & (-idx)

        def bit_query(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res

        def range_update(l: int, r: int, val: int):
            bit_add(l, val)
            bit_add(r + 1, val)

        # Initialize BIT with initial characters
        chars = [ord(c) - ord('a') for c in s]
        for i in range(n):
            mask = 1 << chars[i]
            range_update(tin[i], tout[i], mask)

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_c = ord(parts[2]) - ord('a')
                old_c = chars[u]
                if new_c != old_c:
                    delta = (1 << new_c) ^ (1 << old_c)
                    range_update(tin[u], tout[u], delta)
                    chars[u] = new_c
            else:
                u = int(parts[1])
                v = int(parts[2])
                p_u = bit_query(tin[u])
                p_v = bit_query(tin[v])
                lca = get_lca(u, v)
                val_lca = 1 << chars[lca]
                path_mask = p_u ^ p_v ^ val_lca
                # Path forms a palindrome if at most one bit is set
                ans.append((path_mask & (path_mask - 1)) == 0)

        return ans
```

---

## Why This Works

The simple path between $u$ and $v$ decomposes into the path from $\text{LCA}(u, v)$ to $u$ and the path from $\text{LCA}(u, v)$ to $v$. In the sum $P(u) \oplus P(v)$, every node on the path from root to $\text{LCA}(u, v)$ is traversed twice and thus cancels out under XOR ($x \oplus x = 0$). Adding back $\text{val}(\text{LCA}(u, v))$ accounts for the vertex at the junction exactly once, leaving the exact parity bitmask of the tree path. Since a change at node $u$ affects the root paths of precisely the nodes in $u$'s subtree, subtree updates via a difference Fenwick tree maintain these root-to-node XOR values in $O(\log n)$ time.

---
<sub>Generated 2026-10-29 06:21 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
