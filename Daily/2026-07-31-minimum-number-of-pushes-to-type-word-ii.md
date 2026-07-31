# [3016] Minimum Number of Pushes to Type Word II

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-07-31 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/)

**Topics:** Hash Table, String, Greedy, Sorting, Counting

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a string word containing lowercase English letters.

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

Input: word = "xyzxyzxyzxyz"
Output: 12
Explanation: The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> one push on key 3
"z" -> one push on key 4
Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
It can be shown that no other mapping can provide a lower cost.
Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.

Example 3:

Input: word = "aabbccddeeffgghhiiiiii"
Output: 24
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
"f" -> one push on key 7
"g" -> one push on key 8
"h" -> two pushes on key 9
"i" -> one push on key 9
Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.
It can be shown that no other mapping can provide a lower cost.

Constraints:

- 1 <= word.length <= 10^5

- word consists of lowercase English letters.

**Examples / sample tests:**

```
"abcde"
"xyzxyzxyzxyz"
"aabbccddeeffgghhiiiiii"
```

---

## Problem Summary
You are given a string `word` and need to remap keys 2-9 on a telephone keypad to minimize the total number of pushes required to type `word`. Each unique letter in `word` must be mapped to exactly one key. The first letter mapped to a key costs 1 push, the second costs 2 pushes, and so on.

## Intuition
The core idea is to be **greedy**. To minimize the total number of pushes, we should always assign characters that appear **most frequently** in the `word` to positions that require **fewer pushes**.

Think about it:
1.  We have 8 keys (2 through 9).
2.  Each key can have multiple letters mapped to it.
3.  The first letter on *any* key costs 1 push.
4.  The second letter on *any* key costs 2 pushes.
5.  The third letter on *any* key costs 3 pushes, and so on.

Since we have 8 keys, we have 8 "slots" that cost 1 push each (one slot on each of the 8 keys). After these 8 slots are filled, we then have another 8 "slots" that cost 2 pushes each (the second letter on each of the 8 keys). This pattern continues.

Therefore, the optimal strategy is:
*   Find the frequency of each unique character in `word`.
*   Sort these characters by their frequencies in **descending order**.
*   Assign the 8 most frequent characters to the 8 "1-push" slots.
*   Assign the next 8 most frequent characters to the 8 "2-push" slots.
*   Assign the next 8 most frequent characters to the 8 "3-push" slots, and so on.

By doing this, we ensure that characters we type more often contribute less to the total push count.

