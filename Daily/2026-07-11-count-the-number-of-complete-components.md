# [2685] Count the Number of Complete Components

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-07-11 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/count-the-number-of-complete-components/)

**Topics:** Depth-First Search, Breadth-First Search, Union-Find, Graph Theory

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [a_i, b_i] denotes that there exists an undirected edge connecting vertices a_i and b_i.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

Example 1:

Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.

Example 2:

Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.

Constraints:

- 1 <= n <= 50

- 0 <= edges.length <= n * (n - 1) / 2

- edges[i].length == 2

- 0 <= a_i, b_i <= n - 1

- a_i != b_i

- There are no repeated edges.

**Examples / sample tests:**

```
6
[[0,1],[0,2],[1,2],[3,4]]
6
[[0,1],[0,2],[1,2],[3,4],[3,5]]
```

---

## Problem Summary
This problem asks us to count how many "complete connected components" exist in a given undirected graph. A **connected component** is a subgraph where all vertices are reachable from each other. A connected component is **complete** if every pair of distinct vertices within that component is connected by an edge.

## Intuition
The problem has two main parts:
1.  **Identify connected components**: This is a standard graph traversal problem. We can use either **Depth-First Search (DFS)** or **Breadth-First Search (BFS)** to find all vertices belonging to a single connected component. We'll need a way to keep track of visited vertices to ensure we process each component exactly once.
2.  **Check if a component is complete**: Once we've identified all vertices in a connected component, say it has `m` vertices. A complete graph with `m` vertices (also known as a **clique** or `K_m`) has a very specific number of edges. Each of the `m` vertices is connected to `m-1` other vertices. If we sum `m * (m-1)`, we've counted each edge twice (once for `u` to `v`, and once for `v` to `u`). Therefore, a complete graph with `m` vertices has exactly `m * (m-1) / 2` edges.
    So, for each connected component, we just need to count its number of vertices (`m`) and its number of edges (`e`). If `e` equals `m * (m-1) / 2`, then the component is complete.

## Approach
The optimal approach involves iterating through all vertices, and for each unvisited vertex, initiating a graph traversal (DFS or BFS) to find its entire connected component. During this traversal, we'll simultaneously count the nodes and edges within that component.

Here are the concrete steps:

1.  **Build Adjacency List**: First, convert the `edges` list into an **adjacency list** representation of the graph. This makes it easy to find neighbors of any vertex. `adj[u]` will store a list of vertices connected to `u`.
2.  **Initialize `visited` array**: Create a boolean array `visited` of size `n`, initialized to `False`. This helps track which vertices have already been processed as part of a component.
3.  **Initialize `complete_components_count`**: This variable will store our final answer, initialized to `0`.
4.  **Iterate through vertices**: Loop from `i = 0` to `n - 1`.
    *   If `visited[i]` is `False`: This means `i` belongs to a new, unvisited connected component.
        *   **Start Traversal (DFS/BFS)**: Begin a traversal (e.g., DFS using a stack) from vertex `i`.
        *   **Count Nodes and Sum Degrees**: During the traversal, keep track of:
            *   `nodes_in_current_component`: The number of vertices encountered in this component.
            *   `sum_of_degrees_in_current_component`: The sum of degrees of all vertices in this component. For each vertex `u` popped from the stack, increment `nodes_in_current_component` by 1 and add `len(adj[u])` (its degree) to `sum_of_degrees_in_current_component`. Mark `u` as visited.
            *   For each neighbor `v` of `u`: if `v` hasn't been visited, mark it visited and add it to the stack (or queue).
        *   **Calculate Edges**: Once the traversal for the component finishes (stack/queue is empty), calculate the number of edges in this component: `edges_in_current_component = sum_of_degrees_in_current_component // 2`. (Remember, the sum of degrees in any graph is twice the number of edges).
        *   **Check for Completeness**: Calculate the number of edges required for a complete graph with `nodes_in_current_component` vertices: `required_edges = nodes_in_current_component * (nodes_in_current_component - 1) // 2`.
        *   **Increment Count**: If `edges_in_current_component == required_edges`, then this component is complete. Increment `complete_components_count`.
5.  **Return Result**: After iterating through all vertices, `complete_components_count` will hold the total number of complete connected components. Return this value.

## Visualization
Let's visualize the process with an example graph containing three components.

