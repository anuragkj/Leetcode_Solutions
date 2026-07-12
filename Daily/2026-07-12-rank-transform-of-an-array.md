# [1331] Rank Transform of an Array

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-07-12 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/rank-transform-of-an-array/)

**Topics:** Array, Hash Table, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

- Rank is an integer starting from 1.

- The larger the element, the larger the rank. If two elements are equal, their rank must be the same.

- Rank should be as small as possible.

Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.

Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]

Constraints:

- 0 <= arr.length <= 10^5

- -10^9 <= arr[i] <= 10^9

**Examples / sample tests:**

```
[40,10,20,30]
[100,100,100]
[37,12,28,9,100,56,80,5,12]
```

---

## Problem Summary
Given an array of integers, the task is to replace each number with its "rank". Ranks start from 1, are assigned based on the element's size (larger elements get larger ranks), and equal elements must share the same rank. The goal is to assign the smallest possible ranks while following these rules.

## Intuition
The problem asks us to determine the **relative order** of elements. If we know which element is the smallest, second smallest, and so on, we can assign ranks. The key insight is that we only care about the ranks of **unique** numbers. If we sort all the unique numbers present in the array, we can easily assign them ranks: the smallest unique number gets rank 1, the next smallest gets rank 2, and so forth. Once we have this mapping from each unique number to its rank, we can simply go through the original array and replace each number with its corresponding rank.

## Approach
The optimal algorithm involves sorting the unique elements and using a hash map (dictionary in Python) to store the value-to-rank mapping.

Here are the concrete steps:

1.  **Handle Empty Array**: First, check if the input array `arr` is empty. If it is, return an empty list immediately, as there are no elements to rank.
2.  **Extract and Sort Unique Elements**:
    *   Convert the input array `arr` into a `set`. This automatically removes all duplicate elements, leaving only unique values.
    *   Convert this `set` back into a `list`.
    *   **Sort** this new list of unique elements in ascending order. Let's call this `sorted_unique_elements`.
3.  **Create Rank Mapping**:
    *   Initialize an empty dictionary, say `rank_map`, to store the mapping from each unique number to its rank.
    *   Initialize a `current_rank` variable to `1`.
    *   Iterate through `sorted_unique_elements`:
        *   For each `element`, assign `current_rank` to it in `rank_map` (i.e., `rank_map[element] = current_rank`).
        *   Increment `current_rank` by `1` for the next unique element.
4.  **Transform Original Array**:
    *   Initialize an empty list, say `result`, which will store the final ranked array.
    *   Iterate through the *original* input array `arr`:
        *   For each `number` in `arr`, look up its rank in `rank_map` (i.e., `rank_map[number]`).
        *   Append this retrieved rank to the `result` list.
5.  **Return Result**: Finally, return the `result` list.

## Visualization
```mermaid
graph TD
    A[Input arr] --> B{Convert to Set};
    B --> C[Unique Elements Set];
    C --> D{Convert to List & Sort};
    D --> E[Sorted Unique List];
    E --> F{Iterate Sorted Unique List};
    F --> G[Assign Rank 1];
    F --> H[Assign Rank 2];
    F --> I[...];
    F --> J[Assign Rank N];
    G --&gt; K{Build Rank Map};
    H --&gt; K;
    I --&gt; K;
    J --&gt; K;
    K[Rank Map (Value -> Rank)]
    A --> L{Iterate Original arr};
    L --> M[Look up Rank for each element in Rank Map];
    M --> N[Build Result Array];
    N --> O[Final Result];
```

## Dry Run
Let's walk through **Example 1: `arr = [40,10,20,30]`**

1.  **Input**: `arr = [40,10,20,30]`
2.  **Handle Empty Array**: `arr` is not empty.
3.  **Extract and Sort Unique Elements**:
    *   `set(arr)` becomes `{10, 20, 30, 40}`.
    *   `list(set(arr))` becomes `[10, 20, 30, 40]` (order might vary, but sorting fixes it).
    *   `sorted_unique_elements` = `[10, 20, 30, 40]`
