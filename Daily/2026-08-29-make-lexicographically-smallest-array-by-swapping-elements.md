# [2948] Make Lexicographically Smallest Array by Swapping Elements

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-08-29 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/)

**Topics:** Array, Union-Find, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 0-indexed array of positive integers nums and a positive integer limit.

In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.

Return the lexicographically smallest array that can be obtained by performing the operation any number of times.

An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.

Example 1:

Input: nums = [1,5,3,9,8], limit = 2
Output: [1,3,5,8,9]
Explanation: Apply the operation 2 times:
- Swap nums[1] with nums[2]. The array becomes [1,3,5,9,8]
- Swap nums[3] with nums[4]. The array becomes [1,3,5,8,9]
We cannot obtain a lexicographically smaller array by applying any more operations.
Note that it may be possible to get the same result by doing different operations.

Example 2:

Input: nums = [1,7,6,18,2,1], limit = 3
Output: [1,6,7,18,1,2]
Explanation: Apply the operation 3 times:
- Swap nums[1] with nums[2]. The array becomes [1,6,7,18,2,1]
- Swap nums[0] with nums[4]. The array becomes [2,6,7,18,1,1]
- Swap nums[0] with nums[5]. The array becomes [1,6,7,18,1,2]
We cannot obtain a lexicographically smaller array by applying any more operations.

Example 3:

Input: nums = [1,7,28,19,10], limit = 3
Output: [1,7,28,19,10]
Explanation: [1,7,28,19,10] is the lexicographically smallest array we can obtain because we cannot apply the operation on any two indices.

Constraints:

- 1 <= nums.length <= 10^5

- 1 <= nums[i] <= 10^9

- 1 <= limit <= 10^9

**Examples / sample tests:**

```
[1,5,3,9,8]
2
[1,7,6,18,2,1]
3
[1,7,28,19,10]
3
```

---

## Problem Summary
You are given an array of positive integers `nums` and a `limit`. You can swap any two elements `nums[i]` and `nums[j]` if their absolute difference `|nums[i] - nums[j]|` is less than or equal to `limit`. The goal is to perform any number of these operations to obtain the lexicographically smallest possible array.

## Intuition
The core idea revolves around understanding the swap operation. If `nums[i]` can be swapped with `nums[j]`, and `nums[j]` can be swapped with `nums[k]`, then `nums[i]`, `nums[j]`, and `nums[k]` are all "connected" and can effectively be moved to any of the original positions `i, j, k`. This forms **connected components** of indices.

