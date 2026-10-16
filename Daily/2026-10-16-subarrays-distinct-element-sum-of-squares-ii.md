# [2916] Subarrays Distinct Element Sum of Squares II

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-10-16 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/)

**Topics:** Array, Hash Table, Binary Indexed Tree, Segment Tree

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

- Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].

Return the sum of the squares of distinct counts of all subarrays of nums.

Since the answer may be very large, return it modulo 10^9 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 1^2 + 1^2 + 1^2 + 2^2 + 2^2 + 2^2 = 15.

Example 2:

Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 1^2 + 1^2 + 1^2 = 3.

Constraints:

- 1 <= nums.length <= 10^5

- 1 <= nums[i] <= 10^5

**Examples / sample tests:**

```
[1,2,1]
[2,2]
```

---

## Problem Summary
The problem asks us to calculate the sum of the squares of distinct counts for all possible subarrays of a given integer array `nums`. A subarray's distinct count is the number of unique values it contains. Since the total sum can be very large, we must return the result modulo `10^9 + 7`.

## Intuition
A naive approach of iterating through all `O(N^2)` subarrays and for each, counting distinct elements in `O(N)` time (using a hash set) would lead to an `O(N^3)` solution, which is too slow for `N=10^5`. An `O(N^2)` approach (e.g., sliding window with a frequency map for each subarray) is also too slow. We need something closer to `O(N log N)`.

Let's fix the right endpoint `j` and iterate `j` from `0` to `N-1`. For each `j`, we want to calculate `sum(f(i, j)^2)` for all `0 <= i <= j`, where `f(i, j)` is the distinct count of `nums[i..j]`. The total answer will be the sum of these `sum(f(i, j)^2)` values over all `j`.

Consider how `f(i, j)` changes when we move from `j-1` to `j`.
When we process `nums[j]`:
1.  For any subarray `nums[i..j-1]`, its distinct count `f(i, j-1)` might increase by 1 to become `f(i, j)` if `nums[j]` is a new element in `nums[i..j-1]`.
2.  If `nums[j]` has appeared before at `prev_idx = last_occurrence[nums[j]]`, then for `i <= prev_idx`, `nums[j]` is already present in `nums[i..j-1]`. So, `f(i, j) = f(i, j-1)`.
3.  For `i` such that `prev_idx < i <= j-1`, `nums[j]` is *not* present in `nums[i..j-1]`. So, `f(i, j) = f(i, j-1) + 1`.
4.  For the new subarray `nums[j..j]`, its distinct count `f(j, j)` is always 1.

Notice that the distinct counts `f(i, j)` for `i` in the range `[prev_idx + 1, j]` all increase by 1 (or become 1 if `i=j` and `f(j, j-1)` was implicitly 0). This is a **range update** operation. We need to maintain these `f(i, j)` values and efficiently query the sum of their squares.

A **Segment Tree with Lazy Propagation** is perfect for this. Each node in the segment tree will store:
*   The count of elements in its range.
*   The sum of `f(i, j)` values (`sum_val`).
*   The sum of squares of `f(i, j)` values (`sum_sq_val`).
*   A `lazy_add` value representing a pending addition to all elements in its range.

When we add `C` to a range of values `x_k`:
*   The new sum `sum(x_k + C)` becomes `sum(x_k) + C * count`.
*   The new sum of squares `sum((x_k + C)^2)` becomes `sum(x_k^2 + 2Cx_k + C^2) = sum(x_k^2) + 2C * sum(x_k) + C^2 * count`.
This allows us to update `sum_val` and `sum_sq_val` efficiently in `O(log N)` time per range update.

## Approach
We will use a segment tree with lazy propagation to maintain the distinct counts `f(i, j)` for all `0 <= i <= j` for the current `j`.

1.  **Initialization**:
    *   Set `MOD = 10^9 + 7`.
    *   Initialize `total_sum_sq_of_distinct_counts = 0`.
    *   Create a `SegmentTree` instance for `N` elements (indices `0` to `N-1`). Each node in the tree will store `[sum_val, sum_sq_val, lazy_add]`, all initialized to `0`.
    *   Initialize `last_occurrence = {}` to store the last seen index for each number (`value -> index`).

