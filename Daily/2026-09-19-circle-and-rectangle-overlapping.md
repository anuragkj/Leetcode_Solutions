# [1401] Circle and Rectangle Overlapping

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-09-19 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/circle-and-rectangle-overlapping/)

**Topics:** Math, Geometry

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (x_i, y_i) that belongs to the circle and the rectangle at the same time.

Example 1:

Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0).

Example 2:

Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false

Example 3:

Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true

Constraints:

- 1 <= radius <= 2000

- -10^4 <= xCenter, yCenter <= 10^4

- -10^4 <= x1 < x2 <= 10^4

- -10^4 <= y1 < y2 <= 10^4

**Examples / sample tests:**

```
1
0
0
1
-1
3
1
1
1
1
1
-3
2
-1
1
0
0
-1
0
0
1
```

---

## Problem Summary
We need to determine if a given circle and an axis-aligned rectangle overlap. The circle is defined by its `radius` and center `(xCenter, yCenter)`. The rectangle is defined by its bottom-left `(x1, y1)` and top-right `(x2, y2)` corners.

## Intuition
The core idea to solve this problem is to find the **closest point on the rectangle to the circle's center**. Once we have this closest point, we can calculate the distance between it and the circle's center. If this distance is less than or equal to the circle's `radius`, then the circle and rectangle must overlap. Otherwise, they do not. This approach works because if any part of the rectangle is inside the circle, or if they touch, the closest point on the rectangle to the circle's center will necessarily be within or on the boundary of the circle.

## Approach
The algorithm focuses on finding the coordinates of the point on the rectangle that is nearest to the circle's center `(xCenter, yCenter)`.

1.  **Find the closest X-coordinate (`closestX`) on the rectangle to `xCenter`**:
    *   If `xCenter` is to the left of the rectangle (i.e., `xCenter < x1`), the closest X-coordinate on the rectangle is `x1`.
    *   If `xCenter` is to the right of the rectangle (i.e., `xCenter > x2`), the closest X-coordinate on the rectangle is `x2`.
    *   If `xCenter` is horizontally within the rectangle (i.e., `x1 <= xCenter <= x2`), the closest X-coordinate on the rectangle is `xCenter` itself.
    *   This logic can be concisely expressed as `closestX = max(x1, min(xCenter, x2))`.

2.  **Find the closest Y-coordinate (`closestY`) on the rectangle to `yCenter`**:
    *   Apply the same logic as for the X-coordinate:
    *   `closestY = max(y1, min(yCenter, y2))`.

3.  **Calculate the squared distance**:
    *   Let `(closestX, closestY)` be the point on the rectangle found in steps 1 and 2.
    *   Calculate the horizontal difference: `distX = xCenter - closestX`.
    *   Calculate the vertical difference: `distY = yCenter - closestY`.
    *   The squared Euclidean distance from `(xCenter, yCenter)` to `(closestX, closestY)` is `squared_distance = distX * distX + distY * distY`.
    *   We use squared distance to avoid calculating `sqrt()`, which can be computationally expensive and introduce floating-point precision issues.

4.  **Check for overlap**:
    *   Compare the `squared_distance` to the `radius * radius` (squared radius).
    *   If `squared_distance <= radius * radius`, the circle and rectangle overlap. Return `True`.
    *   Otherwise, they do not overlap. Return `False`.

## Visualization

Let `(Cx, Cy)` be `(xCenter, yCenter)`.
The rectangle spans from `x1` to `x2` horizontally, and `y1` to `y2` vertically.

```
                                 (Cx, Cy)
                                    .
                                    |
                                    |
                                    v
       +-------------------------------------------------+
       |                                                 |
       |                                                 |
       |                                                 |
       |                                                 |
       |                                                 |
       +-------------------------------------------------+
     (x1,y1)                                         (x2,y2)

To find the closest X-coordinate on the rectangle to Cx:
- If Cx < x1: closestX = x1
- If Cx > x2: closestX = x2
- If x1 <= Cx <= x2: closestX = Cx

Example 1: Cx < x1
  Cx
  .
  +-----------------+
  |                 |
  |                 |
  +-----------------+
  closestX = x1

Example 2: Cx > x2
                    Cx
                    .
  +-----------------+
  |                 |
  |                 |
  +-----------------+
  closestX = x2

Example 3: x1 <= Cx <= x2
  +-----------------+
  |   Cx            |
  |   .             |
  +-----------------+
  closestX = Cx

The same logic applies vertically for Cy to find closestY.
The point (closestX, closestY) is the point on the rectangle closest to (Cx, Cy).
```

## Dry Run
Let's walk through **Example 1**:
`radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1`

