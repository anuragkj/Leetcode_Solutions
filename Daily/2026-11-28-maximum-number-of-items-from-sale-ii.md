# [3947] Maximum Number of Items From Sale II

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-11-28 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/)

**Topics:** Array, Greedy, Sorting, Heap (Priority Queue)

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a 2D integer array items, where items[i] = [factor_i, price_i] represents the i^th item. You are also given an integer budget.

There are unlimited copies of each item available for purchase. You may buy any number of copies of any items such that the total cost of the purchased copies is at most budget.

After buying items, you may receive free copies according to the following rules:

- Each purchased copy of item i can give you at most one free copy of another item j.

- The free item must satisfy i != j and factor_i divides factor_j.

- For each ordered pair (i, j), you can receive a free copy of item j from purchases of item i at most once, regardless of how many copies of item i you buy.

- The same item j can be received multiple times for free if it is received from purchases of different item types.

Return the maximum total number of item copies you can obtain, including both purchased copies and free copies, while spending at most budget on purchased items.

Example 1:

Input: items = [[1,6],[2,4],[3,5]], budget = 19

Output: 5

Explanation:

- You can buy 2 copies of item 0 and 1 copy of item 1 for a total cost of 2 * 6 + 4 = 16, which is not greater than budget = 19.

- One purchased copy of item 0 gives 1 free copy of item 1, because factor_0 = 1 divides factor_1 = 2.

- The other purchased copy of item 0 gives 1 free copy of item 2, because factor_0 = 1 divides factor_2 = 3.

- You leave with 3 purchased copies and 2 free copies, for a total of 5 item copies.

Example 2:

Input: items = [[2,8],[1,10],[6,6],[4,12],[5,20],[5,17]], budget = 35

Output: 7

Explanation:

- You can buy 2 copies of item 0, 1 copy of item 1, and 1 copy of item 2 for a total cost of 2 * 8 + 10 + 6 = 32, which is not greater than budget = 35.

- One purchased copy of item 0 gives 1 free copy of item 2, because factor_0 = 2 divides factor_2 = 6.

- The other purchased copy of item 0 gives 1 free copy of item 3, because factor_0 = 2 divides factor_3 = 4.

- The purchased copy of item 1 gives 1 free copy of item 2, because factor_1 = 1 divides factor_2 = 6.

- Buying item 2 gives no free copy, because factor_2 = 6 does not divide the factor of any other item.

- You leave with 4 purchased copies and 3 free copies, for a total of 7 item copies.

Constraints:

- 1 <= items.length <= 10^5

- items[i] = [factor_i, price_i]

- 1 <= factor_i <= items.length

- 1 <= price_i <= 10^9

- 1 <= budget <= 10^9

**Examples / sample tests:**

```
[[1,6],[2,4],[3,5]]
19
[[2,8],[1,10],[6,6],[4,12],[5,20],[5,17]]
35
```

---

## Problem Summary
You're given items with a `factor` and `price`. You can buy unlimited copies within a `budget`. Each purchased copy of item `i` can give one free copy of item `j` if `factor_i` divides `factor_j` and `i != j`. This free copy for an `(i, j)` pair can only be obtained once, regardless of how many `i` copies you buy. The goal is to maximize the total number of items (purchased + free).

## Intuition
The core idea is to identify the "value" of each purchase. When you buy an item, you get one purchased copy. Additionally, if this is one of the first few copies of item `i` you buy, it might also unlock a free copy of another item `j`.

Let's define `gain[i]` for each item `i` as the maximum number of *distinct types* of free items `j` you can get by purchasing item `i`. The problem states that "For each ordered pair (i, j), you can receive a free copy of item j from purchases of item i at most once". This means if `factor_i` divides `factor_j`, buying *any* copies of `i` gives you *one* free `j`. If `factor_i` also divides `factor_k`, buying `i` also gives *one* free `k`. So, `gain[i]` is the count of distinct item types `j` (where `j != i`) such that `factor_i` divides `factor_j`.

If you buy `c` copies of item `i`:
- You get `c` purchased copies.
- You get `min(c, gain[i])` free copies. This is because each purchased copy can trigger at most one free item, and you can only trigger `gain[i]` distinct free item types from item `i`.
- Total items obtained: `c + min(c, gain[i])`.

