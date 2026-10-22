# [3942] Minimum Operations to Sort a Permutation

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-10-22 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/)

**Topics:** Array

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums of length n, where nums is a permutation of the integers from 0 to n - 1.

You may perform only the following operations:

- Reverse the entire array.

- Rotate Left by One: Move the first element to the end of the array, and rest elements to left by one position.

Return an integer denoting the minimum number of operations required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return -1.

Example 1:

Input: nums = [0,2,1]

Output: 2

Explanation:

- Rotate Left by one: [2, 1, 0]

- Reverse the array: [0, 1, 2]

The array becomes sorted in 2 operations, which is minimal

Example 2:

Input: nums = [1,0,2]

Output: 2

Explanation:

- Reverse the array: [2, 0, 1]

- Rotate Left by one: [0, 1, 2]

The array becomes sorted in 2 operations, which is minimal.

Example 3:

Input: nums = [2,0,1,3]

Output: -1

Explanation:

It is impossible to reach [2, 0, 1, 3]. Thus, the answer is -1.

Constraints:

- 1 <= n == nums.length <= 10^5

- 0 <= nums[i] <= n - 1

- nums is a permutation of integers from 0 to n - 1.

**Examples / sample tests:**

```
[0,2,1]
[1,0,2]
[2,0,1,3]
```

---

## Problem Summary
You are given a permutation of integers from `0` to `n-1`. Your goal is to sort it into `[0, 1, ..., n-1]` using the minimum number of operations. The allowed operations are: reversing the entire array, or rotating the array left by one position. If sorting is impossible, return -1.

## Intuition
The key insight comes from analyzing the effects of the operations. A **left rotation** simply shifts elements cyclically. A **reverse** operation flips the array. If you apply these operations repeatedly, you'll notice that the array always remains a *rotation* of either the original sorted sequence `[0, 1, ..., n-1]` or the original reverse-sorted sequence `[n-1, n-2, ..., 0]`.

This means there are only two "families" of arrays reachable:
1.  **Family 0 (Sorted-like):** Arrays that are rotations of `[0, 1, ..., n-1]`. Examples: `[0, 1, 2]`, `[1, 2, 0]`, `[2, 0, 1]`.
2.  **Family 1 (Reverse-sorted-like):** Arrays that are rotations of `[n-1, n-2, ..., 0]`. Examples: `[2, 1, 0]`, `[1, 0, 2]`, `[0, 2, 1]`.

If the input `nums` does not belong to either of these families, it's impossible to sort, and we should return -1. Otherwise, we can model this problem as finding the shortest path in a graph where each node is a unique array state, and edges are the operations. Since there are `N` possible rotations for each of the `2` families, there are `2N` total reachable states. This small number of states suggests a **Breadth-First Search (BFS)**.

## Approach
1.  **Identify Initial State:**
    *   First, find the index of `0` in `nums`. Let this be `idx_0`.
    *   **Check Family 0:** Starting from `idx_0`, check if the elements in `nums` follow the pattern `0, 1, 2, ..., n-1` cyclically. That is, `nums[(idx_0 + k) % n]` should be equal to `k` for all `k` from `0` to `n-1`.
        *   If it matches, `nums` belongs to Family 0. The "shift" (number of left rotations from `[0, ..., n-1]`) is `idx_0`. So, the initial state is `(type=0, shift=idx_0)`.
    *   **Check Family 1:** If it's not Family 0, check if `nums` belongs to Family 1. Starting from `idx_0`, check if the elements follow the pattern `0, n-1, n-2, ..., 1` cyclically. That is, `nums[(idx_0 + k) % n]` should be equal to `(n - k) % n` for all `k` from `0` to `n-1`.
        *   If it matches, `nums` belongs to Family 1. The canonical form for Family 1 is `[n-1, n-2, ..., 0]`, where `0` is at index `n-1`. If `0` is at `idx_0` in `nums`, then `nums` is `(idx_0 - (n-1) + n) % n` left rotations away from this canonical form. So, the initial state is `(type=1, shift=(idx_0 - (n-1) + n) % n)`.
    *   If `nums` doesn't match either pattern, return -1.

