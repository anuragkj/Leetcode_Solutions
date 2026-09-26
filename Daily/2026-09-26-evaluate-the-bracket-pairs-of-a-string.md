# [1807] Evaluate the Bracket Pairs of a String

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-09-26 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/)

**Topics:** Array, Hash Table, String

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.

- For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the keys "name" and "age".

You know the values of a wide range of keys. This is represented by a 2D string array knowledge where each knowledge[i] = [key_i, value_i] indicates that key key_i has a value of value_i.

You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key key_i, you will:

- Replace key_i and the bracket pair with the key's corresponding value_i.

- If you do not know the value of the key, you will replace key_i and the bracket pair with a question mark "?" (without the quotation marks).

Each key will appear at most once in your knowledge. There will not be any nested brackets in s.

Return the resulting string after evaluating all of the bracket pairs.

Example 1:

Input: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
Output: "bobistwoyearsold"
Explanation:
The key "name" has a value of "bob", so replace "(name)" with "bob".
The key "age" has a value of "two", so replace "(age)" with "two".

Example 2:

Input: s = "hi(name)", knowledge = [["a","b"]]
Output: "hi?"
Explanation: As you do not know the value of the key "name", replace "(name)" with "?".

Example 3:

Input: s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
Output: "yesyesyesaaa"
Explanation: The same key can appear multiple times.
The key "a" has a value of "yes", so replace all occurrences of "(a)" with "yes".
Notice that the "a"s not in a bracket pair are not evaluated.

Constraints:

- 1 <= s.length <= 10^5

- 0 <= knowledge.length <= 10^5

- knowledge[i].length == 2

- 1 <= key_i.length, value_i.length <= 10

- s consists of lowercase English letters and round brackets '(' and ')'.

- Every open bracket '(' in s will have a corresponding close bracket ')'.

- The key in each bracket pair of s will be non-empty.

- There will not be any nested bracket pairs in s.

- key_i and value_i consist of lowercase English letters.

- Each key_i in knowledge is unique.

**Examples / sample tests:**

```
"(name)is(age)yearsold"
[["name","bob"],["age","two"]]
"hi(name)"
[["a","b"]]
"(a)(a)(a)aaa"
[["a","yes"]]
```

---

## Problem Summary
You are given a string `s` containing bracketed keys like `(name)` and a `knowledge` base mapping keys to values. Your task is to replace each bracketed key in `s` with its corresponding value from `knowledge`. If a key is not found in `knowledge`, replace its bracket pair with a question mark `?`.

## Intuition
The core idea is to iterate through the input string `s` and identify two types of segments: plain text and bracketed keys. For plain text, we simply append it to our result. For bracketed keys, we need to extract the key, look it up in our `knowledge` base, and then append either its value or a `?` to the result.

To efficiently look up keys, converting the `knowledge` list of lists into a **hash map (Python dictionary)** is crucial. This allows us to find a key's value in nearly constant time. Since there are no nested brackets and every `(` has a matching `)`, we can process the string linearly, character by character.

## Approach
1.  **Preprocess Knowledge**: Convert the `knowledge` list of lists into a dictionary for O(1) average-time lookups.
    *   Initialize an empty dictionary, say `knowledge_map`.
    *   For each `[key, value]` pair in the input `knowledge` list, add `key: value` to `knowledge_map`.

2.  **Initialize Result Builder**: Create an empty list, say `result_parts`, to store parts of the final string. Using a list and then `"".join()` at the end is more efficient in Python than repeatedly concatenating strings.

3.  **Iterate Through String `s`**: Use a pointer `i` starting from `0` to traverse `s`.

4.  **Handle Non-Bracketed Characters**:
    *   If `s[i]` is not an opening bracket `(`:
        *   Append `s[i]` to `result_parts`.
        *   Increment `i` by 1.

5.  **Handle Bracketed Keys**:
    *   If `s[i]` is an opening bracket `(`:
        *   Increment `i` by 1 to move past `(`.
        *   Initialize an empty string, say `current_key`, to build the key.
        *   **Extract Key**: While `s[i]` is not a closing bracket `)`:
            *   Append `s[i]` to `current_key`.
            *   Increment `i` by 1.
        *   **Lookup and Replace**: After finding the closing bracket `)`:
            *   Look up `current_key` in `knowledge_map`.
            *   If `current_key` is found in `knowledge_map`, append `knowledge_map[current_key]` to `result_parts`.
            *   Otherwise (key not found), append `'?'` to `result_parts`.
        *   Increment `i` by 1 to move past `)`.