This means the first `gain[i]` copies of item `i` are "boosted": each costs `price_i` but gives 2 items (1 purchased + 1 free). Any subsequent copies (beyond `gain[i]`) are "regular": each costs `price_i` and gives 1 item (1 purchased + 0 free).

To maximize total items within a budget, we should always prioritize purchases that give us the most items per unit of cost. This is a classic **greedy strategy**: always pick the option with the lowest "effective cost per item".
- For a boosted copy: `price_i` cost for 2 items => effective cost `price_i / 2`.
- For a regular copy: `price_i` cost for 1 item => effective cost `price_i / 1`.

Since `price_i / 2` is always less than `price_i / 1` (for `price_i > 0`), boosted copies are always more cost-effective than regular copies of the same item. Our strategy will be to collect all these "purchase opportunities" (boosted and regular), sort them by their effective cost per item, and buy them greedily until the budget runs out.

## Approach
1.  **Precompute `gain[i]` for each item `i`**:
    *   First, determine the `max_factor_val` present in `items` to size auxiliary arrays.
    *   Create a boolean array `factor_presence` where `factor_presence[f]` is `True` if there's at least one item with `factor = f`.
    *   Create an integer array `factor_item_counts` where `factor_item_counts[f]` stores how many items have `factor = f`.
    *   Compute `factor_multiples_count[f]`: for each `f`, count how many distinct multiples `m` (where `m <= max_factor_val`) exist such that `factor_presence[m]` is `True`. This can be done efficiently by iterating `f` from 1 to `max_factor_val`, and for each `f`, iterating its multiples `f, 2f, 3f, ...` up to `max_factor_val`. This step takes `O(max_factor_val log max_factor_val)` time.
    *   For each item `i` with `factor_i = items[i][0]`:
        *   Initialize `gain[i] = factor_multiples_count[factor_i]`.
        *   **Crucial Adjustment for `i != j`**: `factor_multiples_count[factor_i]` includes `factor_i` itself. If item `i` is the *only* item with `factor_i` (i.e., `factor_item_counts[factor_i] == 1`), then you cannot get a free copy of an item *of type `factor_i`* from item `i` because there's no *other* item `j` with `factor_j = factor_i`. In this specific case, subtract 1 from `gain[i]`.
        *   Ensure `gain[i]` is non-negative: `gain[i] = max(0, gain[i])`.

2.  **Create a list of all "purchase opportunities"**:
    *   For each item `i` (with `price_i = items[i][1]` and computed `gain_i`):
        *   If `gain_i > 0`: Add a "boosted" opportunity: `(price_i, 2, gain_i)`. This means `gain_i` copies are available, each costing `price_i` and yielding 2 items.
        *   Add a "regular" opportunity: `(price_i, 1, float('inf'))`. This means unlimited copies are available, each costing `price_i` and yielding 1 item.
    *   Each opportunity is represented as `(cost, items_gained, quantity_available)`.

3.  **Sort opportunities**:
    *   Sort the `all_options` list based on their **effective cost per item**: `cost / items_gained`. This ensures we prioritize the most efficient purchases.

4.  **Greedy Purchase**:
    *   Initialize `total_items = 0` and `remaining_budget = budget`.
    *   Iterate through the `all_options` list (which is now sorted by effective cost per item):
        *   If `remaining_budget` is 0, break the loop.
        *   For the current opportunity `(cost, items_gained, quantity_available)`:
            *   Calculate `num_to_buy = min(quantity_available, remaining_budget // cost)`. This is how many units of this opportunity we can afford and are available.
            *   Add `num_to_buy * items_gained` to `total_items`.
            *   Subtract `num_to_buy * cost` from `remaining_budget`.
    *   Return `total_items`.

## Visualization

Let's illustrate the `all_options` list and the greedy purchase process.

**Initial State (after `gain` calculation):**
`items = [[1,6],[2,4],[3,5]]`, `budget = 19`
`gain = [2, 0, 0]` (for items 0, 1, 2 respectively)

