class Solution:
    def countSubstrings(self, s: str) -> int:
        def countpalindrome(i,j):
            count = 0
            while(i>=0 and j<len(s)):
                if s[i] == s[j]:
                    count+=1
                    i-=1
                    j+=1
                else:
                    break
            
            return count

        total = 0        
        for i in range(len(s)-1):
            total+=countpalindrome(i,i)
            total+=countpalindrome(i,i+1)
        total+=1
        return total

