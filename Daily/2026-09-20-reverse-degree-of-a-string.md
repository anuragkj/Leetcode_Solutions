# [3498] Reverse Degree of a String

**Difficulty:** Easy &nbsp;·&nbsp; **Daily Challenge:** 2026-09-20 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/reverse-degree-of-a-string/)

**Topics:** String, Simulation

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given a string s, calculate its reverse degree.

The reverse degree is calculated as follows:

- For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its position in the string (1-indexed).

- Sum these products for all characters in the string.

Return the reverse degree of s.

Example 1:

Input: s = "abc"

Output: 148

Explanation:

			Letter
			Index in Reversed Alphabet
			Index in String
			Product

			'a'
			26
			1
			26

			'b'
			25
			2
			50

			'c'
			24
			3
			72

The reversed degree is 26 + 50 + 72 = 148.

Example 2:

Input: s = "zaza"

Output: 160

Explanation:

			Letter
			Index in Reversed Alphabet
			Index in String
			Product

			'z'
			1
			1
			1

			'a'
			26
			2
			52

			'z'
			1
			3
			3

			'a'
			26
			4
			104

The reverse degree is 1 + 52 + 3 + 104 = 160.

Constraints:

- 1 <= s.length <= 1000

- s contains only lowercase English letters.

**Examples / sample tests:**

```
"abc"
"zaza"
```

---

## Problem Summary
The problem asks us to calculate the "reverse degree" of a given string `s`. This degree is found by iterating through each character, multiplying its position in the reversed alphabet (where 'a'=26, 'b'=25, ..., 'z'=1) by its 1-indexed position in the string, and summing these products.

## Intuition
The problem statement provides a very direct and explicit formula for calculating the reverse degree. There are no hidden tricks or complex algorithms required. The core idea is to **simulate** the described process step-by-step:
1.  We need to go through each character of the string.
2.  For each character, we need two values:
    *   Its **1-indexed position in the string**: If we iterate using a 0-indexed loop (like `enumerate` in Python), this will simply be `index + 1`.
    *   Its **position in the reversed alphabet**: We know 'a' maps to 26, 'b' to 25, and so on, down to 'z' mapping to 1. We can derive this mapping. Standard alphabet position (0-indexed) for 'a' is 0, 'b' is 1, ..., 'z' is 25. Notice that `reversed_position = 26 - standard_0_indexed_position`. For example, 'a' (standard 0) -> 26 - 0 = 26. 'z' (standard 25) -> 26 - 25 = 1. This formula works perfectly.
3.  Once we have these two values for a character, we multiply them and add the result to a running total.

## Approach
The optimal approach is a straightforward **simulation** of the calculation described in the problem statement.

