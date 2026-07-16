# [3867] Sum of GCD of Formed Pairs

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-07-16 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/)

**Topics:** Array, Math, Two Pointers, Sorting, Simulation, Number Theory

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums of length n.

Construct an array prefixGcd where for each index i:

- Let mx_i = max(nums[0], nums[1], ..., nums[i]).

- prefixGcd[i] = gcd(nums[i], mx_i).

After constructing prefixGcd:

- Sort prefixGcd in non-decreasing order.

- Form pairs by taking the smallest unpaired element and the largest unpaired element.

- Repeat this process until no more pairs can be formed.

- For each formed pair, compute the gcd of the two elements.

- If n is odd, the middle element in the prefixGcd array remains unpaired and should be ignored.

Return an integer denoting the sum of the GCD values of all formed pairs.

The term gcd(a, b) denotes the greatest common divisor of a and b.

Example 1:

Input: nums = [2,6,4]

Output: 2

Explanation:

Construct prefixGcd:

			i
			nums[i]
			mx_i
			prefixGcd[i]

			0
			2
			2
			2

			1
			6
			6
			6

			2
			4
			6
			2

prefixGcd = [2, 6, 2]. After sorting, it forms [2, 2, 6].

Pair the smallest and largest elements: gcd(2, 6) = 2. The remaining middle element 2 is ignored. Thus, the sum is 2.

Example 2:

Input: nums = [3,6,2,8]

Output: 5

Explanation:

Construct prefixGcd:

			i
			nums[i]
			mx_i
			prefixGcd[i]

			0
			3
			3
			3

			1
			6
			6
			6

			2
			2
			6
			2

			3
			8
			8
			8

prefixGcd = [3, 6, 2, 8]. After sorting, it forms [2, 3, 6, 8].

Form pairs: gcd(2, 8) = 2 and gcd(3, 6) = 3. Thus, the sum is 2 + 3 = 5.

Constraints:

- 1 <= n == nums.length <= 10^5

- 1 <= nums[i] <= 10^​​​​​​​9

**Examples / sample tests:**

```
[2,6,4]
[3,6,2,8]
```

---

## Problem Summary
Given an integer array `nums`, we first construct a new array `prefixGcd`. Each `prefixGcd[i]` is the greatest common divisor (GCD) of `nums[i]` and the maximum value encountered in `nums` up to index `i`. After constructing `prefixGcd`, we sort it, then repeatedly pair the smallest remaining element with the largest remaining element, summing the GCDs of these pairs. If `n` is odd, the middle element is ignored.

## Intuition
The problem breaks down into several distinct, sequential steps.
1.  **Constructing `prefixGcd`**: This requires keeping track of the **running maximum** element seen so far in `nums`. As we iterate through `nums`, we update this maximum and then calculate `gcd(nums[i], current_max)`.
2.  **Sorting `prefixGcd`**: Once `prefixGcd` is fully constructed, we need to sort it. This is a standard operation.
3.  **Pairing and Summing GCDs**: The instruction to "form pairs by taking the smallest unpaired element and the largest unpaired element" immediately suggests a **two-pointer** approach on the sorted `prefixGcd` array. We can place one pointer at the beginning (smallest) and one at the end (largest), calculate their GCD, add it to a running sum, and then move both pointers inwards until they meet or cross. This naturally handles both even and odd lengths, as the `left < right` condition will stop before the middle element is processed if `n` is odd.

## Approach
The optimal algorithm involves three main phases:

1.  **Compute `prefixGcd` array**:
    *   Initialize an empty list `prefixGcd` and a variable `current_max = 0` (or `nums[0]` if `n >= 1`).
    *   Iterate through `nums` from `i = 0` to `n-1`:
        *   Update `current_max = max(current_max, nums[i])`.
        *   Calculate `gcd_val = gcd(nums[i], current_max)` using Python's `math.gcd` function.
        *   Append `gcd_val` to the `prefixGcd` list.

2.  **Sort `prefixGcd`**:
    *   Sort the `prefixGcd` list in non-decreasing order.

3.  **Pair elements and sum GCDs**:
    *   Initialize `total_gcd_sum = 0`.
    *   Initialize two pointers: `left = 0` and `right = len(prefixGcd) - 1`.
    *   While `left < right`:
        *   Calculate `pair_gcd = gcd(prefixGcd[left], prefixGcd[right])`.
        *   Add `pair_gcd` to `total_gcd_sum`.
        *   Increment `left` by 1.
        *   Decrement `right` by 1.
    *   Return `total_gcd_sum`.

## Visualization

Let's visualize the pairing step with `prefixGcd = [2, 3, 6, 8]` (after construction and sorting from Example 2).

