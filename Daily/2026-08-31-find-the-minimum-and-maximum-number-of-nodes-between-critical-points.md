# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-08-31 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/)

**Topics:** Linked List

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

Example 1:

Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].

Example 2:

Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
Explanation: There are three critical points:
- [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.

Example 3:

Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
Explanation: There are two critical points:
- [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.

Constraints:

- The number of nodes in the list is in the range [2, 10^5].

- 1 <= Node.val <= 10^5

**Examples / sample tests:**

```
[3,1]
[5,3,1,2,5,1,2]
[1,3,2,2,3,2,2,2,7]
```

---

## Problem Summary
This problem asks us to find the minimum and maximum distances between "critical points" in a singly linked list. A critical point is defined as a node that is either a local maxima (its value is strictly greater than its neighbors) or a local minima (its value is strictly smaller than its neighbors). We need to return an array `[minDistance, maxDistance]`, or `[-1, -1]` if fewer than two critical points exist.

## Intuition
To identify a critical point, we need to compare a node's value with its immediate previous and next nodes. This means we'll need to look at three nodes at a time as we traverse the list. Since distances are involved, we'll also need to keep track of the **indices** or **positions** of these critical points within the list.

The key observations are:
1.  **Three-pointer approach**: We can use three pointers (`prev_node`, `curr_node`, `next_node`) to efficiently check the critical point condition for `curr_node`.
2.  **Index tracking**: Linked lists don't inherently provide indices. We'll need a counter (`current_idx`) that increments with each step to simulate node positions.
3.  **Minimum distance**: The minimum distance between any two critical points will always be found between **adjacent** critical points in the list. As we find critical points, we can update this minimum.
4.  **Maximum distance**: The maximum distance between any two critical points will always be the distance between the **first** critical point found and the **last** critical point found. This is a common pattern for range-based maximums.
5.  **Edge cases**: A critical point requires both a previous and a next node, so the head and tail nodes can never be critical. Also, if we find fewer than two critical points in total, we cannot calculate any distances, so we return `[-1, -1]`.

## Approach
We will traverse the linked list once using a three-pointer "sliding window" and an index counter.

1.  **Initialization**:
    *   `min_dist`: Initialize to `float('inf')`. This will store the minimum distance between adjacent critical points.
    *   `first_critical_idx`: Initialize to `-1`. This will store the index of the very first critical point encountered.
    *   `last_critical_idx`: Initialize to `-1`. This will store the index of the most recently encountered critical point. This variable will also help calculate `min_dist` by acting as the "previous critical point index".
    *   `prev_node`: Pointer to the `head` of the list (index 0).
    *   `curr_node`: Pointer to `head.next` (index 1).
    *   `next_node`: Pointer to `head.next.next` (index 2).
    *   `current_idx`: An integer counter, initialized to `1` (representing the index of `curr_node`).

2.  **Handle Small Lists**: If the list has fewer than 3 nodes (`head` is `None`, `head.next` is `None`, or `head.next.next` is `None`), no critical points can exist. Return `[-1, -1]` immediately.

3.  **Traversal**: Iterate while `next_node` is not `None`. This ensures that `curr_node` always has both a `prev_node` and a `next_node` for comparison.
    *   Inside the loop, check if `curr_node` is a critical point:
        *   It's a local maxima if `curr_node.val > prev_node.val` AND `curr_node.val > next_node.val`.
        *   It's a local minima if `curr_node.val < prev_node.val` AND `curr_node.val < next_node.val`.
    *   **If `curr_node` is a critical point**:
        *   If `first_critical_idx` is still `-1`, set `first_critical_idx = current_idx`. This captures the very first critical point.
        *   If `last_critical_idx` is not `-1` (meaning we've found at least one critical point before this one), calculate the distance to the previous critical point: `current_idx - last_critical_idx`. Update `min_dist = min(min_dist, current_idx - last_critical_idx)`.
        *   Update `last_critical_idx = current_idx`. This makes `current_idx` the "previous critical point" for the *next* critical point we might find.
    *   **Advance Pointers**: Move the pointers forward for the next iteration:
        *   `prev_node = curr_node`
        *   `curr_node = next_node`
        *   `next_node = next_node.next`
    *   **Increment Index**: Increment `current_idx` by 1.

4.  **Final Result Calculation**: After the loop finishes:
    *   If `first_critical_idx` is still `-1` or `first_critical_idx == last_critical_idx`, it means we found fewer than two distinct critical points. Return `[-1, -1]`.
    *   Otherwise, we have at least two critical points. Calculate `max_dist = last_critical_idx - first_critical_idx`.
    *   Return `[min_dist, max_dist]`.

## Visualization
Let's trace the pointers and index for `head = [5,3,1,2,5,1,2]` (indices 0-6).

```mermaid
graph TD
    subgraph Initial State
        A[head (idx 0): 5] --> B[curr (idx 1): 3] --> C[next (idx 2): 1] --> D[Node (idx 3): 2] --> E[Node (idx 4): 5] --> F[Node (idx 5): 1] --> G[Node (idx 6): 2] --> H[None];
        A -- prev_node --> A;
        B -- curr_node --> B;
        C -- next_node --> C;
        I[current_idx = 1]
        J[first_critical_idx = -1]
        K[last_critical_idx = -1]
        L[min_dist = inf]
    end

    subgraph Iteration 1 (curr_node = 3, idx = 1)
        A1[5] --> B1[3] --> C1[1] --> D1[2] --> E1[5] --> F1[1] --> G1[2] --> H1[None];
        A1 -- prev_node --> A1;
        B1 -- curr_node --> B1;
        C1 -- next_node --> C1;
        M1[3 is NOT critical (5 > 3, but 3 is not > 1; 5 not < 3)]
        N1[current_idx = 2]
        O1[first_critical_idx = -1]
        P1[last_critical_idx = -1]
        Q1[min_dist = inf]
    end

    subgraph Iteration 2 (curr_node = 1, idx = 2)
        A2[5] --> B2[3] --> C2[1] --> D2[2] --> E2[5] --> F2[1] --> G2[2] --> H2[None];
        B2 -- prev_node --> B2;
        C2 -- curr_node --> C2;
        D2 -- next_node --> D2;
        M2[1 IS critical (3 > 1 < 2, local minima)]
        N2[first_critical_idx = 2]
        O2[last_critical_idx = 2]
        P2[min_dist = inf]
        Q2[current_idx = 3]
    end

    subgraph Iteration 3 (curr_node = 2, idx = 3)
        A3[5] --> B3[3] --> C3[1] --> D3[2] --> E3[5] --> F3[1] --> G3[2] --> H3[None];
        C3 -- prev_node --> C3;
        D3 -- curr_node --> D3;
        E3 -- next_node --> E3;
        M3[2 is NOT critical (1 < 2, but 2 is not > 5; 1 not > 2)]
        N3[first_critical_idx = 2]
        O3[last_critical_idx = 2]
        P3[min_dist = inf]
        Q3[current_idx = 4]
    end

    subgraph Iteration 4 (curr_node = 5, idx = 4)
        A4[5] --> B4[3] --> C4[1] --> D4[2] --> E4[5] --> F4[1] --> G4[2] --> H4[None];
        D4 -- prev_node --> D4;
        E4 -- curr_node --> E4;
        F4 -- next_node --> F4;
        M4[5 IS critical (2 < 5 > 1, local maxima)]
        N4[first_critical_idx = 2]
        O4[last_critical_idx = 4]
        P4[min_dist = min(inf, 4-2=2) = 2]
        Q4[current_idx = 5]
    end

    subgraph Iteration 5 (curr_node = 1, idx = 5)
        A5[5] --> B5[3] --> C5[1] --> D5[2] --> E5[5] --> F5[1] --> G5[2] --> H5[None];
        E5 -- prev_node --> E5;
        F5 -- curr_node --> F5;
        G5 -- next_node --> G5;
        M5[1 IS critical (5 > 1 < 2, local minima)]
        N5[first_critical_idx = 2]
        O5[last_critical_idx = 5]
        P5[min_dist = min(2, 5-4=1) = 1]
        Q5[current_idx = 6]
    end

    subgraph Iteration 6 (curr_node = 2, idx = 6)
        A6[5] --> B6[3] --> C6[1] --> D6[2] --> E6[5] --> F6[1] --> G6[2] --> H6[None];
        F6 -- prev_node --> F6;
        G6 -- curr_node --> G6;
        H6 -- next_node --> H6;
        M6[2 is NOT critical (1 < 2, but next is None)]
        N6[first_critical_idx = 2]
        O6[last_critical_idx = 5]
        P6[min_dist = 1]
        Q6[current_idx = 7]
    end

    subgraph Final Result
        R[Loop ends (next_node is None)]
        S[first_critical_idx = 2, last_critical_idx = 5]
        T[max_dist = last_critical_idx - first_critical_idx = 5 - 2 = 3]
        U[Return [min_dist, max_dist] = [1, 3]]
    end
```

## Dry Run
Let's trace Example 2: `head = [5,3,1,2,5,1,2]`

| `current_idx` | `prev.val` | `curr.val` | `next.val` | Is Critical? | `first_critical_idx` | `last_critical_idx` | `min_dist` |
| :------------ | :--------- | :--------- | :--------- | :----------- | :------------------- | :------------------ | :--------- |
| Initial       | -          | -          | -          | -            | -1                   | -1                  | `inf`      |
| 1             | 5          | 3          | 1          | No           | -1                   | -1                  | `inf`      |
| 2             | 3          | 1          | 2          | Yes (minima) | 2                    | 2                   | `inf`      |
| 3             | 1          | 2          | 5          | No           | 2                    | 2                   | `inf`      |
| 4             | 2          | 5          | 1          | Yes (maxima) | 2                    | 4                   | `min(inf, 4-2=2) = 2` |
| 5             | 5          | 1          | 2          | Yes (minima) | 2                    | 5                   | `min(2, 5-4=1) = 1` |
| 6             | 1          | 2          | `None`     | No           | 2                    | 5                   | 1          |

**After loop**:
`first_critical_idx = 2`
`last_critical_idx = 5`
Since `first_critical_idx` is not -1 and `first_critical_idx != last_critical_idx`, we have at least two critical points.
`max_dist = last_critical_idx - first_critical_idx = 5 - 2 = 3`.
**Final Result**: `[1, 3]`. This matches the example output.

## Complexity
*   **Time Complexity**: O(N), where N is the number of nodes in the linked list. We traverse the list exactly once to identify all critical points and calculate distances.
*   **Space Complexity**: O(1). We only use a few constant-space variables (pointers, indices, distances) regardless of the list's size.

## Edge Cases
*   **List with fewer than 3 nodes**: `[3,1]`, `[1]`, `[]`. Our initial check `if not head or not head.next or not head.next.next:` handles this by returning `[-1, -1]`. This is correct because a critical point requires both a previous and a next node.
*   **List with no critical points**: `[1,2,3,4,5]` (strictly increasing) or `[5,4,3,2,1]` (strictly decreasing) or `[1,1,1,1,1]` (all same values). In these cases, `first_critical_idx` will remain `-1` (or `first_critical_idx == last_critical_idx` if only one critical point is found by chance, e.g., `[1,2,1,2,3]`). The final check `if first_critical_idx == -1 or first_critical_idx == last_critical_idx:` correctly returns `[-1, -1]`.
*   **List with exactly one critical point**: `[1,5,2,3,4]`. Here, `5` (index 1) is a local maxima. `first_critical_idx` becomes 1, `last_critical_idx` becomes 1. The final check correctly returns `[-1, -1]`.
*   **Critical points are adjacent**: `[1,3,2,1,5]`. `3` (idx 1) is maxima, `2` (idx 2) is minima. `min_dist` will correctly be `2-1=1`.
*   **All critical points are maxima/minima**: The logic correctly identifies both types and treats them equally for distance calculations.

## Solution
```python
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Handle edge case: A list must have at least 3 nodes to have any critical points.
        # A critical point needs both a previous and a next node.
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        # Initialize variables to track critical points and distances
        min_dist = float('inf')  # Stores the minimum distance between adjacent critical points
        first_critical_idx = -1  # Stores the index of the first critical point found
        last_critical_idx = -1   # Stores the index of the most recently found critical point

        # Pointers for list traversal
        # prev_node is at index current_idx - 1
        # curr_node is at index current_idx
        # next_node is at index current_idx + 1
        prev_node = head
        curr_node = head.next
        next_node = head.next.next

        # current_idx tracks the 0-based index of curr_node
        current_idx = 1 

        # Traverse the list until next_node becomes None.
        # This ensures curr_node always has both a previous and a next node for comparison.
        while next_node:
            # Check if curr_node is a local maxima or local minima
            is_local_maxima = (curr_node.val > prev_node.val and curr_node.val > next_node.val)
            is_local_minima = (curr_node.val < prev_node.val and curr_node.val < next_node.val)

            if is_local_maxima or is_local_minima:
                # This is a critical point
                if first_critical_idx == -1:
                    # If this is the first critical point found, record its index
                    first_critical_idx = current_idx
                
                if last_critical_idx != -1:
                    # If we've found a previous critical point, calculate the distance
                    # and update min_dist if this distance is smaller
                    min_dist = min(min_dist, current_idx - last_critical_idx)
                
                # Update last_critical_idx to the current critical point's index
                # This serves as the 'previous' critical point for the next calculation
                last_critical_idx = current_idx
            
            # Move all three pointers one step forward
            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next
            
            # Increment the current index
            current_idx += 1
        
        # After the traversal, check if we found at least two distinct critical points.
        # If first_critical_idx is still -1, no critical points were found.
        # If first_critical_idx == last_critical_idx, only one critical point was found.
        if first_critical_idx == -1 or first_critical_idx == last_critical_idx:
            return [-1, -1]
        else:
            # Calculate the maximum distance: distance between the first and last critical points
            max_dist = last_critical_idx - first_critical_idx
            return [min_dist, max_dist]

```

## Why This Works
This solution works by performing a **single pass** through the linked list. During this pass, it efficiently identifies all critical points using a three-pointer sliding window. By maintaining `first_critical_idx` and `last_critical_idx`, it can correctly determine the maximum distance (which is always between the first and last critical points). Simultaneously, by comparing the `current_idx` with `last_critical_idx` whenever a new critical point is found, it continuously updates `min_dist` to capture the smallest distance between any two *adjacent* critical points. The initial checks and final conditional return correctly handle cases with insufficient critical points, ensuring correctness and optimality.

---
<sub>Generated 2026-08-31 05:59 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
