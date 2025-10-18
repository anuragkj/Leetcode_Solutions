class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxi = 0
        dic = {}

        for r in range(len(s)):
            dic[s[r]]=dic.get(s[r], 0)+1
            while dic[s[r]] > 1:
                dic[s[l]] -= 1
                l+=1
            maxi = max(maxi, r-l+1)
        return maxi
        
