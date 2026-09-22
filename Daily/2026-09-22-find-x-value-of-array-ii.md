# [3525] Find X Value of Array II

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-09-22 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/find-x-value-of-array-ii/)

**Topics:** Array, Math, Segment Tree

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an array of positive integers nums and a positive integer k. You are also given a 2D array queries, where queries[i] = [index_i, value_i, start_i, x_i].

You are allowed to perform an operation once on nums, where you can remove any suffix from nums such that nums remains non-empty.

The x-value of nums for a given x is defined as the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x modulo k.

For each query in queries you need to determine the x-value of nums for x_i after performing the following actions:

- Update nums[index_i] to value_i. Only this step persists for the rest of the queries.

- Remove the prefix nums[0..(start_i - 1)] (where nums[0..(-1)] will be used to represent the empty prefix).

Return an array result of size queries.length where result[i] is the answer for the i^th query.

A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.

A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.

Note that the prefix and suffix to be chosen for the operation can be empty.

Note that x-value has a different definition in this version.

Example 1:

Input: nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]

Output: [2,2,2]

Explanation:

- For query 0, nums becomes [1, 2, 2, 4, 5], and the empty prefix must be removed. The possible operations are:

- Remove the suffix [2, 4, 5]. nums becomes [1, 2].

- Remove the empty suffix. nums becomes [1, 2, 2, 4, 5] with a product 80, which gives remainder 2 when divided by 3.

- For query 1, nums becomes [1, 2, 2, 3, 5], and the prefix [1, 2, 2] must be removed. The possible operations are:

- Remove the empty suffix. nums becomes [3, 5].

- Remove the suffix [5]. nums becomes [3].

- For query 2, nums becomes [1, 2, 2, 3, 5], and the empty prefix must be removed. The possible operations are:

- Remove the suffix [2, 2, 3, 5]. nums becomes [1].

- Remove the suffix [3, 5]. nums becomes [1, 2, 2].

Example 2:

Input: nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]]

Output: [1,0]

Explanation:

- For query 0, nums becomes [2, 2, 4, 8, 16, 32]. The only possible operation is:

- Remove the suffix [2, 4, 8, 16, 32].

- For query 1, nums becomes [2, 2, 4, 8, 16, 32]. There is no possible way to perform the operation.

Example 3:

Input: nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]]

Output: [5]

Constraints:

- 1 <= nums[i] <= 10^9

- 1 <= nums.length <= 10^5

- 1 <= k <= 5

- 1 <= queries.length <= 2 * 10^4

- queries[i] == [index_i, value_i, start_i, x_i]

- 0 <= index_i <= nums.length - 1

- 1 <= value_i <= 10^9

- 0 <= start_i <= nums.length - 1

- 0 <= x_i <= k - 1

**Examples / sample tests:**

```
[1,2,3,4,5]
3
[[2,2,0,2],[3,3,3,0],[0,1,0,1]]
[1,2,4,8,16,32]
4
[[0,2,0,2],[0,2,0,1]]
[1,1,2,1,1]
2
[[2,1,0,1]]
```

---

## Problem Summary
You are given an array `nums`, a modulus `k`, and a list of `queries`. For each query, first update an element in `nums` (this update is permanent). Then, consider a subarray of `nums` starting from a given `start_i`. On this subarray, count how many of its non-empty prefixes have a product that leaves a remainder of `x_i` when divided by `k`.

## Intuition
The core challenge involves two things:
1.  **Point Updates and Range Queries**: We need to update individual elements in `nums` and then query properties of a subarray (`nums[start_i:]`). This immediately suggests a **Segment Tree**.
2.  **Product Modulo `k` for Prefixes**: For a given subarray, we need to find the product modulo `k` for *all* its prefixes. Since `k` is very small (up to 5), we can track information for each possible remainder `0, 1, ..., k-1`.

The key observation is that when merging two segments `[L, M]` and `[M+1, R]` in a segment tree:
*   Prefixes entirely within `[L, M]` contribute directly to the combined result.
*   Prefixes that span across the midpoint, i.e., `nums[L...M]` followed by a prefix of `nums[M+1...R]`, form new prefix products. The product of `nums[L...M]` (let's call it `P_left`) can be multiplied by each prefix product from `nums[M+1...R]` (let's call them `P_right_j`) to get `(P_left * P_right_j) % k`.

This means each segment tree node should store not just the total product of its range, but also the **counts of prefix products for each remainder modulo `k`**.

