# [1606] Find Servers That Handled Most Number of Requests

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-11-09 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/)

**Topics:** Array, Heap (Priority Queue), Simulation, Ordered Set

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You have k servers numbered from 0 to k-1 that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but cannot handle more than one request at a time. The requests are assigned to servers according to a specific algorithm:

- The i^th (0-indexed) request arrives.

- If all servers are busy, the request is dropped (not handled at all).

- If the (i % k)^th server is available, assign the request to that server.

- Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the i^th server is busy, try to assign the request to the (i+1)^th server, then the (i+2)^th server, and so on.

You are given a strictly increasing array arrival of positive integers, where arrival[i] represents the arrival time of the i^th request, and another array load, where load[i] represents the load of the i^th request (the time it takes to complete). Your goal is to find the busiest server(s). A server is considered busiest if it handled the most number of requests successfully among all the servers.

Return a list containing the IDs (0-indexed) of the busiest server(s). You may return the IDs in any order.

Example 1:

Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3]
Output: [1]
Explanation:
All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.

Example 2:

Input: k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
Output: [0]
Explanation:
The first 3 requests are handled by first 3 servers.
Request 3 comes in. It is handled by server 0 since the server is available.
Server 0 handled two requests, while servers 1 and 2 handled one request each. Hence server 0 is the busiest server.

Example 3:

Input: k = 3, arrival = [1,2,3], load = [10,12,11]
Output: [0,1,2]
Explanation: Each server handles a single request, so they are all considered the busiest.

Constraints:

- 1 <= k <= 10^5

- 1 <= arrival.length, load.length <= 10^5

- arrival.length == load.length

- 1 <= arrival[i], load[i] <= 10^9

- arrival is strictly increasing.

**Examples / sample tests:**

```
3
[1,2,3,4,5]
[5,2,3,3,3]
3
[1,2,3,4]
[1,2,1,2]
3
[1,2,3]
[10,12,11]
```

---

## Problem Summary
We have `k` servers and `N` requests. Each request arrives at a specific time and has a load (duration). Servers can only handle one request at a time. Requests are assigned to servers based on a specific rule: first try server `i % k`, then `(i % k) + 1`, wrapping around, to find the next available server. If all servers are busy, the request is dropped. The goal is to find which server(s) handled the most requests.

## Intuition
This problem is a **simulation**. We need to process requests in chronological order of their arrival. The core challenges are:
1.  **Tracking server availability**: Servers become free when their current task finishes. We need an efficient way to know which servers are busy and when they will become free. A **min-heap** storing `(finish_time, server_id)` pairs is perfect for this, as it allows us to quickly identify servers that become free earliest.
2.  **Efficiently finding the next available server**: The assignment rule requires finding the "next available server" starting from `i % k`, wrapping around. A naive linear scan through `k` servers for each request would be `O(N*K)`, which is too slow for `N, K = 10^5`. We need a data structure that can:
    *   Store the IDs of currently available servers.
    *   Efficiently find the smallest available server ID greater than or equal to a target ID (e.g., `i % k`).
    *   If no such server exists, efficiently find the smallest available server ID (wrapping around).
    *   Add and remove server IDs efficiently.
    An **ordered set** (like `std::set` in C++ or `TreeSet` in Java) provides these operations in `O(log K)` time. In Python, without external libraries like `sortedcontainers.SortedList`, we can implement this functionality using a **Segment Tree**. A segment tree can maintain the count of available servers in ranges and efficiently query for the first available server in a given range.

## Approach
We will simulate the process using a min-heap for busy servers and a segment tree for available servers.

1.  **Initialization**:
    *   `request_counts = [0] * k`: An array to store the number of requests handled by each server.
    *   `busy_servers = []`: A min-heap to store `(finish_time, server_id)` for servers currently handling a request. The heap is ordered by `finish_time`.
    *   `segment_tree`: A segment tree initialized over the range `[0, k-1]`. Each leaf `i` represents server `i`. A leaf value of `1` means server `i` is available, `0` means it's busy. Internal nodes store the sum of their children (total available servers in their range). Initially, all servers are available, so all leaves are `1`.

