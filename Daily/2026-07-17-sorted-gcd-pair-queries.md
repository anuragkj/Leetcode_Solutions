# [3312] Sorted GCD Pair Queries

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-07-17 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/sorted-gcd-pair-queries/)

**Topics:** Array, Hash Table, Math, Binary Search, Combinatorics, Counting, Number Theory, Prefix Sum

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums of length n and an integer array queries.

Let gcdPairs denote an array obtained by calculating the GCD of all possible pairs (nums[i], nums[j]), where 0 <= i < j < n, and then sorting these values in ascending order.

For each query queries[i], you need to find the element at index queries[i] in gcdPairs.

Return an integer array answer, where answer[i] is the value at gcdPairs[queries[i]] for each query.

The term gcd(a, b) denotes the greatest common divisor of a and b.

Example 1:

Input: nums = [2,3,4], queries = [0,2,2]

Output: [1,2,2]

Explanation:

gcdPairs = [gcd(nums[0], nums[1]), gcd(nums[0], nums[2]), gcd(nums[1], nums[2])] = [1, 2, 1].

After sorting in ascending order, gcdPairs = [1, 1, 2].

So, the answer is [gcdPairs[queries[0]], gcdPairs[queries[1]], gcdPairs[queries[2]]] = [1, 2, 2].

Example 2:

Input: nums = [4,4,2,1], queries = [5,3,1,0]

Output: [4,2,1,1]

Explanation:

gcdPairs sorted in ascending order is [1, 1, 1, 2, 2, 4].

Example 3:

Input: nums = [2,2], queries = [0,0]

Output: [2,2]

Explanation:

gcdPairs = [2].

Constraints:

- 2 <= n == nums.length <= 10^5

- 1 <= nums[i] <= 5 * 10^4

- 1 <= queries.length <= 10^5

- 0 <= queries[i] < n * (n - 1) / 2

**Examples / sample tests:**

```
[2,3,4]
[0,2,2]
[4,4,2,1]
[5,3,1,0]
[2,2]
[0,0]
```

---

## Problem Summary
You are given an array of numbers `nums` and a list of `queries`. For each possible pair of distinct numbers `(nums[i], nums[j])` from the input array, calculate their greatest common divisor (GCD). Collect all these GCDs into a new array called `gcdPairs`, sort it in ascending order, and then for each `queries[k]`, find and return the element at that 0-indexed position in `gcdPairs`.

## Intuition
Generating all `N*(N-1)/2` pairs and their GCDs explicitly would be too slow for `N=10^5`. The key insight is to **count** how many pairs result in each possible GCD value, rather than listing them all. The maximum possible GCD value is limited by the maximum value in `nums` (which is `5 * 10^4`). This suggests an approach based on iterating through possible GCD values.

We can use a technique called **inclusion-exclusion**. First, for each potential GCD `g`, we count how many pairs have a GCD of *at least* `g`. This is easy: count how many numbers in `nums` are multiples of `g`, say `C_g`. Any two distinct numbers chosen from these `C_g` numbers will have a GCD that is a multiple of `g` (i.e., `g`, `2g`, `3g`, etc.). The number of such pairs is `C_g * (C_g - 1) / 2`. Let's call this `pairs_with_gcd_at_least[g]`.

Then, to find the exact count of pairs with GCD *exactly* `g`, we subtract the counts of pairs whose GCD is `2g`, `3g`, `4g`, and so on, from `pairs_with_gcd_at_least[g]`. By iterating `g` downwards from the maximum possible value, we ensure that the counts for `2g, 3g, ...` are already computed when we need them. Once we have the exact counts for each GCD value, we can use a **prefix sum** array and **binary search** to efficiently answer the queries.

## Approach
The algorithm proceeds in five main steps:

1.  **Frequency Array (`counts`):** Create an array `counts` where `counts[x]` stores how many times the number `x` appears in `nums`. The size of this array will be `MAX_POSSIBLE_VAL + 1`, where `MAX_POSSIBLE_VAL` is `5 * 10^4` (the maximum value of `nums[i]`).
    *   *Example:* For `nums = [2,3,4]`, `counts = [0,0,1,1,1]` (indices 1,2,3,4).