## Approach
We will use a **Segment Tree** where each node stores information about a contiguous subsegment of `nums`.

1.  **Node Structure**: Each node in our segment tree will be a dictionary with two keys:
    *   `'counts'`: A list of size `k`. `counts[r]` will store the number of prefixes within the node's range whose product modulo `k` is `r`.
    *   `'total_product'`: The product of all elements in the node's range, modulo `k`. This is used when combining with a right segment.

2.  **`create_empty_node()` Helper**: A utility function to return a new node initialized with `counts = [0]*k` and `total_product = 1` (1 is the multiplicative identity).

3.  **`merge(left_node, right_node)` Function**: This is the heart of the segment tree. It takes two child nodes and combines their information to form a parent node.
    *   Handle `None` nodes: If a child node is `None` (meaning its range was outside the query), simply return the other node.
    *   `new_node['total_product'] = (left_node['total_product'] * right_node['total_product']) % k`.
    *   `new_node['counts']` is initialized by copying `left_node['counts']`. These are prefixes entirely within the left segment.
    *   For prefixes that span across the midpoint: Iterate through `r_right` from `0` to `k-1`. If `right_node['counts'][r_right]` is greater than 0, it means there are `right_node['counts'][r_right]` prefixes in the right segment whose product modulo `k` is `r_right`. When these are appended to the full left segment (with product `left_node['total_product']`), their new product modulo `k` will be `(left_node['total_product'] * r_right) % k`. Add these counts to `new_node['counts']` at the appropriate remainder index.

4.  **`build(node_idx, L, R)` Function**:
    *   **Base Case**: If `L == R` (a leaf node representing a single element `nums[L]`):
        *   Create a new node.
        *   `val_mod_k = nums[L] % k`.
        *   Set `node['counts'][val_mod_k] = 1` (the element itself is a prefix).
        *   Set `node['total_product'] = val_mod_k`.
    *   **Recursive Step**: Recursively build the left child (`build(2*node_idx, L, M)`) and the right child (`build(2*node_idx+1, M+1, R)`), then `merge` their results to populate the current node `tree[node_idx]`.

5.  **`update(node_idx, L, R, target_idx, new_val)` Function**:
    *   **Base Case**: If `L == R == target_idx` (found the leaf node to update):
        *   Create a new node for `new_val`.
        *   `val_mod_k = new_val % k`.
        *   Set `node['counts'][val_mod_k] = 1` and `node['total_product'] = val_mod_k`.
    *   **Recursive Step**: If `target_idx` is in the left half, recurse left; otherwise, recurse right. After the child is updated, `merge` its children to update the current node `tree[node_idx]`.

6.  **`query(node_idx, L, R, query_L, query_R)` Function**:
    *   **No Overlap**: If the current segment `[L, R]` is completely outside the query range `[query_L, query_R]`, return `None`.
    *   **Full Overlap**: If the current segment `[L, R]` is completely inside the query range, return `tree[node_idx]`.
    *   **Partial Overlap**: Recursively query the left child and the right child. Then `merge` their results.

7.  **Main Logic**:
    *   Initialize the segment tree by calling `build(1, 0, N-1)`.
    *   For each query `[index_i, value_i, start_i, x_i]`:
        *   Update the `nums` array at `index_i` to `value_i` (this is persistent).
        *   Call `update(1, 0, N-1, index_i, value_i)` to reflect this change in the segment tree.
        *   The effective array for the operation is `nums[start_i ... N-1]`. If `start_i >= N`, the effective array is empty, so there are 0 ways.
        *   Call `query(1, 0, N-1, start_i, N-1)` to get the combined node for this range.
        *   The answer for the query is `result_node['counts'][x_i]`. Append this to the `results` list.

