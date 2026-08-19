# [1386] Cinema Seat Allocation

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-08-19 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/cinema-seat-allocation/)

**Topics:** Array, Hash Table, Greedy, Bit Manipulation

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

A cinema has n rows of seats, numbered from 1 to n. Each row has 10 seats, numbered from 1 to 10.

You are given a 2D integer array reservedSeats, where reservedSeats[i] = [row_i, seat_i] means that seat seat_i in row row_i is already reserved.

A four-person group must be assigned to four seats in the same row. The group can be seated in one of the following seat blocks:

- seats 2, 3, 4, 5

- seats 4, 5, 6, 7

- seats 6, 7, 8, 9

A block can be used only if none of its seats are reserved. Each seat can be assigned to at most one group.

Return an integer denoting the maximum number of four-person groups that can be assigned.

Example 1:

Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.

Example 2:

Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2

Example 3:

Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4

Constraints:

- 1 <= n <= 10^9

- 1 <= reservedSeats.length <= min(10 * n, 10^4)

- reservedSeats[i] == [row_i, seat_i]

- 1 <= row_i <= n

- 1 <= seat_i <= 10

- All reservedSeats[i] are distinct.

**Examples / sample tests:**

```
3
[[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
2
[[2,1],[1,8],[2,6]]
4
[[4,3],[1,4],[4,6],[1,7]]
```

---

## Problem Summary
The goal is to find the maximum number of four-person groups that can be seated in a cinema with `n` rows and 10 seats per row. We are given a list of already reserved seats. A group must occupy four contiguous seats in one of three specific blocks: seats 2-5, 4-7, or 6-9.

## Intuition
The key observation is that `n` (the number of rows) can be extremely large (up to 10^9), while the number of `reservedSeats` is relatively small (up to 10^4). This means most rows will have no reserved seats at all.

1.  **Rows without reservations**: For any row that has *no* reserved seats, we can always place two four-person groups. For example, one group in seats 2,3,4,5 and another in seats 6,7,8,9. These two blocks are completely separate.
2.  **Rows with reservations**: We only need to carefully analyze rows that actually have reserved seats. For these rows, we need to determine the maximum number of groups (0, 1, or 2) that can be seated.
3.  **Maximum groups per row**: A single row has 10 seats. The three possible blocks are:
    *   **Left**: seats 2, 3, 4, 5
    *   **Middle**: seats 4, 5, 6, 7
    *   **Right**: seats 6, 7, 8, 9
    Notice that the Middle block overlaps with both Left (seats 4,5) and Right (seats 6,7). This means we can never place three groups. We can place at most two groups (Left and Right, as they are disjoint). If we can't place both Left and Right, we try to place one group.

