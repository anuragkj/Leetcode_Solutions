# [3876] Construct Uniform Parity Array II

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-09-03 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/construct-uniform-parity-array-ii/)

**Topics:** Array, Math

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an array nums1 of n distinct integers.

You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.

For each index i, you must choose exactly one of the following (in any order):

- nums2[i] = nums1[i]​​​​​​​

- nums2[i] = nums1[i] - nums1[j], for an index j != i, such that nums1[i] - nums1[j] >= 1

Return true if it is possible to construct such an array, otherwise return false.

Example 1:

Input: nums1 = [1,4,7]

Output: true

Explanation:​​​​​​​​​​​​​​

- Set nums2[0] = nums1[0] = 1.

- Set nums2[1] = nums1[1] - nums1[0] = 4 - 1 = 3.

- Set nums2[2] = nums1[2] = 7.

- nums2 = [1, 3, 7], and all elements are odd. Thus, the answer is true.

Example 2:

Input: nums1 = [2,3]

Output: false

Explanation:

It is not possible to construct nums2 such that all elements have the same parity. Thus, the answer is false.

Example 3:

Input: nums1 = [4,6]

Output: true

Explanation:

- Set nums2[0] = nums1[0] = 4.

- Set nums2[1] = nums1[1] = 6.

- nums2 = [4, 6], and all elements are even. Thus, the answer is true.

Constraints:

- 1 <= n == nums1.length <= 10^5

- 1 <= nums1[i] <= 10^9

- nums1 consists of distinct integers.

**Examples / sample tests:**

```
[1,4,7]
[2,3]
[4,6]
```

---

## Problem Summary
You are given an array `nums1` of distinct integers. Your goal is to construct a new array `nums2` of the same length, where all elements in `nums2` are either **all odd** or **all even**. For each `nums2[i]`, you can either take `nums1[i]` directly, or subtract another `nums1[j]` (where `j != i` and `nums1[i] - nums1[j] >= 1`). Return `true` if such an array `nums2` can be constructed, `false` otherwise.

## Intuition
The core of this problem revolves around **parity** (whether a number is odd or even). We need to make all elements in `nums2` have the *same parity*. This immediately suggests two independent goals:
1.  Can we make all elements in `nums2` **even**?
2.  Can we make all elements in `nums2` **odd**?

If either of these is possible, the answer is `true`. If both are impossible, the answer is `false`.

Let's analyze how the operations affect parity:
*   **Option 1: `nums2[i] = nums1[i]`**
    The parity of `nums2[i]` is the same as `nums1[i]`. No change.
