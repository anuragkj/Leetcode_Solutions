# [3534] Path Existence Queries in a Graph II

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-07-10 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/)

**Topics:** Array, Two Pointers, Binary Search, Dynamic Programming, Greedy, Bit Manipulation, Graph Theory, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.

You are also given an integer array nums of length n and an integer maxDiff.

An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).

You are also given a 2D integer array queries. For each queries[i] = [u_i, v_i], find the minimum distance between nodes u_i and v_i_. If no path exists between the two nodes, return -1 for that query.

Return an array answer, where answer[i] is the result of the i^th query.

Note: The edges between the nodes are unweighted.

Example 1:

Input: n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]

Output: [1,1]

Explanation:

The resulting graph is:

			Query
			Shortest Path
			Minimum Distance

			[0, 3]
			0 → 3
			1

			[2, 4]
			2 → 4
			1

Thus, the output is [1, 1].

Example 2:

Input: n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]]

Output: [1,2,-1,1]

Explanation:

The resulting graph is:

			Query
			Shortest Path
			Minimum Distance

			[0, 1]
			0 → 1
			1

			[0, 2]
			0 → 1 → 2
			2

			[2, 3]
			None
			-1

			[4, 3]
			3 → 4
			1

Thus, the output is [1, 2, -1, 1].

Example 3:

Input: n = 3, nums = [3,6,1], maxDiff = 1, queries = [[0,0],[0,1],[1,2]]

Output: [0,-1,-1]

Explanation:

There are no edges between any two nodes because:

- Nodes 0 and 1: |nums[0] - nums[1]| = |3 - 6| = 3 > 1

- Nodes 0 and 2: |nums[0] - nums[2]| = |3 - 1| = 2 > 1

- Nodes 1 and 2: |nums[1] - nums[2]| = |6 - 1| = 5 > 1

Thus, no node can reach any other node, and the output is [0, -1, -1].

Constraints:

- 1 <= n == nums.length <= 10^5

- 0 <= nums[i] <= 10^5

- 0 <= maxDiff <= 10^5

- 1 <= queries.length <= 10^5

- queries[i] == [u_i, v_i]

- 0 <= u_i, v_i < n

**Examples / sample tests:**

```
5
[1,8,3,4,2]
3
[[0,3],[2,4]]
5
[5,3,1,9,10]
2
[[0,1],[0,2],[2,3],[4,3]]
3
[3,6,1]
1
[[0,0],[0,1],[1,2]]
```

---

## Problem Summary
You are given `n` nodes, each with a value `nums[i]`. An undirected edge exists between nodes `i` and `j` if `|nums[i] - nums[j]| <= maxDiff`. For several queries `[u, v]`, you need to find the minimum number of edges (shortest path distance) between `u` and `v`. If no path exists, return -1.

## Intuition
The core challenge is that the graph can be dense (many edges), making standard BFS for each query too slow (`O(Q * (N+E))` where `E` can be `O(N^2)`). The constraints (`N, Q <= 10^5`) suggest a solution around `O((N+Q) log N)` or `O((N+Q) log^2 N)`.

The key observation comes from the hint: "Sort the nodes according to `nums[i]`". If we sort the nodes by their `nums` values, say `p_0, p_1, ..., p_{n-1}` such that `nums[p_0] <= nums[p_1] <= ... <= nums[p_{n-1}]`, then for any node `p_i`, its neighbors `p_j` (satisfying `|nums[p_i] - nums[p_j]| <= maxDiff`) will form a **contiguous range** of indices `[L, R]` within this sorted list. This range `[L, R]` can be found efficiently using binary search (or two pointers).

This structure allows us to use **binary lifting (or binary jumping)**, a technique typically used for path queries on trees, but adaptable here. Instead of finding the `2^k`-th ancestor, we find the **range of sorted indices** reachable from a node in `2^k` steps. If node `p_i` can reach any node in the range `[min_idx_A, max_idx_A]` in `2^{k-1}` steps, and each node `p_x` in `[min_idx_A, max_idx_A]` can reach a range `[min_idx_B_x, max_idx_B_x]` in another `2^{k-1}` steps, then `p_i` can reach the union of all `[min_idx_B_x, max_idx_B_x]` in `2^k` steps. This union is simply `[min(min_idx_B_x), max(max_idx_B_x)]`. Finding this min/max over a range is a **Range Minimum/Maximum Query (RMQ)**, which can be efficiently answered using a **Sparse Table**.

By precomputing these reachable ranges for `2^k` steps, we can answer each query by "binary lifting" the path, accumulating steps until the target node `v` is within the reachable range.

## Approach
The solution involves several steps:
1.  **Preprocessing Nodes:**
    *   Create `indexed_nums`: a list of `(nums[i], i)` pairs for all nodes.
    *   Sort `indexed_nums` based on `nums[i]` values. This gives us `sorted_nodes` (original indices in sorted order) and `nums_val_at_sorted_idx` (the `nums` values themselves, sorted).
    *   Create a `pos` array where `pos[original_idx]` gives its index in the `sorted_nodes` array. This allows quick mapping between original node IDs and their sorted positions.

2.  **Binary Lifting Precomputation (Sparse Tables):**
    *

---
<sub>Generated 2026-07-10 04:37 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
