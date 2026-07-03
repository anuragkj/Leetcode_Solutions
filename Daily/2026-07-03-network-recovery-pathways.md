# [3620] Network Recovery Pathways

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-07-03 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/network-recovery-pathways/)

**Topics:** Array, Binary Search, Dynamic Programming, Graph Theory, Topological Sort, Heap (Priority Queue), Shortest Path

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a directed acyclic graph of n nodes numbered from 0 to n − 1. This is represented by a 2D array edges of length m, where edges[i] = [u_i, v_i, cost_i] indicates a one‑way communication from node u_i to node v_i with a recovery cost of cost_i.

Some nodes may be offline. You are given a boolean array online where online[i] = true means node i is online. Nodes 0 and n − 1 are always online.

A path from 0 to n − 1 is valid if:

- All intermediate nodes on the path are online.
	The total recovery cost of all edges on the path does not exceed k.

For each valid path, define its score as the minimum edge‑cost along that path.

Return the maximum path score (i.e., the largest minimum-edge cost) among all valid paths. If no valid path exists, return -1.

Example 1:

Input: edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], online = [true,true,true,true], k = 10

Output: 3

Explanation:

	The graph has two possible routes from node 0 to node 3:

		Path 0 → 1 → 3

			Total cost = 5 + 10 = 15, which exceeds k (15 > 10), so this path is invalid.

		Path 0 → 2 → 3

			Total cost = 3 + 4 = 7 <= k, so this path is valid.

			The minimum edge‐cost along this path is min(3, 4) = 3.

	There are no other valid paths. Hence, the maximum among all valid path‐scores is 3.

Example 2:

Input: edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [true,true,true,false,true], k = 12

Output: 6

Explanation:

	Node 3 is offline, so any path passing through 3 is invalid.

	Consider the remaining routes from 0 to 4:

		Path 0 → 1 → 4

			Total cost = 7 + 5 = 12 <= k, so this path is valid.

			The minimum edge‐cost along this path is min(7, 5) = 5.

		Path 0 → 2 → 3 → 4

			Node 3 is offline, so this path is invalid regardless of cost.

		Path 0 → 2 → 4

			Total cost = 6 + 6 = 12 <= k, so this path is valid.

			The minimum edge‐cost along this path is min(6, 6) = 6.

	Among the two valid paths, their scores are 5 and 6. Therefore, the answer is 6.

Constraints:

	n == online.length
	2 <= n <= 5 * 10^4
	0 <= m == edges.length <= min(10^5, n * (n - 1) / 2)
	edges[i] = [u_i, v_i, cost_i]
	0 <= u_i, v_i < n
	u_i != v_i
	0 <= cost_i <= 10^9
	0 <= k <= 5 * 10^13
	online[i] is either true or false, and both online[0] and online[n − 1] are true.
	The given graph is a directed acyclic graph.

**Examples / sample tests:**

```
[[0,1,5],[1,3,10],[0,2,3],[2,3,4]]
[true,true,true,true]
10
[[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]]
[true,true,true,false,true]
12
```

---

## Problem Summary
We need to find a path from node 0 to node `n-1` in a directed acyclic graph (DAG). This path must only use online intermediate nodes, and its total edge cost cannot exceed `k`. Among all such valid paths, we want to find the one whose minimum edge cost is maximized, and return this maximum "minimum edge cost" (score). If no valid path exists, return -1.

## Intuition
The problem asks us to find the **maximum of minimums**. This is a classic pattern that strongly suggests **binary search on the answer**.

Let's say we want to check if it's possible to achieve a path score of *at least* `X`. This means we are looking for a path from node 0 to `n-1` where:
1.  Every edge on the path has a cost of **at least `X`**.
2.  All intermediate nodes on the path are online.
3.  The total cost of all edges on the path does not exceed `k`.

If we can efficiently check this condition for any given `X`, we can use binary search to find the largest `X` for which the condition holds.

