# [835] Image Overlap

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-09-13 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/image-overlap/)

**Topics:** Array, Matrix

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.

Example 1:

Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1

Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0

Constraints:

- n == img1.length == img1[i].length

- n == img2.length == img2[i].length

- 1 <= n <= 30

- img1[i][j] is either 0 or 1.

- img2[i][j] is either 0 or 1.

**Examples / sample tests:**

```
[[1,1,0],[0,1,0],[0,1,0]]
[[0,0,0],[0,1,1],[0,0,1]]
[[1]]
[[1]]
[[0]]
[[0]]
```

---

## Problem Summary
You are given two square binary matrices (images) of size `n x n`. The goal is to slide one image (e.g., `img1`) over the other (`img2`) in any direction (up, down, left, right) and by any amount. For each possible translation, we count the number of positions where both images have a `1`. The task is to find the **largest possible overlap** among all translations.

## Intuition
The core idea is that we need to try **every single possible way** `img1` can be positioned relative to `img2`. Since we can slide `img1` up/down/left/right, this means `img1`'s top-left corner `(0,0)` can effectively be placed at various `(row_offset, col_offset)` positions relative to `img2`'s `(0,0)`.

Consider an `n x n` image.
- If `img1` is shifted `n-1` units to the right, its first column aligns with `img2`'s last column.
- If `img1` is shifted `n-1` units to the left, its last column aligns with `img2`'s first column.
- The same logic applies for up/down shifts.
Therefore, the `row_offset` and `col_offset` can range from `-(n-1)` to `(n-1)`. For each such `(row_offset, col_offset)` pair, we calculate the overlap and keep track of the maximum.

## Approach
The optimal approach involves systematically trying every possible relative translation between the two images and calculating the overlap for each.

1.  **Initialize `max_overlap = 0`**. This variable will store the largest overlap found.
2.  **Determine the range of translations**: For an `n x n` image, `img1` can be shifted relative to `img2` by `dr` rows and `dc` columns. Both `dr` and `dc` can range from `-(n-1)` to `(n-1)`.
    *   `dr` (row offset): `-(n-1), ..., 0, ..., (n-1)`
    *   `dc` (column offset): `-(n-1), ..., 0, ..., (n-1)`
