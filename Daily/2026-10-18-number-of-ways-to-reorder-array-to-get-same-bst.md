# [1569] Number of Ways to Reorder Array to Get Same BST

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-10-18 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/)

**Topics:** Array, Math, Divide and Conquer, Dynamic Programming, Tree, Union-Find, Binary Search Tree, Memoization, Combinatorics, Binary Tree, Fermat's Little Theorem

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

- For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.

Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:

Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.

Example 2:

Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST:
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]

Example 3:

Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.

Constraints:

- 1 <= nums.length <= 1000

- 1 <= nums[i] <= nums.length

- All integers in nums are distinct.

**Examples / sample tests:**

```
[2,1,3]
[3,4,5,1,2]
[1,2,3]
```

---

## Problem Summary
Given an array `nums` representing a permutation of integers, we construct a Binary Search Tree (BST) by inserting elements in order. The goal is to find the total number of *different* ways to reorder `nums` such that inserting the reordered elements still yields a BST identical to the one formed by the original `nums`. The result should be returned modulo 10^9 + 7.

## Intuition
The key to solving this problem lies in understanding how a Binary Search Tree is constructed and what makes two BSTs identical.

1.  **The Root is Fixed:** When building a BST by inserting elements sequentially, the very first element inserted *always* becomes the root of the tree. Therefore, for two arrays to form identical BSTs, their first elements (which become their roots) **must be the same**.
2.  **Recursive Structure:** Once the root is determined, all subsequent elements smaller than the root will eventually be inserted into its left subtree, and all elements larger than the root will be inserted into its right subtree. For the overall BSTs to be identical, their **left subtrees must be identical**, and their **right subtrees must be identical**. This recursive nature strongly suggests a **divide and conquer** approach.
3.  **Interleaving Elements:** Suppose we have `L` elements that belong to the left subtree and `R` elements that belong to the right subtree. After the root, these `L+R` elements can appear in any order in the input array, *as long as their relative order within the left subtree's elements is preserved* (to form the correct left subtree) and *their relative order within the right subtree's elements is preserved* (to form the correct right subtree). The number of ways to interleave `L` distinct items and `R` distinct items into `L+R` available slots is given by the **binomial coefficient** `C(L+R, L)` (or `C(L+R, R)`).
4.  **Combining Results:** The total number of ways to form a specific subtree structure is the product of:
    *   The number of ways to interleave the elements destined for its left and right subtrees.
    *   The number of ways to form its left subtree (found recursively).
    *   The number of ways to form its right subtree (found recursively).

## Approach
We will implement a recursive, divide-and-conquer algorithm.

