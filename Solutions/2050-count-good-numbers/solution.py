class Solution:
    def countGoodNumbers(self, n: int) -> int:
       
        MOD = 10**9 + 7
        evens = (n + 1) // 2  
        odds = n // 2         
        
        return (pow(5, evens, MOD) * pow(4, odds, MOD)) % MOD
