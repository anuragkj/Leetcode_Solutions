class Solution:
    def countSubstrings(self, s: str) -> int:
        def countpali(left, right):
            if left < 0 or right >= len(s):
                return 0
            if s[left] == s[right]:
                return 1 + countpali(left - 1, right + 1)
            return 0

        ret = 0
        for i in range(len(s)):
            countodd = countpali(i-1, i+1)
            counteven = countpali(i, i+1)
            ret += countodd + counteven
        return len(s)+ret
