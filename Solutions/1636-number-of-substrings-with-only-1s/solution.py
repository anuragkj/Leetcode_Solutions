class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        left = 0
        count = 0

        for right in range(len(s)):
            if s[right] == '0':
                left = right + 1
            else:
                count = (count + (right - left + 1) % mod) % mod
                
        return count
