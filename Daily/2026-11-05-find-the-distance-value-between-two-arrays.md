# [1385] Find the Distance Value Between Two Arrays

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-11-05 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/)

**Topics:** Array, Two Pointers, Binary Search, Sorting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation:
For arr1[0]=4 we have:
|4-10|=6 > d=2
|4-9|=5 > d=2
|4-1|=3 > d=2
|4-8|=4 > d=2
For arr1[1]=5 we have:
|5-10|=5 > d=2
|5-9|=4 > d=2
|5-1|=4 > d=2
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2

Example 2:

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2

Example 3:

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1

Constraints:

- 1 <= arr1.length, arr2.length <= 500

- -1000 <= arr1[i], arr2[j] <= 1000

- 0 <= d <= 100

**Examples / sample tests:**

```
[4,5,8]
[10,9,1,8]
2
[1,4,2,3]
[-4,-3,6,10,20,30]
3
[2,1,100,3]
[-5,-2,10,-3,7]
6
```

---

## Problem Summary
We are given two integer arrays, `arr1` and `arr2`, and an integer `d`. The goal is to find the "distance value" between these arrays. This value is defined as the count of elements `arr1[i]` for which there is *no* element `arr2[j]` satisfying the condition `|arr1[i] - arr2[j]| <= d`.

## Intuition
The problem asks us to count elements in `arr1` that are "far enough" from *all* elements in `arr2`. The condition `|arr1[i] - arr2[j]| <= d` can be rewritten as `arr1[i] - d <= arr2[j] <= arr1[i] + d`. This means for a given `arr1[i]`, we are looking for any `arr2[j]` that falls within the range `[arr1[i] - d, arr1[i] + d]`.

If we find *any* `arr2[j]` in this range, then `arr1[i]` does *not* contribute to the distance value. If, after checking all `arr2[j]`, we find *no* element in this range, then `arr1[i]` *does* contribute.

To efficiently check if any `arr2[j]` falls into a specific range `[lower_bound, upper_bound]`, we can **sort `arr2`**. Once `arr2` is sorted, we can use **binary search** to quickly determine if such an element exists for each `arr1[i]`.

## Approach
The optimal algorithm leverages sorting and binary search:

1.  Initialize a counter `distance_value` to 0. This will store our final result.
2.  **Sort `arr2`** in ascending order. This is the crucial step that enables efficient searching.
3.  Iterate through each `num1` in `arr1`:
    a.  Assume `num1` *will* contribute to the `distance_value` (set a flag, e.g., `is_valid = True`).
    b.  Calculate the **lower bound** (`lb = num1 - d`) and **upper bound** (`ub = num1 + d`) for the "forbidden" range. If any `arr2[j]` falls within `[lb, ub]`, then `num1` is not valid.
    c.  Use **binary search** on the sorted `arr2` to find if any element `num2` satisfies `lb <= num2 <= ub`.
        i.  Specifically, use `bisect_left(arr2, lb)` (from Python's `bisect` module) to find the index `idx` where `lb` could be inserted while maintaining sorted order. `idx` will point to the first element in `arr2` that is greater than or equal to `lb`.
        ii. Check two conditions:
            1.  Is `idx` a valid index in `arr2`? (`idx < len(arr2)`)
            2.  Is the element at `arr2[idx]` less than or equal to `ub`? (`arr2[idx] <= ub`)
        iii. If both conditions are true, it means we found an element `arr2[idx]` such that `lb <= arr2[idx] <= ub`. This implies `|num1 - arr2[idx]| <= d`, so `num1` does *not* contribute to the distance value. Set `is_valid = False`.
    d.  If `is_valid` is still `True` after this check (meaning no `arr2[j]` was found in the forbidden range), increment `distance_value`.
4.  After checking all elements in `arr1`, return `distance_value`.

## Visualization

Let's visualize the range check for an `arr1[i]` value.

```mermaid
graph TD
    subgraph Number Line
        A[... arr1[i]-d ...] --> B(arr1[i])
        B --> C[... arr1[i]+d ...]
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#fff,stroke:#333,stroke-width:2px

    subgraph arr2 (Sorted)
        D[arr2[0]] --> E[arr2[1]]
        E --> F[...]
        F --> G[arr2[k]]
        G --> H[...]
        H --> I[arr2[m-1]]
    end

    subgraph Check for arr1[i]
        J(Target Range: [arr1[i]-d, arr1[i]+d])
        K{Is there any arr2[j] such that arr1[i]-d <= arr2[j] <= arr1[i]+d ?}
        L[Yes, found arr2[j]]
        M[No, none found]
        N[arr1[i] does NOT contribute]
        O[arr1[i] DOES contribute]
    end

    J --> K
    K -- Yes --> L
    L --> N
    K -- No --> M
    M --> O

    linkStyle 0 stroke-width:2px,fill:none,stroke:red;
    linkStyle 1 stroke-width:2px,fill:none,stroke:red;
    linkStyle 2 stroke-width:2px,fill:none,stroke:red;

    subgraph Example: arr1[i]=5, d=2
        P(Range: [3, 7])
        Q{arr2 = [1, 4, 8, 9, 10]}
        R{Is 1 in [3,7]? No}
        S{Is 4 in [3,7]? Yes!}
        T(5 does NOT contribute)
    end

    P --> Q
    Q --> R
    R --> S
    S --> T
```

In the example, for `arr1[i]=5` and `d=2`, the "forbidden" range is `[3, 7]`. We sort `arr2` to `[1, 4, 8, 9, 10]`.
- We binary search for `3` (lower bound). `bisect_left` would point to `4` (index 1).
- `arr2[1]` is `4`. Is `4 <= 7` (upper bound)? Yes.
- Since we found `4` within the range `[3, 7]`, `arr1[i]=5` does *not* contribute to the distance value.

## Dry Run

Let's walk through **Example 1**:
`arr1 = [4, 5, 8]`, `arr2 = [10, 9, 1, 8]`, `d = 2`

1.  Initialize `distance_value = 0`.
2.  **Sort `arr2`**: `arr2` becomes `[1, 8, 9, 10]`.

| `num1` | `lb` (`num1-d`) | `ub` (`num1+d`) | `bisect_left(arr2, lb)` result (`idx`) | `idx < len(arr2)`? | `arr2[idx] <= ub`? | `is_valid` | `distance_value` | Notes

---
<sub>Generated 2026-11-05 07:16 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