*   **Option 2: `nums2[i] = nums1[i] - nums1[j]`**
    The parity of `A - B` depends on the parities of `A` and `B`:
    *   `Even - Even = Even` (Parity of `A` doesn't change)
    *   `Odd - Odd = Even` (Parity of `A` changes)
    *   `Even - Odd = Odd` (Parity of `A` changes)
    *   `Odd - Even = Odd` (Parity of `A` doesn't change)

Notice a pattern: the parity of `nums1[i]` **changes** if and only if `nums1[j]` is **odd**.
This is a crucial observation! If we need to change an element's parity, we *must* subtract an odd number. If we don't need to change its parity, we can subtract an even number (or just use `nums1[i]`).

Since we only care about *changing* parity when `nums1[i]` doesn't match our target, we only need to consider subtracting an **odd** number. To maximize our chances of satisfying the condition `nums1[i] - nums1[j] >= 1` (which means `nums1[i] > nums1[j]`), we should always try to subtract the **smallest odd number** available in `nums1`. Let's call this `min_odd`. If `nums1[i]` is not strictly greater than `min_odd`, then we cannot subtract `min_odd` (or any other odd number, since `min_odd` is the smallest) to change its parity.

So, the strategy boils down to:
1.  Find the `min_odd` (smallest odd number) and `min_even` (smallest even number) in `nums1`.
2.  For each target parity (all even, then all odd):
    *   Iterate through `nums1`. For each `nums1[i]`:
        *   If `nums1[i]` already has the target parity, we're good (just use `nums2[i] = nums1[i]`).
        *   If `nums1[i]` *doesn't* have the target parity, we *must* change it. This requires subtracting an odd number.
            *   Can we subtract `min_odd`? Only if `min_odd` exists (i.e., not `infinity`) AND `nums1[i] > min_odd`.
            *   If we can't, then this target parity is impossible.
    *   If we successfully process all elements, this target parity is possible.

## Approach
1.  **Pre-computation:**
    *   Initialize `min_odd` and `min_even` to `infinity` (a very large number, like `math.inf` in Python).
    *   Iterate through `nums1` once:
        *   If `x` is even, update `min_even = min(min_even, x)`.
        *   If `x` is odd, update `min_odd = min(min_odd, x)`.
    *   This step takes O(N) time.

2.  **Helper Function `can_construct(target_parity)`:**
    *   This function determines if it's possible to make all elements in `nums2` have `target_parity` (where `0` means even, `1` means odd).
    *   **Special Case: No odd numbers in `nums1` (`min_odd == math.inf`)**
        *   If there are no odd numbers in `nums1`, we can never perform an operation that changes parity (because changing parity requires subtracting an odd number).
        *   Therefore, `can_construct` can only return `true` if *all* numbers in `nums1` already match the `target_parity`. Iterate through `nums1`; if any `x` has `x % 2 != target_parity`, return `false`. Otherwise, return `true`.
    *   **General Case: `min_odd` exists (is a finite number)**
        *   Iterate through each `x` in `nums1`:
            *   If `x % 2 == target_parity`: This element already matches. No action needed for this `x`. Continue to the next.
            *   If `x % 2 != target_parity`: This element needs its parity changed.
                *   As established in the intuition, changing parity requires subtracting an odd number. We try to use `min_odd`.
                *   The condition for subtraction is `x - min_odd >= 1`, which simplifies to `x > min_odd`.
                *   If `x <= min_odd`, we cannot subtract `min_odd` (or any other odd number, as `min_odd` is the smallest). In this case, we cannot achieve the `target_parity` for this `x`. Return `false`.
        *   If the loop completes without returning `false`, it means all elements can be made to match `target_parity`. Return `true`.
    *   This step takes O(N) time.

3.  **Main Function `uniformArray`:**
    *   Call `can_construct(0)` (to check if all elements can be made even). If it returns `true`, immediately return `true`.
    *   Otherwise, call `can_construct(1)` (to check if all elements can be made odd). If it returns `true`, immediately return `true`.
    *   If both attempts fail, return `false`.

## Visualization

Let's trace `nums1 = [1, 4, 7]` with `min_odd = 1` and `min_even = 4`.

```
nums1: [1, 4, 7]
min_odd = 1
min_even = 4

------------------------------------------------------------------
Attempt 1: Target ALL EVEN (target_parity = 0)
------------------------------------------------------------------
- Process nums1[0] = 1 (Odd):
    - Does 1 match target_parity (Even)? No.
    - Need to change parity. Subtract min_odd (1).
    - Check condition: Is 1 > min_odd (1)? No (1 is not strictly greater than 1).
    - -> Cannot make nums1[0] even.
    -> FAILED for ALL EVEN.

------------------------------------------------------------------
Attempt 2: Target ALL ODD (target_parity = 1)
------------------------------------------------------------------
- Process nums1[0] = 1 (Odd):
    - Does 1 match target_parity (Odd)? Yes.
    - -> OK. (We can set nums2[0] = 1)

- Process nums1[1] = 4 (Even):
    - Does 4 match target_parity (Odd)? No.
    - Need to change parity. Subtract min_odd (1).
    - Check condition: Is 4 > min_odd (1)? Yes.
    - -> OK. (We can set nums2[1] = 4 - 1 = 3)

- Process nums1[2] = 7 (Odd):
    - Does 7 match target_parity (Odd)? Yes.
    - -> OK. (We can set nums2[2] = 7)

- All elements processed successfully.
-> SUCCEEDED for ALL ODD.

------------------------------------------------------------------
Final Result: TRUE (because Attempt 2 succeeded)
```

## Dry Run

Let's walk through Example 1: `nums1 = [1, 4, 7]`

| Step | `nums1[i]` | `min_odd` | `min_even` | Target Parity | Current `x` | `x % 2` | Target `P` | Action / Check                                                               | Result for `x` | Overall Result |
| :--- | :--------- | :-------- | :--------- | :------------ | :---------- | :------ | :--------- | :--------------------------------------------------------------------------- | :------------- | :------------- |
| 1    |            | `inf`     | `inf`      |               |             |         |            | Initialize `min_odd`, `min_even`                                             |                |                |
| 2    | `1`        | `1`       | `inf`      |               |             |         |            | `1` is odd. `min_odd = min(inf, 1) = 1`.                                    |                |                |
| 3    | `4`        | `1`       | `4`        |               |             |         |            | `4` is even. `min_even = min(inf, 4) = 4`.                                  |                |                |
| 4    | `7`        | `1`       | `4`        |               |             |         |            | `7` is odd. `min_odd = min(1, 7) = 1`.                                      |                |                |
| **Pre-computation Done** |            | `1`       | `4`        |               |             |         |            | `min_odd = 1`, `min_even = 4`                                                |                |                |
| 5    |            |           |            | **0 (Even)**  |             |         |            | Call `can_construct(0)`                                                      |                |                |
| 6    |            |           |            |               | `1`         | `1`     | `0`        | `x % 2 != P`. `min_odd` is `1`. Check `x > min_odd`: Is `1 > 1`? No.        | Fail           | `false`        |
| **`can_construct(0)` returns `false`** |            |           |            |               |             |         |            |                                                                              |                |                |
| 7    |            |           |            | **1 (Odd)**   |             |         |            | Call `can_construct(1)`                                                      |                |                |
| 8    |            |           |            |               | `1`         | `1`     | `1`        | `x % 2 == P`. Matches.                                                       | OK             |                |
| 9    |            |           |            |               | `4`         | `0`     | `1`        | `x % 2 != P`. `min_odd` is `1`. Check `x > min_odd`: Is `4 > 1`? Yes.       | OK             |                |
| 10   |            |           |            |               | `7`         | `1`     | `1`        | `x % 2 == P`. Matches.                                                       | OK             |                |
| **`can_construct(1)` returns `true`** |            |           |            |               |             |         |            | All elements processed successfully for target odd.                          |                | `true`         |
| **Final Result** |            |           |            |               |             |         |            | `can_construct(0)` was `false`, `can_construct(1)` was `true`. Return `true`. |                | `true`         |

## Complexity
*   **Time Complexity:** O(N)
    *   Finding `min_odd` and `min_even` takes one pass through `nums1`, which is O(N).
    *   The `can_construct` function also takes one pass through `nums1`, which is O(N).
    *   We call `can_construct` at most twice.
    *   Therefore, the total time complexity is O(N) + O(N) + O(N) = O(N).
*   **Space Complexity:** O(1)
    *   We only store a few variables (`min_odd`, `min_even`, `target_parity`). This is constant space, regardless of the input size `N`.

## Edge Cases
*   **`n = 1` (single element array):**
    *   `nums1 = [5]`: `min_odd = 5`, `min_even = inf`.
        *   Target Even: `5` is odd, needs change. `5 > min_odd (5)` is false. Fails.
        *   Target Odd: `5` is odd, matches. Succeeds.
        *   Result: `true`. Correct.
*   **All elements have the same parity:**
    *   `nums1 = [2, 4, 6]` (all even): `min_odd = inf`, `min_even = 2`.
        *   Target Even: `min_odd` is `inf`. All `x` are even, matching target. Succeeds.
        *   Target Odd: `min_odd` is `inf`. `2` is even, doesn't match target. Fails.
        *   Result: `true`. Correct.
    *   `nums1 = [1, 3, 5]` (all odd): `min_odd = 1`, `min_even = inf`.
        *   Target Even: `1` is odd, needs change. `1 > min_odd (1)` is false. Fails.
        *   Target Odd: All `x` are odd, matching target. Succeeds.
        *   Result: `true`. Correct.
*   **`nums1` contains only two elements, one odd and one even:**
    *   `nums1 = [2, 3]`: `min_odd = 3`, `min_even = 2`.
        *   Target Even: `3` is odd, needs change. `3 > min_odd (3)` is false. Fails.
        *   Target Odd: `2` is even, needs change. `2 > min_odd (3)` is false. Fails.
        *   Result: `false`. Correct (matches Example 2).

The solution handles these cases correctly due to the careful consideration of `min_odd` and the `x > min_odd` condition.

## Solution

```python
import math

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = math.inf
        min_even = math.inf

        # Step 1: Pre-computation - Find the smallest odd and smallest even numbers in nums1.
        # This takes O(N) time.
        for x in nums1:
            if x % 2 == 0:  # x is even
                min_even = min(min_even, x)
            else:  # x is odd
                min_odd = min(min_odd, x)

        # Helper function to check if we can construct an array where all elements
        # have the specified target_parity (0 for even, 1 for odd).
        # This function takes O(N) time.
        def can_construct(target_parity: int) -> bool:
            # Key insight: To change the parity of a number 'x' (e.g., from even to odd, or odd to even),
            # we MUST subtract an ODD number.
            #   - If x is Even, and we want Odd: Even - Odd = Odd
            #   - If x is Odd, and we want Even: Odd - Odd = Even
            # If we need to change parity, we always try to subtract the smallest odd number (min_odd)
            # to maximize our chances of satisfying the condition `x - min_odd >= 1` (i.e., `x > min_odd`).

            # Case 1: No odd numbers exist in nums1 (min_odd is still math.inf).
            # In this scenario, we cannot perform any parity changes via subtraction.
            # So, we can only succeed if ALL original numbers in nums1 already match the target_parity.
            if min_odd == math.inf:
                for x in nums1:
                    if x % 2 != target_parity:
                        return False # Found a number that doesn't match and can't be changed
                return True # All numbers already match target_parity

            # Case 2: At least one odd number exists in nums1 (min_odd is a finite value).
            # We can potentially change parities.
            for x in nums1:
                if x % 2 != target_parity:
                    # The current number 'x' does not match the target parity.
                    # We MUST use subtraction to change its parity.
                    # We need to subtract an odd number, and we use min_odd.
                    # The problem condition is nums2[i] = nums1[i] - nums1[j] >= 1,
                    # which translates to x - min_odd >= 1, or simply x > min_odd.
                    if x <= min_odd:
                        # If x is not strictly greater than min_odd, we cannot subtract min_odd.
                        # Since min_odd is the smallest odd number, we cannot subtract any other
                        # odd number either (as they would be >= min_odd, making the condition
                        # x > nums1[j] even harder to satisfy).
                        return False # Cannot change parity for this 'x'
            return True # All numbers can be made to match the target_parity

        # Step 2: Try to construct an array where all elements are even (target_parity = 0).
        if can_construct(0):
            return True

        # Step 3: Try to construct an array where all elements are odd (target_parity = 1).
        if can_construct(1):
            return True

        # If neither target parity can be achieved, return False.
        return False

```

## Why This Works
The solution works because it exhaustively checks the only two possible uniform parity states (all even or all odd) and, for each state, employs a **greedy strategy** that is proven to be optimal. The key insight is that changing a number's parity (from odd to even or vice-versa) *always* requires subtracting an odd number. By attempting to subtract the `min_odd` (smallest odd number in `nums1`), we maximize the chance that `nums1[i] > min_odd` holds, allowing the parity change. If `min_odd` doesn't exist, no parity changes are possible. If `nums1[i]` is not strictly greater than `min_odd`, then it cannot be transformed to the target parity via subtraction, as `min_odd` is the smallest available odd number. If this greedy choice fails for any element, that target parity is impossible. Since we check both target parities, if a solution exists, this approach will find it.

---
<sub>Generated 2026-09-03 04:55 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
