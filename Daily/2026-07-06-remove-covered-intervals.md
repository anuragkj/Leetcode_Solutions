# [1288] Remove Covered Intervals

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-07-06 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/remove-covered-intervals/)

**Topics:** Array, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given an array intervals where intervals[i] = [l_i, r_i] represent the interval [l_i, r_i), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1

Constraints:

- 1 <= intervals.length <= 1000

- intervals[i].length == 2

- 0 <= l_i < r_i <= 10^5

- All the given intervals are unique.

**Examples / sample tests:**

```
[[1,4],[3,6],[2,8]]
[[1,4],[2,3]]
```

---

## Problem Summary

Given a list of intervals, we need to remove any interval that is completely **covered** by another interval. An interval $[a, b)$ is covered by $[c, d)$ if and only if $c \le a$ and $b \le d$. We return the count of the remaining intervals.

---

## Intuition

If we compare every interval with every other interval, it will take $O(N^2)$ time. To do this more efficiently, we can **sort** the intervals. 

If we sort the intervals such that we process them from left to right:
1. We sort by **start point ascending**. This ensures that for any current interval, its start point is guaranteed to be greater than or equal to the start points of all previously processed intervals ($c \le a$ is automatically satisfied).
2. If two intervals have the **same start point**, we sort them by **end point descending**. This ensures that the larger, wider interval is processed first, so any smaller interval starting at the same point is immediately recognized as covered.

With this sorting strategy, we only need to keep track of the **maximum end point** seen so far (`max_end`). If a subsequent interval's end point is less than or equal to `max_end`, it is completely covered!

---

## Approach

1. **Sort** the `intervals` array with a custom key:
   - Primary key: `x[0]` (start point) in **ascending** order.
   - Secondary key: `-x[1]` (end point) in **descending** order.
2. Initialize `remaining_count = 0` and `max_end = 0`.
3. Iterate through each interval `[start, end]` in the sorted list:
   - If `end > max_end`: This interval extends further than any interval we have seen so far. It cannot be covered. We increment `remaining_count` and update `max_end = end`.
   - If `end <= max_end`: This interval is completely covered by a previously processed interval. We do nothing (it is discarded).
4. Return `remaining_count`.

---

## Visualization

Let's visualize Example 1: `[[1,4],[3,6],[2,8]]`

After sorting: `[[1,4], [2,8], [3,6]]`

```text
Timeline:
0   1   2   3   4   5   6   7   8
|---|---|---|---|---|---|---|---|
 [=====]                          <- [1,4] (Keep: end 4 > max_end 0. New max_end = 4)
     [=========================]  <- [2,8] (Keep: end 8 > max_end 4. New max_end = 8)
         [=========]              <- [3,6] (Covered: end 6 <= max_end 8. Discard!)
```

---

## Dry Run

### Input: `intervals = [[1,4],[3,6],[2,8]]`
**Sorted Intervals:** `[[1,4], [2,8], [3,6]]`

| Step | Interval `[start, end]` | Condition (`end > max_end`) | Action | `max_end` | `remaining_count` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *Init* | — | — | — | `0` | `0` |
| 1 | `[1, 4]` | `4 > 0` (True) | Keep & Update | `4` | `1` |
| 2 | `[2, 8]` | `8 > 4` (True) | Keep & Update | `8` | `2` |
| 3 | `[3, 6]` | `6 > 8` (False) | Discard (Covered) | `8` | `2` |

**Final Output:** `2`

---

## Complexity

- **Time Complexity:** $\mathcal{O}(N \log N)$ where $N$ is the number of intervals. This is dominated by the sorting step. The subsequent linear scan takes $\mathcal{O}(N)$ time.
- **Space Complexity:** $\mathcal{O}(N)$ or $\mathcal{O}(\log N)$ depending on the sorting implementation details of Python's Timsort (which stores temporary runs).

---

## Edge Cases

- **Single Interval:** `[[1, 4]]` $\rightarrow$ Loop runs once, returns `1`. Handled correctly.
- **Identical Starts:** `[[1, 5], [1, 3]]` $\rightarrow$ Sorted to `[[1, 5], [1, 3]]`. `[1, 5]` sets `max_end = 5`. `[1, 3]` has `3 <= 5`, so it is correctly discarded.
- **No Overlaps:** `[[1, 2], [3, 4]]` $\rightarrow$ `max_end` updates at each step, returns `2`. Handled correctly.

---

## Solution

```python
from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start ascending, then by end descending
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        remaining_count = 0
        max_end = 0
        
        for _, end in intervals:
            # If the current interval extends beyond the furthest end seen so far,
            # it is not covered by any previous interval.
            if end > max_end:
                remaining_count += 1
                max_end = end
                
        return remaining_count
```

---

## Why This Works

By sorting the intervals by start point ascending, we guarantee that any interval processed later starts at or after any interval processed earlier ($c \le a$). By sorting identical start points by end point descending, we ensure that the largest interval is processed first. Consequently, if a subsequent interval has an end point $b \le \text{max\_end}$, it is guaranteed to be nested within a previously seen interval that started before (or at) $a$ and ended at or after $b$.

---
<sub>Generated 2026-07-06 04:56 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
