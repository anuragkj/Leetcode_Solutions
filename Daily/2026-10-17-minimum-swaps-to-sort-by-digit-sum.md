# [3551] Minimum Swaps to Sort by Digit Sum

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-10-17 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/)

**Topics:** Array, Hash Table, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an array nums of distinct positive integers. You need to sort the array in increasing order based on the sum of the digits of each number. If two numbers have the same digit sum, the smaller number appears first in the sorted order.

Return the minimum number of swaps required to rearrange nums into this sorted order.

A swap is defined as exchanging the values at two distinct positions in the array.

Example 1:

Input: nums = [37,100]

Output: 1

Explanation:

- Compute the digit sum for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]

- Sort the integers based on digit sum: [100, 37]. Swap 37 with 100 to obtain the sorted order.

- Thus, the minimum number of swaps required to rearrange nums is 1.

Example 2:

Input: nums = [22,14,33,7]

Output: 0

Explanation:

- Compute the digit sum for each integer: [2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]

- Sort the integers based on digit sum: [22, 14, 33, 7]. The array is already sorted.

- Thus, the minimum number of swaps required to rearrange nums is 0.

Example 3:

Input: nums = [18,43,34,16]

Output: 2

Explanation:

- Compute the digit sum for each integer: [1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]

- Sort the integers based on digit sum: [16, 34, 43, 18]. Swap 18 with 16, and swap 43 with 34 to obtain the sorted order.

- Thus, the minimum number of swaps required to rearrange nums is 2.

Constraints:

- 1 <= nums.length <= 10^5

- 1 <= nums[i] <= 10^9

- nums consists of distinct positive integers.

**Examples / sample tests:**

```
[37,100]
[22,14,33,7]
[18,43,34,16]
```

---

## Problem Summary
You are given an array of distinct positive integers. The goal is to sort this array based on a custom rule: first, by the sum of the digits of each number in increasing order. If two numbers have the same digit sum, the smaller number should come first. You need to find the minimum number of swaps required to transform the original array into this specific sorted order.

## Intuition
The core of this problem lies in finding the **minimum number of swaps to sort an array** when the target sorted order is known. This is a classic problem that can be solved by understanding **permutation cycles**.

Imagine each number in the original array has an "original position" (its index). After sorting according to the custom rules, each number will have a "final position". We can create a mapping that tells us, for each original position, where the element currently at that position *should* end up. This mapping defines a permutation.

A key insight is that if a permutation can be decomposed into `C` disjoint cycles, then the minimum number of swaps required to sort it is `N - C`, where `N` is the total number of elements. Each cycle of length `k` requires `k-1` swaps to sort. Summing `(k-1)` over all cycles gives `sum(k) - sum(1)` which is `N - C`.

So, the strategy is:
1.  Figure out the desired final position for each element.
2.  Construct the permutation mapping.
3.  Count the cycles in this permutation.
4.  Calculate `N - C`.

## Approach
Here's a step-by-step approach:

1.  **Define a `get_digit_sum` helper function:** This function will take an integer `n` and return the sum of its digits. For example, `get_digit_sum(37)` returns `10`.

2.  **Pair numbers with their original indices:** Create a list of tuples, where each tuple is `(number, original_index)`. This is crucial because we need to track where each original number came from.
    *   Example: `nums = [37, 100]` becomes `[(37, 0), (100, 1)]`.

3.  **Sort these pairs:** Sort the list of `(number, original_index)` tuples using a custom sorting key.
    *   The primary sorting key is the **digit sum** of the `number` (ascending).
    *   The secondary sorting key (for tie-breaking) is the `number` itself (ascending).
    *   Example: `[(37, 0), (100, 1)]` sorted by `(digit_sum, value)` becomes `[(100, 1), (37, 0)]` because `(1, 100)` comes before `(10, 37)`.

4.  **Create a `target_indices` mapping:** After sorting, the `j`-th element in the `sorted_pairs` list tells us which original number should be at the `j`-th position in the final sorted array. We need to build an array, let's call it `target_indices`, where `target_indices[i]` stores the **final sorted index** for the number that was originally at index `i`.
    *   Initialize `target_indices` as an array of size `N`.
    *   Iterate through `sorted_pairs`: for each `(value, original_idx)` at `j`-th position in `sorted_pairs`, set `target_indices[original_idx] = j`.
    *   Example: If `sorted_pairs = [(100, 1), (37, 0)]`:
        *   For `(100, 1)` at `j=0`: `target_indices[1] = 0`.
        *   For `(37, 0)` at `j=1`: `target_indices[0] = 1`.
        *   So, `target_indices = [1, 0]`. This means the element originally at index 0 (which is 37) should go to index 1, and the element originally at index 1 (which is 100) should go to index 0.

