# [3886] Sum of Sortable Integers

**Difficulty:** Hard &nbsp;·&nbsp; **Daily Challenge:** 2026-10-20 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/sum-of-sortable-integers/)

**Topics:** Array, Math, Sorting, Enumeration

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given an integer array nums of length n.

An integer k is called sortable if k divides n and you can sort nums in non-decreasing order by sequentially performing the following operations:

- Partition nums into consecutive subarrays of length k.

- Cyclically rotate each subarray independently any number of times to the left or to the right.

Return an integer denoting the sum of all possible sortable integers k.

Example 1:

Input: nums = [3,1,2]

Output: 3

Explanation:​​​​​​​

- For n = 3, possible divisors are 1 and 3.

- For k = 1: each subarray has one element. No rotation can sort the array.

- For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.

- Only k = 3 is sortable. Hence, the answer is 3.

Example 2:

Input: nums = [7,6,5]

Output: 0

Explanation:

- For n = 3, possible divisors are 1 and 3.

- For k = 1: each subarray has one element. No rotation can sort the array.

- For k = 3: the single subarray [7, 6, 5] cannot be rotated into non-decreasing order.

- No k is sortable. Hence, the answer is 0.

Example 3:

Input: nums = [5,8]

Output: 3

Explanation:​​​​​​​

- For n = 2, possible divisors are 1 and 2.

- Since [5, 8] is already sorted, every divisor is sortable. Hence, the answer is 1 + 2 = 3.

Constraints:

- 1 <= n == nums.length <= 10^5

- 1 <= nums[i] <= 10^5

**Examples / sample tests:**

```
[3,1,2]
[7,6,5]
[5,8]
```

---

## Problem Summary
Given an array `nums` of length `n`, we need to find all integers `k` that divide `n` and allow `nums` to be sorted. Sorting is achieved by partitioning `nums` into `n/k` consecutive subarrays of length `k`, and then cyclically rotating each subarray independently to match its corresponding segment in the globally sorted version of `nums`. The goal is to return the sum of all such "sortable" `k`.

## Intuition
The problem asks us to check a property for several possible values of `k`. The first key observation, explicitly stated, is that `k` must be a **divisor of `n`**. This significantly limits the number of `k` values we need to check.

For a given `k`, the array `nums` is conceptually split into `n/k` blocks. Let `s` be the globally sorted version of `nums`. Then `s` is also conceptually split into `n/k` blocks. For `k` to be sortable, **each block** `nums[i*k : (i+1)*k]` must be transformable into `s[i*k : (i+1)*k]` by cyclic rotation.

So, the core of the problem boils down to: how to efficiently check if one list (`block_A`) can be cyclically rotated to become another list (`block_B`), assuming they have the same length `k`?
1.  **Anagram Check**: If `block_A` can be rotated into `block_B`, they must contain the exact same elements with the exact same frequencies. In other words, they must be **anagrams** of each other. We can check this by comparing their sorted versions or using frequency counts (e.g., `collections.Counter`).
2.  **Cyclic Check**: If they are anagrams, we need to verify if `block_B` is indeed a cyclic shift of `block_A`. A common trick for this is to concatenate `block_A` with itself (`block_A + block_A`) and then check if `block_B` appears as a **sublist** within this doubled list. For example, if `block_A = [3,1,2]`, `block_A + block_A = [3,1,2,3,1,2]`. If `block_B = [1,2,3]`, we can see `[1,2,3]` as a sublist starting at index 1.
    Checking for a sublist efficiently for lists of integers requires algorithms like **KMP** or **polynomial hashing** to achieve `O(k)` time complexity, as a naive check would be `O(k^2)`. Given `n` up to `10^5`, `k` can also be `10^5`, so `O(k^2)` per block is too slow. Polynomial hashing is generally simpler to implement for this purpose.

## Approach
The optimal algorithm involves iterating through divisors, partitioning the array, and using polynomial hashing for efficient cyclic rotation checks.