## Approach
1.  **Count Character Frequencies**: First, we need to know how many times each unique character appears in the input `word`. A hash map (like Python's `dict` or `collections.Counter`) is perfect for this.
    *   Example: For `word = "aabbccddeeffgghhiiiiii"`, we'd get `{'a': 2, 'b': 2, ..., 'h': 2, 'i': 6}`.

2.  **Extract and Sort Frequencies**: Get all the frequency counts from our hash map. Then, sort these frequencies in **descending order**. This ensures that we process the most frequent characters first.
    *   Example: From the frequencies above, we'd get `[6, 2, 2, 2, 2, 2, 2, 2, 2]` (the `6` is for 'i', the `2`s are for 'a' through 'h'). The specific character doesn't matter, only its frequency.

3.  **Calculate Total Pushes Greedily**: Iterate through the sorted frequencies. For each frequency `f` at index `i` (0-indexed) in the sorted list:
    *   Determine the **push cost** for this character. Since there are 8 keys, the first 8 characters (indices 0-7) will be assigned to 1 push. The next 8 characters (indices 8-15) will be assigned to 2 pushes, and so on.
    *   The push cost for the character at index `i` can be calculated as `(i // 8) + 1`.
        *   For `i = 0` to `7`, `i // 8` is `0`, so cost is `0 + 1 = 1`.
        *   For `i = 8` to `15`, `i // 8` is `1`, so cost is `1 + 1 = 2`.
        *   And so on.
    *   Multiply this `push_cost` by the character's `frequency` (`f`) and add it to a running `total_pushes`.

4.  **Return Total Pushes**: After iterating through all unique characters, the `total_pushes` will be the minimum possible.

## Visualization

Imagine the 8 keys (2-9) as columns, and the "push count" (1st letter, 2nd letter, etc.) as rows. We fill these slots with the most frequent characters first.

```
Keypad Slots:
----------------------------------------------------------------------------------------------------------------
| Push Cost 1 (1st letter on key) | Push Cost 2 (2nd letter on key) | Push Cost 3 (3rd letter on key) | ...
----------------------------------------------------------------------------------------------------------------
Key 2: | char_1 (freq_1)           | char_9 (freq_9)                 | char_17 (freq_17)               | ...
Key 3: | char_2 (freq_2)           | char_10 (freq_10)               | char_18 (freq_18)               | ...
Key 4: | char_3 (freq_3)           | char_11 (freq_11)               | char_19 (freq_19)               | ...
Key 5: | char_4 (freq_4)           | char_12 (freq_12)               | char_20 (freq_20)               | ...
Key 6: | char_5 (freq_5)           | char_13 (freq_13)               | char_21 (freq_21)               | ...
Key 7: | char_6 (freq_6)           | char_14 (freq_14)               | char_22 (freq_22)               | ...
Key 8: | char_7 (freq_7)           | char_15 (freq_15)               | char_23 (freq_23)               | ...
Key 9: | char_8 (freq_8)           | char_16 (freq_16)               | char_24 (freq_24)               | ...
----------------------------------------------------------------------------------------------------------------
```
Here, `char_1, char_2, ..., char_k` represent the unique characters from `word` sorted by their frequencies (`freq_1 >= freq_2 >= ...`) in **descending order**.

*   The characters `char_1` through `char_8` (the 8 most frequent) are assigned to the "1st letter" slots on keys 2 through 9, costing 1 push each.
*   The characters `char_9` through `char_16` (the next 8 most frequent) are assigned to the "2nd letter" slots, costing 2 pushes each.
*   And so on.

This visual confirms that the character at index `i` in the sorted list of unique characters will always have a push cost of `(i // 8) + 1`.

## Dry Run
Let's use Example 3: `word = "aabbccddeeffgghhiiiiii"`

1.  **Count Character Frequencies**:
    `collections.Counter(word)` gives:
    `{'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'g': 2, 'h': 2, 'i': 6}`

2.  **Extract and Sort Frequencies (descending)**:
    The frequencies are `[2, 2, 2, 2, 2, 2, 2, 2, 6]`.
    Sorted in descending order: `[6, 2, 2, 2, 2, 2, 2, 2, 2]`
    (The `6` corresponds to 'i', the `2`s correspond to 'a' through 'h' in some order, which doesn't affect the total pushes).

3.  **Calculate Total Pushes**:
    Initialize `total_pushes = 0`.

    | Index `i` | Frequency `freq` | Push Cost `(i // 8) + 1` | Pushes for this char (`freq * cost`) | Running `total_pushes` |
    | :-------- | :--------------- | :----------------------- | :----------------------------------- | :--------------------- |
    | 0         | 6                | (0 // 8) + 1 = 1         | 6 * 1 = 6                            | 6                      |
    | 1         | 2                | (1 // 8) + 1 = 1         | 2 * 1 = 2                            | 6 + 2 = 8              |
    | 2         | 2                | (2 // 8) + 1 = 1         | 2 * 1 = 2                            | 8 + 2 = 10             |
    | 3         | 2                | (3 // 8) + 1 = 1         | 2 * 1 = 2                            | 10 + 2 = 12            |
    | 4         | 2                | (4 // 8) + 1 = 1         | 2 * 1 = 2                            | 12 + 2 = 14            |
    | 5         | 2                | (5 // 8) + 1 = 1         | 2 * 1 = 2                            | 14 + 2 = 16            |
    | 6         | 2                | (6 // 8) + 1 = 1         | 2 * 1 = 2                            | 16 + 2 = 18            |
    | 7         | 2                | (7 // 8) + 1 = 1         | 2 * 1 = 2                            | 18 + 2 = 20            |
    | 8         | 2                | (8 // 8) + 1 = 2         | 2 * 2 = 4                            | 20 + 4 = 24            |

    The final `total_pushes` is **24**. This matches the example output.

## Complexity
*   **Time Complexity**:
    *   Counting character frequencies using `collections.Counter` takes O(N) time, where N is the length of `word`.
    *   Sorting the frequencies takes O(K log K) time, where K is the number of unique characters in `word`. Since there are only 26 lowercase English letters, K is at most 26. Thus, K log K is a constant (26 log 26).
    *   Iterating through the sorted frequencies takes O(K) time.
    *   Overall, the dominant factor is counting frequencies, so the time complexity is **O(N)**.

*   **Space Complexity**:
    *   Storing character frequencies requires O(K) space, where K is the number of unique characters. Since K is at most 26, this is effectively **O(1)** constant space.

## Edge Cases
*   **`word` with only one unique character**: E.g., `"aaaaa"`.
    *   Frequencies: `[5]`. Sorted: `[5]`.
    *   `i=0`, `freq=5`, `cost=(0//8)+1=1`. `total_pushes = 5 * 1 = 5`. Correct.
*   **`word` with less than 8 unique characters**: E.g., `"abc"`.
    *   Frequencies: `[1, 1, 1]`. Sorted: `[1, 1, 1]`.
    *   All will be assigned a cost of 1 push. `total_pushes = 1*1 + 1*1 + 1*1 = 3`. Correct.
*   **`word` with exactly 8 unique characters**: E.g., `"abcdefgh"`.
    *   Frequencies: `[1, 1, 1, 1, 1, 1, 1, 1]`. Sorted: `[1, ..., 1]`.
    *   All will be assigned a cost of 1 push. `total_pushes = 8 * 1 = 8`. Correct.
*   **`word` with more than 8 unique characters**: E.g., `"abcdefghi"`.
    *   Frequencies: `[1, ..., 1]` (9 times). Sorted: `[1, ..., 1]`.
    *   First 8 characters get cost 1. The 9th character (at index 8) gets cost `(8//8)+1 = 2`.
    *   `total_pushes = (8 * 1) + (1 * 2) = 10`. Correct.

The solution handles all these cases naturally due to the greedy sorting and the `(i // 8) + 1` push cost calculation.

## Solution
```python
import collections

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Step 1: Count character frequencies
        # collections.Counter is an efficient way to do this.
        freq_map = collections.Counter(word)
        
        # Step 2: Extract frequencies and sort them in descending order.
        # We only care about the frequency values, not the characters themselves,
        # as the problem allows remapping any letter to any key.
        frequencies = list(freq_map.values())
        frequencies.sort(reverse=True)
        
        total_pushes = 0
        
        # Step 3: Iterate through sorted frequencies and calculate total pushes.
        # The 'i'-th character (0-indexed) in the sorted list will be assigned
        # a push cost based on its position.
        # There are 8 keys, so the first 8 characters get 1 push,
        # the next 8 get 2 pushes, and so on.
        # The push cost for the character at index 'i' is (i // 8) + 1.
        for i, freq in enumerate(frequencies):
            # Calculate the number of pushes required for this specific character.
            # For example:
            # i = 0-7: push_cost = 1
            # i = 8-15: push_cost = 2
            # i = 16-23: push_cost = 3
            push_cost = (i // 8) + 1
            
            # Add the total pushes for this character (its frequency * its push cost)
            # to the overall total.
            total_pushes += freq * push_cost
            
        return total_pushes

```

## Why This Works
This greedy approach works because we are always assigning the most "expensive" resources (fewer pushes) to the most "demanding" items (most frequent characters). By sorting frequencies in descending order and assigning them to slots with increasing push costs (1 push, then 2 pushes, then 3 pushes, etc.), we ensure that characters that appear more often in the `word` contribute the least to the total push count. Any other assignment strategy would involve giving a higher-frequency character a higher push cost, or a lower-frequency character a lower push cost, which would either keep the total the same or increase it. This strategy guarantees the minimum total pushes.

---
<sub>Generated 2026-07-31 04:03 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