## Visualization
```mermaid
graph TD
    A[Root: [0, N-1]] --> B[Left Child: [0, M]]
    A --> C[Right Child: [M+1, N-1]]

    subgraph Segment Tree Node Structure
        Node{{Node}}
        Node -- "counts: [c0, c1, ..., c(k-1)]" --> CountsList
        Node -- "total_product: P_total" --> TotalProduct
    end

    subgraph Merge Operation (A = merge(B, C))
        B_counts[B.counts]
        B_total_product[B.total_product]
        C_counts[C.counts]

        B_counts --> A_counts_initial[A.counts = B.counts]
        B_total_product & C_counts --> A_counts_updated[For each r_C in C.counts: A.counts[(B.total_product * r_C) % k] += C.counts[r_C]]
        B_total_product & C_total_product[C.total_product] --> A_total_product[A.total_product = (B.total_product * C.total_product) % k]
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
```
**Explanation**:
*   The Segment Tree recursively divides the array into halves.
*   Each node (like A, B, C) stores `counts` (an array of size `k` for remainders `0` to `k-1`) and `total_product` (product of its range modulo `k`).
*   When `merge(B, C)` creates `A`:
    1.  `A.total_product` is simply `(B.total_product * C.total_product) % k`.
    2.  `A.counts` initially copies all counts from `B.counts` (these are prefixes entirely within the left segment).
    3.  Then, for each remainder `r_C` that appears in `C.counts`, we calculate a new remainder `(B.total_product * r_C) % k`. This represents a prefix that starts in `B` and extends into `C`. We add `C.counts[r_C]` to `A.counts` at this new remainder index.

## Dry Run
Let's trace Example 1: `nums = [1,2,3,4,5]`, `k = 3`.
Initial `build` will create a segment tree. For brevity, let's just show the `query` for the first query.

**Query 0**: `[2,2,0,2]`
1.  **Update**: `nums[2]` becomes `2`. `nums` is now `[1,2,2,4,5]`.
    `update(1, 0, 4, 2, 2)` is called. The leaf for index 2 is updated. All parent nodes up to root are re-merged.
    The segment tree now reflects `[1,2,2,4,5]`.
2.  **Prefix Removal**: `start_i = 0`. Effective array is `nums[0...4]` i.e., `[1,2,2,4,5]`.
3.  **Query**: `query(1, 0, 4, 0, 4)` is called. This will return a node representing the entire array `[1,2,2,4,5]`.
    Let's manually calculate prefixes for `[1,2,2,4,5]` modulo `k=3`:
    *   `[1]` -> `1 % 3 = 1`
    *   `[1,2]` -> `(1*2) % 3 = 2`
    *   `[1,2,2]` -> `(2*2) % 3 = 1`
    *   `[1,2,2,4]` -> `(1*4) % 3 = 1`
    *   `[1,2,2,4,5]` -> `(1*5) % 3 = 2`
    The resulting node from `query` will have:
    `result_node['counts'] = [0, 3, 2]` (3 prefixes yield 1, 2 prefixes yield 2)
    `result_node['total_product'] = 2` (product of `[1,2,2,4,5]` is 80, `80 % 3 = 2`)
4.  **x-value**: `x_i = 2`. The answer is `result_node['counts'][2] = 2`.
    `results = [2]`

**Query 1**: `[3,3,3,0]`
1.  **Update**: `nums[3]` becomes `3`. `nums` is now `[1,2,2,3,5]`.
    `update(1, 0, 4, 3, 3)` is called. Segment tree updated.
2.  **Prefix Removal**: `start_i = 3`. Effective array is `nums[3...4]` i.e., `[3,5]`.
3.  **Query**: `query(1, 0, 4, 3, 4)` is called. This will return a node for `[3,5]`.
    Prefixes for `[3,5]` modulo `k=3`:
    *   `[3]` -> `3 % 3 = 0`
    *   `[3,5]` -> `(0*5) % 3 = 0`
    The resulting node from `query` will have:
    `result_node['counts'] = [2, 0, 0]` (2 prefixes yield 0)
    `result_node['total_product'] = 0` (product of `[3,5]` is 15, `15 % 3 = 0`)
4.  **x-value**: `x_i = 0`. The answer is `result_node['counts'][0] = 2`.
    `results = [2, 2]`

**Query 2**: `[0,1,0,1]`
1.  **Update**: `nums[0]` becomes `1`. `nums` is now `[1,2,2,3,5]` (no actual change from previous query, but update still happens).
    `update(1, 0, 4, 0, 1)` is called. Segment tree updated.
