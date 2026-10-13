# [3727] Maximum Alternating Sum of Squares

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-10-13 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximum-alternating-sum-of-squares/)

**Topics:** Array, Greedy, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums. You may rearrange the elements in any order.

The alternating score of an array arr is defined as:

- score = arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + ...

Return an integer denoting the maximum possible alternating score of nums after rearranging its elements.

Example 1:

Input: nums = [1,2,3]

Output: 12

Explanation:

A possible rearrangement for nums is [2,1,3], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = 2^2 - 1^2 + 3^2 = 4 - 1 + 9 = 12

Example 2:

Input: nums = [1,-1,2,-2,3,-3]

Output: 16

Explanation:

A possible rearrangement for nums is [-3,-1,-2,1,3,2], which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

score = (-3)^2 - (-1)^2 + (-2)^2 - (1)^2 + (3)^2 - (2)^2 = 9 - 1 + 4 - 1 + 9 - 4 = 16

Constraints:

- 1 <= nums.length <= 10^5

- -4 * 10^4 <= nums[i] <= 4 * 10^4

**Examples / sample tests:**

```
[1,2,3]
[1,-1,2,-2,3,-3]
```

---

## Problem Summary

Given an integer array `nums`, you can rearrange its elements in any order. The **alternating score** is defined as $arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + \dots$. Find and return the maximum possible score achievable.

## Intuition

1. **Signs do not matter initially**: Because every element is squared ($arr[i]^2$), negative and positive numbers with the same magnitude contribute identical values.
2. **Fixed number of positive and negative slots**:
   - Even indices ($0, 2, 4, \dots$) have a **positive** sign ($+$). There are $\lceil n / 2 \rceil = (n + 1) // 2$ such positions.
   - Odd indices ($1, 3, 5, \dots$) have a **negative** sign ($-$). There are $\lfloor n / 2 \rfloor = n // 2$ such positions.
3. **Greedy choice**: To maximize $\sum \text{positives} - \sum \text{negatives}$, we should assign the **largest** squared values to positive positions and the **smallest** squared values to negative positions.

## Approach

1. Compute the square of each element in `nums` (or take their absolute values).
2. Sort the squared values in ascending order.
3. Determine $k = n // 2$, which is the number of negative terms.
4. The first $k$ smallest values will be subtracted; the remaining $n - k$ largest values will be added.
5. Return the sum of the top $n - k$ squares minus the sum of the bottom $k$ squares.

## Visualization

For `nums = [1, 2, 3]`:

```text
Squares: [1, 4, 9]  (n = 3)

Positives needed: (3 + 1) // 2 = 2 slots  --> Take largest: [4, 9]
Negatives needed: 3 // 2       = 1 slot   --> Take smallest: [1]

Rearranged:
Index:     0     1     2
Sign:     (+)   (-)   (+)
Value:     4  -  1  +  9  = 12
```

## Dry Run

### Input: `nums = [1, 2, 3]`

1. Square each element: `[1, 4, 9]`
2. Sort ascending: `[1, 4, 9]`
3. Length $n = 3$, $k = 3 // 2 = 1$ negative element.

| Step | Elements Chosen | Operation | Subtotal |
| :--- | :--- | :--- | :--- |
| Negative elements | `[1]` | $-(1)$ | $-1$ |
| Positive elements | `[4, 9]` | $+(4 + 9)$ | $+13$ |
| Final Score | — | $13 - 1$ | **12** |

## Complexity

- **Time Complexity:** $O(n \log n)$ — Sorting the array of $n$ elements dominates the runtime.
- **Space Complexity:** $O(n)$ — Storing squared values (or $O(1)$ auxiliary space if sorting in-place by absolute value).

## Edge Cases

- **$n = 1$**: All elements are positive terms; simply returns $nums[0]^2$.
- **Even length vs. Odd length**: Correctly handled by integer division: $(n + 1) // 2$ elements are added and $n // 2$ elements are subtracted.
- **Negative numbers & zeroes**: Handled naturally since $(-x)^2 = x^2 \ge 0$.

## Solution

```python
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Step 1: Compute squares and sort them in ascending order
        sq = sorted(x * x for x in nums)
        n = len(sq)

        # Step 2: The smallest n // 2 elements are subtracted,
        #         and the remaining elements are added.
        num_negatives = n // 2

        neg_sum = sum(sq[:num_negatives])
        pos_sum = sum(sq[num_negatives:])

        return pos_sum - neg_sum
```

## Why This Works

In any permutation, exactly $\lceil n / 2 \rceil$ positions contribute $+x_i^2$ and $\lfloor n / 2 \rfloor$ positions contribute $-x_i^2$. Because all squared terms are non-negative, by the **rearrangement inequality**, pairing the largest available values with the coefficient $+1$ and the smallest available values with $-1$ strictly maximizes the linear objective function $\sum c_i \cdot y_i$.

---
<sub>Generated 2026-10-13 07:02 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
