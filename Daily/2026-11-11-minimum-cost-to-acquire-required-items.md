# [3789] Minimum Cost to Acquire Required Items

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-11-11 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-cost-to-acquire-required-items/)

**Topics:** Math, Greedy

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given five integers cost1, cost2, costBoth, need1, and need2.

There are three types of items available:

- An item of type 1 costs cost1 and contributes 1 unit to the type 1 requirement only.

- An item of type 2 costs cost2 and contributes 1 unit to the type 2 requirement only.

- An item of type 3 costs costBoth and contributes 1 unit to both type 1 and type 2 requirements.

You must collect enough items so that the total contribution toward type 1 is at least need1 and the total contribution toward type 2 is at least need2.

Return an integer representing the minimum possible total cost to achieve these requirements.

Example 1:

Input: cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2

Output: 3

Explanation:

After buying three type 3 items, which cost 3 * 1 = 3, the total contribution to type 1 is 3 (>= need1 = 3) and to type 2 is 3 (>= need2 = 2).
Any other valid combination would cost more, so the minimum total cost is 3.

Example 2:

Input: cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3

Output: 22

Explanation:

We buy need1 = 2 items of type 1 and need2 = 3 items of type 2: 2 * 5 + 3 * 4 = 10 + 12 = 22.

Any other valid combination would cost more, so the minimum total cost is 22.

Example 3:

Input: cost1 = 5, cost2 = 4, costBoth = 15, need1 = 0, need2 = 0

Output: 0

Explanation:

Since no items are required (need1 = need2 = 0), we buy nothing and pay 0.

Constraints:

- 1 <= cost1, cost2, costBoth <= 10^6

- 0 <= need1, need2 <= 10^9

**Examples / sample tests:**

```
3
2
1
3
2
5
4
15
2
3
5
4
15
0
0
```

---

## Problem Summary
You need to acquire a minimum quantity of two item types, `need1` and `need2`. There are three ways to buy items: Type 1 (costs `cost1`, gives 1 unit of Type 1), Type 2 (costs `cost2`, gives 1 unit of Type 2), and Type 3 (costs `costBoth`, gives 1 unit of **both** Type 1 and Type 2). The goal is to find the minimum total cost to meet both requirements.

## Intuition
This problem can be solved using a **greedy approach**. The key is to figure out the most cost-effective way to satisfy requirements at each stage. Since Type 3 items contribute to both requirements, they are special. We need to compare their cost-effectiveness against buying individual Type 1 and Type 2 items.

Consider these scenarios:
1.  **Getting one unit of Type 1 and one unit of Type 2 simultaneously:** You can either buy one Type 3 item (cost `costBoth`) or buy one Type 1 item and one Type 2 item (total cost `cost1 + cost2`). The cheaper option is `min(costBoth, cost1 + cost2)`.
2.  **Getting one unit of Type 1 only (when Type 2 is not needed):** You can buy a Type 1 item (cost `cost1`) or a Type 3 item (cost `costBoth`). If you buy a Type 3 item, its Type 2 contribution is "wasted" in terms of fulfilling *new* requirements, but it still provides the Type 1 unit. So, the cheaper option is `min(cost1, costBoth)`.
3.  **Getting one unit of Type 2 only (when Type 1 is not needed):** Similar to above, the cheaper option is `min(cost2, costBoth)`.

This suggests a strategy: first satisfy the requirements that overlap (where both types are needed), then satisfy any remaining individual requirements.

## Approach
The optimal algorithm involves three main steps, prioritizing the most efficient purchase for the current needs:

1.  **Initialize `total_cost` to 0.**
2.  **Satisfy the shared requirements:**
    *   Calculate the number of items where **both** Type 1 and Type 2 are needed: `shared_needs = min(need1, need2)`.
    *   Determine the **effective cost per pair** (one Type 1, one Type 2): `effective_cost_both_pair = min(costBoth, cost1 + cost2)`. This is the cheapest way to get one unit of both types.
    *   Add `shared_needs * effective_cost_both_pair` to `total_cost`.
    *   Reduce `need1` by `shared_needs`.
    *   Reduce `need2` by `shared_needs`.
3.  **Satisfy any remaining Type 1 requirements:**
    *   If `need1` is still greater than 0:
        *   Determine the **effective cost per Type 1 unit** (when only Type 1 is needed): `effective_cost_1_only = min(cost1, costBoth)`. This is the cheapest way to get one Type 1 unit, even if a Type 3 item also provides a Type 2 unit that's no longer needed.
        *   Add `need1 * effective_cost_1_only` to `total_cost`.
4.  **Satisfy any remaining Type 2 requirements:**
    *   If `need2` is still greater than 0:
        *   Determine the **effective cost per Type 2 unit** (when only Type 2 is needed): `effective_cost_2_only = min(cost2, costBoth)`.
        *   Add `need2 * effective_cost_2_only` to `total_cost`.
5.  **Return `total_cost`.**

## Visualization

```mermaid
graph TD
    A[Start: need1, need2] --> B{Calculate shared_needs = min(need1, need2)};
    B --> C{Effective cost for 1 of each:
             cost_pair = min(costBoth, cost1 + cost2)};
    C --> D[total_cost += shared_needs * cost_pair];
    D --> E[need1 -= shared_needs, need2 -= shared_needs];
    E --> F{Is need1 > 0?};
    F -- Yes --> G{Effective cost for 1 of Type 1:
                   cost_1 = min(cost1, costBoth)};
    G --> H[total_cost += need1 * cost_1];
    H --> I{Is need2 > 0?};
    F -- No --> I;
    I -- Yes --> J{Effective cost for 1 of Type 2:
                   cost_2 = min(cost2, costBoth)};
    J --> K[total_cost += need2 * cost_2];
    K --> L[Return total_cost];
    I -- No --> L;
```