2.  **BFS Setup:**
    *   We define a state as a tuple `(type, shift)`. `type` is `0` or `1`, and `shift` is an integer from `0` to `n-1`.
    *   The **target state** is `(0, 0)`, representing the sorted array `[0, 1, ..., n-1]`.
    *   Initialize a `queue` with `((initial_state, 0))`, where `0` is the cost.
    *   Initialize a `visited` set to keep track of visited states, adding `initial_state` to it.

3.  **BFS Traversal:**
    *   While the `queue` is not empty:
        *   Dequeue `((current_type, current_shift), cost)`.
        *   If `(current_type, current_shift)` is `(0, 0)`, we've reached the sorted state, so return `cost`.
        *   **Apply Rotate Left:**
            *   The next shift is `(current_shift + 1) % n`. The type remains the same.
            *   `next_state_rot = (current_type, (current_shift + 1) % n)`.
            *   If `next_state_rot` hasn't been visited, mark it visited and enqueue `(next_state_rot, cost + 1)`.
        *   **Apply Reverse:**
            *   The type flips: `next_type_rev = 1 - current_type`.
            *   The new shift is `(n - current_shift) % n`. This is because `k` left rotations of an array, when reversed, become `k` right rotations of the reversed array, which is equivalent to `n-k` left rotations.
            *   `next_state_rev = (1 - current_type, (n - current_shift) % n)`.
            *   If `next_state_rev` hasn't been visited, mark it visited and enqueue `(next_state_rev, cost + 1)`.

## Visualization
Imagine two circular tracks, one for Family 0 states and one for Family 1 states. Each track has `N` positions, indexed `0` to `N-1`, representing the `shift`.

```mermaid
graph TD
    subgraph Family 0 (Rotations of [0,1,...,n-1])
        A0((0,0)) --- A1((0,1))
        A1 --- A2((0,2))
        A2 --- A0
        style A0 fill:#99FF99,stroke:#333,stroke-width:2px
    end

    subgraph Family 1 (Rotations of [n-1,...,0])
        B0((1,0)) --- B1((1,1))
        B1 --- B2((1,2))
        B2 --- B0
    end

    A0 -- Reverse --> B0
    A1 -- Reverse --> B2
    A2 -- Reverse --> B1

    B0 -- Reverse --> A0
    B1 -- Reverse --> A2
    B2 -- Reverse --> A1

    linkStyle 0,1,2,3,4,5 stroke:#aaa,stroke-width:1px,fill:none,stroke-dasharray: 5 5;
    linkStyle 6,7,8,9,10,11 stroke:#f00,stroke-width:2px,fill:none;

    classDef default fill:#fff,stroke:#333,stroke-width:1px;
    classDef family0 fill:#e0ffe0;
    classDef family1 fill:#ffe0e0;
    class A0,A1,A2 family0;
    class B0,B1,B2 family1;
```
*   **Green node (0,0)** is our **target sorted state**.
*   **Horizontal arrows** (dashed lines) represent **Rotate Left** operations, moving from `(type, shift)` to `(type, (shift+1)%n)`.
*   **Vertical arrows** (red lines) represent **Reverse** operations, moving from `(type, shift)` to `(1-type, (n-shift)%n)`.
*   BFS explores this graph layer by layer to find the shortest path from the `initial_state` to `(0,0)`.

## Dry Run
**Example 1: `nums = [0, 2, 1]`, `n = 3`**

