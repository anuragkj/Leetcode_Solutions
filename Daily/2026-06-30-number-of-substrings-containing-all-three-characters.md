# [1358] Number of Substrings Containing All Three Characters

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-06-30 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)

**Topics:** Hash Table, String, Sliding Window

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).

Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".

Example 3:

Input: s = "abc"
Output: 1

Constraints:

- 3 <= s.length <= 5 x 10^4

- s only consists of a, b or c characters.

**Examples / sample tests:**

```
"abcabc"
"aaacb"
"abc"
```

---

## Problem Summary
Given a string `s` composed only of 'a', 'b', and 'c', the task is to count how many substrings contain at least one occurrence of each of these three characters.

## Intuition
A brute-force approach would involve checking every possible substring, which is too slow for the given constraints (O(N^2) substrings, each check taking O(N) or O(1) with a frequency map, leading to O(N^3) or O(N^2) total). We need a more efficient way.

The key observation is that if a substring `s[left...right]` contains all three characters ('a', 'b', 'c'), then any substring `s[left...k]` where `k >= right` will *also* contain all three characters. This is because extending a valid substring can only add more characters, not remove them. This property is a strong indicator for a **sliding window** approach.

We can use two pointers, `left` and `right`, to define our current window. We expand the `right` pointer, adding characters to the window. Once the window `s[left...right]` becomes valid (i.e., contains 'a', 'b', and 'c'), we know that all substrings starting at `left` and ending at `right` or *anywhere after* `right` (up to the end of the string) are also valid. The number of such substrings is `len(s) - right`. We add this quantity to our total count. After counting, we then try to shrink the window from the `left` by removing `s[left]` and incrementing `left`. We continue shrinking `left` as long as the window remains valid, counting `len(s) - right` each time. This process ensures we count all valid substrings efficiently and without duplicates.

## Approach
We will use a **sliding window** technique with two pointers, `left` and `right`, and a frequency array to keep track of character counts within the window.

1.  **Initialization**:
    *   Initialize `n` as the length of the input string `s`.
    *   Initialize `left = 0` (the left pointer of the window).
    *   Initialize `count = 0` (to store the total number of valid substrings).
    *   Initialize a frequency array `freq = [0, 0, 0]` to store counts of 'a', 'b', and 'c' respectively. `freq[0]` for 'a', `freq[1]` for 'b', `freq[2]` for 'c'.

2.  **Expand Window (Right Pointer)**:
    *   Iterate `right` from `0` to `n - 1`:
        *   Add the character `s[right]` to the current window. Increment its count in `freq`. We can map 'a' to index 0, 'b' to 1, 'c' to 2 using `ord(s[right]) - ord('a')`.

3.  **Shrink Window (Left Pointer) and Count Substrings**:
    *   **While** the current window `s[left...right]` is valid (i.e., `freq[0] > 0`, `freq[1] > 0`, and `freq[2] > 0`):
        *   The substring `s[left...right]` is valid. Because of the "at least one occurrence" property, any substring starting at `left` and ending at `right` or *any index after `right`* (up to `n-1`) will also be valid.
        *   The number of such valid substrings is `n - right`. Add this value to `count`.
        *   To find the next potential valid window, we try to shrink the window from the left. Decrement the count of `s[left]` in `freq`.
        *   Increment `left` by 1.

4.  **Return Result**:
    *   After the `right` pointer has traversed the entire string, `count` will hold the total number of valid substrings. Return `count`.

## Visualization

Let's trace `s = "abcabc"` with `N = 6`.
`left` and `right` define the window `[left...right]`. `freq` stores counts of 'a', 'b', 'c'.

```
s = "a b c a b c"
    0 1 2 3 4 5  (indices)

Initial: left=0, count=0, freq=[0,0,0]

right=0, s[0]='a':
  freq=[1,0,0]
  Window: [a]
  Not valid (no 'b', 'c')

right=1, s[1]='b':
  freq=[1,1,0]
  Window: [ab]
  Not valid (no 'c')

right=2, s[2]='c':
  freq=[1,1,1]
  Window: [abc]
  Valid!
  count += (N - right) = (6 - 2) = 4
    (Substrings: "abc", "abca", "abcab", "abcabc")
  Shrink left: s[0]='a' removed. freq=[0,1,1]. left=1
  Window: a[bc]
  Not valid (no 'a')

right=3, s[3]='a':
  freq=[1,1,1]
  Window: a[bca]
  Valid!
  count += (N - right) = (6 - 3) = 3. Total count = 4 + 3 = 7
    (Substrings: "bca", "bcab", "bcabc")
  Shrink left: s[1]='b' removed. freq=[1,0,1]. left=2
  Window: ab[ca]
  Not valid (no 'b')

right=4, s[4]='b':
  freq=[1,1,1]
  Window: ab[cab]
  Valid!
  count += (N - right) = (6 - 4) = 2. Total count = 7 + 2 = 9
    (Substrings: "cab", "cabc")
  Shrink left: s[2]='c' removed. freq=[1,1,0]. left=3
  Window: abc[ab]
  Not valid (no 'c')

right=5, s[5]='c':
  freq=[1,1,1]
  Window: abc[abc]
  Valid!
  count += (N - right) = (6 - 5) = 1. Total count = 9 + 1 = 10
    (Substring: "abc")
  Shrink left: s[3]='a' removed. freq=[0,1,1]. left=4
  Window: abca[bc]
  Not valid (no 'a')

End of string. Final count = 10.
```