6.  **Final Result**: After the loop finishes (when `i` reaches the end of `s`), join all the elements in `result_parts` into a single string and return it.

## Visualization

Let's trace `s = "(name)is(age)yearsold"` with `knowledge_map = {"name": "bob", "age": "two"}`.

```
s = "(name)is(age)yearsold"
    ^
    i=0

1. i=0, s[0] is '('.
   - Move i to 1 (past '(').
   - Start building current_key.
   - i=1, s[1]='n' -> current_key="n"
   - i=2, s[2]='a' -> current_key="na"
   - i=3, s[3]='m' -> current_key="nam"
   - i=4, s[4]='e' -> current_key="name"
   - i=5, s[5]=')'. Key extraction ends. current_key="name".
   - Look up "name" in knowledge_map -> "bob".
   - result_parts = ["bob"]
   - Move i to 6 (past ')').

s = "(name)is(age)yearsold"
          ^
          i=6

2. i=6, s[6] is 'i'. Not '('.
   - Append 'i' to result_parts.
   - result_parts = ["bob", "i"]
   - Move i to 7.

s = "(name)is(age)yearsold"
           ^
           i=7

3. i=7, s[7] is 's'. Not '('.
   - Append 's' to result_parts.
   - result_parts = ["bob", "i", "s"]
   - Move i to 8.

s = "(name)is(age)yearsold"
            ^
            i=8

4. i=8, s[8] is '('.
   - Move i to 9 (past '(').
   - Start building current_key.
   - i=9, s[9]='a' -> current_key="a"
   - i=10, s[10]='g' -> current_key="ag"
   - i=11, s[11]='e' -> current_key="age"
   - i=12, s[12]=')'. Key extraction ends. current_key="age".
   - Look up "age" in knowledge_map -> "two".
   - result_parts = ["bob", "i", "s", "two"]
   - Move i to 13 (past ')').

... and so on for "yearsold".
```

## Dry Run

**Example 1:**
`s = "(name)is(age)yearsold"`
`knowledge = [["name","bob"],["age","two"]]`

**Preprocessing:**
`knowledge_map = {"name": "bob", "age": "two"}`

**Initialization:**
`result_parts = []`
`i = 0`

| `i` | `s[i]` | `Action`                                     | `current_key` (if any) | `Lookup Result` (if any) | `result_parts` (after action)                               |
|-----|--------|----------------------------------------------|------------------------|--------------------------|-------------------------------------------------------------|
| 0   | `(`    | Start key extraction. `i` becomes 1.         |                        |                          | `[]`                                                        |
| 1   | `n`    | Append to `current_key`. `i` becomes 2.      | `n`                    |                          | `[]`                                                        |
| 2   | `a`    | Append to `current_key`. `i` becomes 3.      | `na`                   |                          | `[]`                                                        |
| 3   | `m`    | Append to `current_key`. `i` becomes 4.      | `nam`                  |                          | `[]`                                                        |
| 4   | `e`    | Append to `current_key`. `i` becomes 5.      | `name`                 |                          | `[]`                                                        |
| 5   | `)`    | End key. Lookup "name". Append "bob". `i` becomes 6. | `name`                 | `bob`                    | `["bob"]`                                                   |
| 6   | `i`    | Append `s[i]`. `i` becomes 7.                |                        |                          | `["bob", "i"]`                                              |
| 7   | `s`    | Append `s[i]`. `i` becomes 8.                |                        |                          | `["bob", "i", "s"]`                                         |
| 8   | `(`    | Start key extraction. `i` becomes 9.         |                        |                          | `["bob", "i", "s"]`                                         |
| 9   | `a`    | Append to `current_key`. `i` becomes 10.     | `a`                    |                          | `["bob", "i", "s"]`                                         |
| 10  | `g`    | Append to `current_key`. `i` becomes 11.     | `ag`                   |                          | `["bob", "i", "s"]`                                         |
| 11  | `e`    | Append to `current_key`. `i` becomes 12.     | `age`                  |                          | `["bob", "i", "s"]`                                         |
| 12  | `)`    | End key. Lookup "age". Append "two". `i` becomes 13. | `age`                  | `two`                    | `["bob", "i", "s", "two"]`                                  |
| 13  | `y`    | Append `s[i]`. `i` becomes 14.               |                        |                          | `["bob", "i", "s", "two", "y"]`                             |
| 14  | `e`    | Append `s[i]`. `i` becomes 15.               |                        |                          | `["bob", "i", "s", "two", "y", "e"]`                        |
| 15  | `a`    | Append `s[i]`. `i` becomes 16.               |                        |                          | `["bob", "i", "s", "two", "y", "e", "a"]`                   |
| 16  | `r`    | Append `s[i]`. `i` becomes 17.               |                        |                          | `["bob", "i", "s", "two", "y", "e", "a", "r"]`              |
| 17  | `s`    | Append `s[i]`. `i` becomes 18.               |                        |                          | `["bob", "i", "s", "two", "y", "e", "a", "r", "s"]`         |
| 18  | `o`    | Append `s[i]`. `i` becomes 19.               |                        |                          | `["bob", "i", "s", "two", "y", "e", "a", "r", "s", "o"]`    |
| 19  | `l`    | Append `s[i]`. `i` becomes 20.               |                        |                          | `["bob", "i", "s", "two", "y", "e", "a", "r", "s", "o", "l"]` |
| 20  | `d`    | Append `s[i]`. `i` becomes 21.               |                        |                          | `["bob", "i", "s", "two", "y", "e", "a", "r", "s", "o", "l", "d"]` |
| 21  | `EOF`  | Loop ends.                                   |                        |                          | `["bob", "i", "s", "two", "y", "e", "a", "r", "s", "o", "l", "d"]` |

