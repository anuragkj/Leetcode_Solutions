# [1882] Process Tasks Using Servers

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-11-07 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/process-tasks-using-servers/)

**Topics:** Array, Heap (Priority Queue)

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​ and m​​​​​​ respectively. servers[i] is the weight of the i^​​​​​​th​​​​ server, and tasks[j] is the time needed to process the j^​​​​​​th​​​​ task in seconds.

Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.

At second j, the j^th task is inserted into the queue (starting with the 0^th task being inserted at second 0). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index.

If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of insertion following the weight and index priorities above.

A server that is assigned task j at second t will be free again at second t + tasks[j].

Build an array ans​​​​ of length m, where ans[j] is the index of the server the j^​​​​​​th task will be assigned to.

Return the array ans​​​​.

Example 1:

Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
Output: [2,2,0,2,1,2]
Explanation: Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 2 until second 1.
- At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
- At second 2, task 2 is added and processed using server 0 until second 5.
- At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
- At second 4, task 4 is added and processed using server 1 until second 5.
- At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.

Example 2:

Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
Output: [1,4,1,4,1,3,2]
Explanation: Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 1 until second 2.
- At second 1, task 1 is added and processed using server 4 until second 2.
- At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4.
- At second 3, task 3 is added and processed using server 4 until second 7.
- At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9.
- At second 5, task 5 is added and processed using server 3 until second 7.
- At second 6, task 6 is added and processed using server 2 until second 7.

Constraints:

- servers.length == n

- tasks.length == m

- 1 <= n, m <= 2 * 10^5

- 1 <= servers[i], tasks[j] <= 2 * 10^5

**Examples / sample tests:**

```
[3,3,2]
[1,2,3,2,1,2]
[5,1,4,3,2]
[2,1,2,4,5,2,1]
```

---

## Problem Summary
You are given a list of servers with their processing weights and a list of tasks with their processing times. Tasks arrive one by one, starting at second 0. You must assign each task to an available server. The assignment rules prioritize servers with the smallest weight, then smallest index. If no servers are free, you wait until one becomes free. The goal is to return an array indicating which server each task was assigned to.

## Intuition
This problem is a **simulation** where events happen over time. We need to manage servers that are either **available** or **busy**. Since we always pick the "best" available server (smallest weight, then smallest index), and tasks are processed in order, **priority queues (heaps)** are the natural data structure. We'll need two heaps: one for available servers and one for busy servers, each ordered by different criteria.

## Approach
We will simulate the task assignment process using two min-heaps:

1.  **`available_servers` heap**: Stores servers that are currently free. Each element is `(weight, index)`. This heap naturally prioritizes servers with the smallest weight, and then smallest index (due to tuple comparison).
2.  **`busy_servers` heap**: Stores servers that are currently processing a task. Each element is `(finish_time, weight, index)`. This heap prioritizes servers that will become free earliest. If multiple servers finish at the same time, the `weight` and `index` are included to maintain consistency, though they don't affect the "earliest finish time" priority.

The simulation proceeds task by task, maintaining a `current_time` variable:

1.  **Initialization**:
    *   Populate `available_servers` with `(servers[i], i)` for all `i` from `0` to `n-1`.
    *   Initialize `busy_servers` as empty.
    *   Initialize `ans` array of size `m` with zeros.
    *   Set `current_time = 0`.

2.  **Iterate through tasks**: For each `task_idx` from `0` to `m-1`:
    a.  **Advance `current_time`**: The `task_idx`-th task arrives at second `task_idx`. We must ensure `current_time` is at least `task_idx`. So, update `current_time = max(current_time, task_idx)`.
    b.  **Handle waiting for servers**: If `available_servers` is empty (meaning all servers are busy), we *must* wait for a server to become free. In this scenario, update `current_time = max(current_time, busy_servers[0][0])` to jump to the earliest time a server becomes free.
    c.  **Release busy servers**: Move any servers from `busy_servers` to `available_servers` whose `finish_time` is less than or equal to the `current_time`. This is done in a `while` loop, as multiple servers might become free simultaneously. For each server `(finish_time, weight, index)` popped from `busy_servers`, push `(weight, index)` to `available_servers`.
    d.  **Assign the task**:
        *   Pop the best available server `(server_weight, server_idx)` from `available_servers`.
        *   Record `ans[task_idx] = server_idx`.
        *   Calculate its `finish_time = current_time + tasks[task_idx]`.
        *   Push `(finish_time, server_weight, server_idx)` into `busy_servers`.

3.  **Return `ans`**.

