# [3875] Construct Uniform Parity Array I

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-09-02 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/construct-uniform-parity-array-i/)

**Topics:** Array, Math

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an array nums1 of n distinct integers.

You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.

For each index i, you must choose exactly one of the following (in any order):

- nums2[i] = nums1[i]

- nums2[i] = nums1[i] - nums1[j], for an index j != i

Return true if it is possible to construct such an array, otherwise, return false.

Example 1:

Input: nums1 = [2,3]

Output: true

Explanation:

- Choose nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1.

- Choose nums2[1] = nums1[1] = 3.

- nums2 = [-1, 3], and both elements are odd. Thus, the answer is true​​​​​​​.

Example 2:

Input: nums1 = [4,6]

Output: true

Explanation:​​​​​​​

- Choose nums2[0] = nums1[0] = 4.

- Choose nums2[1] = nums1[1] = 6.

- nums2 = [4, 6], and all elements are even. Thus, the answer is true.

Constraints:

- 1 <= n == nums1.length <= 100

- 1 <= nums1[i] <= 100

- nums1 consists of distinct integers.

**Examples / sample tests:**

```
[2,3]
[4,6]
```

---

## Problem Summary
You are given an array `nums1` of `n` distinct integers. The goal is to determine if it's possible to construct another array `nums2` of the same length, such that all elements in `nums2` are either all odd or all even. For each `nums2[i]`, you can either set it to `nums1[i]` or to `nums1[i] - nums1[j]` for any other index `j`.

## Intuition
The core of this problem lies in understanding **parity** (whether a number is odd or even). We need to make all elements in `nums2` have the same parity. Let's analyze how the two construction rules affect parity:

1.  **`nums2[i] = nums1[i]`**: The parity of `nums2[i]` is simply the **same** as `nums1[i]`.
2.  **`nums2[i] = nums1[i] - nums1[j]` (where `j != i`)**:
    *   If `nums1[i]` and `nums1[j]` have the **same parity** (both even or both odd), their difference `nums1[i] - nums1[j]` will be **even**.
    *   If `nums1[i]` and `nums1[j]` have **different parities** (one even, one odd), their difference `nums1[i] - nums1[j]` will be **odd**.

Our strategy will be to check if we can achieve an "all even" `nums2` OR an "all odd" `nums2`. The key observation will be the count of odd numbers in the original `nums1`.

## Approach
The approach involves counting the number of odd integers in `nums1` and then analyzing the possibilities based on this count.

1.  **Count Odd Numbers:** Iterate through `nums1` and count how many odd integers it contains. Let this count be `O`.

2.  **Check if an "All Even" `nums2` is possible:**
    *   **If `O = 0` (all numbers in `nums1` are even):** We can simply choose `nums2[i] = nums1[i]` for every `i`. All elements in `nums2` will be even. So, an "all even" `nums2` is **possible**.
    *   **If `O = 1` (exactly one odd number in `nums1`):** Let `nums1[k]` be the only odd number. To make `nums2[k]` even, we would need to use `nums2[k] = nums1[k] - nums1[j]` where `nums1[j]` is also odd. However, since `nums1[k]` is the *only* odd number, there is no other odd `nums1[j]` (`j != k`) to subtract. Thus, `nums2[k]` cannot be made even. So, an "all even" `nums2` is **impossible**.
    *   **If `O >= 2` (at least two odd numbers in `nums1`):**
        *   For any `nums1[i]` that is already even: Choose `nums2[i] = nums1[i]`. It's even.
        *   For any `nums1[i]` that is odd: Since `O >= 2`, we can always find at least one *other* odd number `nums1[j]` (`j != i`). Choose `nums2[i] = nums1[i] - nums1[j]`. This will result in an even number (Odd - Odd = Even).
        *   Therefore, an "all even" `nums2` is **possible**.
    *   **Summary for "All Even": Possible if `O = 0` OR `O >= 2`.**