**`all_options` before sorting:**
```
Item 0: price=6, gain=2
  -> (cost=6, items_gained=2, quantity_available=2)  // Boosted
  -> (cost=6, items_gained=1, quantity_available=inf) // Regular
Item 1: price=4, gain=0
  -> (cost=4, items_gained=1, quantity_available=inf) // Regular
Item 2: price=5, gain=0
  -> (cost=5, items_gained=1, quantity_available=inf) // Regular
```

**`all_options` sorted by `cost / items_gained`:**
```
Effective Cost | (Cost, Items Gained, Quantity Available) | Description
---------------|------------------------------------------|-------------------------
3              | (6, 2, 2)                                | Item 0 Boosted
4              | (4, 1, inf)                              | Item 1 Regular
5              | (5, 1, inf)                              | Item 2 Regular
6              | (6, 1, inf)                              | Item 0 Regular
```

**Greedy Purchase Process:**
```
Budget: 19, Total Items: 0

1. Process (6, 2, 2) [Item 0 Boosted]:
   - Can buy: min(2, 19 // 6) = min(2, 3) = 2 units
   - Cost: 2 * 6 = 12
   - Items: 2 * 2 = 4
   - Budget: 19 - 12 = 7
   - Total Items: 0 + 4 = 4

2. Process (4, 1, inf) [Item 1 Regular]:
   - Can buy: min(inf, 7 // 4) = min(inf, 1) = 1 unit
   - Cost: 1 * 4 = 4
   - Items: 1 * 1 = 1
   - Budget: 7 - 4 = 3
   - Total Items: 4 + 1 = 5

3. Process (5, 1, inf) [Item 2 Regular]:
   - Can buy: min(inf, 3 // 5) = min(inf, 0) = 0 units
   - Budget: 3 (no change)
   - Total Items: 5 (no change)

4. Process (6, 1, inf) [Item 0 Regular]:
   - Can buy: min(inf, 3 // 6) = min(inf, 0) = 0 units
   - Budget: 3 (no change)
   - Total Items: 5 (no change)

Final Total Items: 5
```

## Dry Run

Let's walk through **Example 1**: `items = [[1,6],[2,4],[3,5]]`, `budget = 19`.

**1. Precompute `gain`:**
*   `N = 3`. `max_factor_val = 3`.
*   `factor_presence = [False, True, True, True]` (factors 1, 2, 3 are present)
*   `factor_item_counts = [0, 1, 1, 1]` (one item for each factor 1, 2, 3)
*   `factor_multiples_count`:
    *   `f=1`: Multiples 1, 2, 3 are present. `factor_multiples_count[1] = 3`.
    *   `f=2`: Multiple 2 is present. `factor_multiples_count[2] = 1`.
    *   `f=3`: Multiple 3 is present. `factor_multiples_count[3] = 1`.
*   Calculate `gain` for each item:
    *   **Item 0 `[1,6]`**: `factor_0 = 1`. `gain[0] = factor_multiples_count[1] = 3`. Since `factor_item_counts[1] == 1`, we subtract 1. `gain[0] = 3 - 1 = 2`.
    *   **Item 1 `[2,4]`**: `factor_1 = 2`. `gain[1] = factor_multiples_count[2] = 1`. Since `factor_item_counts[2] == 1`, we subtract 1. `gain[1] = 1 - 1 = 0`.
    *   **Item 2 `[3,5]`**: `factor_2 = 3`. `gain[2] = factor_multiples_count[3] = 1`. Since `factor_item_counts[3] == 1`, we subtract 1. `gain[2] = 1 - 1 = 0`.
*   Resulting `gain = [2, 0, 0]`.

**2. Create `all_options`:**
*   **Item 0 (`price=6`, `gain=2`):**
    *   Boosted: `(6, 2, 2)`
    *   Regular: `(6, 1, inf)`
*   **Item 1 (`price=4`, `gain=0`):**
    *   Regular: `(4, 1, inf)` (no boosted option as `gain=0`)
*   **Item 2 (`price=5`, `gain=0`):**
    *   Regular: `(5, 1, inf)` (no boosted option as `gain=0`)
*   `all_options = [(6, 2, 2), (6, 1, inf), (4, 1, inf), (5, 1, inf)]`

