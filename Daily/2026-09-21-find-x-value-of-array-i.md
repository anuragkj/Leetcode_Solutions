# [3524] Find X Value of Array I

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-09-21 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/find-x-value-of-array-i/)

**Topics:** Array, Math, Dynamic Programming

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an array of positive integers nums, and a positive integer k.

You are allowed to perform an operation once on nums, where in each operation you can remove any non-overlapping prefix and suffix from nums such that nums remains non-empty.

You need to find the x-value of nums, which is the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x when divided by k.

Return an array result of size k where result[x] is the x-value of nums for 0 <= x <= k - 1.

A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.

A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.

Note that the prefix and suffix to be chosen for the operation can be empty.

Example 1:

Input: nums = [1,2,3,4,5], k = 3

Output: [9,2,4]

Explanation:

- For x = 0, the possible operations include all possible ways to remove non-overlapping prefix/suffix that do not remove nums[2] == 3.

- For x = 1, the possible operations are:

- Remove the empty prefix and the suffix [2, 3, 4, 5]. nums becomes [1].

- Remove the prefix [1, 2, 3] and the suffix [5]. nums becomes [4].

- For x = 2, the possible operations are:

- Remove the empty prefix and the suffix [3, 4, 5]. nums becomes [1, 2].

- Remove the prefix [1] and the suffix [3, 4, 5]. nums becomes [2].

- Remove the prefix [1, 2, 3] and the empty suffix. nums becomes [4, 5].

- Remove the prefix [1, 2, 3, 4] and the empty suffix. nums becomes [5].

Example 2:

Input: nums = [1,2,4,8,16,32], k = 4

Output: [18,1,2,0]

Explanation:

- For x = 0, the only operations that do not result in x = 0 are:

- Remove the empty prefix and the suffix [4, 8, 16, 32]. nums becomes [1, 2].

- Remove the empty prefix and the suffix [2, 4, 8, 16, 32]. nums becomes [1].

- Remove the prefix [1] and the suffix [4, 8, 16, 32]. nums becomes [2].

- For x = 1, the only possible operation is:

- Remove the empty prefix and the suffix [2, 4, 8, 16, 32]. nums becomes [1].

- For x = 2, the possible operations are:

- Remove the empty prefix and the suffix [4, 8, 16, 32]. nums becomes [1, 2].

- Remove the prefix [1] and the suffix [4, 8, 16, 32]. nums becomes [2].

- For x = 3, there is no possible way to perform the operation.

Example 3:

Input: nums = [1,1,2,1,1], k = 2

Output: [9,6]

Constraints:

- 1 <= nums[i] <= 10^9

- 1 <= nums.length <= 10^5

- 1 <= k <= 5

**Examples / sample tests:**

```
[1,2,3,4,5]
3
[1,2,4,8,16,32]
4
[1,1,2,1,1]
2
```

---

## Problem Summary
Given an array `nums` of positive integers and a positive integer `k`, we need to find all possible non-empty contiguous subarrays. For each such subarray, calculate the product of its elements modulo `k`. The goal is to return an array `result` of size `k`, where `result[x]` is the total count of subarrays whose product modulo `k` equals `x`.

## Intuition
The core of the problem is to count **contiguous non-empty subarrays** and their product modulo `k`. A brute-force approach of checking all `N*(N+1)/2` subarrays would be `O(N^2)` at best (if product calculation is `O(1)`), which is too slow for `N=10^5`.

The key observation comes from the constraint `k <= 5`. This small value of `k` is a strong hint that `k` can be part of our state in a **dynamic programming** solution. When calculating products modulo `k`, we only care about the remainder. The property `(A * B) % k = ((A % k) * (B % k)) % k` is crucial.

Consider how subarrays are formed: a subarray `nums[i...j]` is either just `nums[j]` itself, or it's `nums[j]` appended to a subarray `nums[i...j-1]` that ends at the previous element. This structure is perfect for dynamic programming.

## Approach
We will use a dynamic programming approach to efficiently count subarrays.

1.  **Initialize `final_answer` array:** Create an array `final_answer` of size `k`, initialized with zeros. `final_answer[x]` will store the total count of subarrays whose product modulo `k` is `x`.

2.  **Initialize `current_remainders_count` array:** Create an array `current_remainders_count` of size `k`, also initialized with zeros. `current_remainders_count[r]` will store the count of subarrays *ending at the current element being processed* whose product modulo `k` is `r`.