## Dry Run
Let's trace Example 1: `cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2`

| Step | Variable | Value | Explanation |
| :--- | :------- | :---- | :---------- |
| 1    | `total_cost` | `0` | Initialize total cost. |
| 2.1  | `shared_needs` | `min(3, 2) = 2` | We need 2 units of both types. |
| 2.2  | `effective_cost_both_pair` | `min(costBoth, cost1 + cost2) = min(1, 3 + 2) = min(1, 5) = 1` | Buying a Type 3 item is cheaper than one Type 1 + one Type 2. |
| 2.3  | `total_cost` | `0 + 2 * 1 = 2` | Cost for 2 shared units. |
| 2.4  | `need1` | `3 - 2 = 1` | Remaining Type 1 need. |
| 2.5  | `need2` | `2 - 2 = 0` | Remaining Type 2 need. |
| 3    | `need1 > 0` | `1 > 0` (True) | We still need Type 1 items. |
| 3.1  | `effective_cost_1_only` | `min(cost1, costBoth) = min(3, 1) = 1` | Buying a Type 3 item is cheaper than a Type 1 item. |
| 3.2  | `total_cost` | `2 + 1 * 1 = 3` | Cost for the remaining 1 Type 1 unit. |
| 4    | `need2 > 0` | `0 > 0` (False) | No remaining Type 2 needs. |
| 5    | `total_cost` | `3` | Final result. |

The minimum total cost is `3`.

## Complexity
*   **Time Complexity:** **O(1)**. The solution involves a fixed number of arithmetic operations and comparisons, regardless of the input values (which can be large, but don't affect the number of operations).
*   **Space Complexity:** **O(1)**. Only a few variables are used to store costs and needs, consuming constant memory.

## Edge Cases
*   **`need1 = 0, need2 = 0`**: The `shared_needs` will be 0, and both `need1` and `need2` will remain 0 after the first step. The `total_cost` will correctly be 0.
*   **One requirement is 0 (e.g., `need1 = 5, need2 = 0`)**: `shared_needs` will be 0. The algorithm will then only process the remaining `need1` (step 3) and skip `need2` (step 4), correctly calculating the cost for only Type 1 items.
*   **`costBoth` is very high**: In this case, `min(costBoth, cost1 + cost2)` will likely choose `cost1 + cost2`. Similarly, `min(cost1, costBoth)` will choose `cost1`, and `min(cost2, costBoth)` will choose `cost2`. This correctly defaults to buying individual items.
*   **`costBoth` is very low**: `min(costBoth, cost1 + cost2)` will likely choose `costBoth`. `min(cost1, costBoth)` will choose `costBoth`, and `min(cost2, costBoth)` will choose `costBoth`. This correctly defaults to using Type 3 items even if only one type is strictly needed.
*   **Large `need1`, `need2` values (up to 10^9)**: Python's arbitrary-precision integers handle large numbers automatically, so `need * cost` calculations (which can reach `10^9 * 10^6 = 10^15`) will not overflow.

## Solution

```python
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        total_cost = 0

        # Handle the base case where no items are needed
        if need1 == 0 and need2 == 0:
            return 0

        # Step 1: Satisfy the shared requirements
        # Determine how many units of both types are needed
        shared_needs = min(need1, need2)

        # Calculate the most cost-effective way to get one unit of both Type 1 and Type 2.
        # Option A: Buy one Type 3 item (costBoth)
        # Option B: Buy one Type 1 item and one Type 2 item (cost1 + cost2)
        effective_cost_both_pair = min(costBoth, cost1 + cost2)
        
        # Add the cost for satisfying the shared requirements
        total_cost += shared_needs * effective_cost_both_pair
        
        # Reduce the remaining requirements
        need1 -= shared_needs
        need2 -= shared_needs

        # Step 2: Satisfy any remaining Type 1 requirements
        if need1 > 0:
            # Calculate the most cost-effective way to get one unit of Type 1 only.
            # Option A: Buy one Type 1 item (cost1)
            # Option B: Buy one Type 3 item (costBoth) - its Type 2 contribution is "extra" but still provides Type 1
            effective_cost_1_only = min(cost1, costBoth)
            total_cost += need1 * effective_cost_1_only
        
        # Step 3: Satisfy any remaining Type 2 requirements
        if need2 > 0:
            # Calculate the most cost-effective way to get one unit of Type 2 only.
            # Option A: Buy one Type 2 item (cost2)
            # Option B: Buy one Type 3 item (costBoth) - its Type 1 contribution is "extra"
            effective_cost_2_only = min(cost2, costBoth)
            total_cost += need2 * effective_cost_2_only
            
        return total_cost

```

## Why This Works
This greedy approach is optimal because decisions made at each step are locally optimal and do not negatively impact the optimality of future steps. By first addressing the **shared requirements** using the cheapest way to acquire both types (`min(costBoth, cost1 + cost2)`), we ensure that the most efficient option for fulfilling overlapping needs is always chosen. After this, any **remaining requirements** are for a single item type. For these, we again choose the cheapest way to acquire that specific type (`min(cost1, costBoth)` for Type 1, `min(cost2, costBoth)` for Type 2), even if it means using a Type 3 item and "wasting" its contribution to the other type. Since the cost functions are linear (cost per item is constant), and the requirements are independent after the shared portion is handled, this sequential optimal choice leads to a globally optimal minimum total cost.

---
<sub>Generated 2026-11-11 06:59 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