**3. Sort `all_options` by `cost / items_gained`:**
*   `(6, 2, 2)`: `6/2 = 3`
*   `(4, 1, inf)`: `4/1 = 4`
*   `(5, 1, inf)`: `5/1 = 5`
*   `(6, 1, inf)`: `6/1 = 6`
*   Sorted `all_options = [(6, 2, 2), (4, 1, inf), (5, 1, inf), (6, 1, inf)]`

**4. Greedy Purchase:**
| Option (cost, items, qty) | `remaining_budget` | `total_items` | `num_to_buy` | Cost Spent | Items Gained |
| :------------------------ | :----------------: | :-----------: | :----------: | :---------: | :-----------: |
| Initial                   |         19         |       0       |      -       |      -      |       -       |
| `(6, 2, 2)`               |         19         |       0       | `min(2, 19//6=3)` = 2 | `2*6=12`    | `2*2=4`       |
| After `(6, 2, 2)`         |         7          |       4       |      -       |      -      |       -       |
| `(4, 1, inf)`             |         7          |       4       | `min(inf, 7//4=1)` = 1 | `1*4=4`     | `1*1=1`       |
| After `(4, 1, inf)`       |         3          |       5       |      -       |      -      |       -       |
| `(5, 1, inf)`             |         3          |       5       | `min(inf, 3//5=0)` = 0 | `0*5=0`     | `0*1=0`       |
| After `(5, 1, inf)`       |         3          |       5       |      -       |      -      |       -       |
| `(6, 1, inf)`             |         3          |       5       | `min(inf, 3//6=0)` = 0 | `0*6=0`     | `0*1=0`       |
| Final                     |         3          |       5       |      -       |      -      |       -       |

**Final Result:** `total_items = 5`. This matches the example output.

## Complexity

*   **Time Complexity**: `O(N log N + max_factor_val log max_factor_val)`.
    *   Precomputing `gain` involves iterating factors and their multiples, which is `O(max_factor_val log max_factor_val)`.
    *   Creating `all_options` is `O(N)`.
    *   Sorting `all_options` (which has `2N` entries) is `O(N log N)`.
    *   The greedy purchase loop is `O(N)`.
    *   Since `max_factor_val <= N` (from constraints), the overall time complexity simplifies to `O(N log N)`.
*   **Space Complexity**: `O(N + max_factor_val)`.
    *   `factor_presence`, `factor_item_counts`, `factor_multiples_count` arrays take `O(max_factor_val)` space.
    *   `gain` array takes `O(N)` space.
    *   `all_options` list takes `O(N)` space.
    *   Overall, this simplifies to `O(N)`.

## Edge Cases

*   **`budget = 0`**: The `remaining_budget // cost` calculation will correctly yield 0, resulting in `total_items = 0`.
*   **`items.length = 1`**: E.g., `items = [[5, 100]]`, `budget = 100`.
    *   `max_factor_val = 5`. `factor_presence[5]=True`, `factor_item_counts[5]=1`.
    *   `factor_multiples_count[5]=1`.
    *   `gain[0]` for item `[5,100]` will be `1 - 1 = 0` (because `factor_item_counts[5] == 1`).
    *   Only a regular option `(100, 1, inf)` is added. `num_to_buy = 100 // 100 = 1`. `total_items = 1`. Correct.
*   **All items have the same factor**: E.g., `items = [[1,10],[1,5],[1,20]]`, `budget = 100`.
    *   `factor_item_counts[1] = 3`.
    *   For each item `i` with `factor_i = 1`, `gain[i] = factor_multiples_count[1] = 1`. No subtraction because `factor_item_counts[1] > 1`.
    *   Each item gets `gain=1`. `all_options` will correctly include `(10,2,1)`, `(5,2,1)`, `(20,2,1)` (boosted) and `(10,1,inf)`, `(5,1,inf)`, `(20,1,inf)` (regular). Sorting by effective cost will correctly prioritize the cheapest boosted items, then cheapest regular items.
*   **Large `price_i` or `budget`**: `price_i` and `budget` can be up to `10^9`.
    *   `num_to_buy * cost` can be `10^9 * 10^9 = 10^18`, which fits in Python's arbitrary-precision integers.
    *   `total_items` can be `2 * 10^9`, also fits in Python's integers.
    *   Floating point division for `cost / items_gained` is generally safe for sorting keys; precision issues are unlikely to affect the relative order for distinct values, and for ties, any order is fine.