3.  **Iterate through `nums`:** Process each `num` in the input array `nums` from left to right.

    a.  **Calculate `num_mod_k`:** Get the remainder of the current `num` when divided by `k`: `num_mod_k = num % k`.

    b.  **Create `new_remainders_count`:** For each `num`, we'll compute a `new_remainders_count` array. This array will represent the counts of subarrays *ending at the current `num`*. Initialize it to `[0] * k`.

    c.  **Subarray `[num]`:** The current `num` itself forms a subarray. Its product modulo `k` is `num_mod_k`. So, increment `new_remainders_count[num_mod_k]` by 1.

    d.  **Extend previous subarrays:** Iterate through all possible previous remainders `r_prev` from `0` to `k-1`.
        *   If `current_remainders_count[r_prev]` is greater than 0, it means there were `current_remainders_count[r_prev]` subarrays ending at the *previous* element whose product modulo `k` was `r_prev`.
        *   By appending the current `num` to these subarrays, their new product modulo `k` will be `(r_prev * num_mod_k) % k`. Let this be `new_r`.
        *   Add `current_remainders_count[r_prev]` to `new_remainders_count[new_r]`.

    e.  **Update `current_remainders_count`:** After processing all extensions, `new_remainders_count` now correctly holds the counts for all subarrays ending at the current `num`. Update `current_remainders_count = new_remainders_count` for the next iteration.

    f.  **Accumulate to `final_answer`:** Add all counts from the updated `current_remainders_count` to `final_answer`. This is because all these subarrays (ending at the current `num`) are valid subarrays that contribute to the total counts. For each `r` from `0` to `k-1`, `final_answer[r] += current_remainders_count[r]`.

4.  **Return `final_answer`:** After iterating through all elements in `nums`, `final_answer` will contain the desired counts for each `x`.

## Visualization

Let's visualize the DP state updates for `nums = [A, B, C]`, `k=K`.

```
Initial State:
  final_answer = [0, 0, ..., 0] (size K)
  current_remainders_count = [0, 0, ..., 0] (size K)

Processing A (nums[0]):
  num_mod_k = A % K
  new_remainders_count = [0, ..., 0]
  new_remainders_count[num_mod_k] += 1  (for subarray [A])
  
  current_remainders_count = new_remainders_count
  final_answer += current_remainders_count
  
  Example: current_remainders_count = [0, 1, 0] if A%K=1
           final_answer = [0, 1, 0]

Processing B (nums[1]):
  num_mod_k = B % K
  new_remainders_count = [0, ..., 0]
  new_remainders_count[num_mod_k] += 1  (for subarray [B])
  
  For each r_prev in current_remainders_count (from A):
    If current_remainders_count[r_prev] > 0:
      new_r = (r_prev * num_mod_k) % K
      new_remainders_count[new_r] += current_remainders_count[r_prev] (for subarrays like [A,B])
  
  current_remainders_count = new_remainders_count
  final_answer += current_remainders_count
  
  Example: current_remainders_count = [0, 0, 2] if A%K=1, B%K=2.
           (1 for [B], 1 for [A,B] where (1*2)%3=2)
           final_answer = [0, 1, 0] + [0, 0, 2] = [0, 1, 2]

Processing C (nums[2]):
  num_mod_k = C % K
  new_remainders_count = [0, ..., 0]
  new_remainders_count[num_mod_k] += 1  (for subarray [C])
  
  For each r_prev in current_remainders_count (from B):
    If current_remainders_count[r_prev] > 0:
      new_r = (r_prev * num_mod_k) % K
      new_remainders_count[new_r] += current_remainders_count[r_prev] (for subarrays like [A,B,C], [B,C])
  
  current_remainders_count = new_remainders_count
  final_answer += current_remainders_count
  
  Example: current_remainders_count = [3, 0, 0] if A%K=1, B%K=2, C%K=0.
           (1 for [C], 2 for [A,B,C] and [B,C] where (2*0)%3=0)
           final_answer = [0, 1, 2] + [3, 0, 0] = [3, 1, 2]
```

## Dry Run
Let's trace Example 1: `nums = [1,2,3,4,5]`, `k = 3`.

`final_answer = [0, 0, 0]`
`current_remainders_count = [0, 0, 0]`

| `i` | `num` | `num_mod_k` | `new_remainders_count` (initial) | `new_remainders_count` (after `[num]`) | `new_remainders_count` (after extending `current_remainders_count`) | `current_remainders_count` (updated) | `final_answer` (updated) |
| :-- | :---- | :---------- | :------------------------------- | :------------------------------------- | :------------------------------------------------------------------ | :----------------------------------- | :----------------------- |
| -   | -     | -           | -                                | -                                      | -                                                                   | `[0, 0, 0]`                          | `[0, 0, 0]`              |
| 0   | 1     | 1           | `[0, 0, 0]`                      | `[0, 1, 0]`                            | `[0, 1, 0]` (no previous subarrays)                                 | `[0, 1, 0]`                          | `[0, 1, 0]`              |
| 1   | 2     | 2           | `[0, 0, 0]`                      | `[0, 0, 1]`                            | `[0, 0, 1]` (for `[2]`) + `current_remainders_count[1]=1` (for `[1]`) * `2%3=2` -> `[0, 0, 1]` + `[0, 0, 1]` = `[0, 0, 2]` | `[0, 0, 2]`                          | `[0, 1, 2]`              |
| 2   | 3     | 0           | `[0, 0, 0]`                      | `[1, 0, 0]`                            | `[1, 0, 0]` (for `[3]`) + `current_remainders_count[2]=2` (for `[1,2]`) * `3%3=0` -> `[1, 0, 0]` + `[2, 0, 0]` = `[3, 0, 0]` | `[3, 0, 0]`                          | `[3, 1, 2]`              |
| 3   | 4     | 1           | `[0, 0, 0]`                      | `[0, 1, 0]`                            | `[0, 1, 0]` (for `[4]`) + `current_remainders_count[0]=3` (for `[3]`, `[1,2,3]`) * `4%3=1` -> `[0, 1, 0]` + `[3, 0, 0]` = `[3, 1, 0]` | `[3, 1, 0]`                          | `[6, 2, 2]`              |
| 4   | 5     | 2           | `[0, 0, 0]`                      | `[0, 0, 1]`                            | `[0, 0, 1]` (for `[5]`) + `current_remainders_count[0]=3` (for `[3]`, `[1,2,3]`, `[4]`) * `5%3=2` -> `[3, 0, 1]` + `current_remainders_count[1]=1` (for `[3,4]`) * `5%3=2` -> `[3, 0, 2]` | `[3, 0, 2]`                          | `[9, 2, 4]`              |

