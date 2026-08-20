# [3069] Distribute Elements Into Two Arrays I

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-08-20 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/distribute-elements-into-two-arrays-i/)

**Topics:** Array, Simulation

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 1-indexed array of distinct integers nums of length n.

You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first operation, append nums[1] to arr1. In the second operation, append nums[2] to arr2. Afterwards, in the i^th operation:

- If the last element of arr1 is greater than the last element of arr2, append nums[i] to arr1. Otherwise, append nums[i] to arr2.

The array result is formed by concatenating the arrays arr1 and arr2. For example, if arr1 == [1,2,3] and arr2 == [4,5,6], then result = [1,2,3,4,5,6].

Return the array result.

Example 1:

Input: nums = [2,1,3]
Output: [2,3,1]
Explanation: After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3^rd operation, as the last element of arr1 is greater than the last element of arr2 (2 > 1), append nums[3] to arr1.
After 3 operations, arr1 = [2,3] and arr2 = [1].
Hence, the array result formed by concatenation is [2,3,1].

Example 2:

Input: nums = [5,4,3,8]
Output: [5,3,4,8]
Explanation: After the first 2 operations, arr1 = [5] and arr2 = [4].
In the 3^rd operation, as the last element of arr1 is greater than the last element of arr2 (5 > 4), append nums[3] to arr1, hence arr1 becomes [5,3].
In the 4^th operation, as the last element of arr2 is greater than the last element of arr1 (4 > 3), append nums[4] to arr2, hence arr2 becomes [4,8].
After 4 operations, arr1 = [5,3] and arr2 = [4,8].
Hence, the array result formed by concatenation is [5,3,4,8].

Constraints:

- 3 <= n <= 50

- 1 <= nums[i] <= 100

- All elements in nums are distinct.

**Examples / sample tests:**

```
[2,1,3]
[5,4,3,8]
```

---

## Problem Summary
You are given an array `nums` of distinct integers. The task is to distribute all elements of `nums` into two new arrays, `arr1` and `arr2`. The first element of `nums` goes to `arr1`, the second to `arr2`. For subsequent elements, append to `arr1` if its last element is greater than `arr2`'s last element; otherwise, append to `arr2`. Finally, return the concatenation of `arr1` and `arr2`.

## Intuition
The problem describes a very specific, step-by-step process for distributing elements. This immediately suggests a **direct simulation** approach. We need to maintain `arr1` and `arr2` as we build them, always keeping track of their last elements to make the decision for the next incoming number. Since the input array size `n` is small (up to 50), a straightforward simulation will be highly efficient and perfectly acceptable.

## Approach
We will simulate the distribution process exactly as described:

1.  **Initialization**: Create two empty lists, `arr1` and `arr2`.
2.  **First Operation**: Append the first element of `nums` (which is `nums[0]` in 0-indexed Python) to `arr1`.
3.  **Second Operation**: Append the second element of `nums` (which is `nums[1]` in 0-indexed Python) to `arr2`.
4.  **Subsequent Operations**: Iterate through the rest of the elements in `nums`, starting from the third element (`nums[2]` in 0-indexed Python) up to the last element (`nums[n-1]`). For each element `current_num = nums[i]`:
    *   Get the **last element of `arr1`** (i.e., `arr1[-1]`).
    *   Get the **last element of `arr2`** (i.e., `arr2[-1]`).
    *   **Compare**: If `arr1[-1]` is strictly greater than `arr2[-1]`, append `current_num` to `arr1`.
    *   **Otherwise**: (If `arr1[-1]` is less than or equal to `arr2[-1]`), append `current_num` to `arr2`.
5.  **Final Result**: Once all elements from `nums` have been distributed, concatenate `arr1` and `arr2` (e.g., `arr1 + arr2`) and return the combined list.

## Visualization
```mermaid
graph TD
    A[Start] --> B{Initialize arr1 = [], arr2 = []};
    B --> C{arr1.append(nums[0])};
    C --> D{arr2.append(nums[1])};
    D --> E{For i from 2 to n-1:};
    E --> F{current_num = nums[i]};
    F --> G{last_arr1 = arr1[-1]};
    G --> H{last_arr2 = arr2[-1]};
    H --> I{last_arr1 > last_arr2?};
    I -- Yes --> J{arr1.append(current_num)};
    I -- No --> K{arr2.append(current_num)};
    J --> E;
    K --> E;
    E --> L{Loop End};
    L --> M{Return arr1 + arr2};
    M --> N[End];
```

