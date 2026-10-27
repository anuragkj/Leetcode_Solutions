# [3963] Create Grid With Exactly One Path

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-10-27 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/create-grid-with-exactly-one-path/)

**Topics:** —

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given two integers m and n, representing the number of rows and columns of a grid.

Construct any m x n grid consisting only of the characters '.' and '#', where:

- '.' represents a free cell.

- '#' represents an obstacle cell.

A valid path is a sequence of free cells that:

- Starts at the top-left cell (0, 0).

- Ends at the bottom-right cell (m - 1, n - 1).

- Moves only:

- Right, from (i, j) to (i, j + 1), or

- Down, from (i, j) to (i + 1, j).

Return any grid such that there is exactly one valid path from the top-left cell to the bottom-right cell.

Example 1:

Input: m = 2, n = 3

Output: ["..#","#.."]

Explanation:

The only valid path is: (0,0) → (0,1) → (1,1) → (1,2)

Example 2:

Input: m = 3, n = 3

Output: ["..#","#..","##."]

Explanation:

The only valid path is: (0,0) → (0,1) → (1,1) → (1,2) → (2,2)

Example 3:

Input: m = 1, n = 4

Output: ["...."]

Explanation:

The only valid path is: (0,0) → (0,1) → (0,2) → (0,3)

Constraints:

- 1 <= m, n <= 25

**Examples / sample tests:**

```
2
3
3
3
1
4
```

---

**Problem Summary**
Construct an `m x n` grid using `.` (free) and `#` (obstacle) cells such that there is exactly one valid path from the top-left (0,0) to the bottom-right (m-1, n-1), moving only right or down.

**Intuition**
The key insight is that we only need to find *one* simple path and make sure it's the *only* possible path. If we define a specific route and make all its cells free ('.'), then fill **all other cells** with obstacles ('#'), any attempt to deviate from our chosen path will be blocked. This guarantees uniqueness.

**Approach**
1.  **Initialize the grid:** Create an `m x n` grid, initially filling every cell with an obstacle character (`'#'`). This is our baseline: no paths exist yet.
2.  **Define the unique path:** We'll use a straightforward path: first, go all the way **right** across the top row, then go all the way **down** along the last column.
    *   This path covers all cells `(0, j)` for `0 <= j < n` (the entire first row).
    *   It then continues with cells `(i, n-1)` for `1 <= i < m` (the last column, starting from the second row, as `(0, n-1)` is already part of the first row segment).
3.  **Mark path cells as free:** Iterate through the cells identified in step 2 and change their character in the grid from `'#'` to `'.'`.
    *   For `j` from `0` to `n-1`, set `grid[0][j] = '.'`.
    *   For `i` from `1` to `m-1`, set `grid[i][n-1] = '.'`.
4.  **Format output:** Convert the 2D list of characters into a `list[str]`, where each inner list of characters is joined into a single string.

**Visualization**
Let's illustrate with `m = 3, n = 4` using the "right then down" path.

**1. Initial Grid (all '#')**
```
####
####
####
```

**2. Mark First Row as Free ('.')**
(Cells `(0,0), (0,1), (0,2), (0,3)` become `'.'`)
```
....
####
####
```

**3. Mark Last Column (from row 1) as Free ('.')**
(Cells `(1,3), (2,3)` become `'.'`. Note `(0,3)` is already `'.'`)
```
....
###.
###.
```

**Final Grid:**
The unique path is `(0,0) → (0,1) → (0,2) → (0,3) → (1,3) → (2,3)`.
Any deviation from this path (e.g., trying to move down from `(0,1)` to `(1,1)`) would lead to an obstacle (`#`).

**Dry Run**
Example 1: `m = 2, n = 3`

| Step | Action

---
<sub>Generated 2026-10-27 05:29 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
