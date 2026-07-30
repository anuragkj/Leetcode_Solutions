# [3014] Minimum Number of Pushes to Type Word I

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-07-30 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/)

**Topics:** Math, String, Greedy

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a string word containing distinct lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.

Example 1:

Input: word = "abcde"
Output: 5
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.

Example 2:

Input: word = "xycdefghij"
Output: 12
Explanation: The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> two pushes on key 2
"c" -> one push on key 3
"d" -> two pushes on key 3
"e" -> one push on key 4
"f" -> one push on key 5
"g" -> one push on key 6
"h" -> one push on key 7
"i" -> one push on key 8
"j" -> one push on key 9
Total cost is 1 + 2 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 = 12.
It can be shown that no other mapping can provide a lower cost.

Constraints:

- 1 <= word.length <= 26

- word consists of lowercase English letters.

- All letters in word are distinct.

**Examples / sample tests:**

```
"abcde"
"xycdefghij"
```

---

## Problem Summary
You are given a string of distinct lowercase English letters. Your goal is to map these letters to a telephone keypad (keys 2-9, 8 keys total) to minimize the total number of pushes required to type the entire word. Typing a letter costs 1 push if it's the first letter mapped to a key, 2 pushes if it's the second, 3 pushes if it's the third, and so on.

## Intuition
To minimize the total number of pushes, we should always try to use the cheapest available "slots" on the keypad first. The cost of typing a letter depends on its position on a key: 1 push for the 1st letter, 2 pushes for the 2nd, 3 pushes for the 3rd, etc.

