class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        vowels = set('aeiou')
        vowel_count, cons_count = defaultdict(int), 0 # counters for vowels and consonants
        left = count = substrs = 0 # left pointer for window, count of valid substrs, and total valid substrs

        def minus_char(char): # removes a vowel or consonant count
            if char in vowels:
                vowel_count[char] -= 1
                if vowel_count[char] == 0:
                    del vowel_count[char] # remove if vowel is empty for faster valid substr check
            else:
                nonlocal cons_count
                cons_count -= 1

        for char in word:
            # add current character for right pointer of window
            if char in vowels:
                vowel_count[char] += 1
            else:
                cons_count += 1
                count = 0 # can't keep expanding previous valid substrs, so reset count

            while cons_count > k: # shrink left side of window if too many consonants
                minus_char(word[left])
                left += 1

            # if window has k consonants and at least 1 of each vowel, then its valid substr so count + 1
            # count keeps increasing while shrinking left side of window until condition breaks
            while cons_count == k and len(vowel_count) == 5:
                count += 1 # current window has valid substr
                minus_char(word[left]) # loop continues if vowel removed and at least 5, stops if consonant
                left += 1 # shrink window
            
            # when moving right pointer, can make new substr if the right char is a vowel, else count resets
            # each new vowel means all valid substrs have another variant, so add count and not just 1
            substrs += count

        return substrs
