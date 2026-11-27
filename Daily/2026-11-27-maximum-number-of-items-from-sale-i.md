# [3946] Maximum Number of Items From Sale I

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-11-27 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximum-number-of-items-from-sale-i/)

**Topics:** Array, Dynamic Programming, Greedy

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 2D integer array items, where items[i] = [factor_i, price_i] represents the i^th item. You are also given an integer budget.

There are unlimited copies of each item available for purchase.You may buy any number of copies of any items such that the total cost of the purchased copies is at most budget.

After buying items, you may receive free copies according to the following rules:

- For each item i that you bought at least one copy of, you receive one free copy of every item j such that j != i and factor_i divides factor_j.

- Buying multiple copies of the same item i does not give additional free copies through item i.

- The same item j can be received multiple times for free if it is received from purchases of different item types.

Return the maximum total number of item copies you can obtain, including both purchased copies and free copies, while spending at most budget on purchased items.

Example 1:

Input: items = [[6,2],[2,6],[3,4]], budget = 9

Output: 4

Explanation:

- You can buy 2 copies of item 0 and 1 copy of item 2 for a total cost of 2 * 2 + 4 = 8, which is not greater than budget = 9.

- Buying item 2 gives 1 free copy of item 0, because factor_2 = 3 divides factor_0 = 6.

- You leave with 3 purchased copies and 1 free copy, for a total of 4 item copies.

Example 2:

Input: items = [[2,4],[3,2],[4,1],[6,4],[12,4]], budget = 8

Output: 10

Explanation:

- You can buy 1 copy of item 0, 1 copy of item 1, and 2 copies of item 2 for a total cost of 4 + 2 + 2 * 1 = 8.

- Buying item 0 gives 1 free copy of items 2, 3, and 4.

- Buying item 1 gives 1 free copy of items 3 and 4.

- Buying item 2 gives 1 free copy of item 4.

- Thus, you receive 6 free copies. You leave with 4 purchased copies and 6 free copies, for a total of 10 item copies.

Constraints:

- 1 <= items.length <= 1000

- items[i] = [factor_i, price_i]

- 1 <= factor_i, price_i <= 1500

- 1 <= budget <= 1500

**Examples / sample tests:**

```
[[6,2],[2,6],[3,4]]
9
[[2,4],[3,2],[4,1],[6,4],[12,4]]
8
```

---

## Problem Summary
You're given a list of items, each with a `factor` and a `price`. You have a `budget` and can buy unlimited copies of any item. The twist is that buying the *first* copy of an item `i` gives you free copies of other items `j` if `factor_i` divides `factor_j` (and `j` is not `i`). Subsequent copies of item `i` only add one purchased item. The goal is to maximize the total number of items (purchased + free) within your budget.

## Intuition
The core observation that cracks this problem is that buying the **first copy of an item is special**. It's like an "activation" that grants bonus free items. Any copies of that item bought *after* the first one are just regular purchases, adding only one item for its price. This structure suggests a dynamic programming approach, similar to the knapsack problem, where each item has two "modes" of purchase:
1.  **Activation Mode**: Buy the first copy. This costs `price_i` and gives `1` purchased item plus `free_count[i]` free items.
2.  **Bulk Mode**: Buy additional copies. Each costs `price_i` and gives `1` purchased item. This mode is only available *after* the item has been activated.

## Approach
We'll use a dynamic programming (DP) approach. Let `dp[b]` be the maximum number of items we can obtain with a budget of `b`.

1.  **Precompute `free_count` for each item:**
    *   For each item `i`, calculate `free_count[i]`: the number of distinct item types `j` (where `j != i`) such that `items[i][0]` (factor of item `i`) divides `items[j][0]` (factor of item `j`).
    *   This takes `O(N^2)` time, where `N` is the number of item types.

2.  **Initialize DP array:**
    *   Create a `dp` array of size `budget + 1`, initialized with zeros. `dp[b]` will store the maximum items for budget `b`.