## Solution

```python
import collections
import math
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        N = len(items)
        
        # Step 1: Precompute gain[i] for each item i
        # gain[i] = number of distinct item types j (j != i) such that factor_i divides factor_j
        
        # Find the maximum factor value to size arrays.
        # Constraint: 1 <= factor_i <= items.length, so max_factor_val <= N.
        max_factor_val = 0
        for factor, _ in items:
            max_factor_val = max(max_factor_val, factor)
        
        # factor_presence[f] is True if there's at least one item with factor f
        factor_presence = [False] * (max_factor_val + 1)
        # factor_item_counts[f] is the number of items that have factor f
        factor_item_counts = [0] * (max_factor_val + 1)
        
        for factor, _ in items:
            factor_presence[factor] = True
            factor_item_counts[factor] += 1
        
        # factor_multiples_count[f] = count of distinct factors 'm' such that 'm' is a multiple of 'f'
        # AND there is an item with factor 'm'.
        factor_multiples_count = [0] * (max_factor_val + 1)
        for f in range(1, max_factor_val + 1):
            # Iterate through multiples of f
            for multiple in range(f, max_factor_val + 1, f):
                if factor_presence[multiple]:
                    factor_multiples_count[f] += 1
        
        gain = [0] * N
        for i in range(N):
            factor_i = items[i][0]
            # Initial gain is the count of distinct factor types that are multiples of factor_i
            gain[i] = factor_multiples_count[factor_i]
            
            # Adjustment for i != j rule:
            # If factor_i itself is a multiple (which it always is), and item i is the ONLY item
            # with factor_i, then we cannot get a free copy of an item of type factor_i from item i.
            # In this specific case, we must subtract 1 from the gain.
            if factor_item_counts[factor_i] == 1:
                gain[i] -= 1
            
            # Gain cannot be negative
            gain[i] = max(0, gain[i])
        
        # Step 2 & 3: Create and sort all "purchase opportunities"
        # Each opportunity is (cost, items_gained, quantity_available)
        # items_gained can be 2 (for boosted copies) or 1 (for regular copies)
        # quantity_available is gain[i] for boosted, or infinity for regular
        
        all_options = []
        for i in range(N):
            price_i = items[i][1]
            gain_i = gain[i]
            
            # Boosted copies: up to gain_i copies, each gives 2 items for price_i
            if gain_i > 0:
                all_options.append((price_i, 2, gain_i))
            
            # Regular copies: unlimited copies, each gives 1 item for price_i
            all_options.append((price_i, 1, float('inf')))
        
        # Sort opportunities by effective cost per item (cost / items_gained)
        # This ensures we always pick the most cost-effective purchases first.
        all_options.sort(key=lambda x: x[0] / x[1])
        
        # Step 4: Greedy Purchase
        total_items = 0
        remaining_budget = budget
        
        for cost, items_gained, quantity_available in all_options:
            if remaining_budget == 0:
                break
            
            # Calculate how many units of this opportunity we can buy
            # Limited by quantity_available and remaining_budget
            # Use integer division for remaining_budget // cost
            num_to_buy = min(quantity_available, remaining_budget // cost)
            
            total_items += num_to_buy * items_gained
            remaining_budget -= num_to_buy * cost
            
        return total_items

```

## Why This Works

This solution works because it applies a **greedy strategy** based on the principle of maximizing value per unit of cost. By transforming the problem into a set of "purchase opportunities" – where each opportunity represents buying a unit of an item (either a "boosted" unit yielding 2 items or a "regular" unit yielding 1 item) at a certain cost – we can then sort these opportunities by their effective cost per item (`cost / items_gained`). Iterating through this sorted list and purchasing as many units as possible from the cheapest opportunities first guarantees that we are always making the most efficient use of our budget. This is analogous to the fractional knapsack problem, where taking items with the highest value-to-weight ratio is optimal. The `gain[i]` precomputation correctly identifies how many "boosted" opportunities each item provides, ensuring the `i != j` rule and distinct free item types are respected.

---
<sub>Generated 2026-11-28 08:23 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