## Visualization
```mermaid
graph TD
    subgraph "Simulation Loop (for each task_idx from 0 to m-1)"
        A[Start task_idx] --> B{current_time = max(current_time, task_idx)};
        B --> C{Is Available Servers empty AND Busy Servers not empty?};
        C -- Yes --> D[current_time = max(current_time, Busy Servers[0].finish_time)];
        C -- No --> E[Continue];
        D --> E;
        E --> F{Release Servers: While Busy Servers[0].finish_time <= current_time};
        F -- Yes --> G[Pop (finish_time, w, idx) from Busy Servers];
        G --> H[Push (w, idx) to Available Servers];
        H --> F;
        F -- No --> I{Assign Task: Pop (w, idx) from Available Servers};
        I --> J[ans[task_idx] = idx];
        J --> K[finish_time = current_time + tasks[task_idx]];
        K --> L[Push (finish_time, w, idx) to Busy Servers];
        L --> M[End task_idx];
    end

    subgraph "Data Structures"
        AvailableServersHeap["Available Servers (min-heap)
        (weight, index)"]
        BusyServersHeap["Busy Servers (min-heap)
        (finish_time, weight, index)"]
    end

    H -- Server becomes free --> AvailableServersHeap;
    I -- Server becomes busy --> BusyServersHeap;
    L -- Server becomes busy --> BusyServersHeap;
```

## Dry Run
Let's trace Example 1: `servers = [3,3,2]`, `tasks = [1,2,3,2,1,2]`
`n=3, m=6`
Initial: `current_time = 0`, `ans = [0]*6`
`available_servers = [(2,2), (3,0), (3,1)]` (heap order: smallest weight, then smallest index)
`busy_servers = []`

| `task_idx` | `tasks[task_idx]` | `current_time` (before update) | `current_time` (after update) | `available_servers` (before release) | `busy_servers` (before release) | Servers Released (to `available_servers`) | `available_servers` (after release) | Server Assigned (`idx`) | `finish_time` | `busy_servers` (after assignment) | `ans` (partial) |
| :--------: | :---------------: | :-----------------------------: | :----------------------------: | :----------------------------------: | :-----------------------------: | :---------------------------------------: | :---------------------------------: | :---------------------: | :-----------: | :---------------------------------------: | :--------------: |
| 0          | 1                 | 0                               | `max(0,0)=0`                   | `[(2,2), (3,0), (3,1)]`              | `[]`                            | -                                         | `[(2,2), (3,0), (3,1)]`             | 2                       | `0+1=1`       | `[(1,2,2)]`                               | `[2,_,_,_,_,_]`  |
| 1          | 2                 | 0                               | `max(0,1)=1`                   | `[(3,0), (3,1)]`                     | `[(1,2,2)]`                     | `(2,2)` from `(1,2,2)`                    | `[(2,2), (3,0), (3,1)]`             | 2                       | `1+2=3`       | `[(3,2,2)]`                               | `[2,2,_,_,_,_]`  |
| 2          | 3                 | 1                               | `max(1,2)=2`                   | `[(3,0), (3,1)]`                     | `[(3,2,2)]`                     | -                                         | `[(3,0), (3,1)]`                    | 0                       | `2+3=5`       | `[(3,2,2), (5,3,0)]`                      | `[2,2,0,_,_,_]`  |
| 3          | 2                 | 2                               | `max(2,3)=3`                   | `[(3,1)]`                            | `[(3,2,2), (5,3,0)]`            | `(2,2)` from `(3,2,2)`                    | `[(2,2), (3,1)]`                    | 2                       | `3+2=5`       | `[(5,2,2), (5,3,0)]`                      | `[2,2,0,2,_,_]`  |
| 4          | 1                 | 3                               | `max(3,4)=4`                   | `[(3,1)]`                            | `[(5,2,2), (5,3,0)]`            | -                                         | `[(3,1)]`                           | 1                       | `4+1=5`       | `[(5,2,2), (5,3,0), (5,3,1)]`             | `[2,2,0,2,1,_]`  |
| 5          | 2                 | 4                               | `max(4,5)=5`                   | `[]`                                 | `[(5,2,2), (5,3,0), (5,3,1)]`   | `(2,2)` from `(5,2,2)`, `(3,0)` from `(5,3,0)`, `(3,1)` from `(5,3,1)` | `[(2,2), (3,0), (3,1)]`             | 2                       | `5+2=7`       | `[(7,2,2)]`                               | `[2,2,0,2,1,2]`  |