2.  **Process Requests**: Iterate through each request `i` from `0` to `N-1`:
    *   Get `current_arrival_time = arrival[i]` and `current_load = load[i]`.
    *   **Free up servers**: While `busy_servers` is not empty and the earliest `finish_time` (`busy_servers[0][0]`) is less than or equal to `current_arrival_time`:
        *   Pop `(finish_time, server_id)` from `busy_servers`.
        *   Mark `server_id` as available in the `segment_tree` (update its leaf value to `1`).
    *   **Check for dropped request**: If the `segment_tree`'s root value is `0` (meaning no servers are available), the request is dropped. Continue to the next request.
    *   **Find target server**:
        *   Calculate `preferred_server_start_idx = i % k`.
        *   **Query the Segment Tree**:
            *   First, try to find the smallest available `server_id` in the range `[preferred_server_start_idx, k-1]` using `segment_tree.query(preferred_server_start_idx)`.
            *   If this returns `-1` (no server found in that range), it means we need to wrap around. Query the segment tree again for the smallest available `server_id` in the range `[0, k-1]` using `segment_tree.query(0)`. This will always succeed if the tree's root value is not `0`.
        *   Let the found server be `assigned_server_id`.
    *   **Assign request**:
        *   Mark `assigned_server_id` as busy in the `segment_tree` (update its leaf value to `0`).
        *   Increment `request_counts[assigned_server_id]`.
        *   Calculate `finish_time = current_arrival_time + current_load`.
        *   Push `(finish_time, assigned_server_id)` onto `busy_servers`.

3.  **Find Busiest Servers**:
    *   Find `max_requests = max(request_counts)`.
    *   Collect all `server_id`s where `request_counts[server_id] == max_requests`.
    *   Return this list.

## Visualization
Let's visualize the segment tree and its operations.
A segment tree for `k=3` servers (0, 1, 2) initially all available:

```
Segment Tree (values are counts of available servers in range):

             [3] (range 0-2)
            /   \
  (node 2) [2] (range 0-1)  (node 3) [1] (range 2-2)
          /   \
(node 4) [1] (range 0-0) (node 5) [1] (range 1-1)
```

**Scenario: Request `i` arrives, `i%k = 0`. Server 0 is assigned.**

1.  **Update Segment Tree**: Mark server 0 as busy (value `0`).
    *   `update(server_id=0, value=0)`:
        *   Leaf for server 0 (node 4) changes from `1` to `0`.
        *   Parent node 2 (range 0-1) sum becomes `0 + 1 = 1`.
        *   Root node 1 (range 0-2) sum becomes `1 + 1 = 2`.

    ```
             [2] (range 0-2)
            /   \
  (node 2) [1] (range 0-1)  (node 3) [1] (range 2-2)
          /   \
(node 4) [0] (range 0-0) (node 5) [1] (range 1-1)
    ```

2.  **Query Segment Tree**: Find smallest available server `>= 0`.
    *   `query(target_idx=0)`:
        *   Start at root (node 1, range 0-2). Count `2 > 0`. `target_idx=0 <= mid=1`. Go left (node 2, range 0-1).
        *   Node 2 (range 0-1). Count `1 > 0`. `target_idx=0 <= mid=0`. Go left (node 4, range 0-0).
        *   Node 4 (range 0-0). Count `0`. Return `-1`. (Server 0 is busy)
        *   Back to Node 2. Left child failed. `target_idx=0 <= end=1`. Go right (node 5, range 1-1).
        *   Node 5 (range 1-1). Count `1 > 0`. This is a leaf. Return `1`. (Server 1 is available)
    *   Result: `assigned_server_id = 1`.

This illustrates how the segment tree efficiently finds the next available server, even with wrap-around logic.

## Dry Run
Example 1: `k = 3`, `arrival = [1,2,3,4,5]`, `load = [5,2,3,3,3]`

**Initial State:**
*   `request_counts = [0, 0, 0]`
*   `busy_servers = []`
*   `segment_tree`: All servers `[0, 1, 2]` are available. Root count = 3.