| Step | Variable | Value | Explanation |
| :--- | :------- | :---- | :---------- |
| 1    | `xCenter` | 0     | Circle center X-coordinate |
|      | `yCenter` | 0     | Circle center Y-coordinate |
|      | `x1`      | 1     | Rectangle bottom-left X |
|      | `y1`      | -1    | Rectangle bottom-left Y |
|      | `x2`      | 3     | Rectangle top-right X |
|      | `y2`      | 1     | Rectangle top-right Y |
| 2    | `closestX` | `max(x1, min(xCenter, x2))` <br> `= max(1, min(0, 3))` <br> `= max(1, 0)` <br> `= 1` | `xCenter` (0) is less than `x1` (1), so the closest X on the rectangle is `x1`. |
| 3    | `closestY` | `max(y1, min(yCenter, y2))` <br> `= max(-1, min(0, 1))` <br> `= max(-1, 0)` <br> `= 0` | `yCenter` (0) is between `y1` (-1) and `y2` (1), so the closest Y on the rectangle is `yCenter`. |
| 4    | `distX`   | `xCenter - closestX` <br> `= 0 - 1` <br> `= -1` | Horizontal difference. |
| 5    | `distY`   | `yCenter - closestY` <br> `= 0 - 0` <br> `= 0` | Vertical difference. |
| 6    | `squared_distance` | `distX * distX + distY * distY` <br> `= (-1)^2 + 0^2` <br> `= 1 + 0` <br> `= 1` | Squared distance from circle center (0,0) to closest point on rectangle (1,0). |
| 7    | `radius`  | 1     | Given radius. |
| 8    | `radius * radius` | `1 * 1` <br> `= 1` | Squared radius. |
| 9    | `squared_distance <= radius * radius` | `1 <= 1` <br> `= True` | Check if the squared distance is within the squared radius. |
| **Final Result** | | `True` | The circle and rectangle overlap. |

## Complexity
*   **Time Complexity**: O(1)
    *   The solution involves a fixed number of arithmetic operations (comparisons, additions, multiplications), regardless of the input values.
*   **Space Complexity**: O(1)
    *   The solution uses a constant amount of extra space to store a few variables.

## Edge Cases
*   **Circle center is inside the rectangle**: In this case, `closestX` will be `xCenter` and `closestY` will be `yCenter`. The `squared_distance` will be 0, which is always `<= radius * radius` (since `radius >= 1`). The solution correctly returns `True`.
*   **Circle touches the rectangle at a corner**: The `closestX` and `closestY` will correctly identify the corner coordinates. The distance check will then confirm the overlap.
*   **Circle touches the rectangle along an edge**: Similar to the corner case, `closestX` or `closestY` will be `xCenter` or `yCenter` respectively, and the other will be an edge coordinate. The distance check works.
*   **Rectangle is very small (e.g., a line segment or a single point)**: The `min` and `max` operations still correctly clamp `xCenter` and `yCenter` to the valid range of the rectangle, even if that range is degenerate.
*   **Large coordinates**: The coordinates and radius can be up to `10^4` and `2000` respectively. `distX` and `distY` can be up to `2 * 10^4`. `squared_distance` can be up to `(2 * 10^4)^2 + (2 * 10^4)^2 = 4 * 10^8 + 4 * 10^8 = 8 * 10^8`. `radius * radius` can be up to `2000^2 = 4 * 10^6`. These values fit comfortably within standard integer types (Python handles large integers automatically).

## Solution

```python
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Step 1: Find the closest x-coordinate on the rectangle to the circle's center.
        # This clamps xCenter to be within the rectangle's x-bounds [x1, x2].
        # If xCenter is less than x1, closestX becomes x1.
        # If xCenter is greater than x2, closestX becomes x2.
        # If xCenter is between x1 and x2, closestX remains xCenter.
        closestX = max(x1, min(xCenter, x2))

        # Step 2: Find the closest y-coordinate on the rectangle to the circle's center.
        # This clamps yCenter to be within the rectangle's y-bounds [y1, y2].
        # Similar logic as for x-coordinate.
        closestY = max(y1, min(yCenter, y2))

        # Step 3: Calculate the squared distance between the circle's center
        # (xCenter, yCenter) and this closest point on the rectangle (closestX, closestY).
        # We use squared distance to avoid floating-point operations (sqrt)
        # and potential precision issues, comparing it to radius^2.
        distX = xCenter - closestX
        distY = yCenter - closestY
        squared_distance = distX * distX + distY * distY

        # Step 4: Check if this squared distance is less than or equal to the
        # squared radius. If it is, the circle and rectangle overlap.
        return squared_distance <= radius * radius

```

## Why This Works
This approach works because it correctly identifies the **minimum distance** from the circle's center to any point on the rectangle. If the circle and rectangle overlap, then there must be at least one point on the rectangle that is within or on the boundary of the circle. This implies that the point on the rectangle closest to the circle's center must have a distance less than or equal to the radius. Conversely, if the closest point on the rectangle is further away than the radius, then no part of the rectangle can be inside the circle, ensuring no overlap. The `max(min())` clamping logic precisely finds the coordinates of this closest point on an axis-aligned rectangle.

---
<sub>Generated 2026-09-19 04:55 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
