# [3532] Path Existence Queries in a Graph I

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-07-09 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/path-existence-queries-in-a-graph-i/)

**Topics:** Array, Hash Table, Binary Search, Union-Find, Graph Theory

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.

You are also given an integer array nums of length n sorted in non-decreasing order, and an integer maxDiff.

An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).

You are also given a 2D integer array queries. For each queries[i] = [u_i, v_i], determine whether there exists a path between nodes u_i and v_i.

Return a boolean array answer, where answer[i] is true if there exists a path between u_i and v_i in the i^th query and false otherwise.

Example 1:

Input: n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]

Output: [true,false]

Explanation:

- Query [0,0]: Node 0 has a trivial path to itself.

- Query [0,1]: There is no edge between Node 0 and Node 1 because |nums[0] - nums[1]| = |1 - 3| = 2, which is greater than maxDiff.

- Thus, the final answer after processing all the queries is [true, false].

Example 2:

Input: n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]

Output: [false,false,true,true]

Explanation:

The resulting graph is:

- Query [0,1]: There is no edge between Node 0 and Node 1 because |nums[0] - nums[1]| = |2 - 5| = 3, which is greater than maxDiff.

- Query [0,2]: There is no edge between Node 0 and Node 2 because |nums[0] - nums[2]| = |2 - 6| = 4, which is greater than maxDiff.

- Query [1,3]: There is a path between Node 1 and Node 3 through Node 2 since |nums[1] - nums[2]| = |5 - 6| = 1 and |nums[2] - nums[3]| = |6 - 8| = 2, both of which are within maxDiff.

- Query [2,3]: There is an edge between Node 2 and Node 3 because |nums[2] - nums[3]| = |6 - 8| = 2, which is equal to maxDiff.

- Thus, the final answer after processing all the queries is [false, false, true, true].

Constraints:

- 1 <= n == nums.length <= 10^5

- 0 <= nums[i] <= 10^5

- nums is sorted in non-decreasing order.

- 0 <= maxDiff <= 10^5

- 1 <= queries.length <= 10^5

- queries[i] == [u_i, v_i]

- 0 <= u_i, v_i < n

**Examples / sample tests:**

```
2
[1,3]
1
[[0,0],[0,1]]
4
[2,5,6,8]
2
[[0,1],[0,2],[1,3],[2,3]]
```

---

## Problem Summary
We're given `n` nodes, each with a value `nums[i]`. An undirected edge exists between nodes `i` and `j` if `|nums[i] - nums[j]| <= maxDiff`. We need to answer multiple queries, each asking if a path exists between two given nodes `u` and `v`.

## Intuition
The problem asks for path existence in a graph, which is a classic application of **Connected Components**. If two nodes `u` and `v` are in the same connected component, a path exists between them. Otherwise, it doesn't. The challenge is that the graph isn't given explicitly; we have to deduce its edges.

The `nums` array is **sorted in non-decreasing order**. This is a crucial piece of information. If `nums[i]` and `nums[j]` are connected (meaning `|nums[i] - nums[j]| <= maxDiff`), and `i < k < j`, then `nums[i] <= nums[k] <= nums[j]`. This implies that `nums[k]` is also "close" to both `nums[i]` and `nums[j]`. Specifically, `nums[k] - nums[i] <= nums[j] - nums[i] <= maxDiff` and `nums[j] - nums[k] <= nums[j] - nums[i] <= maxDiff`. This means node `k` is connected to both `i` and `j`.

This property is powerful: if two nodes `i` and `j` are in the same connected component, then **all nodes with indices between `i` and `j` are also in that same component**. This means connected components in this graph are always **contiguous segments of indices** (e.g., nodes `[L, L+1, ..., R]`).

Therefore, to find all connected components, we only need to check for edges between **adjacent nodes** `i` and `i+1`. If `|nums[i+1] - nums[i]| <= maxDiff`, we connect `i` and `i+1`. By transitivity, this will correctly group all nodes within a contiguous segment. A **Union-Find** data structure is perfect for efficiently managing and querying these connected components.