| Req `i` | `arrival[i]` | `load[i]` | `i%k` | Free Servers | `busy_servers` (heap) | `segment_tree` (available servers) | `request_counts` | Action |
| :------ | :----------- | :-------- | :---- | :----------- | :-------------------- | :--------------------------------- | :--------------- | :----- |
| Init    |              |           |       |              | `[]`                  | `[0,1,2]`                          | `[0,0,0]`        |        |
| **0**   | 1            | 5         | 0     | None         | `[]`                  | `[0,1,2]`                          | `[0,0,0]`        | `arrival=1`. `i%k=0`. `query(0)` finds `0`. Assign `0`. `busy_servers.push((6,0))`. `segment_tree.update(0,0)`. |
|         |              |           |       |              | `[(6, 0)]`            | `[1,2]`                            | `[1,0,0]`        |        |
| **1**   | 2            | 2         | 1     | None         | `[(6, 0)]`            | `[1,2]`                            | `[1,0,0]`        | `arrival=2`. `i%k=1`. `query(1)` finds `1`. Assign `1`. `busy_servers.push((4,1))`. `segment_tree.update(1,0)`. |
|         |              |           |       |              | `[(4, 1), (6, 0)]`    | `[2]`                              | `[1,1,0]`        |        |
| **2**   | 3            | 3         | 2     | None         | `[(4, 1), (6, 0)]`    | `[2]`                              | `[1,1,0]`        | `arrival=3`. `i%k=2`. `query(2)` finds `2`. Assign `2`. `busy_servers.push((6,2))`. `segment_tree.update(2,0)`. |
|         |              |           |       |              | `[(4, 1), (6, 0), (6, 2)]` | `[]`                               | `[1,1,1]`        |        |
| **3**   | 4            | 3         | 0     | Server 1     | `[(6, 0), (6, 2)]`    | `[1]`                              | `[1,1,1]`        | `arrival=4`. `busy_servers[0][0]=4 <= 4`. Pop `(4,1)`. `segment_tree.update(1,1)`. `i%k=0`. `query(0)` finds `1`. Assign `1`. `busy_servers.push((7,1))`. `segment_tree.update(1,0)`. |
|         |              |           |       |              | `[(6, 0), (6, 2), (7, 1)]` | `[]`                               | `[1,2,1]`        |        |
| **4**   | 5            | 3         | 1     | None         | `[(6, 0), (6, 2), (7, 1)]` | `[]`                               | `[1,2,1]`        | `arrival=5`. `busy_servers[0][0]=6 > 5`. No servers freed. `segment_tree` root count is `0`. Request dropped. |
| **Final** |              |           |       |              |                       |                                    | `[1,2,1]`        | `max_requests = 2`. Server `1` handled 2 requests. |

Final Result: `[1]`

## Complexity
*   **Time Complexity**: `O(N log K)`.
    *   Each of the `N` requests involves:
        *   Popping from `busy_servers` (heap): `O(log K)`. In total, each server is pushed/popped at most `N` times from the heap, but more accurately, each request causes one push, and each server is freed once per request it handles. The total number of heap operations is `O(N)`.
        *   Updating the segment tree (marking available/busy): `O(log K)`. Total `O(N log K)`.
        *   Querying the segment tree (finding an available server): `O(log K)`. Total `O(N log K)`.
    *   Therefore, the dominant factor is `N` operations, each taking `O(log K)` time.
*   **Space Complexity**: `O(K)`.
    *   `request_counts` array: `O(K)`.
    *   `busy_servers` heap: Stores at most `K` items (one for each server). `O(K)`.
    *   `segment_tree`: Uses `O(K)` space for its internal array. `O(K)`.

## Edge Cases
*   **`k=1`**: Only one server. All requests go to it unless it's busy. The segment tree and heap handle this correctly.
*   **All servers busy**: The `segment_tree.query` will return `-1` even after wrapping around (as the root count will be 0), and the request will be dropped. Correctly handled.
*   **All servers handle 0 requests**: `max_requests` will be 0, and all server IDs `0..k-1` will be returned. Correctly handled.
*   **All servers handle the same number of requests**: All server IDs `0..k-1` will be returned. Correctly handled.
*   **Large `arrival[i]` and `load[i]`**: `finish_time` can be up to `2 * 10^9`. Python integers handle arbitrary size, so no overflow issues.

## Solution