```mermaid
graph TD
    subgraph Component 1 (Complete)
        A --- B
        A --- C
        B --- C
    end
    subgraph Component 2 (Not Complete)
        D --- E
        D --- F
    end
    subgraph Component 3 (Complete)
        G
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:2px
    style E fill:#ccf,stroke:#333,stroke-width:2px
    style F fill:#ccf,stroke:#333,stroke-width:2px
    style G fill:#9f9,stroke:#333,stroke-width:2px

    classDef complete fill:#f9f,stroke:#333,stroke-width:2px;
    classDef incomplete fill:#ccf,stroke:#333,stroke-width:2px;
    classDef single fill:#9f9,stroke:#333,stroke-width:2px;

    class A,B,C complete;
    class D,E,F incomplete;
    class G single;
```
1.  **Component 1 (A, B, C)**:
    *   DFS/BFS starts from A. Discovers B, C.
    *   **Nodes (`m`) = 3**.
    *   **Sum of Degrees**: `deg(A)=2, deg(B)=2, deg(C)=2`. Sum = `2+2+2 = 6`.
    *   **Edges (`e`) = 6 / 2 = 3**.
    *   **Required Edges** for `m=3`: `3 * (3-1) / 2 = 3`.
    *   Since `e == required_edges` (3 == 3), this component is **Complete**. `complete_components_count` becomes 1.

2.  **Component 2 (D, E, F)**:
    *   DFS/BFS starts from D (assuming A,B,C are now visited). Discovers E, F.
    *   **Nodes (`m`) = 3**.
    *   **Sum of Degrees**: `deg(D)=2, deg(E)=1, deg(F)=1`. Sum = `2+1+1 = 4`.
    *   **Edges (`e`) = 4 / 2 = 2**.
    *   **Required Edges** for `m=3`: `3 * (3-1) / 2 = 3`.
    *   Since `e != required_edges` (2 != 3), this component is **NOT Complete**. `complete_components_count` remains 1.

3.  **Component 3 (G)**:
    *   DFS/BFS starts from G (assuming D,E,F are now visited).
    *   **Nodes (`m`) = 1**.
    *   **Sum of Degrees**: `deg(G)=0`. Sum = `0`.
    *   **Edges (`e`) = 0 / 2 = 0**.
    *   **Required Edges** for `m=1`: `1 * (1-1) / 2 = 0`.
    *   Since `e == required_edges` (0 == 0), this component is **Complete**. `complete_components_count` becomes 2.

Final answer: 2 complete components.

## Dry Run
Let's trace Example 1: `n = 6`, `edges = [[0,1],[0,2],[1,2],[3,4]]`

**1. Build Adjacency List:**
`adj = {`
`  0: [1, 2],`
`  1: [0, 2],`
`  2: [0, 1],`
`  3: [4],`
`  4: [3],`
`  5: []`
`}`

**2. Initialize:**
`visited = [False, False, False, False, False, False]`
`complete_components_count = 0`

**3. Iterate through vertices:**

| Current Vertex `i` | `visited` state (before check) | DFS Start Node | Nodes in Comp (`m`) | Sum of Degrees (`sum_deg`) | Edges in Comp (`e = sum_deg/2`) | Required Edges (`m*(m-1)/2`) | Is Complete? | `complete_components_count` |
| :----------------- | :--------------------------- | :------------- | :------------------ | :------------------------- | :------------------------------- | :--------------------------- | :----------- | :-------------------------- |
| **0**              | `[F,F,F,F,F,F]`              | 0              |                     |                            |                                  |                              |              |                             |
|                    |                              | **DFS(0)**     |                     |                            |                                  |                              |              |                             |
|                    |                              | - Pop 0        | `m=1`               | `sum_deg=len(adj[0])=2`    |                                  |                              |              |                             |
|                    |                              | - Push 1, 2    |                     |                            |                                  |                              |              |                             |
|                    |                              | - Pop 2        | `m=2`               | `sum_deg=2+len(adj[2])=2+2=4`|                                  |                              |              |                             |
|                    |                              | - Pop 1        | `m=3`               | `sum_deg=4+len(adj[1])=4+2=6`|                                  |                              |              |                             |
|                    |                              | **DFS End**    | `m=3`               | `sum_deg=6`                | `e=6//2=3`                       | `3*(3-1)//2 = 3`             | Yes          | `1`                         |
|                    | `[T,T,T,F,F,F]`              |                |                     |                            |                                  |                              |              |                             |
| **1**              | `[T,T,T,F,F,F]`              | - (visited)    |                     |                            |                                  |                              |              |                             |
| **2**              | `[T,T,T,F,F,F]`              | - (visited)    |                     |                            |                                  |                              |              |                             |
| **3**              | `[T,T,T,F,F,F]`              | 3              |                     |                            |                                  |                              |              |                             |
|                    |                              | **DFS(3)**     |                     |                            |                                  |                              |              |                             |
|                    |                              | - Pop 3        | `m=1`               | `sum_deg=len(adj[3])=1`    |                                  |                              |              |                             |
|                    |                              | - Push 4       |                     |                            |                                  |                              |              |                             |
|                    |                              | - Pop 4        | `m=2`               | `sum_deg=1+len(adj[4])=1+1=2`|                                  |                              |              |                             |
|                    |                              | **DFS End**    | `m=2`               | `sum_deg=2`                | `e=2//2=1`                       | `2*(2-1)//2 = 1`             | Yes          | `2`                         |
|                    | `[T,T,T,T,T,F]`              |                |                     |                            |                                  |                              |              |                             |
| **4**              | `[T,T,T,T,T,F]`              | - (visited)    |                     |                            |                                  |                              |              |                             |
| **5**              | `[T,T,T,T,T,F]`              | 5              |                     |                            |                                  |                              |              |                             |
|                    |                              | **DFS(5)**     |                     |                            |                                  |                              |              |                             |
|                    |                              | - Pop 5        | `m=1`               | `sum_deg=len(adj[5])=0`    |                                  |                              |              |                             |
|                    |                              | **DFS End**    | `m=1`               | `sum_deg=0`                | `e=0//2=0`                       | `1*(1-1)//2 = 0`             | Yes          | `3`                         |
|                    | `[T,T,T,T,T,T]`              |                |                     |                            |                                  |                              |              |                             |