2.  **Prefix Removal**: `start_i = 0`. Effective array is `nums[0...4]` i.e., `[1,2,2,3,5]`.
3.  **Query**: `query(1, 0, 4, 0, 4)` is called. This will return a node for `[1,2,2,3,5]`.
    Prefixes for `[1,2,2,3,5]` modulo `k=3`:
    *   `[1]` -> `1 % 3 = 1`
    *   `[1,2]` -> `(1*2) % 3 = 2`
    *   `[1,2,2]` -> `(2*2) % 3 = 1`
    *   `[1,2,2,3]` -> `(1*3) % 3 = 0`
    *   `[1,2,2,3,5]` -> `(0*5) % 3 = 0`
    The resulting node from `query` will have:
    `result_node['counts'] = [2, 2, 1]` (2 prefixes yield 0, 2 prefixes yield 1, 1 prefix yields 2)
    `result_node['total_product'] = 0` (product of `[1,2,2,3,5]` is 60, `60 % 3 = 0`)
4.  **x-value**: `x_i = 1`. The answer is `result_node['counts'][1] = 2`.
    `results = [2, 2, 2]`

Final Result: `[2,2,2]`. Matches example output.

## Complexity
*   **Time Complexity**:
    *   Building the segment tree takes `O(N * k)` time, as there are `O(N)` nodes and each `merge` operation takes `O(k)` time.
    *   Each `update` operation takes `O(log N * k)` time, traversing `O(log N)` nodes and performing `O(k)` work per node.
    *   Each `query` operation takes `O(log N * k)` time for the same reason.
    *   Total time complexity: `O(N * k + Q * log N * k)`, where `N` is `nums.length` and `Q` is `queries.length`.
    *   Given `N=10^5`, `Q=2*10^4`, `k=5`: `10^5 * 5 + 2*10^4 * log(10^5) * 5` is approximately `5*10^5 + 2*10^4 * 17 * 5` which is roughly `5*10^5 + 1.7*10^6 = 2.2 * 10^6` operations, well within typical time limits.
*   **Space Complexity**:
    *   The segment tree stores `O(N)` nodes. Each node stores a `counts` array of size `k`.
    *   Total space complexity: `O(N * k)`.
    *   Given `N=10^5`, `k=5`: `4 * 10^5 * 5 = 2 * 10^6` integers, which is acceptable.

## Edge Cases
*   **`k = 1`**: All products modulo 1 are 0. If `x_i = 0`, the answer will be the number of non-empty prefixes in the effective array. If `x_i != 0`, the answer is 0. The segment tree correctly handles `val % 1 = 0` and `(P * r) % 1 = 0`.
*   **`start_i = N - 1`**: The effective array is `[nums[N-1]]`. The query range is `[N-1, N-1]`, which is a single leaf node. The solution correctly processes this.
*   **`start_i >= N`**: The effective array is empty. No non-empty suffixes can be removed. The problem statement implies the remaining array must be non-empty. My solution explicitly checks `start_i >= N` and returns 0, which is correct.
*   **All elements are multiples of `k`**: All products will be `0 % k`. If `x_i = 0`, the answer will be the number of non-empty prefixes. If `x_i != 0`, the answer is 0. The modulo arithmetic handles this naturally.
*   **`nums` contains `1`**: `1 % k` is `1`. `(P * 1) % k = P % k`. `1` acts as a multiplicative identity. The logic correctly propagates this.