## Dry Run
Let's trace Example 1: `nums = [2,1,3]`

| Operation | `i` | `nums[i]` | `arr1` (last) | `arr2` (last) | Condition (`arr1_last > arr2_last`) | Action                 | `arr1`    | `arr2`    |
| :-------- | :-: | :-------: | :------------: | :------------: | :----------------------------------: | :--------------------- | :-------- | :-------- |
| Initial   | -   | -         | -              | -              | -                                    | -                      | `[]`      | `[]`      |
| 1st op    | 0   | 2         | -              | -              | -                                    | `arr1.append(2)`       | `[2]`     | `[]`      |
| 2nd op    | 1   | 1         | -              | -              | -                                    | `arr2.append(1)`       | `[2]`     | `[1]`     |
| 3rd op    | 2   | 3         | 2              | 1              | `2 > 1` (True)                       | `arr1.append(3)`       | `[2,3]`   | `[1]`     |
| **Final** | -   | -         | -              | -              | -                                    | Concatenate `arr1 + arr2` | `[2,3,1]` |           |

The final result is `[2,3,1]`, which matches the example output.

## Complexity
*   **Time Complexity**: O(N)
    *   We iterate through the `nums` array exactly once (after the first two initial appends).
    *   Appending elements to Python lists takes amortized O(1) time.
    *   Concatenating the two final lists (`arr1 + arr2`) takes O(N) time, where N is the total number of elements.
    *   Therefore, the overall time complexity is dominated by the single pass and concatenation, resulting in O(N).
*   **Space Complexity**: O(N)
    *   We create two new lists, `arr1` and `arr2`, which together store all N elements from the original `nums` array.
    *   This requires space proportional to the input size, hence O(N).

## Edge Cases
*   **Smallest `n` (n=3)**: The problem constraints state `3 <= n <= 50`. This means `nums` will always have at least 3 elements. Our approach correctly handles this: `nums[0]` goes to `arr1`, `nums[1]` to `arr2`, and `nums[2]` is processed in the loop, ensuring `arr1` and `arr2` always have at least one element before the loop starts, so `arr1[-1]` and `arr2[-1]` are always valid.
*   **Distinct Elements**: The problem states all elements in `nums` are distinct. This simplifies the comparison `arr1[-1] > arr2[-1]` as we don't need to worry about `arr1[-1] == arr2[-1]` requiring special handling beyond the "otherwise" clause (which correctly covers the equality case).
*   **Value Range**: `1 <= nums[i] <= 100`. This range is small and doesn't affect the logic or complexity.

## Solution

```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # Initialize arr1 and arr2.
        # According to the problem statement:
        # "In the first operation, append nums[1] to arr1." (nums[0] in 0-indexed Python)
        # "In the second operation, append nums[2] to arr2." (nums[1] in 0-indexed Python)
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        # Iterate through the rest of the elements starting from the third element (index 2)
        # "Afterwards, in the i^th operation: append nums[i]..."
        # This corresponds to nums[i-1] in 0-indexed Python for the original problem's i.
        # So, for 0-indexed 'k' from 2 to n-1, we process nums[k].
        for k in range(2, len(nums)):
            # Get the last elements of arr1 and arr2
            last_arr1 = arr1[-1]
            last_arr2 = arr2[-1]

            # Apply the distribution rule
            if last_arr1 > last_arr2:
                arr1.append(nums[k])
            else:
                arr2.append(nums[k])
        
        # Concatenate arr1 and arr2 to form the result array
        return arr1 + arr2

```

## Why This Works
This solution works because it **directly simulates** the process described in the problem statement. Each element is processed sequentially according to the given rules. By maintaining `arr1` and `arr2` and always comparing their most recently added elements, we ensure that the distribution logic is applied correctly at every step. The problem constraints are small, making this straightforward simulation approach both correct and optimal in terms of efficiency. There are no hidden complexities or optimizations required beyond faithfully executing the specified operations.

---
<sub>Generated 2026-08-20 02:02 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