1.  **Identify Initial State:**
    *   `idx_0 = 0` (since `nums[0] == 0`).
    *   **Check Family 0:**
        *   `k=0`: `nums[(0+0)%3] = nums[0] = 0`. Expected `0`. Match.
        *   `k=1`: `nums[(0+1)%3] = nums[1] = 2`. Expected `1`. No match.
        *   Not Family 0.
    *   **Check Family 1:**
        *   `k=0`: `nums[(0+0)%3] = nums[0] = 0`. Expected `(3-0)%3 = 0`. Match.
        *   `k=1`: `nums[(0+1)%3] = nums[1] = 2`. Expected `(3-1)%3 = 2`. Match.
        *   `k=2`: `nums[(0+2)%3] = nums[2] = 1`. Expected `(3-2)%3 = 1`. Match.
        *   Matches Family 1.
        *   `shift = (idx_0 - (n-1) + n) % n = (0 - (3-1) + 3) % 3 = (0 - 2 + 3) % 3 = 1`.
    *   **Initial State:** `(type=1, shift=1)`.

2.  **BFS:**
    *   `queue = [(((1, 1), 0))]`
    *   `visited = {(1, 1)}`
    *   Target: `(0, 0)`

| Step | Current State (type, shift) | Cost | Operation | Next State (type, shift) | Cost | Queue (newly added) | Visited (newly added) |
| :--- | :-------------------------- | :--- | :-------- | :----------------------- | :--- | :------------------ | :-------------------- |
| 1    | `(1, 1)`                    | `0`  |           |                          |      |                     |                       |
|      |                             |      | Rotate L  | `(1, (1+1)%3) = (1, 2)`  | `1`  | `[((1, 2), 1)]`     | `{(1, 2)}`            |
|      |                             |      | Reverse   | `(0, (3-1)%3) = (0, 2)`  | `1`  | `[((0, 2), 1)]`     | `{(0, 2)}`            |
| 2    | `(1, 2)`                    | `1`  |           |                          |      |                     |                       |
|      |                             |      | Rotate L  | `(1, (2+1)%3) = (1, 0)`  | `2`  | `[((1, 0), 2)]`     | `{(1, 0)}`            |
|      |                             |      | Reverse   | `(0, (3-2)%3) = (0, 1)`  | `2`  | `[((0, 1), 2)]`     | `{(0, 1)}`            |
| 3    | `(0, 2)`                    | `1`  |           |                          |      |                     |                       |
|      |                             |      | Rotate L  | `(0, (2+1)%3) = (0, 0)`  | `2`  |                     |                       |
|      |                             |      |           | **Target Reached!**      |      |                     |                       |

**Final Result: 2**

## Complexity
*   **Time Complexity:** `O(N)`.
    *   Identifying the initial state takes `O(N)` time (finding `idx_0` and two `N`-length checks).
    *   The BFS explores at most `2N` states. Each state transition takes `O(1)` time. Thus, the BFS is `O(N)`.
    *   Total: `O(N)`.
*   **Space Complexity:** `O(N)`.
    *   The `queue` can store up to `2N` states.
    *   The `visited` set can store up to `2N` states.
    *   Total: `O(N)`.

## Edge Cases
*   **`n = 1`, `nums = [0]`:**
    *   `idx_0 = 0`. Matches Family 0 with `shift = 0`. Initial state `(0, 0)`.
    *   BFS immediately finds `(0, 0)` as the target. Returns `0`. Correct.
*   **Already Sorted: `nums = [0, 1, ..., n-1]`:**
    *   `idx_0 = 0`. Matches Family 0 with `shift = 0`. Initial state `(0, 0)`.
    *   BFS immediately finds `(0, 0)` as the target. Returns `0`. Correct.
*   **Reverse Sorted: `nums = [n-1, n-2, ..., 0]`:**
    *   `idx_0 = n-1`. Matches Family 1 with `shift = 0`. Initial state `(1, 0)`.
    *   BFS: `(1, 0)` -> Reverse -> `(0, 0)`. Returns `1`. Correct.
*   **Impossible Case: `nums = [2, 0, 1, 3]` (`n=4`)**
    *   `idx_0 = 1`.
    *   Does not match Family 0 (e.g., `nums[3]=3` but `k=2` should be `2`).
    *   Does not match Family 1 (e.g., `nums[3]=3` but `k=2` should be `(4-2)%4=2`).
    *   Returns `-1`. Correct.

## Solution

