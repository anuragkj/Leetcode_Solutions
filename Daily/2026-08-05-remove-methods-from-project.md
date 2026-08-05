# [3310] Remove Methods From Project

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-08-05 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/remove-methods-from-project/)

**Topics:** Depth-First Search, Breadth-First Search, Graph Theory

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are maintaining a project that has n methods numbered from 0 to n - 1.

You are given two integers n and k, and a 2D integer array invocations, where invocations[i] = [a_i, b_i] indicates that method a_i invokes method b_i.

There is a known bug in method k. Method k, along with any method invoked by it, either directly or indirectly, are considered suspicious and we aim to remove them.

A group of methods can only be removed if no method outside the group invokes any methods within it.

Return an array containing all the remaining methods after removing all the suspicious methods. You may return the answer in any order. If it is not possible to remove all the suspicious methods, none should be removed.

Example 1:

Input: n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]

Output: [0,1,2,3]

Explanation:

Method 2 and method 1 are suspicious, but they are directly invoked by methods 3 and 0, which are not suspicious. We return all elements without removing anything.

Example 2:

Input: n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]

Output: [3,4]

Explanation:

Methods 0, 1, and 2 are suspicious and they are not directly invoked by any other method. We can remove them.

Example 3:

Input: n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]

Output: []

Explanation:

All methods are suspicious. We can remove them.

Constraints:

- 1 <= n <= 10^5

- 0 <= k <= n - 1

- 0 <= invocations.length <= 2 * 10^5

- invocations[i] == [a_i, b_i]

- 0 <= a_i, b_i <= n - 1

- a_i != b_i

- invocations[i] != invocations[j]

**Examples / sample tests:**

```
4
1
[[1,2],[0,1],[3,2]]
5
0
[[1,2],[0,2],[0,1],[3,4]]
3
2
[[1,2],[0,1],[2,0]]
```

---

## Problem Summary
You have `n` software methods, and `invocations` describe which method calls another. Method `k` has a bug, making it and all methods it directly or indirectly invokes **suspicious**. These suspicious methods can only be removed if no non-suspicious method invokes any suspicious method. Return the methods that remain after removal, or all `n` methods if removal isn't possible.

## Intuition
The problem has two main parts:
1.  **Identify all suspicious methods:** Method `k` is suspicious. Any method invoked by a suspicious method is also suspicious. This is a classic **reachability problem** in a directed graph. We can use Depth-First Search (DFS) or Breadth-First Search (BFS) starting from `k` to find all methods reachable from `k`. These are our suspicious methods.
2.  **Check the removal condition:** The tricky part is "A group of methods can only be removed if no method outside the group invokes any methods within it." This means if we find *any* invocation `(a, b)` where `a` is a **non-suspicious** method and `b` is a **suspicious** method, then the removal condition is violated. In this scenario, we cannot remove anything, and all `n` methods must be returned. If no such problematic invocation exists, then we can safely remove all suspicious methods.

## Approach
We will use a graph traversal algorithm (DFS) to identify suspicious methods and then iterate through all original invocations to check the removal condition.

1.  **Build the Graph:** Create an **adjacency list** `adj` where `adj[u]` stores a list of methods `v` that `u` invokes. This represents the directed graph of method calls.
2.  **Find Suspicious Methods:**
    *   Initialize an empty `set` called `suspicious` to store all suspicious method IDs.
    *   Perform an **iterative Depth-First Search (DFS)** starting from method `k`.
    *   Add `k` to the `suspicious` set and push it onto a stack.
    *   While the stack is not empty:
        *   Pop a `current_method` from the stack.
        *   For each `neighbor` that `current_method` invokes:
            *   If `neighbor` has not yet been marked `suspicious` (i.e., not in the `suspicious` set), add `neighbor` to `suspicious` and push it onto the stack.
3.  **Check Removal Condition:**
    *   Initialize a boolean flag `can_remove = True`.
    *   Iterate through *every original invocation* `[a, b]` in the `invocations` array.
    *   For each `[a, b]`:
        *   If `b` is in the `suspicious` set (meaning `b` is a suspicious method) AND `a` is *not* in the `suspicious` set (meaning `a` is a non-suspicious method):
            *   This violates the removal condition. Set `can_remove = False` and immediately `break` from the loop, as we've found a blocking invocation.