## Dry Run
Let's walk through Example 1: `s = "abcabc"`

`n = 6`, `left = 0`, `count = 0`, `freq = [0, 0, 0]`

| `right` | `s[right]` | `freq` (after add) | `isValid?` (`freq[0]>0 && freq[1]>0 && freq[2]>0`) | `count` (before add) | `add (n - right)` | `count` (after add) | `s[left]` (removed) | `freq` (after remove) | `left` |
| :------ | :--------- | :----------------- | :-------------------------------------------------- | :------------------- | :---------------- | :------------------ | :------------------ | :-------------------- | :----- |
| 0       | 'a'        | `[1,0,0]`          | No                                                  | 0                    | 0                 | 0                   | -                   | `[1,0,0]`             | 0      |
| 1       | 'b'        | `[1,1,0]`          | No                                                  | 0                    | 0                 | 0                   | -                   | `[1,1,0]`             | 0      |
| 2       | 'c'        | `[1,1,1]`          | Yes                                                 | 0                    | `(6-2)=4`         | 4                   | 'a'                 | `[0,1,1]`             | 1      |
| 3       | 'a'        | `[1,1,1]`          | Yes                                                 | 4                    | `(6-3)=3`         | 7                   | 'b'                 | `[1,0,1]`             | 2      |
| 4       | 'b'        | `[1,1,1]`          | Yes                                                 | 7                    | `(6-4)=2`         | 9                   | 'c'                 | `[1,1,0]`             | 3      |
| 5       | 'c'        | `[1,1,1]`          | Yes                                                 | 9                    | `(6-5)=1`         | 10                  | 'a'                 | `[0,1,1]`             | 4      |

Final Result: `count = 10`.

## Complexity
*   **Time Complexity**: O(N). Both the `left` and `right` pointers traverse the string at most once. Each character is added to the frequency map once (by `right`) and removed from it at most once (by `left`). All operations inside the loops are O(1).
*   **Space Complexity**: O(1). The frequency array `freq` stores counts for only 3 characters ('a', 'b', 'c'), so its size is constant regardless of the input string length.

## Edge Cases
*   **Smallest valid input**: `s = "abc"`. The solution correctly identifies `s[0...2]` as valid, adds `(3-2)=1` to count, and returns 1.
*   **String with many repeated characters**: `s = "aaacb"`. The solution handles this by incrementing `freq['a']` multiple times. When `right` reaches 'b', the window `s[0...4]` becomes valid. The `while` loop then correctly shrinks `left` three times, counting `(5-4)=1` for each valid starting position (`s[0...4]`, `s[1...4]`, `s[2...4]`), resulting in a total count of 3.
*   **String where 'a', 'b', 'c' appear far apart**: The sliding window naturally expands until all characters are present, then counts. The distance between characters doesn't affect the logic, only how quickly the window becomes valid.

## Solution

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        # freq[0] for 'a', freq[1] for 'b', freq[2] for 'c'
        freq = [0, 0, 0] 
        
        left = 0
        count = 0
        
        # Iterate with the right pointer to expand the window
        for right in range(n):
            # Add the current character s[right] to the window's frequency count
            # ord(char) - ord('a') maps 'a'->0, 'b'->1, 'c'->2
            freq[ord(s[right]) - ord('a')] += 1
            
            # While the current window s[left...right] contains at least one of each character
            # (i.e., all counts in freq are greater than 0)
            while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                # This window s[left...right] is valid.
                # Any substring starting at 'left' and ending at 'right' or any index
                # further to the right (up to n-1) will also be valid.
                # The number of such substrings is (n - 1) - right + 1 = n - right.
                # We add this to our total count.
                count += (n - right)
                
                # Now, shrink the window from the left to find new valid substrings
                # starting at a later position.
                freq[ord(s[left]) - ord('a')] -= 1
                left += 1
                
        return count

```

## Why This Works
This sliding window approach works because of the "at least one occurrence" condition. When `s[left...right]` is the *first* window ending at `right` that contains all three characters, we know that all substrings `s[left...k]` where `k` ranges from `right` to `n-1` are also valid. By adding `(n - right)` to `count`, we efficiently account for all these substrings. Then, by shrinking the window from the `left` (incrementing `left` and decrementing `s[left]`'s count), we are effectively looking for the *next* distinct starting position `left'` for which `s[left'...right]` (or `s[left'...right']` for some `right'`) becomes valid. This process ensures that every valid substring is counted exactly once: it's counted when its leftmost possible starting position `left` forms a valid window with some `right` pointer.

---
<sub>Generated 2026-06-30 17:02 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