```python
import collections
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Determine the initial state (type, shift) of nums
        # type 0: rotation of [0, 1, ..., n-1] (e.g., [0,1,2], [1,2,0], [2,0,1])
        # type 1: rotation of [n-1, n-2, ..., 0] (e.g., [2,1,0], [1,0,2], [0,2,1])
        # shift: number of left rotations from the canonical form (e.g., [0,1,2] for type 0, [n-1,...,0] for type 1)

        idx_0 = nums.index(0) # Find the index of 0 in the array

        initial_state = None

        # Check if nums is a rotation of [0, 1, ..., n-1] (Family 0)
        is_family_0 = True
        for k in range(n):
            # Check if elements starting from idx_0 follow the pattern 0, 1, 2, ...
            if nums[(idx_0 + k) % n] != k:
                is_family_0 = False
                break
        
        if is_family_0:
            initial_state = (0, idx_0) # type 0, shift is idx_0
        else:
            # Check if nums is a rotation of [n-1, n-2, ..., 0] (Family 1)
            is_family_1 = True
            for k in range(n):
                # Check if elements starting from idx_0 follow the pattern 0, n-1, n-2, ...
                # (n - k) % n gives 0, n-1, n-2, ... for k=0, 1, 2, ...
                if nums[(idx_0 + k) % n] != (n - k) % n:
                    is_family_1 = False
                    break
            
            if is_family_1:
                # Canonical form for type 1 is [n-1, n-2, ..., 0].
                # In this form, 0 is at index n-1.
                # If 0 is at idx_0 in nums, then nums is (idx_0 - (n-1) + n) % n
                # left rotations away from the canonical form.
                initial_state = (1, (idx_0 - (n - 1) + n) % n)
            else:
                # If nums doesn't belong to either family, it's impossible to sort.
                return -1

        # Step 2: Perform BFS to find the minimum operations
        # State: (type, shift)
        # Target state: (0, 0) representing the sorted array [0, 1, ..., n-1]
        
        queue = collections.deque([(initial_state, 0)]) # Store (state, cost)
        visited = {initial_state} # Keep track of visited states to avoid cycles and redundant work

        while queue:
            (current_type, current_shift), cost = queue.popleft()

            # If we reached the target sorted state, return the cost
            if (current_type, current_shift) == (0, 0):
                return cost

            # Operation 1: Rotate Left by One
            # Type remains the same, shift increments (cyclically)
            next_shift_rot = (current_shift + 1) % n
            next_state_rot = (current_type, next_shift_rot)
            if next_state_rot not in visited:
                visited.add(next_state_rot)
                queue.append((next_state_rot, cost + 1))

            # Operation 2: Reverse the entire array
            # Type flips (0 becomes 1, 1 becomes 0)
            # Shift changes: if array A is 'k' left rotations of B, then reverse(A) is 'k' right rotations of reverse(B).
            # 'k' right rotations is equivalent to 'n-k' left rotations.
            next_type_rev = 1 - current_type
            next_shift_rev = (n - current_shift) % n
            next_state_rev = (next_type_rev, next_shift_rev)
            if next_state_rev not in visited:
                visited.add(next_state_rev)
                queue.append((next_state_rev, cost + 1))
        
        # This line should theoretically not be reached if initial_state is valid,
        # as all 2N states form a connected graph.
        return -1

```

## Why This Works
The solution works because it correctly identifies the entire state space reachable by the given operations and then uses Breadth-First Search (BFS) to find the shortest path within this state space. The key insight is that any array reachable from `[0, ..., n-1]` must be either a rotation of `[0, ..., n-1]` itself (Family 0) or a rotation of `[n-1, ..., 0]` (Family 1). By representing each such array state compactly as `(type, shift)`, we create a graph with `2N` nodes. BFS guarantees finding the minimum number of operations (shortest path) to transform the initial `nums` state into the target sorted state `(0, 0)`. If the initial `nums` doesn't fit into either family, it's impossible to reach the sorted state, and the initial check correctly handles this by returning -1.

---
<sub>Generated 2026-10-22 05:15 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