This leads to a **greedy strategy**:
*   First, count all rows that have *no* reservations. Each contributes 2 groups.
*   Then, for each row that *does* have reservations:
    *   Check if both the **Left (2-5)** and **Right (6-9)** blocks are entirely free. If so, we can place **two** groups. This is the optimal configuration for two groups as they are disjoint.
    *   Otherwise (if we can't place two groups), check if *any* of the three blocks (Left, Middle, or Right) is entirely free. If so, we can place **one** group.
    *   If none of the blocks are free, we place zero groups in that row.

## Approach
1.  **Store Reserved Seats Efficiently**: Since we'll be checking seat availability for specific rows, it's best to organize the `reservedSeats` by row. Use a **hash map (dictionary)** where keys are `row_id`s and values are **sets** of `seat_id`s reserved in that row. This allows for `O(1)` average-time lookup to check if a seat is reserved.
    *   Initialize `row_reservations = defaultdict(set)`.
    *   Iterate through `reservedSeats`: for each `[r, s]`, add `s` to `row_reservations[r]`.

2.  **Initialize Total Groups**: Calculate the groups from rows with *no* reservations.
    *   `total_groups = (n - len(row_reservations)) * 2`.
    *   `len(row_reservations)` gives the count of unique rows that have at least one reserved seat. `n - len(row_reservations)` is the count of rows with no reservations. Each of these can accommodate 2 groups.

3.  **Process Rows with Reservations**: Iterate through each `row_id` present in `row_reservations`. For each such row:
    *   Get the `reserved` set for the current `row_id`.
    *   **Check Left Block (seats 2,3,4,5)**: Iterate `s` from 2 to 5. If any `s` is in `reserved`, `left_block_free = False`.
    *   **Check Right Block (seats 6,7,8,9)**: Iterate `s` from 6 to 9. If any `s` is in `reserved`, `right_block_free = False`.
    *   **Check Middle Block (seats 4,5,6,7)**: Iterate `s` from 4 to 7. If any `s` is in `reserved`, `middle_block_free = False`.
    *   **Apply Decision Logic**:
        *   If `left_block_free` is `True` AND `right_block_free` is `True`: Add `2` to `total_groups`.
        *   Else if `left_block_free` is `True` OR `right_block_free` is `True` OR `middle_block_free` is `True`: Add `1` to `total_groups`.
        *   Else (no block is free): Add `0` (do nothing).

4.  **Return Result**: After processing all rows with reservations, `total_groups` will hold the maximum number of four-person groups.

## Visualization

A single row of 10 seats, showing the three possible blocks:

```
Seats: 1  2  3  4  5  6  7  8  9 10
       |---------------------------|
          [Left Block]
             [Middle Block]
                [Right Block]
```

Example: Row with some reserved seats (X) and possible group placements (G):

```
Seats: 1  2  3  4  5  6  7  8  9 10
       |---------------------------|
Row 1: X  X  .  .  .  .  .  X  .  .   (Reserved: 1,2,8)
          ^ ^ ^ ^
          Left Block (blocked by 2)
             ^ ^ ^ ^
             Middle Block (free) -> G G G G
                ^ ^ ^ ^
                Right Block (blocked by 8)

Result for Row 1: 1 group (Middle)
```

Example: Row with reservations allowing two groups:

```
Seats: 1  2  3  4  5  6  7  8  9 10
       |---------------------------|
Row 3: X  .  .  .  .  .  .  .  .  X   (Reserved: 1,10)
          ^ ^ ^ ^
          Left Block (free) -> G G G G
             ^ ^ ^ ^
             Middle Block (free)
                ^ ^ ^ ^
                Right Block (free) -> G G G G

Result for Row 3: 2 groups (Left and Right)
```

## Dry Run
Let's trace Example 1: `n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]`

1.  **Initialize**: `total_groups = 0`
    `row_reservations = defaultdict(set)`

2.  **Populate `row_reservations`**:
    *   `[1,2]` -> `row_reservations[1].add(2)`
    *   `[1,3]` -> `row_reservations[1].add(3)`
    *   `[1,8]` -> `row_reservations[1].add(8)`
    *   `[2,6]` -> `row_reservations[2].add(6)`
    *   `[3,1]` -> `row_reservations[3].add(1)`
    *   `[3,10]` -> `row_reservations[3].add(10)`

    Final `row_reservations`:
    *   `1: {2, 3, 8}`
    *   `2: {6}`
    *   `3: {1, 10}`

3.  **Initial `total_groups` calculation**:
    *   `len(row_reservations)` is 3 (rows 1, 2, 3).
    *   `total_groups = (n - len(row_reservations)) * 2 = (3 - 3) * 2 = 0`.
    *   (This is correct because all 3 rows have reservations in this example.)

4.  **Process Rows with Reservations**:

    | Row | Reserved Seats | Left (2-5) Free? | Right (6-9) Free? | Middle (4-7) Free? | Groups Added | `total_groups` |
    | :-- | :------------- | :--------------- | :---------------- | :----------------- | :----------- | :------------- |
    | **1** | `{2, 3, 8}`    | No (2,3 reserved)| No (8 reserved)   | Yes (4,5,6,7 free) | 1            | 1              |
    |     |                | _(2,3 in {2,3,8})_ | _(8 in {2,3,8})_  | _(none in {2,3,8})_ |              |                |
    | **2** | `{6}`          | Yes (2,3,4,5 free)| No (6 reserved)   | No (6 reserved)    | 1            | 2              |
    |     |                | _(none in {6})_   | _(6 in {6})_      | _(6 in {6})_       |              |                |
    | **3** | `{1, 10}`      | Yes (2,3,4,5 free)| Yes (6,7,8,9 free)| Yes (4,5,6,7 free) | 2            | 4              |
    |     |                | _(none in {1,10})_ | _(none in {1,10})_ | _(none in {1,10})_ |              |                |

5.  **Final Result**: `total_groups = 4`. This matches Example 1 output.

## Complexity
*   **Time Complexity**: `O(R)`, where `R` is `len(reservedSeats)`.
    *   Populating `row_reservations` takes `O(R)` time, as each insertion into a hash set is `O(1)` on average.
    *   Iterating through `row_reservations` takes `O(U)` time, where `U` is the number of unique rows with reservations (`U <= R`).
    *   Inside the loop, checking the three blocks involves at most `4 + 4 + 4 = 12` seat lookups. Each lookup in a hash set is `O(1)` on average.
    *   Therefore, the total time is `O(R + U * 12)`, which simplifies to `O(R)`.
*   **Space Complexity**: `O(R)`.
    *   The `row_reservations` dictionary stores at most `U` entries. Each entry's value is a set of reserved seats for that row, which can contain at most 10 seats.
    *   Thus, the total space is `O(U * 10)`, which simplifies to `O(U)`. Since `U <= R`, the space complexity is `O(R)`.

## Edge Cases
*   **`n` is very large, `reservedSeats` is small**: Handled by the initial calculation `(n - len(row_reservations)) * 2`, which efficiently accounts for all empty rows without iterating them.
*   **`reservedSeats` is empty**: `len(row_reservations)` will be 0. `total_groups` will be `n * 2`, which is correct as all `n` rows can accommodate two groups.
*   **All seats in a row are reserved**: The checks for `left_block_free`, `right_block_free`, `middle_block_free` will all be `False`. `0` groups will be added for that row, which is correct.
*   **Only seats 1 or 10 are reserved**: These seats are outside all three blocks (2-5, 4-7, 6-9). So, `left_block_free` and `right_block_free` will both be `True`, and `2` groups will be added, which is correct.
*   **Reservations block only the middle section of a block**: E.g., `[1,4]` reserves seat 4. This blocks Left (2-5) and Middle (4-7), but Right (6-9) remains free. The logic correctly identifies `right_block_free` as `True` and adds `1` group.

## Solution

```python
from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Use a dictionary to store reserved seats for each row.
        # Keys are row_ids, values are sets of seat_ids.
        # Using a set allows for O(1) average-time lookup for seat availability.
        row_reservations = defaultdict(set)
        for r, s in reservedSeats:
            row_reservations[r].add(s)

        # Initialize total_groups.
        # First, account for rows that have NO reserved seats.
        # There are (n - len(row_reservations)) such rows.
        # Each of these rows can accommodate 2 groups (e.g., seats 2-5 and 6-9).
        total_groups = (n - len(row_reservations)) * 2

        # Now, iterate through the rows that DO have reserved seats.
        # For each such row, determine how many groups can be placed (0, 1, or 2).
        for row_id in row_reservations:
            reserved = row_reservations[row_id]

            # Flags to check if the three possible 4-seat blocks are free.
            left_block_free = True   # Seats 2, 3, 4, 5
            middle_block_free = True # Seats 4, 5, 6, 7
            right_block_free = True  # Seats 6, 7, 8, 9

            # Check left block (seats 2-5)
            for s in range(2, 6): # Python range is exclusive at the end
                if s in reserved:
                    left_block_free = False
                    break
            
            # Check right block (seats 6-9)
            for s in range(6, 10):
                if s in reserved:
                    right_block_free = False
                    break
            
            # Check middle block (seats 4-7)
            for s in range(4, 8):
                if s in reserved:
                    middle_block_free = False
                    break

            # Decision Logic:
            # Prioritize placing two groups if possible (left and right blocks are disjoint).
            if left_block_free and right_block_free:
                total_groups += 2
            # If two groups are not possible, try to place one group.
            # One group can be placed if any of the three blocks (left, right, or middle) is free.
            elif left_block_free or right_block_free or middle_block_free:
                total_groups += 1
            # Else (if none of the above conditions are met), 0 groups can be placed in this row.

        return total_groups

```

## Why This Works
This solution works because it correctly leverages the problem constraints and the nature of the seat blocks. By first accounting for the vast majority of rows that are completely empty (each contributing 2 groups), it efficiently handles the large `n` constraint. For the relatively few rows with reservations, the greedy decision logic is optimal:
1.  Prioritizing `left_block_free` AND `right_block_free` ensures we capture the maximum possible (2) groups, as these two blocks are disjoint and don't interfere with each other.
2.  If two groups aren't possible, checking `left_block_free` OR `right_block_free` OR `middle_block_free` correctly identifies if at least one group can be placed. The `middle_block` is crucial here because it can sometimes be free even if both the `left_block` and `right_block` are individually blocked (e.g., if seats 2,3 are reserved and seats 8,9 are reserved, but 4,5,6,7 are free). This ensures we don't miss any single-group opportunities.
This comprehensive check guarantees that for every row, we find the maximum number of groups that can be seated.

---
<sub>Generated 2026-08-19 02:04 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
