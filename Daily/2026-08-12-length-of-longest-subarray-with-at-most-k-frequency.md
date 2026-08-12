# [2958] Length of Longest Subarray With at Most K Frequency

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-08-12 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/)

**Topics:** Array, Hash Table, Sliding Window

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums and an integer k.

The frequency of an element x is the number of times it occurs in an array.

An array is called good if the frequency of each element in this array is less than or equal to k.

Return the length of the longest good subarray of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,2,3,1,2,3,1,2], k = 2
Output: 6
Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
It can be shown that there are no good subarrays with length more than 6.

Example 2:

Input: nums = [1,2,1,2,1,2,1,2], k = 1
Output: 2
Explanation: The longest possible good subarray is [1,2] since the values 1 and 2 occur at most once in this subarray. Note that the subarray [2,1] is also good.
It can be shown that there are no good subarrays with length more than 2.

Example 3:

Input: nums = [5,5,5,5,5,5,5], k = 4
Output: 4
Explanation: The longest possible good subarray is [5,5,5,5] since the value 5 occurs 4 times in this subarray.
It can be shown that there are no good subarrays with length more than 4.

Constraints:

- 1 <= nums.length <= 10^5

- 1 <= nums[i] <= 10^9

- 1 <= k <= nums.length

**Examples / sample tests:**

```
[1,2,3,1,2,3,1,2]
2
[1,2,1,2,1,2,1,2]
1
[5,5,5,5,5,5,5]
4
```

---

## Problem Summary
Given an array `nums` and an integer `k`, find the longest contiguous subarray where the frequency of each element within that subarray is at most `k`.