3.  **Check if an "All Odd" `nums2` is possible:**
    *   **If `O = 0` (all numbers in `nums1` are even):** To make any `nums2[i]` odd, we would need to use `nums2[i] = nums1[i] - nums1[j]` where `nums1[j]` is odd. But there are no odd numbers in `nums1`. So, an "all odd" `nums2` is **impossible**.
    *   **If `O >= 1` (at least one odd number in `nums1`):**
        *   For any `nums1[i]` that is already odd: Choose `nums2[i] = nums1[i]`. It's odd.
        *   For any `nums1[i]` that is even: Since `O >= 1`, we can pick *any* odd number `nums1[j]` from `nums1`. Choose `nums2[i] = nums1[i] - nums1[j]`. This will result in an odd number (Even - Odd = Odd).
        *   Therefore, an "all odd" `nums2` is **possible**.
    *   **Summary for "All Odd": Possible if `O >= 1`.**

4.  **Final Result:** We need to return `true` if *either* an "all even" `nums2` is possible *OR* an "all odd" `nums2` is possible.
    *   **If `O = 0`:** "All Even" is possible. Result: `true`.
    *   **If `O = 1`:** "All Odd" is possible. Result: `true`.
    *   **If `O >= 2`:** "All Even" is possible AND "All Odd" is possible. Result: `true`.

    As you can see, in all possible scenarios for `O`, at least one of the target parities (all even or all odd) is achievable. This means the answer is **always `true`**.

## Visualization
```mermaid
graph TD
    A[Start] --> B{Count odd numbers in nums1 (O)};
    B --> C{Is O = 0?};
    C -- Yes --> D["All Even" nums2 is possible];
    C -- No --> E{Is O = 1?};
    E -- Yes --> F["All Odd" nums2 is possible];
    E -- No (O >= 2) --> G["All Even" nums2 is possible];
    G --> H["All Odd" nums2 is possible];
    D --> I[Return True];
    F --> I;
    G --> I;
    H --> I;
```

## Dry Run
Let's walk through Example 1: `nums1 = [2,3]`

1.  **Count Odd Numbers:**
    *   `2` is even.
    *   `3` is odd.
    *   The count of odd numbers `O = 1`.