Final result: `[2,2,0,2,1,2]`.

## Complexity
*   **Time Complexity**: `O((N + M) log N)`.
    *   Initializing `available_servers` takes `O(N log N)`.
    *   The main loop runs `M` times. In each iteration, we perform a constant number of heap operations (push/pop). Each server is pushed to `available_servers` once initially, then cycles between `available_servers` and `busy_servers` at most `M` times. Thus, the total number of heap operations across all `M` tasks is `O(N + M)`. Each heap operation takes `O(log N)` time.
*   **Space Complexity**: `O(N + M)`.
    *   `available_servers` and `busy_servers` heaps store up to `N` server tuples each, contributing `O(N)`.
    *   The `ans` array stores `M` integers, contributing `O(M)`.

## Edge Cases
*   **`n=1` (single server)**: The single server will handle all tasks sequentially. `current_time` will always jump to the server's `finish_time` if `available_servers` is empty. The logic correctly handles this.
*   **`m=1` (single task)**: The task is assigned to the best available server. The loop runs once, and the correct server is chosen.
*   **All servers have the same weight**: The tie-breaking rule (smallest index) is naturally handled by Python's tuple comparison in the heap.
*   **All tasks have the same duration**: No special handling needed; the simulation proceeds as usual.
*   **`m < n` (more servers than tasks)**: Some servers might never be used. This is fine; the `available_servers` heap will simply retain those unused servers.
*   **Large `tasks[j]` or `servers[i]` values**: Python's arbitrary-precision integers handle large `finish_time` or `weight` values without overflow.

## Solution

```python
import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)

        # Min-heap for available servers: (weight, index)
        # Prioritizes smallest weight, then smallest index.
        available_servers = []
        for i in range(n):
            heapq.heappush(available_servers, (servers[i], i))

        # Min-heap for busy servers: (finish_time, weight, index)
        # Prioritizes earliest finish_time. For ties in finish_time,
        # weight and index are included for consistent ordering, though
        # they don't affect the "earliest finish time" priority.
        busy_servers = []

        ans = [0] * m
        current_time = 0 # Simulates the current time in seconds

        for task_idx in range(m):
            # Task 'task_idx' arrives at second 'task_idx'.
            # The current simulation time must be at least 'task_idx' to process this task.
            # If current_time < task_idx, it means we processed previous tasks faster than new ones arrived,
            # so we can advance current_time to task_idx.
            current_time = max(current_time, task_idx)

            # Step 1: Release servers that become free by current_time.
            # If there are no available servers, we MUST wait for one to become free.
            # In this case, current_time must advance to the finish_time of the earliest busy server.
            if not available_servers and busy_servers:
                # No free servers, so we must wait. Advance current_time to when the next server becomes free.
                # This is the "wait until a server becomes free" condition.
                current_time = max(current_time, busy_servers[0][0])

            # Move all servers that are now free (finish_time <= current_time)
            # from busy_servers to available_servers.
            while busy_servers and busy_servers[0][0] <= current_time:
                finish_time, server_weight, server_idx = heapq.heappop(busy_servers)
                heapq.heappush(available_servers, (server_weight, server_idx))

            # Step 2: Assign the current task.
            # At this point, 'available_servers' must contain at least one server.
            # This is guaranteed because:
            # 1. If 'available_servers' was initially not empty, it still isn't.
            # 2. If 'available_servers' was empty, we advanced 'current_time' in the 'if' block above
            #    to ensure at least one server became free, so it must have moved from
            #    'busy_servers' to 'available_servers' by the 'while' loop.
            
            # Pop the best available server according to priority (weight, then index).
            server_weight, server_idx = heapq.heappop(available_servers)
            ans[task_idx] = server_idx

            # Calculate its finish time and move it to busy_servers.
            finish_time = current_time + tasks[task_idx]
            heapq.heappush(busy_servers, (finish_time, server_weight, server_idx))
        
        return ans

```

## Why This Works
The solution correctly simulates the task assignment process by maintaining two priority queues that accurately reflect the state of all servers at any given `current_time`. The `current_time` variable ensures that tasks are not processed before their arrival time and that the system waits if no servers are available. By always moving all servers that become free *by* `current_time` to the `available_servers` heap before assigning a task, we guarantee that the task is assigned to the highest-priority server (smallest weight, then smallest index) among all truly available servers at that moment, adhering to all problem rules. This greedy approach works because task assignments are independent and always prioritize the "best" server locally, which also leads to the globally optimal assignment for each task.

---
<sub>Generated 2026-11-07 06:28 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