To make an array lexicographically smallest, we want the smallest possible number at index 0, then the smallest possible number at index 1 (given index 0's value), and so on. If a set of numbers `S` (from `nums`) are all connected and occupy a set of original indices `P`, then to minimize the array lexicographically, we should place the smallest value from `S` into the smallest index from `P`, the second smallest value from `S` into the second smallest index from `P`, and so forth. In essence, we **sort the values in `S` and assign them to the sorted indices in `P`**.

The challenge is efficiently finding these connected components. A brute-force check of all pairs is too slow. The key observation is that if we sort the numbers themselves, say `v_0 <= v_1 <= ... <= v_{N-1}`, then if `v_i` and `v_k` are connectable (i.e., `v_k - v_i <= limit`), all numbers `v_j` such that `i < j < k` must also be connectable to `v_i` and `v_k` (or form a path between them). This means we only need to check **adjacent elements in the sorted list** to establish connections.

## Approach
The optimal approach involves using a **Union-Find (DSU)** data structure to identify connected components based on the swap rule.

1.  **Pair Values with Original Indices:** Create a list of tuples `(value, original_index)` for each element in the input `nums` array. This preserves the original positions.
    *   Example: `nums = [1,5,3,9,8]` becomes `[(1,0), (5,1), (3,2), (9,3), (8,4)]`.

2.  **Sort Paired Elements:** Sort this list of `(value, original_index)` pairs primarily by their `value`.
    *   Example: `[(1,0), (3,2), (5,1), (8,4), (9,3)]`.

3.  **Initialize Union-Find:** Create a DSU structure for `N` elements, where `N` is the length of `nums`. Each element (representing an original index) is initially in its own set.

4.  **Build Connected Components using DSU:**
    *   Iterate through the **sorted** `(value, original_index)` pairs from `i = 0` to `N-2`.
    *   For each pair `(val1, idx1)` at `indexed_nums[i]` and `(val2, idx2)` at `indexed_nums[i+1]`:
        *   If `val2 - val1 <= limit`, it means these two values are "close enough" to be part of the same component. Perform a `union(idx1, idx2)` operation in the DSU. This connects their original indices.

5.  **Group Elements by Component:**
    *   Create a dictionary (e.g., `defaultdict`) where keys are the **root representatives** of the connected components (obtained via `dsu.find(i)` for each original index `i`).
    *   For each original index `i` from `0` to `N-1`:
        *   Find its root `r = dsu.find(i)`.
        *   Add `nums[i]` to a list of `values` associated with `r`.
        *   Add `i` to a list of `indices` associated with `r`.

6.  **Construct the Result Array:**
    *   Initialize an empty `result` array of size `N`.
    *   For each component (i.e., for each `root` in your dictionary):
        *   Get the `values` list and `indices` list for that component.
        *   **Sort** both the `values` list and the `indices` list in ascending order.
        *   Iterate `k` from `0` to `len(values) - 1`: Assign `result[sorted_indices[k]] = sorted_values[k]`. This places the smallest value into the smallest available index within that component, and so on.

7.  **Return `result`**.

## Visualization
Let's trace Example 1: `nums = [1,5,3,9,8]`, `limit = 2`

1.  **Original Array (with indices):**
    ```
    Index:  0  1  2  3  4
    Value:  1  5  3  9  8
    ```

2.  **Pair (Value, Original Index) and Sort by Value:**
    ```
    Pairs: (1,0), (3,2), (5,1), (8,4), (9,3)
    ```

3.  **Build Connected Components (DSU) using sorted pairs:**
    *   Compare (1,0) and (3,2): `|3-1|=2 <= limit`. Connect original indices 0 and 2.
    *   Compare (3,2) and (5,1): `|5-3|=2 <= limit`. Connect original indices 2 and 1.
    *   Compare (5,1) and (8,4): `|8-5|=3 > limit`. No connection.
    *   Compare (8,4) and (9,3): `|9-8|=1 <= limit`. Connect original indices 4 and 3.

    **Resulting Components (groups of original indices):**
    ```
    Component 1: {0, 1, 2}  (Original values: nums[0]=1, nums[1]=5, nums[2]=3)
    Component 2: {3, 4}     (Original values: nums[3]=9, nums[4]=8)
    ```

4.  **Sort Values and Indices within each Component, then Assign:**
    *   **Component 1:**
        *   Original indices: `[0, 1, 2]` -> Sorted indices: `[0, 1, 2]`
        *   Values: `[1, 5, 3]` -> Sorted values: `[1, 3, 5]`
        *   Assign: `result[0]=1, result[1]=3, result[2]=5`

    *   **Component 2:**
        *   Original indices: `[3, 4]` -> Sorted indices: `[3, 4]`
        *   Values: `[9, 8]` -> Sorted values: `[8, 9]`
        *   Assign: `result[3]=8, result[4]=9`

5.  **Final Lexicographically Smallest Array:**
    ```
    Index:  0  1  2  3  4
    Value:  1  3  5  8  9
    ```

## Dry Run
Let's walk through Example 1: `nums = [1,5,3,9,8]`, `limit = 2`

| Step | Action | `indexed_nums` (sorted) | DSU `parent` array (simplified) | `components` (partial) | `result` |
| :--- | :----- | :---------------------- | :------------------------------ | :--------------------- | :------- |
| 1    | Init `indexed_nums` | `[(1,0), (5,1), (3,2), (9,3), (8,4)]` | | | |
| 2    | Sort `indexed_nums` | `[(1,0), (3,2), (5,1), (8,4), (9,3)]` | | | |
| 3    | Init DSU (`N=5`) | | `[0,1,2,3,4]` | | |
| 4a   | `i=0`: `(1,0), (3,2)`. `3-1=2 <= limit`. `union(0,2)` | | `[0,1,0,3,4]` | | |
| 4b   | `i=1`: `(3,2), (5,1)`. `5-3=2 <= limit`. `union(2,1)` (roots `0,1`). `union(0,1)` | | `[0,0,0,3,4]` | | |
| 4c   | `i=2`: `(5,1), (8,4)`. `8-5=3 > limit`. No union. | | `[0,0,0,3,4]` | | |
| 4d   | `i=3`: `(8,4), (9,3)`. `9-8=1 <= limit`. `union(4,3)` (roots `4,3`). `union(4,3)` | | `[0,0,0,4,4]` | | |
| 5a   | Group: `i=0`, `root=0`. `nums[0]=1` | | | `0: {v:[1], i:[0]}` | |
| 5b   | Group: `i=1`, `root=0`. `nums[1]=5` | | | `0: {v:[1,5], i:[0,1]}` | |
| 5c   | Group: `i=2`, `root=0`. `nums[2]=3` | | | `0: {v:[1,5,3], i:[0,1,2]}` | |
| 5d   | Group: `i=3`, `root=4`. `nums[3]=9` | | | `4: {v:[9], i:[3]}` | |
| 5e   | Group: `i=4`, `root=4`. `nums[4]=8` | | | `4: {v:[9,8], i:[3,4]}` | |
| 6a   | Component `root=0`: `values=[1,5,3]`, `indices=[0,1,2]` | | | | `[0,0,0,0,0]` |
|      | Sort: `values=[1,3,5]`, `indices=[0,1,2]` | | | | |
|      | Assign: `result[0]=1, result[1]=3, result[2]=5` | | | | `[1,3,5,0,0]` |
| 6b   | Component `root=4`: `values=[9,8]`, `indices=[3,4]` | | | | `[1,3,5,0,0]` |
|      | Sort: `values=[8,9]`, `indices=[3,4]` | | | | |
|      | Assign: `result[3]=8, result[4]=9` | | | | `[1,3,5,8,9]` |
| 7    | **Final Result** | | | | `[1,3,5,8,9]` |

## Complexity
*   **Time Complexity:** `O(N log N)`.
    *   Creating `indexed_nums` takes `O(N)`.
    *   Sorting `indexed_nums` takes `O(N log N)`.
    *   DSU operations (N unions, N finds) take amortized `O(N * α(N))`, which is practically `O(N)`.
    *   Grouping elements into components takes `O(N)` (N finds and appends).
    *   Sorting values and indices within each component: In the worst case, all `N` elements might belong to a single component, leading to `O(N log N)` for sorting. In general, `sum(s_i log s_i)` for component sizes `s_i` is at most `O(N log N)`.
    *   Constructing the final result takes `O(N)`.
    *   The dominant factor is sorting, hence `O(N log N)`.
*   **Space Complexity:** `O(N)`.
    *   `indexed_nums` stores `N` pairs: `O(N)`.
    *   DSU `parent` array: `O(N)`.
    *   `components` dictionary stores `N` values and `N` indices in total: `O(N)`.
    *   `result` array: `O(N)`.

## Edge Cases
*   **`N = 1` (single element array):** The `indexed_nums` will have one element. The DSU loop for building components won't run. The element will form its own component, and the result will be the original array, which is correct.
*   **`limit = 0`:** Only identical numbers can swap. Each distinct number forms its own component. The array remains unchanged, which is correct.
*   **`limit` is very large (e.g., `10^9`):** All numbers can swap with each other as their differences will almost certainly be `<= limit`. All elements will form a single connected component. The result will be the `nums` array sorted in ascending order, which is correct.
*   **All numbers are identical:** All numbers form one component. The array remains unchanged, which is correct.
*   **No swaps possible (e.g., `[1, 7, 28, 19, 10], limit = 3`):** No adjacent elements in the sorted `indexed_nums` will satisfy `val2 - val1 <= limit`. Each element will remain in its own component. The result will be the original array, which is correct.

## Solution

```python
import collections
from typing import List

class DSU:
    def __init__(self, n):
        # Initialize parent array: each element is its own parent
        self.parent = list(range(n))

    def find(self, i):
        # Find the representative (root) of the set containing element i
        # with path compression optimization
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        # Union the sets containing elements i and j
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Make root_i the parent of root_j (simple union)
            self.parent[root_j] = root_i
            return True
        return False

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        # Step 1: Create pairs (value, original_index)
        indexed_nums = []
        for i in range(n):
            indexed_nums.append((nums[i], i))

        # Step 2: Sort these pairs based on their values
        # This is crucial for efficiently identifying connected components
        indexed_nums.sort()

        # Step 3: Initialize Union-Find (DSU) structure
        dsu = DSU(n)

        # Step 4: Build Connected Components
        # Iterate through the sorted pairs and union original indices
        # if their values are within the specified limit.
        for i in range(n - 1):
            val1, idx1 = indexed_nums[i]
            val2, idx2 = indexed_nums[i+1]
            # If the difference between adjacent sorted values is within limit,
            # their original indices belong to the same connected component.
            if val2 - val1 <= limit:
                dsu.union(idx1, idx2)

        # Step 5: Group Elements by Component
        # Use a defaultdict to store values and their original indices for each component.
        # The key for the dictionary will be the root representative of the component.
        components = collections.defaultdict(lambda: {'values': [], 'indices': []})
        for i in range(n):
            root = dsu.find(i) # Find the representative of the component for original index i
            components[root]['values'].append(nums[i]) # Add the value at original index i
            components[root]['indices'].append(i)      # Add the original index i

        # Step 6: Construct the Result Array
        result = [0] * n
        for root in components:
            current_values = components[root]['values']
            current_indices = components[root]['indices']
            
            # To make the array lexicographically smallest,
            # sort the values and indices within each component.
            current_values.sort()
            current_indices.sort()
            
            # Assign the sorted values to the sorted original indices.
            # The smallest value goes to the smallest index, second smallest to second smallest, etc.
            for k in range(len(current_values)):
                result[current_indices[k]] = current_values[k]
        
        return result

```

## Why This Works
The core idea is that the swap operation `|nums[i] - nums[j]| <= limit` defines an **equivalence relation** on indices. If `nums[i]` can swap with `nums[j]`, and `nums[j]` can swap with `nums[k]`, then `nums[i]`, `nums[j]`, and `nums[k]` are all effectively interchangeable among their original positions `i, j, k`. This partitions the original indices into **connected components**. Within each component, any value can be moved to any position originally occupied by an element of that component. To achieve the lexicographically smallest array, for each such component, we must place its smallest available values into its smallest available original indices, its second smallest values into its second smallest indices, and so on.

The crucial step for efficiency is identifying these components. By pairing each number with its original index `(value, original_index)` and then sorting these pairs by `value`, we can use a **Union-Find (DSU)** data structure. If two adjacent elements in this sorted list, `(v_i, idx_i)` and `(v_{i+1}, idx_{i+1})`, satisfy `v_{i+1} - v_i <= limit`, it means they can be directly swapped (or are part of a chain that can swap them). This adjacent check is sufficient because if any two numbers `X` and `Y` are in the same connected component, there exists a path of swaps between them. If `X < Y` and `Y - X <= limit`, then any number `Z` such that `X <= Z <= Y` can also be connected to `X` and `Y`. Therefore, iterating through the sorted `(value, original_index)` pairs and performing a `union` operation on `idx_i` and `idx_{i+1}` whenever `v_{i+1} - v_i <= limit` correctly identifies all connected components. Once components are formed, we simply sort the values and indices within each component and assign them in order to construct the lexicographically smallest result.

---
<sub>Generated 2026-08-29 07:19 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