2.  **Check "All Even" possibility:**
    *   Is `O = 0` OR `O >= 2`? No, `O = 1` fits neither condition.
    *   So, an "all even" `nums2` is **impossible**. (Specifically, `nums1[1]=3` is odd, and there's no other odd number to subtract to make it even.)

3.  **Check "All Odd" possibility:**
    *   Is `O >= 1`? Yes, `O = 1`.
    *   So, an "all odd" `nums2` is **possible**.
        *   For `nums1[1]=3` (odd): We can choose `nums2[1] = nums1[1] = 3`. (This is odd).
        *   For `nums1[0]=2` (even): We need to make it odd. Since `O >= 1`, we can use the only available odd number, `nums1[1]=3`. Choose `nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1`. (This is odd).
        *   The resulting `nums2` would be `[-1, 3]`, where both elements are odd.

4.  **Final Result:** Since an "all odd" `nums2` is possible, the function returns `true`. This matches the example output.

## Complexity
*   **Time Complexity:** O(1). While a naive implementation might iterate through `nums1` to count odd numbers (O(N)), the logical conclusion is that the answer is always `true`. Therefore, the most optimal solution simply returns `True` without inspecting the input, making it O(1).
*   **Space Complexity:** O(1). No additional data structures are used.

## Edge Cases
The solution inherently handles all edge cases because the logic covers all possible counts of odd numbers (`O = 0`, `O = 1`, `O >= 2`).
*   **`n = 1`:** If `nums1 = [X]`, there is no `j != i`, so `nums2[0]` must be `nums1[0]`. The array `[X]` trivially has uniform parity. My logic: if `X` is even, `O=0`, returns `true`. If `X` is odd, `O=1`, returns `true`. Correct.
*   **All numbers are even:** `nums1 = [2, 4, 6]`. `O=0`. My logic returns `true`. We can construct `nums2 = [2, 4, 6]` (all even). Correct.
*   **All numbers are odd:** `nums1 = [1, 3, 5]`. `O=3`. My logic returns `true`. We can construct `nums2 = [1, 3, 5]` (all odd) or `nums2 = [1-3, 3-1, 5-3] = [-2, 2, 2]` (all even). Correct.
*   **Mixed parities:** `nums1 = [1, 2, 3]`. `O=2`. My logic returns `true`. We can construct `nums2 = [1, 2-1, 3] = [1, 1, 3]` (all odd) or `nums2 = [1-3, 2, 3-1] = [-2, 2, 2]` (all even). Correct.

## Solution
```python
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # This problem asks if it's possible to construct an array nums2
        # where all elements have the same parity (all odd or all even).
        #
        # Let's analyze the parity of the two construction options for nums2[i]:
        # 1. nums2[i] = nums1[i]:
        #    - The parity of nums2[i] is the same as nums1[i].
        #
        # 2. nums2[i] = nums1[i] - nums1[j] (for j != i):
        #    - If nums1[i] and nums1[j] have the SAME parity (both even or both odd),
        #      their difference (nums1[i] - nums1[j]) will be EVEN.
        #    - If nums1[i] and nums1[j] have DIFFERENT parities (one even, one odd),
        #      their difference (nums1[i] - nums1[j]) will be ODD.
        #
        # Let 'O' be the count of odd numbers in nums1.
        #
        # Scenario 1: Can we make all elements of nums2 EVEN?
        # - If nums1[i] is even: We can simply choose nums2[i] = nums1[i]. (It's already even).
        # - If nums1[i] is odd: We MUST use nums2[i] = nums1[i] - nums1[j] where nums1[j] is also odd (j != i).
        #   This is only possible if there are at least two odd numbers in nums1 (O >= 2).
        #   - If O = 0 (all numbers in nums1 are even): Yes, just copy nums1.
        #   - If O = 1 (exactly one odd number in nums1): No, the single odd number cannot be made even by subtraction
        #     because there's no other odd number to subtract.
        #   - If O >= 2 (two or more odd numbers in nums1): Yes, for any odd nums1[i], we can pick another odd nums1[j].
        # Conclusion for "All Even" target: Possible if O == 0 OR O >= 2.
        #
        # Scenario 2: Can we make all elements of nums2 ODD?
        # - If nums1[i] is odd: We can simply choose nums2[i] = nums1[i]. (It's already odd).
        # - If nums1[i] is even: We MUST use nums2[i] = nums1[i] - nums1[j] where nums1[j] is odd.
        #   This is only possible if there is at least one odd number in nums1 (O >= 1).
        #   - If O = 0 (all numbers in nums1 are even): No, there's no odd nums1[j] to subtract.
        #   - If O >= 1 (one or more odd numbers in nums1): Yes, for any even nums1[i], we can pick any odd nums1[j].
        # Conclusion for "All Odd" target: Possible if O >= 1.
        #
        # Combining these possibilities:
        # - If O = 0: "All Even" is possible. (Result: True)
        # - If O = 1: "All Odd" is possible. (Result: True)
        # - If O >= 2: "All Even" is possible AND "All Odd" is possible. (Result: True)
        #
        # In all possible scenarios for the count of odd numbers (O), it is always possible
        # to construct an array nums2 with uniform parity.
        # Therefore, the answer is always True.
        
        return True

```

## Why This Works
The solution works because we can always achieve at least one of the two desired uniform parities (all even or all odd).
1.  **If `nums1` contains only even numbers (count of odd numbers `O = 0`):** We can simply set `nums2[i] = nums1[i]` for all `i`. This results in an `nums2` where all elements are even.
2.  **If `nums1` contains at least one odd number (count of odd numbers `O >= 1`):** We can construct an `nums2` where all elements are odd. For any `nums1[i]` that is already odd, we set `nums2[i] = nums1[i]`. For any `nums1[i]` that is even, we can pick any odd number `nums1[j]` (which exists because `O >= 1`) and set `nums2[i] = nums1[i] - nums1[j]`. Since Even - Odd = Odd, all these `nums2[i]` will be odd.
Since these two conditions (`O = 0` or `O >= 1`) cover all possible inputs for `nums1`, and both lead to a successful construction, the problem is always solvable.

---
<sub>Generated 2026-09-02 04:58 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