## Approach
1.  **Initialize Union-Find:** Create a Union-Find data structure for `n` nodes. Each node `i` initially belongs to its own component (its parent is itself).
2.  **Build Connected Components:**
    *   Iterate `i` from `0` to `n-2` (checking all adjacent pairs of nodes).
    *   For each pair `(i, i+1)`, calculate the absolute difference `|nums[i+1] - nums[i]|`. Since `nums` is sorted, this simplifies to `nums[i+1] - nums[i]`.
    *   If `nums[i+1] - nums[i] <= maxDiff`, it means an edge exists between `i` and `i+1`. Use the `union` operation of the Union-Find structure to merge the components of `i` and `i+1`.
3.  **Process Queries:**
    *   Initialize an empty list `answer` to store the boolean results.
    *   For each query `[u, v]` in `queries`:
        *   Use the `find` operation of the Union-Find structure to determine the representative (root) of the component containing `u` and the representative of the component containing `v`.
        *   If `find(u) == find(v)`, it means `u` and `v` are in the same connected component, so a path exists. Append `true` to `answer`.
        *   Otherwise, they are in different components, and no path exists. Append `false` to `answer`.
4.  **Return `answer`**.

## Visualization

Let's illustrate the Union-Find process for `nums = [2,5,6,8]`, `maxDiff = 2`.

**Initial State (Union-Find `parent` array):**
Each node is its own parent.
```
Nodes:   0   1   2   3
nums:    2   5   6   8
parent: [0,  1,  2,  3]
```

**Step 1: Check (0, 1)**
`nums[1] - nums[0] = 5 - 2 = 3`.
`3 > maxDiff (2)`. No edge. No union.
`parent: [0, 1, 2, 3]`

**Step 2: Check (1, 2)**
`nums[2] - nums[1] = 6 - 5 = 1`.
`1 <= maxDiff (2)`. Edge exists. `union(1, 2)`.
Let's say `union` makes the root of `1` point to the root of `2`.
`find(1)` is `1`. `find(2)` is `2`.
`parent[1] = 2`.
```
Nodes:   0   1   2   3
nums:    2   5   6   8
parent: [0,  2,  2,  3]  <-- Node 1 now points to Node 2
```
Connected components: `{0}`, `{1,2}`, `{3}`

**Step 3: Check (2, 3)**
`nums[3] - nums[2] = 8 - 6 = 2`.
`2 <= maxDiff (2)`. Edge exists. `union(2, 3)`.
`find(2)` is `2`. `find(3)` is `3`.
`parent[2] = 3`.
```
Nodes:   0   1   2   3
nums:    2   5   6   8
parent: [0,  2,  3,  3]  <-- Node 2 now points to Node 3
```
After path compression on subsequent `find` calls, `parent[1]` would eventually point to `3` as well.
Final effective components: `{0}`, `{1,2,3}`.

## Dry Run
Let's use Example 1: `n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]`

**1. Initialize Union-Find:**
`uf.parent = [0, 1]`

**2. Build Connected Components:**
| `i` | `i+1` | `nums[i]` | `nums[i+1]` | `nums[i+1]-nums[i]` | `maxDiff` | Condition `(diff <= maxDiff)` | Action | `uf.parent` (after action) |
| :-- | :---- | :-------- | :---------- | :------------------ | :-------- | :-------------------------- | :----- | :-------------------------- |
| 0   | 1     | 1         | 3           | 2                   | 1         | `2 <= 1` is `False`         | No union | `[0, 1]`                    |

**3. Process Queries:**
`answer = []`

| Query `[u,v]` | `find(u)` | `find(v)` | `find(u) == find(v)` | `answer` |
| :------------ | :-------- | :-------- | :------------------ | :------- |
| `[0,0]`       | `0`       | `0`       | `True`              | `[True]` |
| `[0,1]`       | `0`       | `1`       | `False`             | `[True, False]` |

**Final Result:** `[True, False]` (Matches Example 1 Output)