4.  **Construct Result:**
    *   If `can_remove` is `False`: Return a list containing all method IDs from `0` to `n-1`.
    *   If `can_remove` is `True`: Create an empty list `remaining`. Iterate from `i = 0` to `n-1`. If `i` is *not* in the `suspicious` set, add `i` to `remaining`. Return `remaining`.

## Visualization

Let's illustrate with **Example 1:** `n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]`

```mermaid
graph TD
    subgraph Original Graph
        0 --> 1
        1 --> 2
        3 --> 2
    end

    subgraph Step 1: Identify Suspicious (k=1)
        direction LR
        0
        1(k) --- invokes --> 2
        3
        style 1 fill:#f9f,stroke:#333,stroke-width:2px
        style 2 fill:#f9f,stroke:#333,stroke-width:2px
        linkStyle 1 stroke:#f9f,stroke-width:2px,fill:none;
        linkStyle 2 stroke:#f9f,stroke-width:2px,fill:none;
    end
    
    subgraph Step 2: Check Removal Condition
        direction LR
        0 --- invokes --> 1(Suspicious)
        3 --- invokes --> 2(Suspicious)
        1(Suspicious) --- invokes --> 2(Suspicious)
        style 0 fill:#fff,stroke:#333,stroke-width:2px
        style 3 fill:#fff,stroke:#333,stroke-width:2px
        style 1 fill:#f9f,stroke:#333,stroke-width:2px
        style 2 fill:#f9f,stroke:#333,stroke-width:2px
        linkStyle 0 stroke:red,stroke-width:2px,fill:none;
        linkStyle 1 stroke:red,stroke-width:2px,fill:none;
    end

    subgraph Result: Cannot Remove
        0
        1
        2
        3
    end
```
**Explanation:**
1.  **Original Graph:** Shows the initial method call structure.
2.  **Identify Suspicious (k=1):** We start DFS from `k=1`. `1` invokes `2`. So, `1` and `2` are marked suspicious (pink nodes). `suspicious = {1, 2}`.
3.  **Check Removal Condition:** We iterate through all original invocations:
    *   `(1, 2)`: `1` is suspicious, `2` is suspicious. OK.
    *   `(0, 1)`: `0` is **not** suspicious, but `1` **is** suspicious. This is a violation! (Red arrow from `0` to `1`).
    *   `(3, 2)`: `3` is **not** suspicious, but `2` **is** suspicious. This is also a violation! (Red arrow from `3` to `2`).
    Since we found violations, `can_remove` becomes `False`.
4.  **Result:** Because `can_remove` is `False`, we return all methods: `[0, 1, 2, 3]`.

## Dry Run

Let's walk through **Example 1:** `n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]`

1.  **Build Graph:**
    `adj = {1: [2], 0: [1], 3: [2]}`

2.  **Find Suspicious Methods (DFS from k=1):**
    *   Initialize `suspicious = set()`, `stack = []`
    *   Add `k=1` to `suspicious` and `stack`: `suspicious = {1}`, `stack = [1]`
    *   **Loop 1:**
        *   `current_method = stack.pop()` (which is `1`).
        *   Neighbors of `1`: `[2]`.
        *   `neighbor = 2`. `2` is not in `suspicious`.
        *   Add `2` to `suspicious`: `suspicious = {1, 2}`.
        *   Push `2` to `stack`: `stack = [2]`.
    *   **Loop 2:**
        *   `current_method = stack.pop()` (which is `2`).
        *   Neighbors of `2`: `[]`.
    *   Stack is empty. DFS ends.
    *   **Result of DFS:** `suspicious = {1, 2}`

3.  **Check Removal Condition:**
    *   Initialize `can_remove = True`.

| Iteration (invocation) | `a` | `b` | `b in suspicious`? | `a not in suspicious`? | Condition `(b in suspicious and a not in suspicious)`? | `can_remove` |
| :--------------------- | :-- | :-- | :----------------- | :--------------------- | :----------------------------------------------------- | :----------- |
| `[1,2]`                | 1   | 2   | True               | False                  | False                                                  | True         |
| `[0,1]`                | 0   | 1   | True               | True                   | **True**                                               | **False**    |
| *Break loop*           |     |     |                    |                        |                                                        |              |

4.  **Construct Result:**
    *   `can_remove` is `False`.
    *   Return `list(range(n))`, which is `[0, 1, 2, 3]`.

This matches Example 1's output.

## Complexity