5.  **Count cycles and calculate swaps:**
    *   Initialize `swaps = 0` and a `visited` boolean array of size `N` to `False`.
    *   Iterate `i` from `0` to `N-1`:
        *   If `visited[i]` is `True`, this element is already part of a counted cycle, so continue.
        *   If `visited[i]` is `False`, we've found the start of a new cycle.
            *   Start traversing the cycle: `current_idx = i`, `cycle_size = 0`.
            *   While `visited[current_idx]` is `False`:
                *   Mark `visited[current_idx] = True`.
                *   Move to the next element in the cycle: `current_idx = target_indices[current_idx]`.
                *   Increment `cycle_size`.
            *   Once the cycle is complete (`visited[current_idx]` is `True`), add `(cycle_size - 1)` to `swaps`. (A cycle of length `k` requires `k-1` swaps).

6.  **Return `swaps`**.

## Visualization
Let's trace Example 3: `nums = [18, 43, 34, 16]`

1.  **Original numbers and indices:**
    `[(18, 0), (43, 1), (34, 2), (16, 3)]`

2.  **Digit sums:**
    `get_digit_sum(18) = 9`
    `get_digit_sum(43) = 7`
    `get_digit_sum(34) = 7`
    `get_digit_sum(16) = 7`

3.  **Sort by (digit_sum, value):**
    *   `(18, 0)` -> `(9, 18)`
    *   `(43, 1)` -> `(7, 43)`
    *   `(34, 2)` -> `(7, 34)`
    *   `(16, 3)` -> `(7, 16)`

    Sorted keys: `(7, 16), (7, 34), (7, 43), (9, 18)`
    `sorted_pairs = [(16, 3), (34, 2), (43, 1), (18, 0)]`

4.  **Build `target_indices`:**
    `target_indices = [_, _, _, _]` (size 4)
    *   `j=0`: `(16, 3)` -> `target_indices[3] = 0`
    *   `j=1`: `(34, 2)` -> `target_indices[2] = 1`
    *   `j=2`: `(43, 1)` -> `target_indices[1] = 2`
    *   `j=3`: `(18, 0)` -> `target_indices[0] = 3`

    `target_indices = [3, 2, 1, 0]`

5.  **Cycle Detection:**
    ```
    Original Indices:  0   1   2   3
    Target Indices:    3   2   1   0  (pos_map)

    Permutation cycles:
    Start at i = 0:
    0 -> target_indices[0] = 3
    3 -> target_indices[3] = 0
    Cycle 1: (0 -> 3 -> 0)
    Length = 2. Swaps = 2 - 1 = 1.
    Visited: [T, F, F, T]

    Start at i = 1:
    1 -> target_indices[1] = 2
    2 -> target_indices[2] = 1
    Cycle 2: (1 -> 2 -> 1)
    Length = 2. Swaps = 2 - 1 = 1.
    Visited: [T, T, T, T]

    Start at i = 2: Visited[2] is True. Skip.
    Start at i = 3: Visited[3] is True. Skip.

    Total swaps = 1 + 1 = 2
    ```

## Dry Run
Let's walk through Example 1: `nums = [37, 100]`

| Step | Description                                   | `nums`      | `items`               | `sorted_pairs`        | `target_indices` | `visited`         | `swaps` | `current_idx` | `cycle_size` |
| :--- | :-------------------------------------------- | :---------- | :-------------------- | :-------------------- | :--------------- | :---------------- | :------ | :------------ | :----------- |
| 1    | Initialize                                    | `[37, 100]` |                       |                       | `[0, 0]`         | `[F, F]`          | `0`     |               |              |
| 2    | Create `items` with original indices          |             | `[(37, 0), (100, 1)]` |                       |                  |                   |         |               |              |
| 3    | Calculate digit sums: `ds(37)=10`, `ds(100)=1` |             |                       |                       |                  |                   |         |               |              |
| 4    | Sort `items` by `(digit_sum, value)`          |             |                       | `[(100, 1), (37, 0)]` |                  |                   |         |               |              |
| 5    | Build `target_indices`                        |             |                       |                       | `[1, 0]`         |                   |         |               |              |
| 6    | Loop `i=0`: `visited[0]` is `F`               |             |                       |                       |                  |                   |         | `0`           | `0`          |
| 6.1  |   `visited[0]=T`, `current_idx=target_indices[0]=1`, `cycle_size=1` |             |                       |                       |                  | `[T, F]`          | `0`     | `1`           | `1`          |
| 6.2  |   `visited[1]=F`. `visited[1]=T`, `current_idx=target_indices[1]=0`, `cycle_size=2` |             |                       |                       |                  | `[T, T]`          | `0`     | `0`           | `2`          |
| 6.3  |   `visited[0]=T`. Cycle ends.                 |             |                       |                       |                  |                   |         |               |              |
| 6.4  |   `swaps += (cycle_size - 1) = (2 - 1) = 1`   |             |                       |                       |                  |                   | `1`     |               |              |
| 7    | Loop `i=1`: `visited[1]` is `T`. Skip.        |             |                       |                       |                  |                   | `1`     |               |              |
| 8    | End of loop. Return `swaps`.                  |             |                       |                       |                  |                   | `1`     |               |              |