2.  **Count Multiples Array (`num_multiples`):** Create an array `num_multiples` where `num_multiples[k]` stores the total count of numbers in `nums` that are multiples of `k`.
    *   Iterate `k` from 1 to `MAX_POSSIBLE_VAL`.
    *   For each `k`, iterate through its multiples (`k, 2k, 3k, ...`) up to `MAX_POSSIBLE_VAL`. Sum up `counts[multiple_of_k]` to get `num_multiples[k]`.
    *   *Example:* For `nums = [2,3,4]`, `num_multiples[1]=3` (2,3,4 are multiples of 1), `num_multiples[2]=2` (2,4 are multiples of 2), `num_multiples[3]=1` (3 is a multiple of 3), `num_multiples[4]=1` (4 is a multiple of 4).

3.  **Exact GCD Counts (`exact_gcd_counts`):** Create an array `exact_gcd_counts` where `exact_gcd_counts[g]` stores the number of pairs `(nums[i], nums[j])` whose GCD is *exactly* `g`.
    *   Iterate `g` downwards from `MAX_POSSIBLE_VAL` to 1.
    *   For each `g`, calculate `pairs_with_gcd_at_least_g = num_multiples[g] * (num_multiples[g] - 1) // 2`. This is the number of pairs whose GCD is `g` or a multiple of `g`.
    *   Initialize `exact_gcd_counts[g] = pairs_with_gcd_at_least_g`.
    *   Apply **inclusion-exclusion**: Subtract the counts of pairs whose GCD is `2g, 3g, ...` (i.e., multiples of `g` greater than `g`). Since we iterate `g` downwards, `exact_gcd_counts[2g]`, `exact_gcd_counts[3g]`, etc., will already be correctly computed.
    *   *Example:* For `nums = [2,3,4]`, `exact_gcd_counts[1]=2` (pairs (2,3) and (3,4)), `exact_gcd_counts[2]=1` (pair (2,4)).

4.  **Cumulative Counts (`cumulative_counts`):** Create an array `cumulative_counts` where `cumulative_counts[v]` stores the total number of GCD pairs whose value is less than or equal to `v`. This is a prefix sum of `exact_gcd_counts`.
    *   Iterate `g` from 1 to `MAX_POSSIBLE_VAL`.
    *   `cumulative_counts[g] = cumulative_counts[g-1] + exact_gcd_counts[g]`.
    *   *Example:* For `nums = [2,3,4]`, `cumulative_counts = [0, 2, 3, 3, 3]`. `cumulative_counts[1]=2` means 2 pairs have GCD <= 1. `cumulative_counts[2]=3` means 3 pairs have GCD <= 2.

5.  **Answer Queries:** For each `q_idx` in `queries`:
    *   We need to find the `(q_idx + 1)`-th smallest GCD value (because `q_idx` is 0-indexed).
    *   Use **binary search** (`bisect_left` in Python) on `cumulative_counts` to find the smallest `g` such that `cumulative_counts[g]` is greater than or equal to `(q_idx + 1)`. This `g` is our answer.
    *   *Example:* For `queries = [0,2,2]`:
        *   `q_idx=0`: `bisect_left(cumulative_counts, 0+1)` returns `1`. Answer `1`.
        *   `q_idx=2`: `bisect_left(cumulative_counts, 2+1)` returns `2`. Answer `2`.
        *   `q_idx=2`: `bisect_left(cumulative_counts, 2+1)` returns `2`. Answer `2`.

## Visualization
```mermaid
graph TD
    A[Start] --> B{Initialize `MAX_POSSIBLE_VAL` (50000)};
    B --> C[Step 1: Populate `counts` array from `nums`];
    C --> D[Step 2: Populate `num_multiples` array];
    D --> E[Step 3: Populate `exact_gcd_counts` array (iterating `g` downwards, using inclusion-exclusion)];
    E --> F[Step 4: Populate `cumulative_counts` array (prefix sum of `exact_gcd_counts`)];
    F --> G{Step 5: For each `q_idx` in `queries`};
    G --> H[Find `target_count = q_idx + 1`];
    H --> I[Use `bisect_left(cumulative_counts, target_count)` to find `result_gcd`];
    I --> J[Add `result_gcd` to `answer` list];
    J --> G;
    G -- All queries processed --> K[Return `answer`];
    K --> L[End];

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style L fill:#f9f,stroke:#333,stroke-width:2px
    style C fill:#ccf,stroke:#333,stroke-width:1px
    style D fill:#ccf,stroke:#333,stroke-width:1px
    style E fill:#ccf,stroke:#333,stroke-width:1px
    style F fill:#ccf,stroke:#333,stroke-width:1px
    style J fill:#afa,stroke:#333,stroke-width:1px
```