## Complexity
*   **Time Complexity:** `O((N + Q) * α(N))`
    *   `N` is the number of nodes, `Q` is the number of queries.
    *   Initializing Union-Find: `O(N)`.
    *   Building components: We iterate `N-1` times. Each `union` operation with path compression (and optionally union by rank/size) takes nearly constant amortized time, specifically `O(α(N))`, where `α` is the inverse Ackermann function, which grows extremely slowly (effectively constant for practical `N`). So, `O(N * α(N))`.
    *   Processing queries: We iterate `Q` times. Each `find` operation takes `O(α(N))` amortized time. So, `O(Q * α(N))`.
    *   Total: `O(N + Q)` effectively.
*   **Space Complexity:** `O(N + Q)`
    *   Union-Find `parent` array: `O(N)`.
    *   `answer` array: `O(Q)`.

## Edge Cases
*   **`n = 1`**: The loop for building components (`range(n-1)`) will not run. `uf.parent` remains `[0]`. A query `[0,0]` will correctly return `true`.
*   **`maxDiff = 0`**: Only nodes with identical adjacent `nums` values will be connected.
*   **`maxDiff` is very large**: All `nums[i+1] - nums[i]` will likely be `<= maxDiff`, connecting all nodes into a single component.
*   **All `nums[i]` are the same**: All nodes will be connected into a single component.
*   **All `nums[i]` are vastly different**: Few or no adjacent nodes will connect, resulting in many small components (possibly `n` individual components).
*   **Query `[u,u]`**: A node always has a path to itself. `uf.find(u) == uf.find(u)` will always be true, correctly handling this.

## Solution

```python
from typing import List

# Helper class for Union-Find data structure
class UnionFind:
    def __init__(self, n):
        # Initialize each node as its own parent
        self.parent = list(range(n))
        # Optional: self.rank = [0] * n for union by rank optimization
        # For competitive programming, path compression alone is often sufficient
        # and simpler to implement.

    def find(self, i):
        # If i is the root of its component, return i
        if self.parent[i] == i:
            return i
        # Path compression: set parent[i] directly to the root
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        # Find the roots of the components containing i and j
        root_i = self.find(i)
        root_j = self.find(j)

        # If they are already in the same component, do nothing
        if root_i != root_j:
            # Attach the root of one component to the root of the other
            # (Simple union, without rank/size optimization)
            self.parent[root_i] = root_j
            return True # Indicates a successful union
        return False # Indicates i and j were already connected


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        # Initialize Union-Find structure for 'n' nodes
        uf = UnionFind(n)
        
        # Build connected components based on the edge condition
        # The key insight here, due to 'nums' being sorted, is that
        # if nodes 'i' and 'j' are in the same component, then all nodes 'k'
        # with indices between 'i' and 'j' are also in that component.
        # This means connected components are contiguous segments of indices.
        # Therefore, we only need to check connectivity between adjacent nodes.
        for i in range(n - 1):
            # Since nums is sorted, |nums[i] - nums[i+1]| is simply nums[i+1] - nums[i].
            if nums[i+1] - nums[i] <= maxDiff:
                # If adjacent nodes satisfy the condition, union their components
                uf.union(i, i+1)
        
        # Process all queries
        answer = []
        for u, v in queries:
            # Check if nodes u and v belong to the same connected component
            # by comparing their root parents
            answer.append(uf.find(u) == uf.find(v))
            
        return answer

```

## Why This Works
The solution works because the sorted nature of the `nums` array imposes a specific structure on the graph's connected components. If nodes `i` and `j` are connected (meaning `|nums[i] - nums[j]| <= maxDiff`), and `i < k < j`, then `nums[i] <= nums[k] <= nums[j]`. This implies that `nums[k]` is also within `maxDiff` of both `nums[i]` and `nums[j]`. Therefore, `k` is connected to `i` and `k` is connected to `j`. This property ensures that if any two nodes `i` and `j` are in the same connected component, then all nodes with indices between `i` and `j` are also part of that same component. Consequently, connected components are always contiguous segments of indices. By only performing `union` operations between adjacent nodes `i` and `i+1` when `nums[i+1] - nums[i] <= maxDiff`, we correctly identify and merge these contiguous segments, forming all true connected components. The Union-Find data structure then efficiently answers path existence queries by checking if two nodes belong to the same component.

---
<sub>Generated 2026-07-09 04:34 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