```python
import heapq

# Helper class for Segment Tree
class SegmentTree:
    def __init__(self, k: int):
        self.k = k
        # Tree array size: 4*k is a common safe upper bound for segment trees
        self.tree = [0] * (4 * k) 
        # Build the tree: initially all servers are available (value 1)
        self._build(1, 0, k - 1)

    # Recursively build the segment tree
    # node: current node index in self.tree
    # start, end: range covered by the current node
    def _build(self, node: int, start: int, end: int):
        if start == end:
            # Leaf node: server 'start' is initially available
            self.tree[node] = 1
        else:
            mid = (start + end) // 2
            # Build left child
            self._build(2 * node, start, mid)
            # Build right child
            self._build(2 * node + 1, mid + 1, end)
            # Internal node: sum of children's values (total available servers in range)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    # Update the state of a server (available/busy)
    # node: current node index
    # start, end: range covered by current node
    # idx: server ID to update
    # val: 1 for available, 0 for busy
    def update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            # Found the leaf node for server 'idx'
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                # Server 'idx' is in the left child's range
                self.update(2 * node, start, mid, idx, val)
            else:
                # Server 'idx' is in the right child's range
                self.update(2 * node + 1, mid + 1, end, idx, val)
            # Update current node's value after children are updated
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    # Query to find the smallest available server ID >= query_start
    # node: current node index
    # start, end: range covered by current node
    # query_start: the minimum server ID we are looking for
    def query(self, node: int, start: int, end: int, query_start: int) -> int:
        # If no available servers in this segment, or segment is entirely before query_start
        if self.tree[node] == 0 or end < query_start:
            return -1
        
        # If we are at a leaf node and it's available
        if start == end:
            return start # This server is available and is the first in its range
        
        mid = (start + end) // 2
        
        res = -1
        # Try left child first if its range overlaps with query_start
        if query_start <= mid:
            res = self.query(2 * node, start, mid, query_start)
            if res != -1:
                return res
        
        # If left child didn't find anything, or query_start is in right child's range
        # Ensure we search from max(query_start, mid + 1) for the right child
        return self.query(2 * node + 1, mid + 1, end, max(query_start, mid + 1))


class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        request_counts = [0] * k
        
        # busy_servers: min-heap of (finish_time, server_id)
        # Stores servers that are currently busy, ordered by when they become free.
        busy_servers = [] 
        
        # segment_tree: Manages available servers.
        # Allows O(log K) update (mark busy/available) and query (find first available >= target).
        segment_tree = SegmentTree(k)
        
        n = len(arrival)
        
        for i in range(n):
            current_arrival_time = arrival[i]
            current_load = load[i]
            
            # Step 1: Free up servers whose tasks have finished by current_arrival_time
            # Pop all servers from busy_servers whose finish_time is <= current_arrival_time
            while busy_servers and busy_servers[0][0] <= current_arrival_time:
                _finish_time, server_id = heapq.heappop(busy_servers)
                # Mark this server as available in the segment tree
                segment_tree.update(1, 0, k - 1, server_id, 1) # 1 for available
            
            # Step 2: If no servers are available, drop the request
            # The root of the segment tree stores the total count of available servers
            if segment_tree.tree[1] == 0:
                continue # Request dropped
            
            # Step 3: Find the target server according to the assignment rules
            # Preferred server index: i % k
            preferred_server_start_idx = i % k
            
            assigned_server_id = -1
            
            # Try to find a server >= preferred_server_start_idx
            assigned_server_id = segment_tree.query(1, 0, k - 1, preferred_server_start_idx)
            
            if assigned_server_id == -1:
                # No server found in the range [preferred_server_start_idx, k-1].
                # Wrap around and find the smallest available server (which must be >= 0).
                assigned_server_id = segment_tree.query(1, 0, k - 1, 0)
            
            # Step 4: Assign the request to the chosen server
            # Mark the assigned server as busy in the segment tree
            segment_tree.update(1, 0, k - 1, assigned_server_id, 0) # 0 for busy
            request_counts[assigned_server_id] += 1
            
            finish_time = current_arrival_time + current_load
            heapq.heappush(busy_servers, (finish_time, assigned_server_id))
        
        # Step 5: Find the busiest server(s)
        max_requests = 0
        if request_counts: # k >= 1, so request_counts will not be empty
            max_requests = max(request_counts)
        
        busiest_server_ids = []
        for server_id in range(k):
            if request_counts[server_id] == max_requests:
                busiest_server_ids.append(server_id)
                
        return busiest_server_ids

```

## Why This Works
This solution correctly simulates the request assignment process by maintaining two key pieces of state:
1.  **`busy_servers` (min-heap)**: This efficiently tracks servers that are currently occupied and, crucially, when they will become free. By always popping the server with the earliest `finish_time`, we ensure that `available_servers` is always up-to-date with respect to the `current_arrival_time`.
2.  **`segment_tree` (for available servers)**: This data structure is central to achieving the required time complexity. It acts as an efficient "ordered set" of available server IDs.
    *   Its `update` operation allows marking a server as busy or available in `O(log K)` time.
    *   Its `query` operation efficiently finds the smallest available server ID that meets the criteria (either `>= i % k` or `>= 0` for wrap-around) in `O(log K)` time. This avoids the `O(K)` linear scan that would lead to a Time Limit Exceeded error.

By combining these two efficient data structures, each request is processed in `O(log K)` time, leading to an overall `O(N log K)` solution, which is optimal for the given constraints. The `request_counts` array correctly aggregates the total requests handled by each server, allowing for a straightforward final determination of the busiest server(s).

---
<sub>Generated 2026-11-09 07:05 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