3.  **Iterate through all possible `(dr, dc)` translation pairs**:
    *   For each `dr` in the range `[-(n-1), n-1]`:
        *   For each `dc` in the range `[-(n-1), n-1]`:
            *   **Calculate `current_overlap` for this `(dr, dc)`**:
                *   Initialize `current_overlap = 0`.
                *   Iterate through every cell `(r, c)` in `img1` (from `0` to `n-1` for both `r` and `c`).
                *   If `img1[r][c]` is `1`:
                    *   Calculate the corresponding coordinates in `img2`: `r_img2 = r + dr` and `c_img2 = c + dc`.
                    *   **Check bounds**: If `0 <= r_img2 < n` and `0 <= c_img2 < n` (meaning this part of `img1` is still within `img2`'s boundaries):
                        *   If `img2[r_img2][c_img2]` is also `1`, then we have an overlap. Increment `current_overlap`.
            *   **Update `max_overlap`**: After checking all cells for the current `(dr, dc)`, update `max_overlap = max(max_overlap, current_overlap)`.
4.  **Return `max_overlap`**.

## Visualization
Let's visualize Example 1: `img1 = [[1,1,0],[0,1,0],[0,1,0]]`, `img2 = [[0,0,0],[0,1,1],[0,0,1]]`. `n=3`.

Consider a translation of `dr=1` (down by 1) and `dc=1` (right by 1).
This means `img1`'s cell `(r,c)` aligns with `img2`'s cell `(r+1, c+1)`.

**1. Original Images:**
```
img1:        img2:
1 1 0        0 0 0
0 1 0        0 1 1
0 1 0        0 0 1
```

**2. Shift `img1` by `dr=1, dc=1` relative to `img2`:**
Imagine `img2` is fixed. `img1`'s top-left `(0,0)` moves to `img2`'s `(1,1)`.

```
Conceptual grid (img2 coordinates):
   (0,0) (0,1) (0,2)
   (1,0) (1,1) (1,2)
   (2,0) (2,1) (2,2)

Values of img2:
   0 0 0
   0 1 1
   0 0 1

Now, let's see where img1's '1's land on this grid:
- img1[0][0] = 1  ->  lands on img2[0+1][0+1] = img2[1][1]
- img1[0][1] = 1  ->  lands on img2[0+1][0+2] = img2[1][2]
- img1[1][1] = 1  ->  lands on img2[1+1][1+1] = img2[2][2]
- Other 1s in img1 (e.g., img1[2][1]) land outside img2's bounds.

Overlaying img1's shifted '1's onto img2 (marked with 'X' if both are 1):
(img2 values are shown, 'X' indicates an overlap of '1's)

   0 0 0
   0 X X  <- img1[0][0]=1 overlaps img2[1][1]=1; img1[0][1]=1 overlaps img2[1][2]=1
   0 0 X  <- img1[1][1]=1 overlaps img2[2][2]=1

Total overlap for this translation: 3
```

## Dry Run
Let's walk through Example 1:
`img1 = [[1,1,0],[0,1,0],[0,1,0]]`
`img2 = [[0,0,0],[0,1,1],[0,0,1]]`
`n = 3`

`max_overlap = 0`

We iterate `dr` from `-(3-1)` to `(3-1)`, i.e., `dr` from `-2` to `2`.
We iterate `dc` from `-(3-1)` to `(3-1)`, i.e., `dc` from `-2` to `2`.

Let's trace the specific case `dr = 1, dc = 1` (as shown in the example explanation).

| `r` | `c` | `img1[r][c]` | `r_img2` (`r+dr`) | `c_img2` (`c+dc`) | Bounds Check (`0<=r_img2<n`, `0<=c_img2<n`) | `img2[r_img2][c_img2]` | Overlap? (`img1[r][c]==1` AND `img2[...] == 1`) | `current_overlap` |
|-----|-----|--------------|-------------------|-------------------|------------------------------------------------|------------------------|-------------------------------------------------|-------------------|
| 0   | 0   | 1            | 1                 | 1                 | OK                                             | 1                      | Yes                                             | 1                 |
| 0   | 1   | 1            | 1                 | 2                 | OK                                             | 1                      | Yes                                             | 2                 |
| 0   | 2   | 0            | 1                 | 3                 | `c_img2` out of bounds                         | -                      | No                                              | 2                 |
| 1   | 0   | 0            | 2                 | 1                 | OK                                             | 0                      | No                                              | 2                 |
| 1   | 1   | 1            | 2                 | 2                 | OK                                             | 1                      | Yes                                             | 3                 |
| 1   | 2   | 0            | 2                 | 3                 | `c_img2` out of bounds                         | -                      | No                                              | 3                 |
| 2   | 0   | 0            | 3                 | 1                 | `r_img2` out of bounds                         | -                      | No                                              | 3                 |
| 2   | 1   | 1            | 3                 | 2                 | `r_img2` out of bounds                         | -                      | No                                              | 3                 |
| 2   | 2   | 0            | 3                 | 3                 | `r_img2`, `c_img2` out of bounds               | -                      | No                                              | 3                 |

After iterating all `(r, c)` for `dr=1, dc=1`: `current_overlap = 3`.
`max_overlap = max(0, 3) = 3`.

This process continues for all other `(dr, dc)` pairs. Since 3 is the maximum possible overlap for this example, `max_overlap` will remain 3.

Final Result: `max_overlap = 3`.

## Complexity
*   **Time Complexity**: `O(N^4)`
    *   There are `(2N-1)` possible values for `dr` and `(2N-1)` possible values for `dc`. This gives `O((2N-1)^2)` or `O(N^2)` pairs of `(dr, dc)` translations.
    *   For each translation, we iterate through all `N x N` cells of `img1` to calculate the overlap. This is `O(N^2)`.
    *   Total time complexity: `O(N^2 * N^2) = O(N^4)`.
    *   Given `N <= 30`, `30^4 = 810,000` operations, which is well within typical time limits.
*   **Space Complexity**: `O(1)`
    *   We only use a few variables to store `n`, `max_overlap`, `current_overlap`, and loop indices. This is constant auxiliary space, not dependent on `N`.

## Edge Cases
*   **`n = 1`**: The smallest possible matrix. The `dr` and `dc` ranges will be `[0, 0]`, meaning only one translation (`dr=0, dc=0`) is checked.
    *   `img1 = [[1]], img2 = [[1]]`: `dr=0, dc=0`. `img1[0][0]==1` and `img2[0][0]==1`. Overlap = 1. Correct.
    *   `img1 = [[0]], img2 = [[0]]`: `dr=0, dc=0`. No `1`s. Overlap = 0. Correct.
*   **All zeros**: If both `img1` and `img2` contain only zeros, `max_overlap` will correctly remain `0`.
*   **All ones**: If both `img1` and `img2` contain only ones, the maximum overlap will be `n*n` (achieved when `dr=0, dc=0`).
*   **No overlap possible**: If `img1` and `img2` have `1`s in positions that can never align (e.g., `img1` has a `1` only at `(0,0)` and `img2` only at `(n-1, n-1)` and `n` is large enough that they can't meet), the `max_overlap` will correctly be `0`.

## Solution

```python
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        max_overlap = 0

        # Iterate through all possible row offsets (dr) for img1 relative to img2.
        # dr ranges from -(n-1) to (n-1).
        # Example: if n=3, dr ranges from -2 to 2.
        for dr in range(-(n - 1), n):
            # Iterate through all possible column offsets (dc) for img1 relative to img2.
            # dc ranges from -(n-1) to (n-1).
            for dc in range(-(n - 1), n):
                current_overlap = 0
                
                # Calculate the overlap for the current (dr, dc) translation.
                # We iterate through img1's coordinates (r, c).
                for r in range(n):
                    for c in range(n):
                        # If img1[r][c] is a '1', it's a potential candidate for overlap.
                        if img1[r][c] == 1:
                            # Calculate the corresponding coordinates in img2.
                            # If img1 is shifted by (dr, dc), then img1[r][c] aligns with img2[r+dr][c+dc].
                            r_img2 = r + dr
                            c_img2 = c + dc

                            # Check if these corresponding img2 coordinates are within its bounds.
                            # '1' bits translated outside the matrix borders are erased.
                            if 0 <= r_img2 < n and 0 <= c_img2 < n:
                                # If img2 also has a '1' at this position, we have an overlap.
                                if img2[r_img2][c_img2] == 1:
                                    current_overlap += 1
                
                # After checking all cells for the current (dr, dc) translation,
                # update the maximum overlap found so far.
                max_overlap = max(max_overlap, current_overlap)
        
        return max_overlap

```

## Why This Works
This solution works because it systematically explores **every single possible relative positioning** of `img1` with respect to `img2` that could result in any overlap. Any translation can be uniquely defined by a `(dr, dc)` shift of `img1`'s top-left corner relative to `img2`'s top-left corner. By iterating `dr` and `dc` through all values from `-(n-1)` to `(n-1)`, we cover all scenarios where at least one cell from `img1` could potentially overlap with a cell in `img2`. For each such relative position, we correctly calculate the number of overlapping `1`s by checking corresponding cells and respecting boundary conditions. Since we check all possibilities and accurately count overlaps, the maximum value found is guaranteed to be the largest possible overlap.

---
<sub>Generated 2026-09-13 05:17 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