1.  Initialize a variable, let's call it `total_reverse_degree`, to `0`. This variable will store the cumulative sum of products.
2.  **Iterate** through the input string `s` character by character. It's helpful to get both the **0-indexed position** (let's call it `i`) and the **character itself** (let's call it `char`) for each step. Python's `enumerate()` function is perfect for this.
3.  Inside the loop, for each `char` at 0-indexed position `i`:
    a.  Calculate its **1-indexed string position**: This is simply `i + 1`.
    b.  Calculate its **0-indexed alphabet position**: We can use `ord(char) - ord('a')`. For example, `ord('a') - ord('a')` is `0`, `ord('b') - ord('a')` is `1`, and so on.
    c.  Calculate its **position in the reversed alphabet**: Using the formula derived in the intuition, this is `26 - (0-indexed alphabet position)`.
    d.  Calculate the **product** of the 1-indexed string position and the reversed alphabet position.
    e.  **Add** this product to `total_reverse_degree`.
4.  After the loop finishes iterating through all characters in the string, `total_reverse_degree` will hold the final result. **Return** this value.

## Visualization
Let's visualize how the "Index in Reversed Alphabet" is calculated for a few characters:

```
Character | ASCII Value (ord()) | ord(char) - ord('a') (0-indexed alphabet pos) | 26 - (0-indexed alphabet pos) (Reversed Alphabet Pos)
----------|---------------------|-----------------------------------------------|---------------------------------------------------------
'a'       | 97                  | 97 - 97 = 0                                   | 26 - 0 = 26
'b'       | 98                  | 98 - 97 = 1                                   | 26 - 1 = 25
'c'       | 99                  | 99 - 97 = 2                                   | 26 - 2 = 24
...       | ...                 | ...                                           | ...
'y'       | 121                 | 121 - 97 = 24                                 | 26 - 24 = 2
'z'       | 122                 | 122 - 97 = 25                                 | 26 - 25 = 1
```

This table clearly shows the mapping from a character to its required reversed alphabet position.

## Dry Run
Let's trace the execution with Example 1: `s = "abc"`

Initialize `total_reverse_degree = 0`.

| `i` (0-idx) | `char` | `string_pos` (`i+1`) | `alpha_0_indexed` (`ord(char)-ord('a')`) | `reversed_alpha_pos` (`26 - alpha_0_indexed`) | `product` (`reversed_alpha_pos * string_pos`) | `total_reverse_degree` (running sum) |
| :---------- | :----- | :------------------- | :--------------------------------------- | :-------------------------------------------- | :-------------------------------------------- | :----------------------------------- |
| 0           | 'a'    | 1                    | 0                                        | 26                                            | 26 \* 1 = 26                                  | 0 + 26 = **26**                      |
| 1           | 'b'    | 2                    | 1                                        | 25                                            | 25 \* 2 = 50                                  | 26 + 50 = **76**                     |
| 2           | 'c'    | 3                    | 2                                        | 24                                            | 24 \* 3 = 72                                  | 76 + 72 = **148**                    |

After iterating through all characters, the final `total_reverse_degree` is **148**. This matches the example output.

## Complexity
*   **Time Complexity**: O(N), where N is the length of the string `s`. We iterate through the string exactly once, performing constant-time calculations for each character.
*   **Space Complexity**: O(1). We only use a few variables to store the running sum and intermediate calculations, regardless of the input string's length.

## Edge Cases
*   **Minimum length string (`s.length = 1`)**: For `s = "a"`, the loop runs once. `i=0`, `char='a'`. `string_pos=1`, `reversed_alpha_pos=26`. Product `26*1=26`. `total_reverse_degree` becomes 26. This is correctly handled.
*   **Maximum length string (`s.length = 1000`)**: The loop will run 1000 times. This is well within typical time limits for competitive programming (usually 10^8 operations per second). The calculations are simple arithmetic, so it will be very fast.
*   **String with all same characters (e.g., "aaaa" or "zzzz")**: The logic correctly applies the same `reversed_alpha_pos` for each character, but multiplies it by its increasing `string_pos`. This is handled correctly by the general formula.
*   **String containing 'a' and 'z'**: These are the extreme ends of the alphabet. Our formula `26 - (ord(char) - ord('a'))` correctly maps 'a' to 26 and 'z' to 1, as shown in the visualization.

## Solution
```python
class Solution:
    def reverseDegree(self, s: str) -> int:
        # Initialize the total reverse degree to 0
        total_reverse_degree = 0

        # Iterate through the string using enumerate to get both index and character
        # 'i' will be the 0-indexed position of the character
        # 'char' will be the character itself
        for i, char in enumerate(s):
            # Step 1: Calculate the 1-indexed position of the character in the string
            # If the 0-indexed position is 'i', the 1-indexed position is 'i + 1'
            string_position = i + 1

            # Step 2: Calculate the 0-indexed position of the character in the standard alphabet
            # 'a' is 0, 'b' is 1, ..., 'z' is 25
            # We use ord() to get the ASCII value and subtract ord('a') to get this 0-indexed value
            alpha_0_indexed_position = ord(char) - ord('a')

            # Step 3: Calculate the position of the character in the reversed alphabet
            # 'a' is 26, 'b' is 25, ..., 'z' is 1
            # This can be derived as 26 - (0-indexed alphabet position)
            reversed_alpha_position = 26 - alpha_0_indexed_position

            # Step 4: Multiply the two calculated positions to get the product for this character
            product = reversed_alpha_position * string_position

            # Step 5: Add this product to our running total
            total_reverse_degree += product

        # After iterating through all characters, return the final sum
        return total_reverse_degree

```

## Why This Works
This solution works because it directly implements the definition of the "reverse degree" as described in the problem statement. By iterating through each character and applying the specified arithmetic operations—calculating the 1-indexed string position and the reversed alphabet position, then multiplying them and summing the results—we are precisely computing the required value. The formulas `i + 1` for string position and `26 - (ord(char) - ord('a'))` for reversed alphabet position are accurate translations of the problem's rules into code, ensuring correctness for all valid inputs.

---
<sub>Generated 2026-09-20 05:17 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
