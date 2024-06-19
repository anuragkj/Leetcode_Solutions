class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)  
        memo = [[0 for _ in range(n)] for _ in range(n)]  
        res = 0  
        
        for i in range(n):  
            memo[i][i] = 1  
            res += 1  
        
        for i in range(n - 1):  
            if s[i] == s[i + 1]:  
                memo[i][i + 1] = 1  
                res += 1  
        
        for i in range(2, n):  
            for j in range(n - i):  
                if s[j] == s[i + j] and memo[j + 1][i + j - 1] == 1:  
                    memo[j][i + j] = 1  
                    res += 1  
        
        return res  