1.  **Precompute Combinations (Pascal's Triangle):** We'll need to calculate binomial coefficients `C(n, k)` efficiently. Since `n` can be up to `len(nums)` (which is 1000), we can precompute these values using Pascal's Triangle up to `N` rows. `C[i][j]` will store `C(i, j)`, calculated as `(C[i-1][j-1] + C[i-1][j]) % MOD`. All calculations must be performed modulo `10^9 + 7`.

2.  **Define a Recursive Function `solve(arr)`:**
    *   This function takes a list `arr` representing the elements that will form the current subtree. The first element `arr[0]` is considered the root of this subtree.
    *   **Base Case:** If `len(arr) <= 2`, there's only `1` way to form that specific subtree. This covers empty lists, single-element lists, and two-element lists (which always form a skewed tree, e.g., `[2,1]` forms a root `2` with left child `1`, and `[1,2]` forms a root `1` with right child `2`).
    *   **Identify Root:** Let `root = arr[0]`.
    *   **Partition Elements:** Create two new lists: `left_subtree_elements` (for elements `x < root` from `arr[1:]`) and `right_subtree_elements` (for elements `y > root` from `arr[1:]`). It's crucial that the *relative order* of elements within these new lists is preserved from `arr[1:]`.
    *   **Recursive Calls:**
        *   `ways_left = solve(left_subtree_elements)`
        *   `ways_right = solve(right_subtree_elements)`
    *   **Calculate Interleaving Ways:**
        *   Let `num_left = len(left_subtree_elements)` and `num_right = len(right_subtree_elements)`.
        *   The number of ways to interleave these elements after the root is `combinations[num_left + num_right][num_left]`.
    *   **Combine Results:** The total number of ways for the current subtree is `(ways_to_interleave * ways_left % MOD * ways_right % MOD) % MOD`.
    *   **Return** this total.

3.  **Initial Call and Final Result:**
    *   Call `solve(nums)` with the original input array.
    *   The problem asks for the number of *other* ways, which implies we should exclude the original ordering itself. So, subtract `1` from the result returned by `solve(nums)`. To handle potential negative results from subtraction before modulo, add `MOD`: `(solve(nums) - 1 + MOD) % MOD`.

## Visualization

Let's trace `nums = [3,4,5,1,2]` to illustrate the process:

```
Original Array: [3, 4, 5, 1, 2]
                                 solve([3,4,5,1,2])
                                 Root = 3
                                 Elements < 3: [1, 2]  (left_subtree_elements)
                                 Elements > 3: [4, 5]  (right_subtree_elements)
                                 num_left = 2, num_right = 2
                                 Ways to interleave: C(2+2, 2) = C(4, 2) = 6
                                 
                                 /                  \
                                /                    \
                               /                      \
                 solve([1,2])                          solve([4,5])
                 Root = 1                              Root = 4
                 Elements < 1: []                      Elements < 4: []
                 Elements > 1: [2]                     Elements > 4: [5]
                 num_left = 0, num_right = 1           num_left = 0, num_right = 1
                 Ways to interleave: C(0+1, 0) = 1     Ways to interleave: C(0+1, 0) = 1
                 
                 /          \                          /          \
                /            \                        /            \
               /              \                      /              \
    solve([])             solve([2])        solve([])             solve([5])
    Returns 1             Returns 1         Returns 1             Returns 1
    (Base Case)           (Base Case)       (Base Case)           (Base Case)

Calculations (bottom-up):
1.  `solve([])` returns 1.
2.  `solve([2])` returns 1.
3.  `solve([1,2])` returns `C(0+1, 0) * solve([]) * solve([2]) = 1 * 1 * 1 = 1`.
4.  `solve([5])` returns 1.
5.  `solve([4,5])` returns `C(0+1, 0) * solve([]) * solve([5]) = 1 * 1 * 1 = 1`.
6.  `solve([3,4,5,1,2])` returns `C(2+2, 2) * solve([1,2]) * solve([4,5]) = 6 * 1 * 1 = 6`.

Final Result: `6 - 1 = 5` (matches Example 2).
```

## Dry Run
Let's trace `nums = [2,1,3]` (Example 1). `MOD = 10^9 + 7`.

**1. Precompute Combinations (up to N=3):**
`combinations` table:
`C[0][0] = 1`
`C[1][0] = 1, C[1][1] = 1`
`C[2][0] = 1, C[2][1] = 2, C[2][2] = 1`
`C[3][0] = 1, C[3][1] = 3, C[3][2] = 3, C[3][3] = 1`

**2. Initial Call: `solve([2,1,3])`**

| Step | `arr`     | `m` | `root` | `left_subtree_elements` | `right_subtree_elements` | `num_left` | `num_right` | `ways_left` | `ways_right` | `ways_to_interleave` | `current_total_ways` |
| :--- | :-------- | :-- | :----- | :---------------------- | :----------------------- | :--------- | :---------- | :---------- | :----------- | :------------------- | :------------------- |
| 2.1  | `[2,1,3]` | 3   | 2      | `[1]`                   | `[3]`                    | 1          | 1           | (call 2.2)  | (call 2.3)   | `C[1+1][1] = C[2][1] = 2` | `2 * 1 * 1 = 2`      |
| 2.2  | `[1]`     | 1   | -      | -                       | -                        | -          | -           | -           | -            | -                    | `1` (Base Case)      |
| 2.3  | `[3]`     | 1   | -      | -                       | -                        | -           | -            | -           | -            | -                    | `1` (Base Case)      |

**3. Return from `solve([2,1,3])`:**
The function call `solve([2,1,3])` returns `2`.

**4. Final Result Calculation:**
`result = (solve(nums) - 1 + MOD) % MOD`
`result = (2 - 1 + MOD) % MOD`
`result = (1 + MOD) % MOD`
`result = 1`

The final output `1` matches Example 1.

## Complexity
*   **Time Complexity:** `O(N^2)`
    *   Precomputing the `combinations` table using Pascal's Triangle takes `O(N^2)` time, where `N` is `len(nums)`.
    *   The `solve` function is called at most `N` times (once for each node in the BST). In each call, we iterate through `arr[1:]` to partition elements, which takes `O(k)` time where `k` is the length of the current `arr`. In the worst case (a completely skewed tree), the recursion depth is `N`, and at each level, the total number of elements processed across all calls is `O(N)`. This results in `O(N^2)` for all recursive calls.
    *   Overall, the time complexity is dominated by `O(N^2)`.
*   **Space Complexity:** `O(N^2)`
    *   The `combinations` table requires `O(N^2)` space.
    *   The recursion stack depth can go up to `O(N)` in the worst case (a completely skewed BST).
    *   The `left_subtree_elements` and `right_subtree_elements` lists created in each recursive call also contribute to space, but their total size at any given recursion level is `O(N)`.
    *   Overall, the space complexity is dominated by `O(N^2)`.

## Edge Cases
*   **`nums` with 1 element (e.g., `[1]`):**
    *   `solve([1])` returns 1 (base case).
    *   Final result: `(1 - 1 + MOD) % MOD = 0`. This is correct, as there are no *other* ways to reorder a single element.
*   **`nums` already sorted (e.g., `[1,2,3]`):**
    *   This forms a right-skewed BST. `solve([1,2,3])` will recursively break down, always finding an empty left subtree. The `ways_to_interleave` will always be `C(0+k, 0) = 1`. The total `solve([1,2,3])` will return 1.
    *   Final result: `(1 - 1 + MOD) % MOD = 0`. Correct, a completely skewed tree can only be formed in one specific order.
*   **`nums` reverse sorted (e.g., `[3,2,1]`):**
    *   This forms a left-skewed BST. Similar to the sorted case, `solve([3,2,1])` will return 1.
    *   Final result: `(1 - 1 + MOD) % MOD = 0`. Correct.

## Solution
```python
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute combinations (Pascal's Triangle)
        # combinations[i][j] stores C(i, j)
        combinations = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            combinations[i][0] = 1  # C(i, 0) is always 1
            for j in range(1, i + 1):
                combinations[i][j] = (combinations[i-1][j-1] + combinations[i-1][j]) % MOD

        def solve(arr: list[int]) -> int:
            m = len(arr)
            # Base case: If the array has 0, 1, or 2 elements, there's only 1 way
            # to form that specific subtree structure.
            # - For 0 or 1 element, it's trivial (empty tree or single node).
            # - For 2 elements (e.g., [2,1] or [1,2]), it forms a skewed tree.
            #   There's only 1 way to order them to get that specific skewed tree.
            if m <= 2:
                return 1

            root = arr[0]
            left_subtree_elements = []
            right_subtree_elements = []

            # Partition elements into left and right subtrees.
            # The relative order of elements within left_subtree_elements
            # and right_subtree_elements is preserved from arr[1:],
            # which is crucial for forming the correct sub-BSTs.
            for x in arr[1:]:
                if x < root:
                    left_subtree_elements.append(x)
                else: # x > root
                    right_subtree_elements.append(x)
            
            num_left = len(left_subtree_elements)
            num_right = len(right_subtree_elements)

            # Calculate the number of ways to interleave the elements
            # from the left and right subtrees after the root.
            # This is C(num_left + num_right, num_left).
            ways_to_interleave = combinations[num_left + num_right][num_left]

            # Recursively find the number of ways for the left and right subtrees
            ways_left = solve(left_subtree_elements)
            ways_right = solve(right_subtree_elements)

            # Combine results:
            # (interleaving ways * ways for left subtree * ways for right subtree) % MOD
            return (ways_to_interleave * ways_left % MOD * ways_right % MOD) % MOD

        # The problem asks for the number of *other* ways, so we subtract 1
        # from the total count (which includes the original ordering itself).
        # We add MOD before taking the final modulo to handle potential negative
        # results if solve(nums) returns 0 (though it will always return at least 1).
        return (solve(nums) - 1 + MOD) % MOD

```

## Why This Works
This solution correctly counts the number of valid reorderings by leveraging the fundamental properties of BST construction. The first element of any sequence that forms a particular BST must be its root. By recursively breaking down the problem into left and right subtrees, we ensure that the structural integrity of the BST is maintained at every level. The combinatorial factor `C(L+R, L)` precisely accounts for all possible ways to interleave the elements of the left and right subtrees *after* the root, while preserving their internal relative order (which is handled by the recursive calls). Multiplying these factors together gives the total number of sequences that would yield the exact same BST. Finally, subtracting 1 accounts for the problem's request to count "other" ways, excluding the original input sequence itself.

---
<sub>Generated 2026-10-18 05:01 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