## Dry Run
Let's trace Example 1: `nums = [2,3,4]`, `queries = [0,2,2]`
`MAX_POSSIBLE_VAL` for this example is 4 (in actual code, it's 50000).

1.  **`counts` array (after processing `nums`):**
    `counts = [0, 0, 1, 1, 1]` (index 0 unused, then counts for 1, 2, 3, 4)

2.  **`num_multiples` array (after processing `counts`):**
    *   `num_multiples[1]` (multiples of 1: 2,3,4) = `counts[2]+counts[3]+counts[4] = 1+1+1 = 3`
    *   `num_multiples[2]` (multiples of 2: 2,4) = `counts[2]+counts[4] = 1+1 = 2`
    *   `num_multiples[3]` (multiples of 3: 3) = `counts[3] = 1`
    *   `num_multiples[4]` (multiples of 4: 4) = `counts[4] = 1`
    `num_multiples = [0, 3, 2, 1, 1]`

3.  **`exact_gcd_counts` array (iterating `g` from 4 down to 1):**
    *   `g=4`: `num_multiples[4]=1`. Pairs with GCD at least 4: `1*(1-1)//2 = 0`. `exact_gcd_counts[4] = 0`.
    *   `g=3`: `num_multiples[3]=1`. Pairs with GCD at least 3: `1*(1-1)//2 = 0`. `exact_gcd_counts[3] = 0`.
    *   `g=2`: `num_multiples[2]=2`. Pairs with GCD at least 2: `2*(2-1)//2 = 1`.
        Subtract `exact_gcd_counts[4]` (since 4 is a multiple of 2): `1 - exact_gcd_counts[4] = 1 - 0 = 1`.
        `exact_gcd_counts[2] = 1`.
    *   `g=1`: `num_multiples[1]=3`. Pairs with GCD at least 1: `3*(3-1)//2 = 3`.
        Subtract `exact_gcd_counts[2]`, `exact_gcd_counts[3]`, `exact_gcd_counts[4]`:
        `3 - exact_gcd_counts[2] - exact_gcd_counts[3] - exact_gcd_counts[4] = 3 - 1 - 0 - 0 = 2`.
        `exact_gcd_counts[1] = 2`.
    `exact_gcd_counts = [0, 2, 1, 0, 0]` (index 0 unused, then counts for GCDs 1, 2, 3, 4)
    (This means: 2 pairs have GCD 1 (e.g., (2,3), (3,4)), 1 pair has GCD 2 (e.g., (2,4)). Total 3 pairs.)

4.  **`cumulative_counts` array:**
    *   `cumulative_counts[1] = exact_gcd_counts[1] = 2`
    *   `cumulative_counts[2] = cumulative_counts[1] + exact_gcd_counts[2] = 2 + 1 = 3`
    *   `cumulative_counts[3] = cumulative_counts[2] + exact_gcd_counts[3] = 3 + 0 = 3`
    *   `cumulative_counts[4] = cumulative_counts[3] + exact_gcd_counts[4] = 3 + 0 = 3`
    `cumulative_counts = [0, 2, 3, 3, 3]` (index 0 unused, then cumulative counts up to GCDs 1, 2, 3, 4)

5.  **Answer `queries = [0,2,2]`:**
    *   For `queries[0] = 0`: We need the `(0+1)=1`-st smallest GCD.
        `bisect.bisect_left(cumulative_counts, 1)` returns `1`. `answer = [1]`
    *   For `queries[1] = 2`: We need the `(2+1)=3`-rd smallest GCD.
        `bisect.bisect_left(cumulative_counts, 3)` returns `2`. `answer = [1, 2]`
    *   For `queries[2] = 2`: We need the `(2+1)=3`-rd smallest GCD.
        `bisect.bisect_left(cumulative_counts, 3)` returns `2`. `answer = [1, 2, 2]`

Final `answer = [1, 2, 2]`.

## Complexity
*   **Time Complexity:** `O(N + MAX_POSSIBLE_VAL * log(MAX_POSSIBLE_VAL) + Q * log(MAX_POSSIBLE_VAL))`
    *   Step 1 (Frequency array): `O(N)` to iterate through `nums`.
    *   Step 2 (Count multiples): `O(MAX_POSSIBLE_VAL * log(MAX_POSSIBLE_VAL))` due to the harmonic series sum (e.g., for `k=1`, iterate `MAX_POSSIBLE_VAL` times; for `k=2`, `MAX_POSSIBLE_VAL/2` times, etc.).
    *   Step 3 (Exact GCD counts): `O(MAX_POSSIBLE_VAL * log(MAX_POSSIBLE_VAL))` for the same reason as Step 2.
    *   Step 4 (Cumulative counts): `O(MAX_POSSIBLE_VAL)`.
    *   Step 5 (Answer queries): `O(Q * log(MAX_POSSIBLE_VAL))` because each query involves a binary search on an array of size `MAX_POSSIBLE_VAL`.
    *   Given `N, Q <= 10^5` and `MAX_POSSIBLE_VAL = 5 * 10^4`, this is efficient enough.

*   **Space Complexity:** `O(MAX_POSSIBLE_VAL)`
    *   We use several arrays (`counts`, `num_multiples`, `exact_gcd_counts`, `cumulative_counts`), each of size `MAX_POSSIBLE_VAL + 1`.

## Edge Cases
*   **`n=2` (minimum `n`):** `nums = [2,2]`, `queries = [0,0]`.
    *   The solution correctly handles this. `exact_gcd_counts[2]` will be 1 (for the pair (2,2)), and `exact_gcd_counts[1]` will be 0 after inclusion-exclusion. `cumulative_counts` will be `[0,0,1]`. Queries for index 0 will correctly return 2.
*   **All elements are the same:** `nums = [5,5,5]`, `queries = [0,1,2]`.
    *   `num_multiples[5]` will be 3. `exact_gcd_counts[5]` will be `3*(2)/2 = 3`. All other `exact_gcd_counts[g]` will be 0 (after inclusion-exclusion for `g=1`). `cumulative_counts` will be `[0,0,0,0,0,3]`. All queries for indices 0, 1, 2 will correctly return 5.
*   **`nums` contains 1:** `nums = [1,2,3]`.
    *   This is handled naturally. `num_multiples[1]` will be `N`. `exact_gcd_counts[1]` will be `N*(N-1)/2` minus counts of pairs with GCDs > 1.
*   **`queries[i]` is the maximum possible index:** `queries[i] = n*(n-1)/2 - 1`.
    *   The `cumulative_counts` array will correctly store the total number of pairs at `cumulative_counts[MAX_POSSIBLE_VAL]`. `bisect_left` will find the correct GCD for the last element.

## Solution

```python
import bisect
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        # Maximum possible value for any nums[i] as per constraints.
        # This defines the upper bound for GCDs and array sizes.
        MAX_POSSIBLE_VAL = 50000 

        # Step 1: Frequency array for nums
        # counts[x] stores how many times x appears in nums.
        # This helps in efficiently calculating multiples later.
        counts = [0] * (MAX_POSSIBLE_VAL + 1)
        for x in nums:
            counts[x] += 1

        # Step 2: Count multiples array
        # num_multiples[k] stores how many elements in nums are multiples of k.
        # This is crucial for finding pairs whose GCD is at least k.
        num_multiples = [0] * (MAX_POSSIBLE_VAL + 1)
        # Iterate through all possible GCD values 'k' from 1 up to MAX_POSSIBLE_VAL.
        for k in range(1, MAX_POSSIBLE_VAL + 1):
            # For each 'k', iterate through its multiples (k, 2k, 3k, ...) up to MAX_POSSIBLE_VAL.
            # Sum up the frequencies of these multiples from the 'counts' array.
            for multiple_of_k in range(k, MAX_POSSIBLE_VAL + 1, k):
                num_multiples[k] += counts[multiple_of_k]

        # Step 3: Count pairs with exact GCD using inclusion-exclusion
        # exact_gcd_counts[g] stores the number of pairs (nums[i], nums[j]) with gcd(nums[i], nums[j]) = g.
        exact_gcd_counts = [0] * (MAX_POSSIBLE_VAL + 1)
        # Iterate downwards from MAX_POSSIBLE_VAL to 1.
        # This order is essential for the inclusion-exclusion principle to work correctly,
        # as we subtract counts of larger multiples first.
        for g in range(MAX_POSSIBLE_VAL, 0, -1):
            # Calculate pairs (a, b) where both a and b are multiples of g.
            # The GCD of such pairs is *at least* g.
            num_elements_multiple_of_g = num_multiples[g]
            # Number of ways to choose 2 distinct elements from num_elements_multiple_of_g.
            # This is nC2 = n * (n - 1) / 2.
            pairs_with_gcd_at_least_g = num_elements_multiple_of_g * (num_elements_multiple_of_g - 1) // 2
            
            exact_gcd_counts[g] = pairs_with_gcd_at_least_g

            # Apply inclusion-exclusion: Subtract counts of pairs whose GCD is a multiple of g (e.g., 2g, 3g, ...).
            # Since we iterate 'g' downwards, exact_gcd_counts[multiple_of_g] for multiple_of_g > g
            # would have already been correctly computed.
            for multiple_of_g in range(2 * g, MAX_POSSIBLE_VAL + 1, g):
                exact_gcd_counts[g] -= exact_gcd_counts[multiple_of_g]
        
        # Step 4: Cumulative counts for answering queries
        # cumulative_counts[v] stores the total number of GCD pairs whose value is <= v.
        # This array acts as a sorted list of prefix sums, allowing binary search.
        # cumulative_counts[0] will be 0.
        cumulative_counts = [0] * (MAX_POSSIBLE_VAL + 1)
        total_pairs_so_far = 0
        for g in range(1, MAX_POSSIBLE_VAL + 1):
            total_pairs_so_far += exact_gcd_counts[g]
            cumulative_counts[g] = total_pairs_so_far
        
        # Step 5: Answer queries using binary search
        answer = []
        for q_idx in queries:
            # Each query q_idx asks for the element at 0-indexed position q_idx.
            # This corresponds to the (q_idx + 1)-th smallest GCD value in the sorted gcdPairs array.
            # We need to find the smallest 'g' such that cumulative_counts[g] is at least (q_idx + 1).
            # bisect_left finds the insertion point for (q_idx + 1) in cumulative_counts,
            # which is exactly the smallest 'g' satisfying the condition.
            result_gcd = bisect.bisect_left(cumulative_counts, q_idx + 1)
            answer.append(result_gcd)
            
        return answer

```

## Why This Works
The solution works by cleverly avoiding the explicit generation of all `N^2` GCD pairs. Instead, it leverages number theory principles:
1.  **Efficient Counting of Multiples:** By pre-calculating `num_multiples[k]`, we quickly know how many numbers in `nums` are divisible by `k`.
2.  **Inclusion-Exclusion for Exact GCDs:** The core idea is that if `num_multiples[g]` elements are multiples of `g`, then any pair formed from these elements will have a GCD that is *at least* `g`. By iterating `g` downwards and subtracting the counts of pairs whose GCD is a *strict multiple* of `g` (e.g., `2g, 3g, ...`), we isolate the pairs whose GCD is *exactly* `g`.
3.  **Prefix Sum for Sorted Access:** Once we have `exact_gcd_counts[g]`, we know how many times each `g` appears in the sorted `gcdPairs`. The `cumulative_counts` array then allows us to quickly determine, for any `k`, what the `k`-th smallest GCD value is using binary search, effectively simulating access to the sorted `gcdPairs` without storing it explicitly.

---
<sub>Generated 2026-07-17 03:50 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