**Final Result:** `"".join(result_parts)` which is `"bobistwoyearsold"`.

## Complexity

*   **Time Complexity**: O(L + K)
    *   **L**: `s.length`. We iterate through the string `s` once. Each character is visited, and key extraction involves iterating over the characters within the key.
    *   **K**: Total length of all keys and values in `knowledge`. Building the `knowledge_map` takes time proportional to the sum of lengths of all keys and values. Dictionary lookups are O(1) on average.
*   **Space Complexity**: O(L + K)
    *   **L**: The `result_parts` list can store up to `s.length` characters in the worst case (e.g., if `s` contains no brackets).
    *   **K**: The `knowledge_map` stores all keys and values from the `knowledge` input, taking space proportional to their total length.

## Edge Cases

*   **`s` with no brackets**: The code will simply iterate through `s` and append each character to `result_parts`, effectively returning `s` unchanged.
*   **`knowledge` is empty**: All bracketed keys will be replaced with `?` as they won't be found in the empty `knowledge_map`.
*   **Key not found**: Handled by the `knowledge_map.get(key, '?')` or `if key in knowledge_map` logic, replacing with `?`.
*   **Same key appears multiple times in `s`**: Example 3 shows `"(a)(a)(a)aaa"`. The `knowledge_map` lookup will correctly return the same value for each occurrence of `(a)`.
*   **`s` contains only brackets**: E.g., `s = "(a)(b)"`. The logic correctly extracts each key and replaces it.
*   **Keys/values are short/long**: Constraints state key/value length up to 10. This doesn't affect the overall O(L+K) complexity but ensures key extraction and lookup are fast.
*   **Constraints on `s.length` and `knowledge.length`**: Up to 10^5. The linear time complexity O(L+K) is efficient enough for these constraints.

## Solution

```python
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Step 1: Preprocess Knowledge into a hash map (dictionary) for O(1) average-time lookups.
        knowledge_map = {key: value for key, value in knowledge}

        # Step 2: Initialize a list to build the result string efficiently.
        result_parts = []
        
        # Step 3: Use a pointer to iterate through the input string s.
        i = 0
        n = len(s)

        while i < n:
            # Step 4: Handle non-bracketed characters.
            if s[i] != '(':
                result_parts.append(s[i])
                i += 1
            # Step 5: Handle bracketed keys.
            else:
                # Move past the opening bracket '('
                i += 1 
                
                # Extract the key
                current_key_start = i
                while s[i] != ')':
                    i += 1
                current_key = s[current_key_start:i]
                
                # Look up the key in knowledge_map and append its value or '?'
                # Using .get() with a default value is concise for this.
                result_parts.append(knowledge_map.get(current_key, '?'))
                
                # Move past the closing bracket ')'
                i += 1
        
        # Step 6: Join all parts to form the final string.
        return "".join(result_parts)

```

## Why This Works

This approach works because it systematically processes the input string `s` from left to right, character by character. By first converting the `knowledge` into a hash map, we ensure that looking up a key is very fast (average O(1)). The problem constraints guarantee that brackets are well-formed and not nested, which simplifies parsing: whenever we see an `(`, we know the next `)` will close the current key. We build the result string by appending characters or looked-up values to a list, which is an efficient way to construct strings in Python. This linear scan and efficient lookup strategy correctly handles all cases, including multiple occurrences of the same key and unknown keys, without needing complex state management or backtracking.

---
<sub>Generated 2026-09-26 05:21 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