```
Initial state:
prefixGcd: [ 2,  3,  6,  8 ]
             ^            ^
           left         right

Iteration 1:
- Pair (prefixGcd[left], prefixGcd[right]) = (2, 8)
- gcd(2, 8) = 2
- total_gcd_sum = 0 + 2 = 2
- Move pointers: left becomes 1, right becomes 2

prefixGcd: [ 2,  3,  6,  8 ]
                ^     ^
              left  right

Iteration 2:
- Pair (prefixGcd[left], prefixGcd[right]) = (3, 6)
- gcd(3, 6) = 3
- total_gcd_sum = 2 + 3 = 5
- Move pointers: left becomes 2, right becomes 1

prefixGcd: [ 2,  3,  6,  8 ]
                   ^ ^
                 right left (left is no longer < right)

Loop terminates because left (2) is not less than right (1).

Final total_gcd_sum = 5.
```

## Dry Run
Let's trace Example 1: `nums = [2, 6, 4]`

**Phase 1: Construct `prefixGcd`**

| `i` | `nums[i]` | `current_max` | `gcd(nums[i], current_max)` | `prefixGcd` (current state) |
| :-- | :-------- | :------------ | :-------------------------- | :-------------------------- |
| 0   | 2         | 2             | `gcd(2, 2)` = 2             | `[2]`                       |
| 1   | 6         | 6             | `gcd(6, 6)` = 6             | `[2, 6]`                    |
| 2   | 4         | 6             | `gcd(4, 6)` = 2             | `[2, 6, 2]`                 |

**Phase 2: Sort `prefixGcd`**

`prefixGcd` becomes `[2, 2, 6]`.

**Phase 3: Pair elements and sum GCDs**

| `left` | `right` | `prefixGcd[left]` | `prefixGcd[right]` | `gcd(left_val, right_val)` | `total_gcd_sum` |
| :----- | :------ | :---------------- | :----------------- | :------------------------- | :-------------- |
| 0      | 2       | 2                 | 6                  | `gcd(2, 6)` = 2            | 2               |
| 1      | 1       | -                 | -                  | -                          | -               |

The loop condition `left < right` (1 < 1) is now false. The loop terminates.

**Final Result**: `total_gcd_sum = 2`.

## Complexity
*   **Time Complexity**: **O(N log N)**
    *   Constructing `prefixGcd`: We iterate through `nums` once (N iterations). In each iteration, we perform a `max` operation (O(1)) and a `gcd` operation. The `gcd` operation for numbers up to 10^9 takes about `log(10^9)` time, which is a small constant (approx. 30 operations). So, this phase is O(N * log(max\_val)), effectively **O(N)**.
    *   Sorting `prefixGcd`: This takes **O(N log N)** time, where N is the length of the array.
    *   Pairing and summing GCDs: We iterate with two pointers, performing N/2 GCD operations. Similar to construction, this is O(N * log(max\_val)), effectively **O(N)**.
    *   The dominant factor is sorting, so the overall time complexity is **O(N log N)**.

*   **Space Complexity**: **O(N)**
    *   We create the `prefixGcd` list, which stores N elements. This requires **O(N)** space.
    *   The sorting algorithm might use additional O(log N) or O(N) space depending on the implementation, but O(N) for `prefixGcd` is the primary factor.

## Edge Cases
*   **`n = 1`**: If `nums = [5]`, `prefixGcd` will be `[gcd(5, 5)] = [5]`. After sorting, it's still `[5]`. The two-pointer loop `left < right` (0 < 0) will immediately be false. `total_gcd_sum` remains 0. This is correct as the problem states the middle element (the only element) is ignored if `n` is odd.
*   **All elements are identical**: `nums = [7, 7, 7]`. `prefixGcd` will be `[7, 7, 7]`. Sorted: `[7, 7, 7]`. `gcd(7, 7) = 7`. Sum = 7. Correct.
*   **Large numbers**: The constraints `nums[i] <= 10^9` are handled correctly by `math.gcd`, which is efficient for such values.
*   **Already sorted/reverse sorted `nums`**: The logic remains unaffected because `prefixGcd` is explicitly sorted before pairing, decoupling the input array's order from the pairing process.

## Solution

```python
import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Phase 1: Construct prefixGcd array
        prefix_gcd_arr = []
        current_max = 0
        for i in range(n):
            current_max = max(current_max, nums[i])
            prefix_gcd_arr.append(math.gcd(nums[i], current_max))
        
        # Phase 2: Sort prefixGcd array
        prefix_gcd_arr.sort()
        
        # Phase 3: Pair elements and sum GCDs using two pointers
        total_gcd_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            total_gcd_sum += math.gcd(prefix_gcd_arr[left], prefix_gcd_arr[right])
            left += 1
            right -= 1
            
        return total_gcd_sum

```

## Why This Works
The solution works because it correctly implements each step of the problem statement. The `prefixGcd` array is built by maintaining a **running maximum**, ensuring `mx_i` is correctly calculated for each index. Sorting `prefixGcd` is crucial because it allows the **two-pointer technique** to efficiently find the smallest and largest available elements for pairing. The `left < right` condition in the two-pointer loop naturally handles both even and odd lengths of `prefixGcd`: for even lengths, all elements are paired; for odd lengths, the middle element is correctly left unpaired and ignored, as required. The `math.gcd` function provides an efficient and correct way to compute the greatest common divisor for each pair.

---
<sub>Generated 2026-07-16 03:48 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
