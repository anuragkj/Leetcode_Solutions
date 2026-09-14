# [836] Rectangle Overlap

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-09-14 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/rectangle-overlap/)

**Topics:** Math, Geometry

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true

Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false

Example 3:

Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false

Constraints:

- rec1.length == 4

- rec2.length == 4

- -10^9 <= rec1[i], rec2[i] <= 10^9

- rec1 and rec2 represent a valid rectangle with a non-zero area.

**Examples / sample tests:**

```
[0,0,2,2]
[1,1,3,3]
[0,0,1,1]
[1,0,2,1]
[0,0,1,1]
[2,2,3,3]
```

---

## Problem Summary
Given two axis-aligned rectangles, each defined by its bottom-left and top-right corner coordinates `[x1, y1, x2, y2]`, determine if they **overlap**. Overlap means their intersection area is positive; merely touching at an edge or corner does not count as overlapping.

## Intuition
When dealing with geometric overlap problems, it's often easier to think about the **opposite**: when do they *not* overlap? If we can define all conditions where two rectangles *do not* overlap, then the negation of those conditions will tell us when they *do* overlap.

Two rectangles **do not overlap** if one is entirely:
1.  To the left of the other.
2.  To the right of the other.
3.  Below the other.
4.  Above the other.

If any of these four conditions are true, the rectangles do not overlap.
Therefore, the rectangles **do overlap** if and only if **NONE** of these four non-overlap conditions are true. This means they must overlap along both the X-axis (horizontally) AND the Y-axis (vertically).

Let's break this down for the X-axis:
*   Rectangle 1's horizontal span: `[rec1[0], rec1[2]]` (from `x1_1` to `x2_1`)
*   Rectangle 2's horizontal span: `[rec2[0], rec2[2]]` (from `x1_2` to `x2_2`)

They *don't* overlap horizontally if:
*   `rec1` is entirely to the left of `rec2`: `rec1[2] <= rec2[0]` (rec1's right edge is at or left of rec2's left edge)
*   `rec1` is entirely to the right of `rec2`: `rec1[0] >= rec2[2]` (rec1's left edge is at or right of rec2's right edge)

Since the problem states "positive area" and "touching does not overlap", we need **strict inequalities**. So, they *don't* overlap horizontally if:
*   `rec1[2] <= rec2[0]`
*   `rec1[0] >= rec2[2]`

Therefore, they *do* overlap horizontally if **neither** of these is true. This means:
*   `NOT (rec1[2] <= rec2[0])` which simplifies to `rec1[2] > rec2[0]` (rec1's right edge is to the right of rec2's left edge)
*   `NOT (rec1[0] >= rec2[2])` which simplifies to `rec1[0] < rec2[2]` (rec1's left edge is to the left of rec2's right edge)

Both of these conditions must be true for horizontal overlap. The same logic applies to vertical overlap using the Y-coordinates.

## Approach
The optimal approach is to check for overlap along the X-axis and Y-axis independently. If both the horizontal and vertical intervals overlap, then the rectangles overlap.

1.  **Extract Coordinates**:
    *   For `rec1`: `x1_1 = rec1[0]`, `y1_1 = rec1[1]`, `x2_1 = rec1[2]`, `y2_1 = rec1[3]`
    *   For `rec2`: `x1_2 = rec2[0]`, `y1_2 = rec2[1]`, `x2_2 = rec2[2]`, `y2_2 = rec2[3]`

2.  **Check for Horizontal Overlap**:
    The rectangles overlap horizontally if:
    *   `rec1`'s right edge is to the right of `rec2`'s left edge (`x2_1 > x1_2`)
    *   **AND** `rec2`'s right edge is to the right of `rec1`'s left edge (`x2_2 > x1_1`)
    If both conditions are true, there is horizontal overlap.

3.  **Check for Vertical Overlap**:
    The rectangles overlap vertically if:
    *   `rec1`'s top edge is above `rec2`'s bottom edge (`y2_1 > y1_2`)
    *   **AND** `rec2`'s top edge is above `rec1`'s bottom edge (`y2_2 > y1_1`)
    If both conditions are true, there is vertical overlap.

4.  **Combine Results**:
    Return `true` if there is **both** horizontal overlap **AND** vertical overlap. Otherwise, return `false`.

## Visualization

Let's visualize the horizontal overlap condition using number lines.
`rec1` is represented by the interval `[x1_1, x2_1]` and `rec2` by `[x1_2, x2_2]`.

**Case 1: Overlap (e.g., `rec1 = [0,2]`, `rec2 = [1,3]`)**
```
X-axis:
rec1:  [0-------2]
rec2:      [1-------3]

Condition 1: x2_1 > x1_2  (2 > 1)  -> True
Condition 2: x2_2 > x1_1  (3 > 0)  -> True
Both True -> Horizontal Overlap!
```

**Case 2: No Overlap (rec1 to the left of rec2, e.g., `rec1 = [0,1]`, `rec2 = [1,2]`)**
```
X-axis:
rec1:  [0---1]
rec2:      [1---2]

Condition 1: x2_1 > x1_2  (1 > 1)  -> False (they only touch)
Condition 2: x2_2 > x1_1  (2 > 0)  -> True
Since Condition 1 is False -> No Horizontal Overlap!
```