## Solution
```python
import collections
from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        N = len(nums)
        
        # Segment Tree Node structure
        # Each node stores:
        # 1. 'counts': A list of size k, where counts[r] is the number of prefixes
        #    in the node's range whose product modulo k is r.
        # 2. 'total_product': The product of all elements in the node's range, modulo k.
        #    Initialized to 1 for multiplication identity.
        
        # Helper function to create an empty node
        def create_empty_node():
            return {'counts': [0] * k, 'total_product': 1}

        # Segment Tree array. Size 4*N is a common safe upper bound for a 1-indexed tree.
        tree = [None] * (4 * N)

        # Merge function for two child nodes
        # Combines the information from left_node and right_node into a new parent node.
        def merge(left_node, right_node):
            # If one of the nodes is None (representing an out-of-query-range segment),
            # return the other node. If both are None, this case should not happen
            # in a valid query range.
            if left_node is None:
                return right_node
            if right_node is None:
                return left_node

            new_node = create_empty_node()
            
            # 1. Calculate the total product of the combined segment.
            new_node['total_product'] = (left_node['total_product'] * right_node['total_product']) % k
            
            # 2. Add counts from left_node. These are prefixes that are entirely
            #    within the left segment.
            for r in range(k):
                new_node['counts'][r] = left_node['counts'][r]
            
            # 3. Add counts from right_node, combined with left_node's full product.
            #    These are prefixes that *span* across the midpoint, starting in the
            #    left segment and extending into the right segment.
            #    Each prefix product 'r_right' from the right segment, when preceded
            #    by the full product of the left segment 'left_prod_full',
            #    results in a new product '(left_prod_full * r_right) % k'.
            left_prod_full = left_node['total_product']
            for r_right in range(k):
                if right_node['counts'][r_right] > 0:
                    new_remainder = (left_prod_full * r_right) % k
                    new_node['counts'][new_remainder] += right_node['counts'][r_right]
            
            return new_node

        # Build the segment tree recursively
        # node_idx: current node's index in the tree array
        # L, R: range [L, R] covered by the current node
        def build(node_idx, L, R):
            if L == R: # Base case: Leaf node for a single element
                node = create_empty_node()
                val_mod_k = nums[L] % k
                node['counts'][val_mod_k] = 1 # This element itself is a prefix
                node['total_product'] = val_mod_k
                tree[node_idx] = node
                return
            
            M = (L + R) // 2
            build(2 * node_idx, L, M) # Build left child
            build(2 * node_idx + 1, M + 1, R) # Build right child
            tree[node_idx] = merge(tree[2 * node_idx], tree[2 * node_idx + 1]) # Merge children

        # Update an element in the segment tree
        # target_idx: index of the element to update
        # new_val: new value for nums[target_idx]
        def update(node_idx, L, R, target_idx, new_val):
            if L == R: # Base case: Found the leaf node corresponding to target_idx
                node = create_empty_node()
                val_mod_k = new_val % k
                node['counts'][val_mod_k] = 1
                node['total_product'] = val_mod_k
                tree[node_idx] = node
                return
            
            M = (L + R) // 2
            if target_idx <= M: # Target is in the left child's range
                update(2 * node_idx, L, M, target_idx, new_val)
            else: # Target is in the right child's range
                update(2 * node_idx + 1, M + 1, R, target_idx, new_val)
            
            # After updating child, re-merge to update current node
            tree[node_idx] = merge(tree[2 * node_idx], tree[2 * node_idx + 1])

        # Query a range in the segment tree
        # query_L, query_R: the range [query_L, query_R] for which to get information
        def query(node_idx, L, R, query_L, query_R):
            # If the current segment [L, R] is completely outside the query range [query_L, query_R]
            if query_L > R or query_R < L:
                return None # Return None, which merge function treats as an identity element
            
            # If the current segment [L, R] is completely inside the query range
            if query_L <= L and R <= query_R:
                return tree[node_idx]
            
            # Otherwise, the query range partially overlaps or spans across children
            M = (L + R) // 2
            left_res = query(2 * node_idx, L, M, query_L, query_R)
            right_res = query(2 * node_idx + 1, M + 1, R, query_L, query_R)
            
            # Merge results from children
            return merge(left_res, right_res)

        # --- Main Logic ---
        # 1. Initial build of the segment tree based on the initial nums array
        build(1, 0, N - 1)
        
        results = []
        for index_i, value_i, start_i, x_i in queries:
            # Step 1: Update nums[index_i] to value_i. This update persists.
            # Update the original nums array (conceptually) and the segment tree.
            nums[index_i] = value_i 
            update(1, 0, N - 1, index_i, value_i)
            
            # Step 2: Determine the effective array for the operation.
            # Remove prefix nums[0..(start_i - 1)] means we consider nums[start_i ... N-1].
            # If start_i is N or greater, the effective array is empty, so no operations are possible.
            if start_i >= N:
                results.append(0)
                continue

            # Step 3: Query the segment tree for the effective range [start_i, N-1].
            # The result_node will contain the 'counts' of prefix products for this subarray.
            result_node = query(1, 0, N - 1, start_i, N - 1)
            
            # Step 4: The x-value is the count of prefixes whose product modulo k is x_i.
            results.append(result_node['counts'][x_i])
            
        return results

```

## Why This Works
The segment tree efficiently maintains the required information (counts of prefix products modulo `k`) across the array. The `merge` operation is designed to correctly combine this information from two adjacent segments: it accounts for prefixes entirely within the left segment, and also for new prefixes formed by taking the full product of the left segment and extending it with prefixes from the right segment. Because `k` is very small, the `O(k)` work per segment tree node is constant-time for practical purposes, making point updates and range queries highly efficient (`O(log N)`). This allows us to answer each query in logarithmic time relative to the array size, after an initial linear-time build.

---
<sub>Generated 2026-09-22 05:18 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