Final Result: `1`

## Complexity
*   **Time Complexity:** `O(N log N * D)`, where `N` is the length of `nums` and `D` is the maximum number of digits in any number (`log10(max_num)`).
    *   Calculating digit sums for all numbers and creating pairs: `O(N * D)`.
    *   Sorting the pairs: `O(N log N)` comparisons. Each comparison involves calculating digit sums, adding `D` to the comparison time. So, `O(N log N * D)`.
    *   Building `target_indices` array: `O(N)`.
    *   Counting cycles: Each element is visited and processed at most twice (once to start a cycle, once to be part of a cycle). `O(N)`.
    *   Since `D` is a small constant (at most 10 for `10^9`), the dominant factor is `O(N log N)`.
*   **Space Complexity:** `O(N)`
    *   To store the `items` (pairs of number and original index).
    *   To store the `target_indices` mapping.
    *   To store the `visited` array.

## Edge Cases
*   **`nums.length = 1`**: The array is already sorted. The algorithm will correctly identify `N=1` and `C=1` (one cycle of length 1), resulting in `1 - 1 = 0` swaps.
*   **Array already sorted by the custom rule**: `nums = [22, 14, 33, 7]`. `target_indices` will be `[0, 1, 2, 3]`. This means each element is already in its correct position. The cycle detection will find `N` cycles of length 1, resulting in `N - N = 0` swaps.
*   **All numbers have the same digit sum**: The tie-breaker (smaller number first) will correctly sort them. The algorithm handles this naturally through the `(digit_sum, value)` sorting key.
*   **Large numbers (up to `10^9`)**: The `get_digit_sum` function handles numbers up to `10^9` efficiently, as it only involves a few divisions and modulo operations (at most 10 iterations).
*   **Distinct positive integers**: The problem statement guarantees distinct positive integers, simplifying things by not needing to handle duplicate values or zero/negative numbers.

## Solution

```python
from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        # Helper function to calculate digit sum
        def get_digit_sum(num: int) -> int:
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s

        # 1. Create pairs of (original_value, original_index)
        # This allows us to track the original position of each number.
        indexed_nums = []
        for i in range(n):
            indexed_nums.append((nums[i], i))

        # 2. Sort these pairs based on the custom rules:
        #    Primary: digit sum (ascending)
        #    Secondary: original value (ascending, for tie-breaking)
        # The key function returns a tuple (digit_sum, value) for comparison.
        sorted_indexed_nums = sorted(indexed_nums, key=lambda x: (get_digit_sum(x[0]), x[0]))

        # 3. Create a mapping from original_index to its target_index
        # target_indices[i] will store the final sorted position for the number
        # that was originally at index i.
        target_indices = [0] * n
        for i in range(n):
            original_value, original_idx = sorted_indexed_nums[i]
            target_indices[original_idx] = i

        # 4. Count cycles in the permutation represented by target_indices
        # The minimum number of swaps is N - C, where N is array length
        # and C is the number of cycles.
        swaps = 0
        visited = [False] * n

        for i in range(n):
            if visited[i]:
                continue # Already part of a counted cycle

            # Start a new cycle
            cycle_size = 0
            current_idx = i
            
            while not visited[current_idx]:
                visited[current_idx] = True
                current_idx = target_indices[current_idx] # Move to the next element in the cycle
                cycle_size += 1
            
            # For a cycle of length k, k-1 swaps are needed
            if cycle_size > 0:
                swaps += (cycle_size - 1)
        
        return swaps

```

## Why This Works
This solution works because the problem of finding the minimum number of swaps to sort an array is equivalent to finding the minimum swaps to transform one permutation into another (the sorted one). This minimum number of swaps is `N - C`, where `N` is the number of elements and `C` is the number of disjoint cycles in the permutation.

By first sorting the numbers based on the custom digit sum and value rules, we establish the **desired final positions** for each element. The `target_indices` array then explicitly defines the permutation: `target_indices[i]` tells us where the element originally at index `i` *should* go. We then traverse this permutation, identifying and counting each cycle. Each cycle of length `k` requires `k-1` swaps to put its elements into their correct positions. Summing `(k-1)` for all cycles correctly yields the total minimum swaps.

---
<sub>Generated 2026-10-17 04:54 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