2.  **Iterate through `nums`**: For each index `j` from `0` to `N-1`:
    a.  Let `val = nums[j]`.
    b.  Find `prev_idx = last_occurrence.get(val, -1)`. This is the last index where `val` appeared. If `val` hasn't appeared before, `prev_idx` will be `-1`.
    c.  **Update Segment Tree**: Call `segment_tree.update_range(prev_idx + 1, j, 1)`. This operation adds `1` to the distinct count for all subarrays `nums[k..j]` where `k` is in the range `[prev_idx + 1, j]`.
        *   For `k` from `prev_idx + 1` to `j-1`, `nums[j]` is a new distinct element, so `f(k, j)` becomes `f(k, j-1) + 1`.
        *   For `k = j`, `nums[j]` is the only element, so `f(j, j)` becomes `1` (from an implicit `0`).
    d.  **Update `last_occurrence`**: Set `last_occurrence[val] = j`.
    e.  **Query Segment Tree**: The segment tree now holds the `f(i, j)` values for `0 <= i <= j`. Query the `sum_sq_val` for the range `[0, j]` from the segment tree. This gives `sum_{0 <= i <= j} f(i, j)^2`.
    f.  Add this `current_sum_sq` to `total_sum_sq_of_distinct_counts`, taking modulo `MOD`.

3.  **Return**: `total_sum_sq_of_distinct_counts`.

### Segment Tree Implementation Details:
*   Each node `tree[node_idx]` stores `[sum_val, sum_sq_val, lazy_add]`.
*   `_push_down(node_idx, start, end)`: Applies `lazy_add` from `node_idx` to its children.
    *   For a child node with `count` elements, `old_sum`, `old_sum_sq`, and `lazy_child`:
        *   `new_sum_sq = (old_sum_sq + 2 * lazy_add * old_sum + lazy_add^2 * count) % MOD`
        *   `new_sum = (old_sum + lazy_add * count) % MOD`
        *   `new_lazy_child = (lazy_child + lazy_add) % MOD`
    *   After pushing, `node_idx.lazy_add` is reset to `0`.