**Final Result:** `[9, 2, 4]`. This matches Example 1.

## Complexity
*   **Time Complexity:** `O(N * k)`. We iterate through `N` elements in `nums`. For each element, we iterate `k` times to update `new_remainders_count` and another `k` times to add to `final_answer`. Since `k` is small (up to 5), this is very efficient.
*   **Space Complexity:** `O(k)`. We use two arrays, `final_answer` and `current_remainders_count`, both of size `k`.

## Edge Cases
*   **`k = 1`**: All products modulo 1 are 0. The solution correctly handles this: `num % 1` is always 0, so `new_r` will always be 0. `final_answer[0]` will accumulate all `N*(N+1)/2` subarray counts, and other `final_answer[x]` will remain 0.
*   **`nums` contains multiples of `k`**: If `num % k == 0`, then `num_mod_k` is 0. Any `r_prev * 0 % k` will result in 0. This means all subarrays extended by such a `num` will have a product modulo `k` of 0. The DP correctly funnels all these counts into `new_remainders_count[0]`.
*   **`nums.length = 1`**: For `nums = [X]`, `k = K`, the loop runs once. `current_remainders_count` will become `[0, ..., 1, ..., 0]` (1 at index `X % K`), and `final_answer` will be updated to this value. This is correct as there's only one subarray `[X]`.
*   **`nums` contains `1`**: If `num % k == 1`, then `num_mod_k` is 1. `(r_prev * 1) % k` is `r_prev`. This means extending subarrays with `1` preserves their product modulo `k`, which is correct.

## Solution

```python
from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        # final_answer[x] will store the total count of subarrays whose product modulo k is x.
        final_answer = [0] * k
        
        # current_remainders_count[r] stores the count of subarrays ending at the current element
        # whose product modulo k is r.
        current_remainders_count = [0] * k
        
        # Iterate through each number in the input array.
        for num in nums:
            # Calculate the current number's remainder modulo k.
            # This is the value we'll use for multiplication.
            num_mod_k = num % k
            
            # new_remainders_count will store the counts for subarrays ending at the current 'num'.
            # It's re-calculated for each 'num'.
            new_remainders_count = [0] * k
            
            # 1. The current number 'num' itself forms a subarray.
            # Its product modulo k is num_mod_k.
            new_remainders_count[num_mod_k] += 1
            
            # 2. Extend all previously found subarrays (ending at the previous element)
            # by appending the current 'num'.
            for r_prev in range(k):
                # If there were any subarrays ending at the previous element with product modulo k = r_prev,
                # we extend them.
                if current_remainders_count[r_prev] > 0:
                    # The new product modulo k will be (r_prev * num_mod_k) % k.
                    new_r = (r_prev * num_mod_k) % k
                    
                    # Add the count of these extended subarrays to the new_remainders_count.
                    new_remainders_count[new_r] += current_remainders_count[r_prev]
            
            # After processing all extensions for the current 'num',
            # update current_remainders_count for the next iteration.
            current_remainders_count = new_remainders_count
            
            # Add the counts of all subarrays ending at the current 'num' to the final_answer.
            # These are all valid subarrays that contribute to the total counts.
            for r in range(k):
                final_answer[r] += current_remainders_count[r]
                
        return final_answer

```

## Why This Works
This dynamic programming approach works because it systematically counts every possible non-empty contiguous subarray exactly once. For each element `nums[i]`, we consider two types of subarrays ending at `nums[i]`:
1.  The subarray consisting only of `nums[i]` itself.
2.  Subarrays formed by appending `nums[i]` to any valid subarray that ended at `nums[i-1]`.
By maintaining `current_remainders_count` (which tracks counts of subarrays ending at `nums[i-1]`) and using it to build `new_remainders_count` (for subarrays ending at `nums[i]`), we ensure that all combinations are covered. The modulo arithmetic property `(A * B) % k = ((A % k) * (B % k)) % k` allows us to only track remainders, keeping the state space small (`k` possible remainders). Summing `current_remainders_count` into `final_answer` at each step correctly aggregates the counts for all subarrays encountered so far.

---
<sub>Generated 2026-09-21 05:20 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