The `check` function (let's call it `can_achieve(min_score)`) would work as follows:
*   **Filter the graph**: Create a new graph containing only edges whose `cost_i` is greater than or equal to `min_score`.
*   **Handle offline nodes**: The problem states "All intermediate nodes on the path are online." Nodes 0 and `n-1` are always online. This means if a node `v` is an intermediate node (`0 < v < n-1`) and `online[v]` is `false`, no valid path can pass through `v`. We can enforce this by simply ignoring any edges that lead *into* such an offline intermediate node `v`.
*   **Find shortest path**: In this filtered graph (with filtered edges and effectively removed offline intermediate nodes), find the minimum total cost to reach node `n-1` from node 0. Since the original graph is a DAG, we can use **Dynamic Programming (DP)** with **topological sort** (often implemented using Kahn's algorithm / BFS) to find shortest paths efficiently.
*   **Check total cost**: If the minimum total cost to reach `n-1` is less than or equal to `k`, then `min_score` is achievable.

## Approach
The algorithm combines binary search on the answer with a shortest path algorithm on a DAG.

1.  **Binary Search Range**:
    *   The minimum possible edge cost is 0.
    *   The maximum possible edge cost is `10^9` (given in constraints).
    *   So, our binary search range for `min_score` will be `[0, 10^9]`.
    *   Initialize `ans = -1` to handle the case where no valid path exists.

2.  **`can_achieve(min_score)` Function**:
    This function determines if there's a path from 0 to `n-1` where all edges have cost `>= min_score`, all intermediate nodes are online, and the total path cost is `<= k`.
    *   **Graph Construction**:
        *   Create an adjacency list `adj` and an `in_degree` array for `n` nodes.
        *   Iterate through all given `edges = [u, v, cost]`:
            *   If `cost < min_score`, **skip this edge**. It doesn't meet our current minimum score requirement.
            *   **Online Node Check**: If `v` is an intermediate node (`0 < v < n-1`) and `online[v]` is `false`, **skip this edge**. This node `v` cannot be part of a valid path, so no edge should lead to it.
            *   Otherwise, add `(v, cost)` to `adj[u]` and increment `in_degree[v]`.
    *   **DAG Shortest Path (Topological Sort + DP)**:
        *   Initialize `dist = [infinity] * n`, where `dist[i]` will store the minimum total cost to reach node `i` from node 0.
        *   Set `dist[0] = 0`.
        *   Initialize a queue `q` with all nodes `i` that have `in_degree[i] == 0`.
        *   **Process Nodes**: While `q` is not empty:
            *   Dequeue a node `u`.
            *   If `dist[u]` is `infinity`, it means `u` is not reachable from node 0 via any valid path (considering `min_score` and online nodes). Skip to the next node.
            *   For each neighbor `v` of `u` with edge cost `cost_uv` (from `adj[u]`):
                *   **Relaxation**: If `dist[u] + cost_uv < dist[v]`, update `dist[v] = dist[u] + cost_uv`.
                *   Decrement `in_degree[v]`. If `in_degree[v]` becomes 0, enqueue `v`.
    *   **Result**: Return `True` if `dist[n-1] <= k`, otherwise `False`.

3.  **Binary Search Loop**:
    *   `while low <= high`:
        *   `mid = low + (high - low) // 2`
        *   If `can_achieve(mid)` is `True`:
            *   `ans = mid` (we found a possible score, try for a higher one)
            *   `low = mid + 1`
        *   Else (`can_achieve(mid)` is `False`):
            *   `high = mid - 1` (this score is too high, try a lower one)
    *   Return `ans`.

## Visualization
Let's illustrate the `can_achieve(min_score)` function with a simple graph.
Suppose `min_score = 5`, `k = 10`, `n=4`. Node 2 is offline.
Original edges: `(0,1,7), (0,2,3), (1,3,6), (2,3,4)`
`online = [T, T, F, T]`

```mermaid
graph TD
    0((0)) --- 1((1))
    0 --- 2((2))
    1 --- 3((3))
    2 --- 3
    style 2 fill:#fdd,stroke:#333,stroke-width:2px;
    link 0 -- 7 --> 1
    link 0 -- 3 --> 2
    link 1 -- 6 --> 3
    link 2 -- 4 --> 3
```

**Step 1: Filter edges based on `min_score = 5` and `online` status.**
*   `cost >= 5`:
    *   `(0,1,7)`: cost 7 >= 5. Node 1 is online. Keep.
    *   `(0,2,3)`: cost 3 < 5. **Discard**.
    *   `(1,3,6)`: cost 6 >= 5. Node 3 is online. Keep.
    *   `(2,3,4)`: cost 4 < 5. **Discard**.
*   **Intermediate Offline Node Check**: Node 2 is `0 < 2 < 3` and `online[2]` is `false`. Any edge leading to node 2 (like `(0,2,3)`) would be discarded. (In this example, `(0,2,3)` was already discarded by cost filter).

**Resulting Graph for `can_achieve(5)`:**

```mermaid
graph TD
    0((0)) --- 1((1))
    1 --- 3((3))
    link 0 -- 7 --> 1
    link 1 -- 6 --> 3
```

**Step 2: DAG Shortest Path (Topological Sort + DP)**
*   `dist = [0, inf, inf, inf]`
*   `in_degree = [0, 1, 0, 1]` (for nodes 0, 1, 2, 3 respectively, based on filtered graph)
*   `q = deque([0])`

1.  **Pop 0**: `dist[0]=0`.
    *   Edge `(0,1,7)`: `dist[1] = min(inf, dist[0]+7) = 7`. `in_degree[1]` becomes 0. `q.append(1)`.
    `q = deque([1])`
2.  **Pop 1**: `dist[1]=7`.
    *   Edge `(1,3,6)`: `dist[3] = min(inf, dist[1]+6) = 7+6 = 13`. `in_degree[3]` becomes 0. `q.append(3)`.
    `q = deque([3])`
3.  **Pop 3**: `dist[3]=13`. No outgoing edges.
    `q = deque([])`

**Step 3: Check total cost**:
*   `dist[n-1] = dist[3] = 13`.
*   Is `13 <= k (10)`? No.
*   So, `can_achieve(5)` returns `False`.

## Dry Run
Let's walk through **Example 1**:
`edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]]`
`online = [true,true,true,true]` (all nodes online)
`k = 10`
`n = 4`

Binary search range for `min_score`: `low = 0`, `high = 10` (max edge cost), `ans = -1`.

| Iteration | `low` | `high` | `mid` | `can_achieve(mid)`? | `dist[3]` | `dist[3] <= k`? | `ans` | Action |
| :-------- | :---- | :----- | :---- | :------------------ | :-------- | :-------------- | :---- | :----- |
| 1         | 0     | 10     | 5     |                     |           |                 | -1    | `mid = 5`. Call `can_achieve(5)`: |
|           |       |        |       | Edges `>=5`: `(0,1,5), (1,3,10)`. Graph: `0 -> 1 -> 3`. |           |                 |       | `dist[0]=0`. `dist[1]=5`. `dist[3]=15`. |
|           |       |        |       | `False`             | 15        | `15 <= 10`? No  | -1    | `high = 4` |
| 2         | 0     | 4      | 2     |                     |           |                 | -1    | `mid = 2`. Call `can_achieve(2)`: |
|           |       |        |       | Edges `>=2`: All edges. Graph: `0 -> 1 -> 3`, `0 -> 2 -> 3`. |           |                 |       | `dist[0]=0`. `dist[1]=5`. `dist[2]=3`. `dist[3]=min(5+10, 3+4)=7`. |
|           |       |        |       | `True`              | 7         | `7 <= 10`? Yes  | 2     | `low = 3`  |
| 3         | 3     | 4      | 3     |                     |           |                 | 2     | `mid = 3`. Call `can_achieve(3)`: |
|           |       |        |       | Edges `>=3`: All edges. Graph: `0 -> 1 -> 3`, `0 -> 2 -> 3`. |           |                 |       | `dist[0]=0`. `dist[1]=5`. `dist[2]=3`. `dist[3]=min(5+10, 3+4)=7`. |
|           |       |        |       | `True`              | 7         | `7 <= 10`? Yes  | 3     | `low = 4`  |
| 4         | 4     | 4      | 4     |                     |           |                 | 3     | `mid = 4`. Call `can_achieve(4)`: |
|           |       |        |       | Edges `>=4`: `(0,1,5), (1,3,10), (2,3,4)`. Edge `(0,2,3)` removed. Graph: `0 -> 1 -> 3`, `2 -> 3`. Node 2 not reachable from 0. |           |                 |       | `dist[0]=0`. `dist[1]=5`. `dist[3]=15`. |
|           |       |        |       | `False`             | 15        | `15 <= 10`? No  | 3     | `high = 3` |
| End       | 4     | 3      |       |                     |           |                 | 3     | Loop terminates (`low > high`). |

Final result: `ans = 3`. This matches Example 1.

## Complexity
*   **Time Complexity**: `O((N + M) * log(MAX_COST))`
    *   The binary search performs `log(MAX_COST)` iterations. `MAX_COST` is `10^9`, so `log(10^9)` is approximately 30.
    *   Inside `can_achieve`:
        *   Building the filtered graph (adjacency list and in-degrees) takes `O(M)` time.
        *   The topological sort (BFS-based) and shortest path calculation takes `O(N + M)` time, as each node and edge is processed at most once.
    *   Total time: `O((N + M) * log(MAX_COST))`. Given `N=5*10^4`, `M=10^5`, this is roughly `(5*10^4 + 10^5) * 30 = 1.5 * 10^5 * 30 = 4.5 * 10^6` operations, which is efficient enough for the given constraints.
*   **Space Complexity**: `O(N + M)`
    *   The adjacency list `adj` stores `M` edges and `N` lists.
    *   The `in_degree` array, `dist` array, and queue `q` all take `O(N)` space.
    *   Total space: `O(N + M)`.

## Edge Cases
*   **No valid path**: If `dist[n-1]` remains `math.inf` in `can_achieve`, or if `can_achieve(0)` (the most permissive check) returns `False`, the binary search will eventually result in `ans = -1`, which is the correct output.
*   **`k = 0`**: The solution correctly handles this. Only paths with a total cost of 0 will be considered valid.
*   **Graph with only `0 -> n-1` edge**: The `can_achieve` function will correctly identify this path if its cost meets `min_score` and `k`.
*   **All intermediate nodes offline**: If `n > 2` and all nodes `1` to `n-2` are offline, `can_achieve` will only consider paths that directly go `0 -> n-1` (if such an edge exists and is valid).
*   **Large `k` values**: `k` can be up to `5 * 10^13`. Python's integers handle arbitrary size, so `dist` values will not overflow. `math.inf` is also suitable.
*   **All edges have the same cost**: The binary search still works correctly, narrowing down to that cost or -1.

## Solution

```python
import collections
import math
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        # Binary search for the maximum possible minimum edge cost (the "score").
        # The score can range from 0 (minimum possible cost_i) to 10^9 (maximum possible cost_i).
        low = 0
        high = 10**9 # Max possible cost_i as per constraints
        ans = -1 # Default return value if no valid path is found
        
        # Helper function to check if a path with minimum edge cost of at least `min_score` exists
        # and its total cost does not exceed `k`.
        def can_achieve(min_score: int) -> bool:
            # Build an adjacency list for the graph, considering only edges with cost >= min_score
            # and filtering out paths through offline intermediate nodes.
            adj = [[] for _ in range(n)]
            in_degree = [0] * n
            
            for u, v, cost in edges:
                if cost >= min_score:
                    # Constraint: "All intermediate nodes on the path are online."
                    # Nodes 0 and n-1 are always online.
                    # If 'v' is an intermediate node (0 < v < n-1) and is offline (`online[v]` is false),
                    # then no valid path can pass through 'v'.
                    # Therefore, we should not consider edges leading to such 'v'.
                    if 0 < v < n - 1 and not online[v]:
                        continue
                    
                    adj[u].append((v, cost))
                    in_degree[v] += 1
            
            # Use dynamic programming (shortest path in a DAG) with topological sort (Kahn's algorithm).
            # dist[i] will store the minimum total cost to reach node 'i' from node 0.
            dist = [math.inf] * n
            dist[0] = 0 # Starting node 0 has a cost of 0 to reach itself
            
            q = collections.deque()
            
            # Initialize queue with nodes having an in-degree of 0.
            # These are potential starting points for paths in the filtered graph.
            for i in range(n):
                if in_degree[i] == 0:
                    q.append(i)
            
            # Process nodes in topological order
            while q:
                u = q.popleft()
                
                # If node 'u' is not reachable from node 0 (or only reachable via invalid paths),
                # we cannot use it to extend paths.
                if dist[u] == math.inf:
                    continue
                
                # We have already filtered out edges leading to intermediate offline nodes during graph construction.
                # So, if dist[u] is not infinity, 'u' itself is a valid node to be on a path.
                
                for v, cost_uv in adj[u]:
                    # Relax edge (u, v): update dist[v] if a shorter path through u is found
                    if dist[u] + cost_uv < dist[v]:
                        dist[v] = dist[u] + cost_uv
                    
                    # Decrement in-degree of v. If it becomes 0, v is ready to be processed.
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        q.append(v)
            
            # A valid path exists if node n-1 is reachable and its total cost is within k.
            return dist[n-1] <= k

        # Binary search loop to find the maximum achievable min_score
        while low <= high:
            mid = low + (high - low) // 2
            if can_achieve(mid):
                ans = mid       # 'mid' is achievable, so we try for a higher score
                low = mid + 1
            else:
                high = mid - 1  # 'mid' is not achievable, so we try for a lower score
                
        return ans

```

## Why This Works
The core idea is that the problem exhibits **monotonicity**, which is the prerequisite for binary search. If we can find a valid path with a minimum edge cost of `X`, we can certainly find a valid path with any minimum edge cost `Y < X`. This is because if we filter the graph to only include edges with cost `>= X`, this filtered graph is a subset of the graph filtered for edges with cost `>= Y`. If a path exists in the `X`-filtered graph, it also exists in the `Y`-filtered graph, and its total cost and minimum edge cost remain the same.

The `can_achieve(min_score)` function correctly verifies if a given `min_score` is possible by:
1.  **Filtering edges by cost**: It only considers edges whose costs are at least `min_score`, directly enforcing the "minimum edge-cost along that path" condition.
2.  **Filtering by online status**: By ignoring edges leading to intermediate offline nodes, it ensures that "All intermediate nodes on the path are online."
3.  **Shortest Path in DAG**: It uses a standard and efficient algorithm (topological sort with DP) to find the minimum total cost path in this carefully constructed, valid subgraph.
4.  **Total Cost Constraint**: Finally, it checks if this minimum total cost path satisfies the `k` limit.

By binary searching over the possible range of `min_score` and using this `can_achieve` function, we efficiently find the largest `min_score` that satisfies all conditions.

---
<sub>Generated 2026-07-03 04:28 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