*   `_pull_up(node_idx)`: Updates `node_idx.sum_val` and `node_idx.sum_sq_val` by summing those of its children.
*   `update_range(query_L, query_R, val_to_add, node_idx, start, end)`:
    *   Base cases: no overlap (return), full overlap (apply `val_to_add` to current node's `sum_val`, `sum_sq_val`, `lazy_add` using the formulas).
    *   Recursive step: `_push_down`, recurse on children, `_pull_up`.
*   `query_range(query_L, query_R, node_idx, start, end)`:
    *   Base cases: no overlap (return `[0,0]`), full overlap (return current node's `[sum_val, sum_sq_val]`).
    *   Recursive step: `_push_down`, recurse on children, combine results.
*   All arithmetic operations must be performed modulo `MOD`.

## Visualization

```mermaid
graph TD
    A[Segment Tree Root: [0, N-1]] --> B[Left Child: [0, M]]
    A --> C[Right Child: [M+1, N-1]]

    subgraph Node Structure
        N_range(Range: [start, end])
        N_count(Count: end - start + 1)
        N_sum(Sum of distinct counts: Σf(i,j))
        N_sum_sq(Sum of squares: Σf(i,j)^2)
        N_lazy(Lazy Add Value: K)
    end

    style N_range fill:#e0e0e0,stroke:#333,stroke-width:1px
    style N_count fill:#f9f,stroke:#333,stroke-width:2px
    style N_sum fill:#f9f,stroke:#333,stroke-width:2px
    style N_sum_sq fill:#f9f,stroke:#333,stroke-width:2px
    style N_lazy fill:#f9f,stroke:#333,stroke-width:2px

    subgraph Iteration for nums[j]
        I_start(Process nums[j])
        I_prev_idx(Get prev_idx = last_occurrence[nums[j]])
        I_update(Call segment_tree.update_range(prev_idx + 1, j, 1))
        I_update_last_occ(last_occurrence[nums[j]] = j)
        I_query(Query segment_tree.query_range(0, j) for sum_sq)
        I_add_to_total(total_sum_sq += sum_sq)
        I_end(End iteration)
    end

    subgraph Update Range Operation (Add C to [L, R])
        U_start(update_range(L, R, C))
        U_check_full_overlap{Node range [ns, ne] fully in [L, R]?}
        U_check_full_overlap -- Yes --> U_apply_C(Apply C to node's sum, sum_sq, lazy)
        U_check_full_overlap -- No, partial --> U_push_down(Push down lazy to children)
        U_push_down --> U_recurse_children(Recurse on children)
        U_recurse_children --> U_pull_up(Pull up sums from children)
        U_check_full_overlap -- No, outside --> U_return(Return)
    end

    subgraph Lazy Push Down (from Parent with lazy K)
        P_start(push_down(node_idx))
        P_calc_left_child_vals(Calculate new sum, sum_sq for Left Child using K)
        P_update_left_lazy(Add K to Left Child's lazy)
        P_calc_right_child_vals(Calculate new sum, sum_sq for Right Child using K)
        P_update_right_lazy(Add K to Right Child's lazy)
        P_clear_parent_lazy(Set Parent's lazy to 0)
        P_end(End push_down)
    end

    I_start --> I_prev_idx --> I_update --> I_update_last_occ --> I_query --> I_add_to_total --> I_end
    U_start --> U_check_full_overlap
    P_start --> P_calc_left_child_vals --> P_update_left_lazy --> P_calc_right_child_vals --> P_update_right_lazy --> P_clear_parent_lazy --> P_end
```

## Dry Run
Let's trace `nums = [1,2,1]`

*   `N=3`, `MOD = 10^9 + 7`.
*   `total_sum_sq_of_distinct_counts = 0`.
*   `segment_tree` initialized for `[0,2]`, all values `[0,0,0]`.
*   `last_occurrence = {}`.

| `j` | `nums[j]` | `val` | `prev_idx` | `Update Range` | Segment Tree State (f(i,j) values) | `Query [0,j]` (sum_sq) | `total_sum_sq_of_distinct_counts` | `last_occurrence` |
| :-- | :-------- | :---- | :--------- | :------------- | :--------------------------------- | :---------------------- | :-------------------------------- | :---------------- |
| 0   | 1         | 1     | -1         | `[0,0]` by +1  | `f(0,0)=1` (others 0)              | `1^2 = 1`               | `1`                               | `{1:0}`           |
| 1   | 2         | 2     | -1         | `[0,1]` by +1  | `f(0,1)=2`, `f(1,1)=1` (others 0)  | `2^2 + 1^2 = 5`         | `1 + 5 = 6`                       | `{1:0, 2:1}`      |
| 2   | 1         | 1     | 0          | `[1,2]` by +1  | `f(0,2)=2` (unchanged), `f(1,2)=2` (from 1+1), `f(2,2)=1` (from 0+1) | `2^2 + 2^2 + 1^2 = 9`   | `6 + 9 = 15`                      | `{1:2, 2:1}`      |

Final `total_sum_sq_of_distinct_counts = 15`. This matches Example 1.

## Complexity
*   **Time Complexity**: `O(N log N)`.
    *   We iterate `N` times (for `j` from `0` to `N-1`).
    *   In each iteration, we perform one `last_occurrence` map lookup/update (`O(1)` average).
    *   We perform one segment tree `update_range` operation and one `query_range` operation. Both take `O(log N)` time due to the tree's height.
    *   Total time: `N * (O(1) + O(log N) + O(log N)) = O(N log N)`.
*   **Space Complexity**: `O(N)`.
    *   The segment tree requires `O(N)` space (approximately `4N` nodes).
    *   The `last_occurrence` dictionary stores at most `N` unique elements, requiring `O(N)` space.

## Edge Cases
*   **`nums.length = 1`**: E.g., `[5]`.
    *   `j=0`, `val=5`, `prev_idx=-1`. Update `[0,0]` by +1. Segment tree has `f(0,0)=1`. Query `[0,0]` gives `1^2=1`. `total_sum_sq = 1`. Correct.
*   **All elements distinct**: E.g., `[1,2,3]`.
    *   `j=0`: `f(0,0)=1`. `total=1`.
    *   `j=1`: `f(0,1)=2, f(1,1)=1`. `total=1+(2^2+1^2)=6`.
    *   `j=2`: `f(0,2)=3, f(1,2)=2, f(2,2)=1`. `total=6+(3^2+2^2+1^2)=20`.
    *   This is correctly handled as `prev_idx` will always be `-1`, leading to updates on `[0, j]`.
*   **All elements same**: E.g., `[2,2,2]`.
    *   `j=0`: `f(0,0)=1`. `total=1`. `last_occurrence={2:0}`.
    *   `j=1`: `prev_idx=0`. Update `[1,1]` by +1. `f(0,1)=1` (unchanged), `f(1,1)=1`. Query `[0,1]` gives `1^2+1^2=2`. `total=1+2=3`. `last_occurrence={2:1}`.
    *   `j=2`: `prev_idx=1`. Update `[2,2]` by +1. `f(0,2)=1, f(1,2)=1, f(2,2)=1`. Query `[0,2]` gives `1^2+1^2+1^2=3`. `total=3+3=6`. `last_occurrence={2:2}`.
    *   This is correctly handled as `prev_idx` will always be `j-1`, leading to updates on `[j, j]`.

The solution correctly handles these cases due to the robust segment tree logic and the `prev_idx + 1` update range.

## Solution

```python
from typing import List

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.MOD = 10**9 + 7
        # Each node stores [sum_val, sum_sq_val, lazy_add]
        # sum_val: sum of distinct counts in this range
        # sum_sq_val: sum of squares of distinct counts in this range
        # lazy_add: value to be added to all elements in this range
        # Initial values are all 0, so no explicit build method is needed.
        self.tree = [[0, 0, 0] for _ in range(4 * n)] 

    def _push_down(self, node_idx, start, end):
        lazy_val = self.tree[node_idx][2]
        if lazy_val == 0:
            return

        mid = (start + end) // 2

        # Apply lazy_val to left child
        left_child_idx = 2 * node_idx + 1
        left_child_count = mid - start + 1
        
        # new_sum_sq = old_sum_sq + 2*C*old_sum + C^2*count
        self.tree[left_child_idx][1] = (self.tree[left_child_idx][1] +
                                        (2 * lazy_val * self.tree[left_child_idx][0]) % self.MOD +
                                        (lazy_val * lazy_val % self.MOD * left_child_count) % self.MOD) % self.MOD
        
        # new_sum = old_sum + C*count
        self.tree[left_child_idx][0] = (self.tree[left_child_idx][0] +
                                        (lazy_val * left_child_count) % self.MOD) % self.MOD
        
        # Propagate lazy_val to left child
        self.tree[left_child_idx][2] = (self.tree[left_child_idx][2] + lazy_val) % self.MOD

        # Apply lazy_val to right child
        right_child_idx = 2 * node_idx + 2
        right_child_count = end - (mid + 1) + 1

        self.tree[right_child_idx][1] = (self.tree[right_child_idx][1] +
                                         (2 * lazy_val * self.tree[right_child_idx][0]) % self.MOD +
                                         (lazy_val * lazy_val % self.MOD * right_child_count) % self.MOD) % self.MOD
        
        self.tree[right_child_idx][0] = (self.tree[right_child_idx][0] +
                                         (lazy_val * right_child_count) % self.MOD) % self.MOD
        
        self.tree[right_child_idx][2] = (self.tree[right_child_idx][2] + lazy_val) % self.MOD

        # Clear lazy_val for current node
        self.tree[node_idx][2] = 0

    def _pull_up(self, node_idx):
        left_child_idx = 2 * node_idx + 1
        right_child_idx = 2 * node_idx + 2
        self.tree[node_idx][0] = (self.tree[left_child_idx][0] + self.tree[right_child_idx][0]) % self.MOD
        self.tree[node_idx][1] = (self.tree[left_child_idx][1] + self.tree[right_child_idx][1]) % self.MOD

    def update_range(self, query_L, query_R, val_to_add, node_idx, start, end):
        # Adjust query range to be within valid segment tree bounds
        query_L = max(0, query_L)
        query_R = min(self.n - 1, query_R)
        
        # No overlap or invalid query range
        if query_L > query_R or query_L > end or query_R < start:
            return

        # Full overlap
        if query_L <= start and end <= query_R:
            node_count = end - start + 1
            # Update sum_sq_val: (x+C)^2 = x^2 + 2Cx + C^2
            self.tree[node_idx][1] = (self.tree[node_idx][1] +
                                      (2 * val_to_add * self.tree[node_idx][0]) % self.MOD +
                                      (val_to_add * val_to_add % self.MOD * node_count) % self.MOD) % self.MOD
            
            # Update sum_val: sum(x+C) = sum(x) + C*count
            self.tree[node_idx][0] = (self.tree[node_idx][0] +
                                      (val_to_add * node_count) % self.MOD) % self.MOD
            
            # Update lazy_add
            self.tree[node_idx][2] = (self.tree[node_idx][2] + val_to_add) % self.MOD
            return

        # Partial overlap, push down lazy and recurse
        self._push_down(node_idx, start, end)
        mid = (start + end) // 2
        self.update_range(query_L, query_R, val_to_add, 2 * node_idx + 1, start, mid)
        self.update_range(query_L, query_R, val_to_add, 2 * node_idx + 2, mid + 1, end)
        self._pull_up(node_idx)

    def query_range(self, query_L, query_R, node_idx, start, end):
        # Adjust query range to be within valid segment tree bounds
        query_L = max(0, query_L)
        query_R = min(self.n - 1, query_R)

        # No overlap or invalid query range
        if query_L > query_R or query_L > end or query_R < start:
            return [0, 0] # Return [sum_val, sum_sq_val]

        # Full overlap
        if query_L <= start and end <= query_R:
            return [self.tree[node_idx][0], self.tree[node_idx][1]]

        # Partial overlap, push down lazy and recurse
        self._push_down(node_idx, start, end)
        mid = (start + end) // 2
        left_res = self.query_range(query_L, query_R, 2 * node_idx + 1, start, mid)
        right_res = self.query_range(query_L, query_R, 2 * node_idx + 2, mid + 1, end)
        
        # Combine results
        return [(left_res[0] + right_res[0]) % self.MOD,
                (left_res[1] + right_res[1]) % self.MOD]


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        segment_tree = SegmentTree(n)
        last_occurrence = {} # Stores {value: last_index}
        
        total_sum_sq_of_distinct_counts = 0
        
        for j in range(n):
            val = nums[j]
            
            # Find the previous occurrence of 'val'. If not found, it's -1.
            prev_idx = last_occurrence.get(val, -1)
            
            # Update the segment tree: add 1 to the range [prev_idx + 1, j].
            # This range covers all subarrays nums[k..j] where nums[j] is a new distinct element
            # (i.e., k > prev_idx), including the new single-element subarray nums[j..j].
            segment_tree.update_range(prev_idx + 1, j, 1, 0, 0, n - 1)
            
            # Update the last occurrence of 'val' to the current index 'j'.
            last_occurrence[val] = j
            
            # Query the sum of squares of distinct counts for all subarrays ending at 'j'.
            # The segment tree's current state for indices [0, j] represents f(i,j) for 0 <= i <= j.
            # We need the sum of squares of these values.
            current_sum_sq = segment_tree.query_range(0, j, 0, 0, n - 1)[1]
            
            total_sum_sq_of_distinct_counts = (total_sum_sq_of_distinct_counts + current_sum_sq) % MOD
            
        return total_sum_sq_of_distinct_counts

```

## Why This Works
The core idea is to iterate through the array, fixing the right endpoint `j` of subarrays. For each `j`, we efficiently update the distinct counts `f(i, j)` for all possible left endpoints `i <= j`. The key observation is that when `nums[j]` is processed, the distinct counts `f(i, j)` either remain the same as `f(i, j-1)` (if `nums[j]` was already present in `nums[i..j-1]`) or increase by 1 (if `nums[j]` is new). This change happens uniformly over a contiguous range of `i` values (from `last_occurrence[nums[j]] + 1` to `j`). A segment tree with lazy propagation is perfectly suited for such range updates and for querying the sum of squares, as the formula for `(x+C)^2` can be expressed in terms of `x^2`, `x`, and `C`. By maintaining `sum(x)` and `sum(x^2)` in each segment tree node, we can perform these updates and queries in `O(log N)` time per step, leading to an overall `O(N log N)` solution.

---
<sub>Generated 2026-10-16 04:53 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