1.  **Precompute Sorted Array**: Create `sorted_nums = sorted(nums)`. This is the target state for the entire array.
2.  **Find Divisors**: Iterate from `1` up to `sqrt(n)` to find all divisors of `n`. Store them in a list. For each `i` that divides `n`, both `i` and `n/i` are divisors.
3.  **Initialize Hashing Parameters**: Set up two pairs of `(prime_base, prime_modulus)` for polynomial hashing. Precompute powers of these bases modulo their respective moduli up to `n`. This is a one-time setup.
4.  **Iterate Through Divisors `k`**: For each `k` found in step 2:
    a.  Assume `k` is sortable (`is_k_sortable = True`).
    b.  **Iterate Through Blocks**: Loop `block_idx` from `0` to `n/k - 1`.
        i.  Extract `current_block = nums[block_idx * k : (block_idx + 1) * k]`.
        ii. Extract `target_block = sorted_nums[block_idx * k : (block_idx + 1) * k]`.
        iii. **Check Cyclic Rotation (`_check_cyclic_rotation` function)**:
            1.  **Anagram Check**: Use `collections.Counter(current_block) == collections.Counter(target_block)`. If they are not anagrams, return `False`.
            2.  **Base Cases**: If `k=0` (shouldn't happen with `k>=1`) or `k=1`, and they are anagrams, they are trivially cyclic rotations. Return `True`.
            3.  **Compute Target Hashes**: Calculate two polynomial hashes for `target_block` using the two `(prime_base, prime_modulus)` pairs.
            4.  **Compute Initial Current Block Hashes**: Calculate two polynomial hashes for `current_block` (representing `current_block[0:k]`).
            5.  **Direct Match Check**: If both `current_block` hashes match `target_block` hashes, perform a direct list comparison (`current_block == target_block`) to avoid hash collisions. If they match, return `True`.
            6.  **Rolling Hash for Rotations**: Iterate `j` from `1` to `k-1` (representing `j` left rotations). In each step, update the two hashes of `current_block` using a rolling hash technique:
                `new_hash = (old_hash - A[j-1] * P^(k-1)) * P + A[j-1]` (all modulo `M`).
                This effectively removes the first element `A[j-1]` and appends it to the end.
            7.  **Check Rotated Hashes**: If both updated hashes match `target_block` hashes, perform a direct list comparison (`current_block[j:] + current_block[:j] == target_block`). If they match, return `True`.
            8.  If no rotation matches, return `False`.
    c.  If `_check_cyclic_rotation` returns `False` for any block, set `is_k_sortable = False` and break from the block loop.
    d.  If `is_k_sortable` remains `True` after checking all blocks for a given `k`, add `k` to `total_sortable_k`.
5.  **Return Sum**: After checking all divisors, return `total_sortable_k`.

## Visualization
Let's visualize the partitioning and cyclic rotation check for `nums = [3,1,2,4,5,6]` and `k=3`.

```
Original Array (nums):
[ 3,  1,  2,   4,  5,  6 ]
  ^----------^   ^----------^
  Block 0        Block 1

Sorted Array (sorted_nums):
[ 1,  2,  3,   4,  5,  6 ]
  ^----------^   ^----------^
  Target Block 0 Target Block 1

Checking k=3:

--- Block 0 ---
current_block: [3, 1, 2]
target_block:  [1, 2, 3]

1. Anagram Check:
   Counter([3,1,2]) == Counter([1,2,3])  -> True (both have one 1, one 2, one 3)

2. Cyclic Check (using rolling hash):
   - Initial state (0 rotations):
     [3, 1, 2]  (hashes computed)
     Is hash([3,1,2]) == hash([1,2,3])? No.
   - 1st rotation (1 left shift):
     Remove 3 from front, add 3 to back -> [1, 2, 3] (hashes updated)
     Is hash([1,2,3]) == hash([1,2,3])? Yes!
     Verify: [1,2,3] == [1,2,3]? Yes.
     Block 0 is sortable.

--- Block 1 ---
current_block: [4, 5, 6]
target_block:  [4, 5, 6]

1. Anagram Check:
   Counter([4,5,6]) == Counter([4,5,6])  -> True

2. Cyclic Check:
   - Initial state (0 rotations):
     [4, 5, 6]  (hashes computed)
     Is hash([4,5,6]) == hash([4,5,6])? Yes!
     Verify: [4,5,6] == [4,5,6]? Yes.
     Block 1 is sortable.

Since all blocks are sortable, k=3 is a sortable integer.
```

## Dry Run
Let's trace Example 1: `nums = [3,1,2]`

**Initial Setup:**
- `n = 3`
- `sorted_nums = [1,2,3]`
- `total_sortable_k = 0`
- `_initialize_powers()` is called once.

**Find Divisors of `n=3`:**
- `i=1`: `3 % 1 == 0`. Add `1`. `1*1 != 3`. Add `3//1 = 3`.
- `divisors = [1, 3]`

**Iterate `k` in `divisors`:**

**1. `k = 1`:**
   - `is_k_sortable = True`
   - **Block `block_idx = 0`:**
     - `start = 0, end = 1`
     - `current_block = nums[0:1] = [3]`
     - `target_block = sorted_nums[0:1] = [1]`
     - Call `_check_cyclic_rotation([3], [1], 1)`:
       - `collections.Counter([3])` is `{3: 1}`.
       - `collections.Counter([1])` is `{1: 1}`.
       - `Counter([3]) != Counter([1])` is `True`.
       - Returns `False`.
   - `is_k_sortable` becomes `False`. Break from block loop.
   - `k=1` is **not** sortable.

**2. `k = 3`:**
   - `is_k_sortable = True`
   - **Block `block_idx = 0`:**
     - `start = 0, end = 3`
     - `current_block = nums[0:3] = [3,1,2]`
     - `target_block = sorted_nums[0:3] = [1,2,3]`
     - Call `_check_cyclic_rotation([3,1,2], [1,2,3], 3)`:
       - `collections.Counter([3,1,2])` is `{3:1, 1:1, 2:1}`.
       - `collections.Counter([1,2,3])` is `{1:1, 2:1, 3:1}`.
       - `Counter`s are equal.
       - `k=3`, not `1`.
       - Compute `hash_B1`, `hash_B2` for `[1,2,3]`.
       - Compute `current_hash1`, `current_hash2` for `[3,1,2]`.
       - `current_hash1 == hash_B1` (and `hash_B2`)? No, `[3,1,2]` is not `[1,2,3]`.
       - **Loop `j` from `1` to `k-1` (i.e., `j=1, 2`):**
         - **`j = 1` (1 left rotation):**
           - `A[j-1]` is `A[0] = 3`.
           - Update `current_hash1`, `current_hash2` by removing `3` from front and adding `3` to back.
           - The hashes now represent the list `[1,2,3]` (conceptually `[3,1,2]` rotated once left).
           - `current_hash1 == hash_B1` (and `hash_B2`)? Yes.
           - Verify: `A[j:] + A[:j]` is `nums[1:] + nums[:1] = [1,2] + [3] = [1,2,3]`.
           - `[1,2,3] == [1,2,3]`? Yes.
           - Returns `True`.
     - `is_k_sortable` remains `True`.
   - Block loop finishes.
   - `k=3` is sortable. `total_sortable_k = 0 + 3 = 3`.

**Final Result:** `3`

## Complexity
-   **Time Complexity**: `O(N log N + |D| * N)`
    -   `sorted(nums)` takes `O(N log N)`.
    -   Finding divisors takes `O(sqrt(N))`. The number of divisors `|D|` is at most `~128` for `N=10^5`.
    -   For each divisor `k`:
        -   There are `n/k` blocks.
        -   Each block involves slicing (`O(k)`) and calling `_check_cyclic_rotation`.
        -   `_check_cyclic_rotation` takes `O(k)` amortized time (due to `Counter` and rolling hash; direct list comparison `O(k)` is rarely hit because of two hash functions).
        -   Total time for one `k` is `(n/k) * O(k) = O(n)`.
    -   Summing over all divisors: `|D| * O(N)`.
    -   Overall: `O(N log N + |D| * N)`. With `N=10^5` and `|D|=128`, this is roughly `10^5 * 17 + 128 * 10^5` which is approximately `1.45 * 10^7` operations, well within typical time limits.

-   **Space Complexity**: `O(N + MAX_N)`
    -   `sorted_nums` takes `O(N)` space.
    -   `_pow_P1` and `_pow_P2` arrays take `O(MAX_N)` space, where `MAX_N` is the maximum possible `n` (10^5).
    -   `divisors` list takes `O(|D|)` space.
    -   `current_block`, `target_block` slices and `collections.Counter` objects take `O(k)` space.
    -   Overall: `O(N + MAX_N)` which simplifies to `O(N)` since `MAX_N` is a constant upper bound for `N`.

## Edge Cases
-   **`n=1`**: `nums=[5]`. Divisor `k=1`. `current_block=[5]`, `target_block=[5]`. `_check_cyclic_rotation` returns `True` (anagrams, `k=1` base case). Sum is `1`. Correct.
-   **`nums` already sorted**: `nums=[1,2,3]`. `sorted_nums=[1,2,3]`.
    -   `k=1`: Each `[x]` vs `[x]` is sortable.
    -   `k=3`: `[1,2,3]` vs `[1,2,3]` is sortable (0 rotations).
    -   Sum `1+3=4`. Correct.
-   **All elements are the same**: `nums=[5,5,5]`. `sorted_nums=[5,5,5]`.
    -   `k=1`: Each `[5]` vs `[5]` is sortable.
    -   `k=3`: `[5,5,5]` vs `[5,5,5]` is sortable.
    -   Sum `1+3=4`. Correct.
-   **`nums` cannot be sorted for any `k`**: `nums=[7,6,5]`. `sorted_nums=[5,6,7]`.
    -   `k=1`: `[7]` vs `[5]` (anagram check fails).
    -   `k=3`: `[7,6,5]` vs `[5,6,7]` (anagram check passes). Rolling hash check: `[7,6,5]` cannot rotate to `[5,6,7]`.
    -   Sum `0`. Correct.
The solution handles these cases correctly due to the robust anagram and cyclic rotation checks.

## Solution

```python
import collections

class Solution:
    # Use two hash functions to minimize collision probability for polynomial hashing.
    # P1, P2 are prime bases, chosen to be larger than the maximum possible value of nums[i] (10^5).
    # M1, M2 are large prime moduli.
    P1 = 100003 
    M1 = 1_000_000_007 
    P2 = 1000003 
    M2 = 1_000_000_009 

    # Precompute powers of P1 and P2 up to MAX_N to avoid repeated calculations.
    # MAX_N is the maximum possible length of nums (10^5) from constraints.
    _MAX_N = 100005 
    _pow_P1 = [1] * (_MAX_N + 1)
    _pow_P2 = [1] * (_MAX_N + 1)
    _initialized = False # Flag to ensure powers are computed only once

    @classmethod
    def _initialize_powers(cls):
        """
        Initializes precomputed powers for hashing. This method is called once
        to set up the static class variables.
        """
        if not cls._initialized:
            for i in range(1, cls._MAX_N + 1):
                cls._pow_P1[i] = (cls._pow_P1[i-1] * cls.P1) % cls.M1
                cls._pow_P2[i] = (cls._pow_P2[i-1] * cls.P2) % cls.M2
            cls._initialized = True

    def sortableIntegers(self, nums: list[int]) -> int:
        # Ensure hashing powers are initialized before any calculations.
        Solution._initialize_powers()

        n = len(nums)
        # Create the target sorted version of the array.
        sorted_nums = sorted(nums) 
        total_sortable_k = 0

        # Step 1: Find all positive integer divisors of n.
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n: # Avoid adding the same divisor twice for perfect squares
                    divisors.append(n // i)
        
        # Step 2: For each divisor k, check if it makes the array sortable.
        for k in divisors:
            is_k_sortable = True
            # Partition nums into n/k consecutive subarrays (blocks).
            for block_idx in range(n // k):
                start = block_idx * k
                end = (block_idx + 1) * k
                current_block = nums[start:end]
                target_block = sorted_nums[start:end]

                # Step 3: Check if the current_block can be cyclically rotated
                # to match the target_block.
                if not self._check_cyclic_rotation(current_block, target_block, k):
                    is_k_sortable = False
                    break # If one block fails, this k is not sortable, move to the next divisor.
            
            # If all blocks for this k were sortable, add k to the total sum.
            if is_k_sortable:
                total_sortable_k += k
        
        return total_sortable_k

    def _check_cyclic_rotation(self, A: list[int], B: list[int], k: int) -> bool:
        """
        Determines if list A can be cyclically rotated to become list B.
        Both lists are assumed to have length k.
        """
        if k == 0: 
            return True # Empty lists are trivially cyclic rotations of each other.

        # Optimization 1: Anagram check. If A and B are not anagrams,
        # no rotation can make them equal. O(k) using Counter.
        if collections.Counter(A) != collections.Counter(B):
            return False

        # Optimization 2: If k=1, and they are anagrams, they must be identical.
        # So, they are trivially sortable.
        if k == 1:
            return True

        # Compute target hashes for list B using both hash functions.
        hash_B1 = 0
        hash_B2 = 0
        for i in range(k):
            hash_B1 = (hash_B1 + B[i] * Solution._pow_P1[k - 1 - i]) % Solution.M1
            hash_B2 = (hash_B2 + B[i] * Solution._pow_P2[k - 1 - i]) % Solution.M2

        # Compute initial window hashes for list A (representing 0 rotations).
        current_hash1 = 0
        current_hash2 = 0
        for i in range(k):
            current_hash1 = (current_hash1 + A[i] * Solution._pow_P1[k - 1 - i]) % Solution.M1
            current_hash2 = (current_hash2 + A[i] * Solution._pow_P2[k - 1 - i]) % Solution.M2

        # Check if A itself is already B (0 rotations).
        if current_hash1 == hash_B1 and current_hash2 == hash_B2:
            # Direct comparison to verify and avoid rare hash collisions.
            if A == B: 
                return True

        # Perform rolling hash for k-1 possible cyclic rotations.
        # In each step, we simulate moving the first element to the end.
        for j in range(1, k): # j represents the number of left rotations performed.
            # Update hash1:
            # 1. Subtract the contribution of the element leaving the front (A[j-1]).
            current_hash1 = (current_hash1 - A[j-1] * Solution._pow_P1[k-1]) % Solution.M1
            current_hash1 = (current_hash1 + Solution.M1) % Solution.M1 # Ensure positive result.
            # 2. Shift all remaining elements left by multiplying by P1.
            current_hash1 = (current_hash1 * Solution.P1) % Solution.M1
            # 3. Add the element that wraps around to the end (which is A[j-1]).
            current_hash1 = (current_hash1 + A[j-1]) % Solution.M1

            # Repeat the same process for hash2.
            current_hash2 = (current_hash2 - A[j-1] * Solution._pow_P2[k-1]) % Solution.M2
            current_hash2 = (current_hash2 + Solution.M2) % Solution.M2 
            current_hash2 = (current_hash2 * Solution.P2) % Solution.M2
            current_hash2 = (current_hash2 + A[j-1]) % Solution.M2 
            
            # If both hashes match, a potential cyclic rotation is found.
            if current_hash1 == hash_B1 and current_hash2 == hash_B2:
                # Verify with direct comparison. This O(k) check is rarely executed
                # due to the very low probability of collision with two hash functions.
                if A[j:] + A[:j] == B: 
                    return True
                    
        return False # No cyclic rotation of A matches B.

```

## Why This Works
The solution works by systematically checking all valid `k` values (divisors of `n`) and for each `k`, verifying if every block can be sorted. The core of the verification lies in the `_check_cyclic_rotation` function. This function correctly identifies if `block_A` can be rotated into `block_B` by first ensuring they are anagrams (a necessary condition for rotation) and then efficiently checking all `k` possible cyclic shifts using a **rolling polynomial hash**. The use of two distinct hash functions significantly reduces the probability of hash collisions, making the amortized time complexity of the `_check_cyclic_rotation` function `O(k)`. This efficiency is crucial because `k` can be as large as `n`, and the overall algorithm needs to process `|D| * N` operations, where `|D|` is the number of divisors of `N`.

---
<sub>Generated 2026-10-20 05:11 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