## Intuition
When asked for the "longest subarray" that satisfies a certain condition, a **sliding window** approach is often very efficient.
Let's consider a window `[left, right]` in the array.
1.  If this window is "good" (all element frequencies are `<= k`), we want to try and make it longer. We can do this by expanding the window to the right.
2.  If this window is *not* "good" (at least one element's frequency is `> k`), we must shrink it. To maintain contiguity and potentially find a good subarray, we shrink it from the left.

The key observation is that if a window `[left, right]` is good, then any smaller window `[left, right-1]` is also good. This monotonicity allows us to use a two-pointer sliding window where the `right` pointer expands and the `left` pointer contracts only when the condition is violated. We need an efficient way to track element frequencies within the current window, for which a **hash map (dictionary)** is perfect.

## Approach
We will use a **sliding window** defined by two pointers, `left` and `right`, and a hash map `freq` to store the counts of elements within the current window `nums[left...right]`.

1.  Initialize `left = 0` and `max_len = 0`.
2.  Initialize an empty hash map `freq` (e.g., `collections.defaultdict(int)` in Python) to store frequencies of numbers in the current window.
3.  Iterate with the `right` pointer from `0` to `len(nums) - 1`:
    a.  Add `nums[right]` to the current window. Increment its frequency in `freq`.
    b.  **Check the "good" condition:** If the frequency of `nums[right]` (the element we just added) now exceeds `k`, the window `nums[left...right]` is no longer "good".
    c.  **Shrink the window:** While `freq[nums[right]] > k`:
        i.  Decrement the frequency of `nums[left]` (the element at the leftmost end of the window).
        ii. Move the `left` pointer one step to the right (`left += 1`).
        This process continues until the frequency of `nums[right]` (and implicitly, all other elements) is back to `k` or less.
    d.  After potentially shrinking, the current window `nums[left...right]` is guaranteed to be "good". Calculate its length (`right - left + 1`) and update `max_len` if this length is greater than the current `max_len`.
4.  After the `right` pointer has traversed the entire array, `max_len` will hold the length of the longest good subarray. Return `max_len`.

## Visualization

Let's trace `nums = [1, 2, 3, 1, 2, 3, 1, 2]`, `k = 2`.

```
nums = [ 1, 2, 3, 1, 2, 3, 1, 2 ]
        ^
        L
        R
freq = {}
max_len = 0

1. R=0, nums[0]=1:
   freq = {1:1}
   Window [1] is good. max_len = max(0, 0-0+1) = 1.
   [ 1, 2, 3, 1, 2, 3, 1, 2 ]
   ^
   L,R

2. R=1, nums[1]=2:
   freq = {1:1, 2:1}
   Window [1,2] is good. max_len = max(1, 1-0+1) = 2.
   [ 1, 2, 3, 1, 2, 3, 1, 2 ]
   ^  ^
   L  R

3. R=2, nums[2]=3:
   freq = {1:1, 2:1, 3:1}
   Window [1,2,3] is good. max_len = max(2, 2-0+1) = 3.
   [ 1, 2, 3, 1, 2, 3, 1, 2 ]
   ^     ^
   L     R

4. R=3, nums[3]=1:
   freq = {1:2, 2:1, 3:1}
   Window [1,2,3,1] is good. max_len = max(3, 3-0+1) = 4.
   [ 1, 2, 3, 1, 2, 3, 1, 2 ]
   ^        ^
   L        R

5. R=4, nums[4]=2:
   freq = {1:2, 2:2, 3:1}
   Window [1,2,3,1,2] is good. max_len = max(4, 4-0+1) = 5.
   [ 1, 2, 3, 1, 2, 3, 1, 2 ]
   ^           ^
   L           R

6. R=5, nums[5]=3:
   freq = {1:2, 2:2, 3:2}
   Window [1,2,3,1,2,3] is good. max_len = max(5, 5-0+1) = 6.
   [ 1, 2, 3, 1, 2, 3, 1, 2 ]
   ^              ^
   L              R

7. R=6, nums[6]=1:
   freq = {1:3, 2:2, 3:2}
   Window [1,2,3,1,2,3,1] is NOT good because freq[1] (3) > k (2).
   Shrink from left:
     nums[L]=nums[0]=1. freq[1] becomes 2. L becomes 1.
     freq = {1:2, 2:2, 3:2}
     Window [2,3,1,2,3,1] is good. max_len = max(6, 6-1+1) = 6.
   [ 1, 2, 3, 1, 2, 3, 1, 2 ]
      ^                 ^
      L                 R

8. R=7, nums[7]=2:
   freq = {1:2, 2:3, 3:2}
   Window [2,3,1,2,3,1,2] is NOT good because freq[2] (3) > k (2).
   Shrink from left:
     nums[L]=nums[1]=2. freq[2] becomes 2. L becomes 2.
     freq = {1:2, 2:2, 3:2}
     Window [3,1,2,3,1,2] is good. max_len = max(6, 7-2+1) = 6.
   [ 1, 2, 3, 1, 2, 3, 1, 2 ]
         ^                ^
         L                R

End of array. Final max_len = 6.
```

## Dry Run
Example 1: `nums = [1,2,3,1,2,3,1,2]`, `k = 2`

| `left` | `right` | `nums[right]` | `freq` (before shrink) | `freq[nums[right]] > k`? | `nums[left]` (if shrink) | `freq` (after shrink) | `max_len` | Current Window |
| :----: | :-----: | :-----------: | :--------------------: | :----------------------: | :----------------------: | :--------------------: | :-------: | :------------- |
| 0      | -       | -             | {}                     | -                        | -                        | {}                     | 0         | []             |
| 0      | 0       | 1             | {1:1}                  | False                    | -                        | {1:1}                  | 1         | [1]            |
| 0      | 1       | 2             | {1:1, 2:1}             | False                    | -                        | {1:1, 2:1}             | 2         | [1,2]          |
| 0      | 2       | 3             | {1:1, 2:1, 3:1}        | False                    | -                        | {1:1, 2:1, 3:1}        | 3         | [1,2,3]        |
| 0      | 3       | 1             | {1:2, 2:1, 3:1}        | False                    | -                        | {1:2, 2:1, 3:1}        | 4         | [1,2,3,1]      |
| 0      | 4       | 2             | {1:2, 2:2, 3:1}        | False                    | -                        | {1:2, 2:2, 3:1}        | 5         | [1,2,3,1,2]    |
| 0      | 5       | 3             | {1:2, 2:2, 3:2}        | False                    | -                        | {1:2, 2:2, 3:2}        | 6         | [1,2,3,1,2,3]  |
| 0      | 6       | 1             | {1:3, 2:2, 3:2}        | True (3 > 2)             | 1                        | {1:2, 2:2, 3:2}        | 6         | [2,3,1,2,3,1]  |
| 1      | 6       | 1             | {1:3, 2:2, 3:2}        | False (after shrink)     | -                        | {1:2, 2:2, 3:2}        | 6         | [2,3,1,2,3,1]  |
| 1      | 7       | 2             | {1:2, 2:3, 3:2}        | True (3 > 2)             | 2                        | {1:2, 2:2, 3:2}        | 6         | [3,1,2,3,1,2]  |
| 2      | 7       | 2             | {1:2, 2:3, 3:2}        | False (after shrink)     | -                        | {1:2, 2:2, 3:2}        | 6         | [3,1,2,3,1,2]  |

Final `max_len`: 6

## Complexity
*   **Time Complexity:** O(N), where N is the length of `nums`. Both the `left` and `right` pointers traverse the array at most once. Each element is added to the hash map once and removed from it at most once. Hash map operations (insertion, deletion, lookup) take O(1) on average.
*   **Space Complexity:** O(D), where D is the number of distinct elements in `nums`. In the worst case, all elements are distinct, so D can be N. Thus, O(N) in the worst case for storing frequencies in the hash map.

## Edge Cases
*   **`k = 1`**: Each element can appear at most once. The window will shrink aggressively. For `[1,2,1,2], k=1`, the output will be 2 (`[1,2]` or `[2,1]`). Our solution handles this by shrinking `left` whenever a duplicate is encountered.
*   **`k = nums.length`**: This means there's no restriction on frequency, as `k` is large enough to accommodate any number of occurrences. The `while freq[current_num] > k` condition will never be met, so `left` will always remain at `0`. The `max_len` will correctly become `len(nums)`.
*   **All elements are the same**: `nums = [5,5,5,5,5], k = 3`. The window will expand until `freq[5]` becomes 4. Then `left` will move forward until `freq[5]` is 3 again. The `max_len` will be `k`. Our solution correctly handles this.
*   **Single element array**: `nums = [7], k = 1`. `max_len` will be 1. Correct.

## Solution

```python
import collections
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0
        # Use a hash map (dictionary) to store frequencies of elements in the current window.
        # collections.defaultdict(int) is convenient as it automatically initializes new keys with 0.
        freq = collections.defaultdict(int)

        # Iterate with the 'right' pointer to expand the window
        for right in range(len(nums)):
            current_num = nums[right]
            
            # Add the current element to the window and update its frequency
            freq[current_num] += 1

            # If the frequency of the current_num exceeds k,
            # the window is no longer "good". We need to shrink it from the left.
            while freq[current_num] > k:
                # Get the element at the 'left' pointer
                num_to_remove = nums[left]
                
                # Decrement its frequency as it's leaving the window
                freq[num_to_remove] -= 1
                
                # Move the 'left' pointer forward to shrink the window
                left += 1
            
            # At this point, the window [left, right] is guaranteed to be "good"
            # (i.e., all elements have frequency <= k).
            # Calculate its length and update max_len if it's longer.
            max_len = max(max_len, right - left + 1)
        
        return max_len

```

## Why This Works
This sliding window approach works because it maintains a crucial invariant: the window `nums[left...right]` is always the *longest possible good subarray ending at `right`*. When `right` expands, we add `nums[right]`. If this addition violates the `k` frequency constraint for `nums[right]`, we *must* shrink the window from `left` until `nums[right]` (and by extension, all other elements in the window) satisfies the constraint again. By doing so, we ensure that `left` is always at the leftmost possible position for a good subarray ending at `right`. Thus, `right - left + 1` correctly gives the length of the longest good subarray ending at `right`, and tracking the maximum of these lengths guarantees finding the overall longest good subarray.

---
<sub>Generated 2026-08-12 03:06 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