4.  **Create Rank Mapping**:
    *   Initialize `rank_map = {}`, `current_rank = 1`.
    *   | `element` (from `sorted_unique_elements`) | `current_rank` | `rank_map` (after update) |
    *   | :---------------------------------------- | :------------- | :---------------------------------------- |
    *   | 10                                        | 1              | `{10: 1}`                                 |
    *   | 20                                        | 2              | `{10: 1, 20: 2}`                          |
    *   | 30                                        | 3              | `{10: 1, 20: 2, 30: 3}`                   |
    *   | 40                                        | 4              | `{10: 1, 20: 2, 30: 3, 40: 4}`            |
5.  **Transform Original Array**:
    *   Initialize `result = []`.
    *   Iterate through `arr = [40,10,20,30]`:
        *   | `number` (from original `arr`) | `rank_map[number]` | `result` (after append) |
        *   | :----------------------------- | :----------------- | :---------------------- |
        *   | 40                             | `rank_map[40]` = 4 | `[4]`                   |
        *   | 10                             | `rank_map[10]` = 1 | `[4, 1]`                |
        *   | 20                             | `rank_map[20]` = 2 | `[4, 1, 2]`             |
        *   | 30                             | `rank_map[30]` = 3 | `[4, 1, 2, 3]`          |
6.  **Return Result**: The final `result` is `[4,1,2,3]`.

## Complexity
*   **Time Complexity**: **O(N log N)**.
    *   Converting `arr` to a `set` takes O(N) on average.
    *   Converting the `set` to a `list` and then sorting it takes O(U log U) time, where U is the number of unique elements. Since U <= N, this is at most O(N log N).
    *   Building the `rank_map` takes O(U) time.
    *   Iterating through the original `arr` and performing `N` dictionary lookups takes O(N) on average (each lookup is O(1) on average).
    *   The dominant factor is the sorting step, leading to O(N log N).
*   **Space Complexity**: **O(N)**.
    *   The `set` to store unique elements can take up to O(N) space (if all elements are unique).
    *   The `sorted_unique_elements` list also takes O(U) space, which is O(N) in the worst case.
    *   The `rank_map` dictionary stores U key-value pairs, taking O(U) space, or O(N) in the worst case.
    *   The `result` list stores N elements, taking O(N) space.
    *   Therefore, the total space complexity is O(N).

## Edge Cases
*   **Empty array `[]`**: The solution explicitly checks for `if not arr:` and returns `[]`, handling this correctly.
*   **Array with one element `[5]`**: `sorted_unique_elements` becomes `[5]`, `rank_map` becomes `{5: 1}`, and the result is `[1]`. Correct.
*   **All elements are the same `[7,7,7]`**: `sorted_unique_elements` becomes `[7]`, `rank_map` becomes `{7: 1}`, and the result is `[1,1,1]`. Correct.
*   **Negative numbers or very large numbers**: The approach works correctly regardless of the magnitude of the numbers, as sorting and hash mapping only depend on their relative order and distinctness, not their absolute values. For example, `[-5, -10, 0]` would correctly yield `[2, 1, 3]`.

## Solution
```python
from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Handle the edge case of an empty array.
        # If there are no elements, there are no ranks to assign.
        if not arr:
            return []

        # Step 1: Get unique elements from the array and sort them.
        # Using a set first efficiently removes duplicates.
        # Then, converting to a list allows us to sort them.
        sorted_unique_elements = sorted(list(set(arr)))

        # Step 2: Create a mapping from each unique element to its rank.
        # Ranks start from 1 and increment for each distinct element.
        rank_map = {}
        current_rank = 1
        for element in sorted_unique_elements:
            rank_map[element] = current_rank
            current_rank += 1 # Move to the next rank for the next unique element

        # Step 3: Transform the original array using the created rank_map.
        # Iterate through the original array and replace each number
        # with its corresponding rank found in the map.
        result = []
        for number in arr:
            result.append(rank_map[number])

        return result

```

## Why This Works
This approach works because it systematically establishes the **relative order** of all numbers in the array. By first identifying all unique numbers and sorting them, we create a definitive sequence from the smallest unique value to the largest. Assigning consecutive ranks (1, 2, 3, ...) to these sorted unique values ensures that all ranking rules are met: ranks start at 1, larger elements get larger ranks, and crucially, equal elements receive the same rank because they all map to the same entry in our `rank_map`. The final step of iterating through the original array and looking up ranks efficiently reconstructs the desired output array, preserving the original positions while applying the new rank values.

---
<sub>Generated 2026-07-12 04:08 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
