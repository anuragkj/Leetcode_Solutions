class Solution:
    def longestPalindrome(self, s: str) -> str:
        largest = ''
        lenl = 0
        for i in range(len(s)):
            left = i
            right = i
            while(left>-1 and right<len(s) and s[left] == s[right]):
                if right - left + 1 > lenl:
                    lenl = right - left + 1
                    largest = s[left:right+1]
                left -= 1
                right += 1
            
            left = i
            right = i+1
            while(left>-1 and right<len(s) and s[left] == s[right]):
                if right - left + 1 > lenl:
                    lenl = right - left + 1
                    largest = s[left:right+1]
                left -= 1
                right += 1
        return largest