Since we have 8 keys (2 through 9), we have:
- 8 "slots" that cost **1 push** each (one for each key's first letter).
- 8 "slots" that cost **2 pushes** each (one for each key's second letter).
- 8 "slots" that cost **3 pushes** each (one for each key's third letter).
- And so on.

The core idea is a **greedy approach**: always assign letters to the slots that require the fewest pushes first. We'll fill all the 1-push slots, then all the 2-push slots, then all the 3-push slots, until all letters from `word` are assigned.

## Approach
1.  Initialize `total_pushes` to 0. This will store our final answer.
2.  Get the `num_letters` by finding the length of the input `word`.
3.  Initialize `key_press_count` to 1. This variable represents the current cost (number of pushes) for a letter (e.g., 1 push, then 2 pushes, then 3 pushes).
4.  We have `keys_available_per_level = 8` (since there are 8 keys from 2 to 9). This means there are 8 slots available for 1-push letters, 8 slots for 2-push letters, etc.
5.  Loop while `num_letters` is greater than 0 (meaning we still have letters to assign):
    a.  Calculate `letters_to_assign_this_round`: This is the minimum of the `num_letters` remaining and the `keys_available_per_level` (which is 8). We can't assign more letters than we have, nor more than the 8 slots at the current `key_press_count` level.
    b.  Add the cost for these letters to `total_pushes`: `total_pushes += letters_to_assign_this_round * key_press_count`.
    c.  Update `num_letters`: Subtract the `letters_to_assign_this_round` from `num_letters`.
    d.  Increment `key_press_count`: Move to the next push level (e.g., if we just assigned 1-push letters, next we'll assign 2-push letters).
6.  Once the loop finishes (when `num_letters` becomes 0), return `total_pushes`.

## Visualization

Imagine our keypad slots organized by the number of pushes they require:

```
Keypad Slots (8 keys total):

Cost 1 Push:  [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ]  (8 slots)
              /   /   /   /   /   /   /   /
             K2  K3  K4  K5  K6  K7  K8  K9  (1st letter on each key)

Cost 2 Pushes: [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ]  (8 slots)
               /   /   /   /   /   /   /   /
              K2  K3  K4  K5  K6  K7  K8  K9  (2nd letter on each key)

Cost 3 Pushes: [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ]  (8 slots)
               /   /   /   /   /   /   /   /
              K2  K3  K4  K5  K6  K7  K8  K9  (3rd letter on each key)

... and so on.
```

Our greedy approach fills these slots from top to bottom (cheapest to most expensive) and left to right (filling all 8 slots at a given cost level before moving to the next).

For `word = "xycdefghij"` (10 letters):

1.  **Cost 1 Push:** We have 10 letters. We fill all 8 slots.
    `[x] [y] [c] [d] [e] [f] [g] [h]` (8 letters assigned, 2 remaining)
    Total pushes: `8 * 1 = 8`
2.  **Cost 2 Pushes:** We have 2 letters remaining. We fill 2 slots.
    `[i] [j] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ] [ _ ]` (2 letters assigned, 0 remaining)
    Total pushes: `8 + (2 * 2) = 12`

All letters assigned. Final total pushes = 12.

## Dry Run

Let's trace `word = "xycdefghij"`.
`num_letters = 10`
`total_pushes = 0`
`key_press_count = 1`
`keys_available_per_level = 8`

| `num_letters` | `key_press_count` | `letters_to_assign_this_round` | `total_pushes` (calculation) | `total_pushes` (new value) |
| :------------ | :---------------- | :----------------------------- | :--------------------------- | :------------------------- |
| 10            | 1                 | `min(10, 8)` = 8               | `0 + (8 * 1)`                | 8                          |
| `10 - 8` = 2  | `1 + 1` = 2       | -                              | -                            | 8                          |
| 2             | 2                 | `min(2, 8)` = 2                | `8 + (2 * 2)`                | 12                         |
| `2 - 2` = 0   | `2 + 1` = 3       | -                              | -                            | 12                         |

The loop terminates because `num_letters` is now 0.
Final result: `total_pushes = 12`.

## Complexity
*   **Time Complexity:** O(1). The maximum length of `word` is 26. Since we assign 8 letters per round, the loop will run at most `ceil(26 / 8) = 4` times. This is a constant number of operations, independent of the input size in a practical sense.
*   **Space Complexity:** O(1). We only use a few integer variables to store counts and totals, which consume constant memory.

## Edge Cases
*   **`word.length = 1` (e.g., "a"):**
    *   `num_letters = 1`, `key_press_count = 1`.
    *   `letters_to_assign_this_round = min(1, 8) = 1`.
    *   `total_pushes = 0 + (1 * 1) = 1`.
    *   `num_letters` becomes 0. Loop ends. Correct, 1 push.
*   **`word.length = 8` (e.g., "abcdefgh"):**
    *   `num_letters = 8`, `key_press_count = 1`.
    *   `letters_to_assign_this_round = min(8, 8) = 8`.
    *   `total_pushes = 0 + (8 * 1) = 8`.
    *   `num_letters` becomes 0. Loop ends. Correct, 8 pushes.
*   **`word.length = 9` (e.g., "abcdefghi"):**
    *   **Round 1:** `num_letters = 9`, `key_press_count = 1`. `letters_to_assign_this_round = min(9, 8) = 8`. `total_pushes = 8`. `num_letters` becomes 1. `key_press_count` becomes 2.
    *   **Round 2:** `num_letters = 1`, `key_press_count = 2`. `letters_to_assign_this_round = min(1, 8) = 1`. `total_pushes = 8 + (1 * 2) = 10`. `num_letters` becomes 0. Loop ends. Correct, 10 pushes.

The solution correctly handles these cases by always prioritizing the cheapest available slots.

## Solution

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        total_pushes = 0
        num_letters = len(word)
        
        # We have 8 keys (2 through 9) available for mapping letters.
        # To minimize pushes, we want to assign letters to positions
        # that require fewer pushes first.
        #
        # There are 8 slots for 1-push letters (1st letter on each of the 8 keys).
        # There are 8 slots for 2-push letters (2nd letter on each of the 8 keys).
        # There are 8 slots for 3-push letters (3rd letter on each of the 8 keys).
        # And so on.
        
        key_press_count = 1 # Represents the current cost (1 push, then 2 pushes, etc.)
        keys_available_per_level = 8 # Number of keys, hence number of slots at each 'push level'
        
        # We continue assigning letters until all letters from the word are placed.
        while num_letters > 0:
            # Determine how many letters can be assigned at the current 'key_press_count' level.
            # This is the minimum of the remaining letters and the 8 slots available at this level.
            letters_to_assign_this_round = min(num_letters, keys_available_per_level)
            
            # Add the pushes for these letters to the total.
            # Each of these letters costs 'key_press_count' pushes.
            total_pushes += letters_to_assign_this_round * key_press_count
            
            # Update the remaining number of letters.
            num_letters -= letters_to_assign_this_round
            
            # Move to the next push level (e.g., from 1 push to 2 pushes, then to 3 pushes).
            key_press_count += 1
            
        return total_pushes

```

## Why This Works
This greedy strategy works because the cost of typing a letter (number of pushes) strictly increases with its position on a key. A 1st position costs 1 push, a 2nd position costs 2 pushes, and so on. By always filling the cheapest available slots first (all 8 one-push slots, then all 8 two-push slots, etc.), we ensure that no letter is assigned to a more expensive slot if a cheaper slot is still available. This guarantees the minimum possible total pushes, as any deviation would involve moving a letter from a cheaper slot to a more expensive one, increasing or maintaining the total cost.

---
<sub>Generated 2026-07-30 03:42 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