*   **Time Complexity:** O(N + E)
    *   Building the adjacency list takes O(E) time, where E is the number of invocations.
    *   The DFS to find suspicious methods visits each node and edge at most once, taking O(N + E) time, where N is the number of methods.
    *   Iterating through all invocations to check the removal condition takes O(E) time.
    *   Constructing the final result list takes O(N) time.
    *   Overall, the dominant factor is O(N + E).
*   **Space Complexity:** O(N + E)
    *   The adjacency list `adj` stores all edges, taking O(N + E) space.
    *   The `suspicious` set can store up to N methods, taking O(N) space.
    *   The DFS stack can store up to N methods in the worst case (e.g., a long chain of invocations), taking O(N) space.
    *   Overall, the dominant factor is O(N + E).

## Edge Cases

*   **`k` is an isolated method:** If `k` invokes nothing and nothing invokes `k`, `suspicious` will only contain `k`. If `k` is not invoked by any other method, `k` will be removed. Otherwise, all methods remain.
*   **No invocations (`invocations` is empty):** `adj` will be empty. `suspicious` will only contain `k`. The loop for checking `can_remove` won't find any invocations, so `can_remove` remains `True`. If `n=1`, `k=0`, result is `[]`. If `n>1`, `k` is removed, others remain. Correct.
*   **All methods are suspicious:** If `k` directly or indirectly invokes all other methods (e.g., a cycle involving all methods, or a chain from `k` to all others), `suspicious` will contain all `n` methods. The `can_remove` check will find no `a not in suspicious` cases, so `can_remove` remains `True`. The result will be `[]`. Correct (Example 3).
*   **Graph is disconnected:** The DFS from `k` will only find methods reachable from `k`. Methods in other disconnected components will not be marked suspicious unless `k` is part of their component. This is handled correctly.
*   **`k` is the only method (`n=1, k=0`):** `suspicious` will be `{0}`. `can_remove` will be `True`. Result `[]`. Correct.

## Solution

```python
import collections
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build the graph using an adjacency list.
        # adj[u] will store a list of methods invoked by method u.
        adj = collections.defaultdict(list)
        for u, v in invocations:
            adj[u].append(v)

        # Step 2: Find all suspicious methods using iterative DFS.
        # A method is suspicious if it's k, or invoked by k (directly or indirectly).
        suspicious = set()
        
        # Use a stack for iterative DFS. Start with method k.
        stack = [k]
        suspicious.add(k) # Method k itself is always suspicious.

        while stack:
            current_method = stack.pop()
            # Explore all methods invoked by the current_method
            for neighbor in adj[current_method]:
                # If this neighbor hasn't been marked suspicious yet,
                # add it to the suspicious set and push it to the stack to explore its invocations.
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    stack.append(neighbor)
        
        # Step 3: Check the removal condition.
        # A group of methods can only be removed if no method outside the group
        # invokes any methods within it.
        # This means, for every invocation (a, b):
        # if b is suspicious AND a is NOT suspicious, then we CANNOT remove.
        can_remove = True
        for a, b in invocations:
            # If 'b' is a suspicious method AND 'a' is a non-suspicious method,
            # then the removal condition is violated.
            if b in suspicious and a not in suspicious:
                can_remove = False
                break # No need to check further, removal is blocked.
        
        # Step 4: Construct the result based on whether removal is possible.
        if not can_remove:
            # If removal is not possible, none should be removed.
            # Return all methods from 0 to n-1.
            return list(range(n))
        else:
            # If removal is possible, return all non-suspicious methods.
            remaining = []
            for i in range(n):
                if i not in suspicious:
                    remaining.append(i)
            return remaining

```

## Why This Works

The solution correctly identifies the set of suspicious methods by performing a graph traversal (DFS) starting from `k`, which precisely captures the "directly or indirectly invoked by `k`" criterion. The core of the problem lies in the removal condition: "A group of methods can only be removed if no method outside the group invokes any methods within it." Our approach directly verifies this by iterating through *all* original invocations. If we find *any* edge `(a, b)` where `a` is a non-suspicious method and `b` is a suspicious method, it means a method outside the suspicious group (`a`) invokes a method inside it (`b`), thus violating the condition. If, after checking all invocations, no such violation is found, it guarantees that all invocations into the suspicious group originate from within the suspicious group itself, making the removal safe and valid according to the problem statement.

---
<sub>Generated 2026-08-05 03:46 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