**Case 3: No Overlap (rec1 to the right of rec2, e.g., `rec1 = [2,3]`, `rec2 = [0,1]`)**
```
X-axis:
rec1:          [2---3]
rec2:  [0---1]

Condition 1: x2_1 > x1_2  (3 > 0)  -> True
Condition 2: x2_2 > x1_1  (1 > 2)  -> False
Since Condition 2 is False -> No Horizontal Overlap!
```

The same logic applies identically to the Y-axis coordinates for vertical overlap. For the rectangles to overlap, both the horizontal and vertical overlap conditions must be met.

## Dry Run

Let's walk through **Example 1**: `rec1 = [0,0,2,2]`, `rec2 = [1,1,3,3]`

1.  **Extract Coordinates**:
    *   `rec1`: `x1_1 = 0`, `y1_1 = 0`, `x2_1 = 2`, `y2_1 = 2`
    *   `rec2`: `x1_2 = 1`, `y1_2 = 1`, `x2_2 = 3`, `y2_2 = 3`

2.  **Check for Horizontal Overlap**:
    *   Is `x2_1 > x1_2`? Is `2 > 1`? **True**
    *   Is `x2_2 > x1_1`? Is `3 > 0`? **True**
    *   Since both are true, `horizontal_overlap = True`.

3.  **Check for Vertical Overlap**:
    *   Is `y2_1 > y1_2`? Is `2 > 1`? **True**
    *   Is `y2_2 > y1_1`? Is `3 > 0`? **True**
    *   Since both are true, `vertical_overlap = True`.

4.  **Combine Results**:
    *   Is `horizontal_overlap AND vertical_overlap`? Is `True AND True`? **True**

**Final Result for Example 1:** `true`

## Complexity

*   **Time Complexity**: **O(1)**
    The solution involves a fixed number of coordinate extractions and comparisons, regardless of the coordinate values.
*   **Space Complexity**: **O(1)**
    The solution uses a constant amount of extra space to store a few variables for coordinates and boolean flags.

## Edge Cases

*   **Rectangles touching at an edge (Example 2):** `rec1 = [0,0,1,1]`, `rec2 = [1,0,2,1]`
    *   Horizontal check: `x2_1 > x1_2` (1 > 1) is `False`.
    *   Since horizontal overlap is `False`, the function correctly returns `False`.
*   **Rectangles touching at a corner:** `rec1 = [0,0,1,1]`, `rec2 = [1,1,2,2]`
    *   Horizontal check: `x2_1 > x1_2` (1 > 1) is `False`.
    *   Since horizontal overlap is `False`, the function correctly returns `False`.
*   **One rectangle completely inside another:** `rec1 = [0,0,5,5]`, `rec2 = [1,1,2,2]`
    *   Horizontal check: `x2_1 > x1_2` (5 > 1) is `True`, AND `x2_2 > x1_1` (2 > 0) is `True`. -> Horizontal overlap `True`.
    *   Vertical check: `y2_1 > y1_2` (5 > 1) is `True`, AND `y2_2 > y1_1` (2 > 0) is `True`. -> Vertical overlap `True`.
    *   Both `True` -> returns `True`. Correct.
*   **Large Coordinates:** The constraints allow coordinates up to `10^9`. Python's integers handle arbitrary size, so simple comparisons work correctly without overflow issues.
*   **Zero-area rectangles:** The problem statement guarantees "a valid rectangle with a non-zero area," meaning `x1 < x2` and `y1 < y2` for both rectangles. This simplifies the problem as we don't need to handle cases like `[0,0,0,5]` (a line) or `[0,0,0,0]` (a point).

## Solution

```python
from typing import List

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # Extract coordinates for rec1
        x1_1, y1_1, x2_1, y2_1 = rec1[0], rec1[1], rec1[2], rec1[3]
        
        # Extract coordinates for rec2
        x1_2, y1_2, x2_2, y2_2 = rec2[0], rec2[1], rec2[2], rec2[3]
        
        # Check for horizontal overlap
        # Condition 1: rec1's right edge is to the right of rec2's left edge
        # Condition 2: rec2's right edge is to the right of rec1's left edge
        # Both must be true for horizontal overlap with positive length
        horizontal_overlap = (x2_1 > x1_2) and (x2_2 > x1_1)
        
        # Check for vertical overlap
        # Condition 1: rec1's top edge is above rec2's bottom edge
        # Condition 2: rec2's top edge is above rec1's bottom edge
        # Both must be true for vertical overlap with positive length
        vertical_overlap = (y2_1 > y1_2) and (y2_2 > y1_1)
        
        # Rectangles overlap if and only if they overlap both horizontally AND vertically
        return horizontal_overlap and vertical_overlap

```

## Why This Works

This solution works by reducing the 2D rectangle overlap problem into two independent 1D interval overlap problems: one for the X-axis and one for the Y-axis. Two rectangles overlap if and only if their projections onto the X-axis overlap *and* their projections onto the Y-axis overlap. The key insight is using strict inequalities (`>`) to ensure a "positive area" intersection, correctly excluding cases where rectangles merely touch at an edge or corner, as specified by the problem. This approach is robust because it directly translates the geometric conditions of non-overlap into algebraic inequalities, and then negates them to find the overlap conditions.

---
<sub>Generated 2026-09-14 05:21 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