3.  **Iterate through each item to update the DP array:**
    *   For each item `i` (with `price_i` and `factor_i`):
        *   Calculate `value_first_purchase = 1 + free_count[i]`. This is the total items gained when buying the first copy of item `i`.
        *   `value_additional_purchase = 1`. This is the total items gained when buying any subsequent copy of item `i`.
        *   Create a temporary `new_dp` array, which is a copy of the current `dp` array. This `new_dp` will accumulate the results for considering item `i`.
        *   **First Pass (0/1 Knapsack for the "first purchase"):**
            *   Iterate `b` (current budget) **downwards** from `budget` to `price_i`.
            *   `new_dp[b] = max(new_dp[b], dp[b - price_i] + value_first_purchase)`
            *   This step considers buying the *first* copy of item `i`. By iterating `b` downwards, `dp[b - price_i]` refers to the maximum items achievable with `b - price_i` budget *without* having considered item `i` yet. This ensures we treat the first purchase as a 0/1 choice (either buy it or don't).
        *   **Second Pass (Unbounded Knapsack for "additional purchases"):**
            *   Iterate `b` (current budget) **upwards** from `price_i` to `budget`.
            *   `new_dp[b] = max(new_dp[b], new_dp[b - price_i] + value_additional_purchase)`
            *   This step considers buying *additional* copies of item `i`. By iterating `b` upwards, `new_dp[b - price_i]` now refers to the maximum items achievable with `b - price_i` budget *potentially including* the first copy (or even multiple copies) of item `i`. This correctly models the unbounded nature of additional purchases. The `max` operation ensures we only take this path if it's better than not buying additional copies.
        *   After both passes for item `i`, update `dp = new_dp`.

4.  **Result:**
    *   The final answer is `dp[budget]`.

## Visualization

Let's illustrate the DP table update for a single item `i` with `price_i = P`, `value_first_purchase = V1`, and `value_additional_purchase = V2`.

```mermaid
graph TD
    A[Initial dp array] --> B{For each item i:};

    B --> C[Copy dp to new_dp];

    C --> D{First Pass: 0/1 Knapsack for First Purchase};
    D --> E{Iterate budget 'b' from BUDGET down to P};
    E --> F[new_dp[b] = max(new_dp[b], dp[b - P] + V1)];
    F --> E;
    E -- Loop ends --> G[new_dp now includes item i's first purchase option];

    G --> H{Second Pass: Unbounded Knapsack for Additional Purchases};
    H --> I{Iterate budget 'b' from P up to BUDGET};
    I --> J[new_dp[b] = max(new_dp[b], new_dp[b - P] + V2)];
    J --> I;
    I -- Loop ends --> K[new_dp now includes item i's additional purchase options];

    K --> L[Update dp = new_dp];
    L --> B;
    B -- All items processed --> M[Return dp[BUDGET]];

```

**Example DP Table State (Simplified for one item, `price=2`, `V1=1`, `V2=1`, `budget=9`):**

| Budget `b` | `dp` (before Item 0) | `new_dp` (after 0/1 pass for Item 0) | `new_dp` (after Unbounded pass for Item 0) |
| :--------- | :------------------- | :----------------------------------- | :----------------------------------------- |
| 0          | 0                    | 0                                    | 0                                          |
| 1          | 0                    | 0                                    | 0                                          |
| 2          | 0                    | `max(0, dp[0]+1)` = 1                | `max(1, new_dp[0]+1)` = 1                  |
| 3          | 0                    | `max(0, dp[1]+1)` = 1                | `max(1, new_dp[1]+1)` = 1                  |
| 4          | 0                    | `max(0, dp[2]+1)` = 1                | `max(1, new_dp[2]+1)` = `max(1, 1+1)` = 2  |
| 5          | 0                    | `max(0, dp[3]+1)` = 1                | `max(1, new_dp[3]+1)` = `max(1, 1+1)` = 2  |
| 6          | 0                    | `max(0, dp[4]+1)` = 1                | `max(1, new_dp[4]+1)` = `max(1, 2+1)` = 3  |
| 7          | 0                    | `max(0, dp[5]+1)` = 1                | `max(1, new_dp[5]+1)` = `max(1, 2+1)` = 3  |
| 8          | 0                    | `max(0, dp[6]+1)` = 1                | `max(1, new_dp[6]+1)` = `max(1, 3+1)` = 4  |
| 9          | 0                    | `max(0, dp[7]+1)` = 1                | `max(1, new_dp[7]+1)` = `max(1, 3+1)` = 4  |

## Dry Run
**Example 1:** `items = [[6,2],[2,6],[3,4]]`, `budget = 9`

**1. Precompute `free_count`:**
*   `items[0] = [6,2]` (factor 6)
*   `items[1] = [2,6]` (factor 2)
*   `items[2] = [3,4]` (factor 3)

| Item `i` | `factor_i` | `j=0` (factor 6) | `j=1` (factor 2) | `j=2` (factor 3) | `free_count[i]` |
| :------- | :--------- | :--------------- | :--------------- | :--------------- | :-------------- |
| 0        | 6          | -                | `2%6!=0`         | `3%6!=0`         | 0               |
| 1        | 2          | `6%2==0` (Yes)   | -                | `3%2!=0`         | 1               |
| 2        | 3          | `6%3==0` (Yes)   | `2%3!=0`         | -                | 1               |
**`free_count = [0, 1, 1]`**

**2. Initialize `dp` array:**
`dp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]` (for budgets 0 to 9)

**3. DP Loop:**

**Item 0: `[6,2]` (price=2, `free_count[0]=0`)**
*   `value_first_purchase = 1 + 0 = 1`
*   `value_additional_purchase = 1`
*   `price_i = 2`

| Budget `b` | `dp` (before item 0) | `new_dp` (after 0/1 pass) | `new_dp` (after Unbounded pass) |
| :--------- | :------------------- | :------------------------ | :------------------------------ |
| 0          | 0                    | 0                         | 0                               |
| 1          | 0                    | 0                         | 0                               |
| 2          | 0                    | `max(0, dp[0]+1)` = 1     | `max(1, new_dp[0]+1)` = 1       |
| 3          | 0                    | `max(0, dp[1]+1)` = 1     | `max(1, new_dp[1]+1)` = 1       |
| 4          | 0                    | `max(0, dp[2]+1)` = 1     | `max(1, new_dp[2]+1)` = 2       |
| 5          | 0                    | `max(0, dp[3]+1)` = 1     | `max(1, new_dp[3]+1)` = 2       |
| 6          | 0                    | `max(0, dp[4]+1)` = 1     | `max(1, new_dp[4]+1)` = 3       |
| 7          | 0                    | `max(0, dp[5]+1)` = 1     | `max(1, new_dp[5]+1)` = 3       |
| 8          | 0                    | `max(0, dp[6]+1)` = 1     | `max(1, new_dp[6]+1)` = 4       |
| 9          | 0                    | `max(0, dp[7]+1)` = 1     | `max(1, new_dp[7]+1)` = 4       |
**`dp` becomes `[0,0,1,1,2,2,3,3,4,4]`**

**Item 1: `[2,6]` (price=6, `free_count[1]=1`)**
*   `value_first_purchase = 1 + 1 = 2`
*   `value_additional_purchase = 1`
*   `price_i = 6`

| Budget `b` | `dp` (before item 1) | `new_dp` (after 0/1 pass) | `new_dp` (after Unbounded pass) |
| :--------- | :------------------- | :------------------------ | :------------------------------ |
| 0-5        | (same as `dp`)       | (same as `dp`)            | (same as `dp`)                  |
| 6          | 3                    | `max(3, dp[0]+2)` = 3     | `max(3, new_dp[0]+1)` = 3       |
| 7          | 3                    | `max(3, dp[1]+2)` = 3     | `max(3, new_dp[1]+1)` = 3       |
| 8          | 4                    | `max(4, dp[2]+2)` = 4     | `max(4, new_dp[2]+1)` = 4       |
| 9          | 4                    | `max(4, dp[3]+2)` = 4     | `max(4, new_dp[3]+1)` = 4       |
**`dp` remains `[0,0,1,1,2,2,3,3,4,4]`**

**Item 2: `[3,4]` (price=4, `free_count[2]=1`)**
*   `value_first_purchase = 1 + 1 = 2`
*   `value_additional_purchase = 1`
*   `price_i = 4`

| Budget `b` | `dp` (before item 2) | `new_dp` (after 0/1 pass) | `new_dp` (after Unbounded pass) |
| :--------- | :------------------- | :------------------------ | :------------------------------ |
| 0-3        | (same as `dp`)       | (same as `dp`)            | (same as `dp`)                  |
| 4          | 2                    | `max(2, dp[0]+2)` = 2     | `max(2, new_dp[0]+1)` = 2       |
| 5          | 2                    | `max(2, dp[1]+2)` = 2     | `max(2, new_dp[1]+1)` = 2       |
| 6          | 3                    | `max(3, dp[2]+2)` = 3     | `max(3, new_dp[2]+1)` = 3       |
| 7          | 3                    | `max(3, dp[3]+2)` = 3     | `max(3, new_dp[3]+1)` = 3       |
| 8          | 4                    | `max(4, dp[4]+2)` = 4     | `max(4, new_dp[4]+1)` = 4       |
| 9          | 4                    | `max(4, dp[5]+2)` = 4     | `max(4, new_dp[5]+1)` = 4       |
**`dp` remains `[0,0,1,1,2,2,3,3,4,4]`**

**Final Result:** `dp[9] = 4`. This matches Example 1.

## Complexity
*   **Time Complexity:** `O(N^2 + N * Budget)`
    *   Precomputing `free_count`: `N` items, each iterating through `N` other items. `O(N^2)`.
    *   DP calculation: `N` items. For each item, two loops iterating up to `Budget`. `O(N * Budget)`.
    *   Given `N <= 1000` and `Budget <= 1500`, this is `1000^2 + 1000 * 1500 = 1,000,000 + 1,500,000 = 2.5 * 10^6` operations, which is efficient enough.
*   **Space Complexity:** `O(N + Budget)`
    *   `free_count` array: `O(N)`.
    *   `dp` array: `O(Budget)`.
    *   `new_dp` array: `O(Budget)`.

## Edge Cases
*   **`budget = 0`**: The `dp` array will be `[0]`. The loops for `b` won't execute. `dp[0]` will correctly return `0`.
*   **`items.length = 1`**: The `free_count` for the single item will be `0` (due to `i == j` check). The DP proceeds normally, treating it as an item with no free bonuses.
*   **All `price_i > budget`**: No items can be purchased. The `dp` array remains all zeros. `dp[budget]` will correctly return `0`.
*   **All `factor_i` are the same**: `free_count` for each item will be `N-1`. The logic handles this correctly.
*   **All `price_i` are the same**: No special handling needed, the DP naturally accounts for this.

## Solution

```python
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Step 1: Precompute free_count for each item
        # free_count[i] stores the number of free items received if item i is purchased at least once.
        # This is the count of items j (where j != i) such that factor_i divides factor_j.
        free_count = [0] * n
        for i in range(n):
            factor_i = items[i][0]
            for j in range(n):
                if i == j:
                    continue # An item does not give itself for free
                factor_j = items[j][0]
                if factor_j % factor_i == 0:
                    free_count[i] += 1

        # Step 2: Initialize DP array
        # dp[b] will store the maximum number of items (purchased + free)
        # that can be obtained with a budget of 'b'.
        dp = [0] * (budget + 1)

        # Step 3: Iterate through each item and update the DP array
        for i in range(n):
            price_i = items[i][1]
            
            # The value gained from buying the first copy of item i:
            # 1 (for the purchased copy itself) + free_count[i] (for free copies)
            value_first_purchase = 1 + free_count[i]
            
            # The value gained from buying additional copies of item i:
            # 1 (for the purchased copy itself)
            value_additional_purchase = 1

            # Create a temporary DP array to store updates for the current item.
            # This is crucial for correctly applying the 0/1 knapsack logic for the first purchase.
            # new_dp[b] will represent the max items considering items up to (i-1) AND item i.
            new_dp = list(dp)

            # First pass: Consider buying the FIRST copy of item i (0/1 Knapsack style)
            # Iterate budget 'b' downwards to ensure dp[b - price_i] refers to
            # a state where item i has NOT been considered yet for the current item's processing.
            for b in range(budget, price_i - 1, -1):
                # If we buy the first copy of item i, we spend price_i and gain value_first_purchase.
                # The remaining budget (b - price_i) must have been used to buy previous items.
                new_dp[b] = max(new_dp[b], dp[b - price_i] + value_first_purchase)
            
            # Second pass: Consider buying ADDITIONAL copies of item i (Unbounded Knapsack style)
            # Iterate budget 'b' upwards. This allows new_dp[b - price_i] to refer to
            # a state where item i *might have already been purchased* (either first or additional copies).
            for b in range(price_i, budget + 1):
                # If we buy an additional copy of item i, we spend price_i and gain value_additional_purchase.
                # This is only valid if item i was already "activated" (bought at least once).
                # The max operation handles this: if new_dp[b - price_i] already includes item i's first purchase,
                # then

---
<sub>Generated 2026-11-27 08:59 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