**Final Result:** `3`

## Complexity
*   **Time Complexity**: `O(N + E)`.
    *   Building the adjacency list takes `O(N + E)` time (where `N` is the number of vertices and `E` is the number of edges).
    *   The outer loop iterates `N` times. Each vertex and each edge is visited at most a constant number of times across all DFS/BFS traversals.
*   **Space Complexity**: `O(N + E)`.
    *   `O(N + E)` for the adjacency list.
    *   `O(N)` for the `visited` array.
    *   `O(N)` for the recursion stack (DFS) or queue (BFS) in the worst case (e.g., a path graph).

Given `N <= 50`, this `O(N+E)` solution is very efficient and well within typical time limits.

## Edge Cases
*   **`n = 1, edges = []`**: A single vertex is a connected component. It has 1 node (`m=1`) and 0 edges (`e=0`). Required edges for `m=1` is `1*(1-1)/2 = 0`. So, it's a complete component. The solution correctly returns 1.
*   **`n = 2, edges = [[0,1]]`**: One component with 2 nodes (`m=2`) and 1 edge (`e=1`). Required edges for `m=2` is `2*(2-1)/2 = 1`. Complete. Returns 1.
*   **`n = 2, edges = []`**: Two separate components, each with 1 node (`m=1`) and 0 edges (`e=0`). Both are complete. Returns 2.
*   **Graph with no edges**: Each of the `n` vertices forms a component of size 1. All `n` components are complete. The solution returns `n`.
*   **Graph with all possible edges (a single complete component)**: The entire graph is one component of size `n`. It will be correctly identified as complete. The solution returns 1.
*   **Disconnected graph**: The algorithm correctly iterates through all vertices, ensuring each connected component is found and checked independently.

## Solution
```python
import collections
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. Build Adjacency List
        # An adjacency list maps each node to a list of its neighbors.
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u) # Graph is undirected, so add edge for both directions

        # 2. Initialize visited array and complete components counter
        # visited[i] will be True if node i has been visited as part of a component.
        visited = [False] * n
        complete_components_count = 0

        # 3. Iterate through all vertices to find connected components
        for i in range(n):
            # If vertex i has not been visited, it means we found a new connected component
            if not visited[i]:
                # Initialize counts for the current component
                nodes_in_current_component = 0
                sum_of_degrees_in_current_component = 0

                # Use a stack for Depth-First Search (DFS)
                stack = [i]
                visited[i] = True # Mark the starting node as visited

                # Perform DFS to find all nodes in this component
                while stack:
                    u = stack.pop()
                    nodes_in_current_component += 1
                    
                    # Add the degree of the current node 'u' to the sum.
                    # The degree of 'u' is simply the number of its neighbors in the adjacency list.
                    sum_of_degrees_in_current_component += len(adj[u])

                    # Explore neighbors
                    for v in adj[u]:
                        if not visited[v]:
                            visited[v] = True # Mark neighbor as visited
                            stack.append(v)   # Add neighbor to stack for further exploration
                
                # 4. After the DFS for this component is complete:
                # Calculate the number of edges in this component.
                # The sum of degrees of all vertices in any graph (or component) is equal to 
                # twice the number of edges. So, edges = sum_of_degrees / 2.
                edges_in_current_component = sum_of_degrees_in_current_component // 2

                # 5. Check if the component is complete.
                # A complete graph with 'm' nodes has exactly m * (m - 1) / 2 edges.
                required_edges_for_completeness = nodes_in_current_component * (nodes_in_current_component - 1) // 2

                if edges_in_current_component == required_edges_for_completeness:
                    complete_components_count += 1
        
        # 6. Return the total count of complete components
        return complete_components_count

```

## Why This Works
This solution works because it systematically identifies every **connected component** in the graph using a standard graph traversal algorithm (DFS). For each component, it accurately counts the number of vertices (`m`) and the total number of edges (`e`) within that component. The core mathematical property that defines a **complete graph** with `m` vertices is having exactly `m * (m - 1) / 2` edges. By comparing the actual number of edges `e` with this `required_edges` formula, we can definitively determine if a connected component is complete. This approach covers all vertices and edges exactly once, ensuring correctness and optimal efficiency.

---
<sub>Generated 2026-07-11 03:54 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
