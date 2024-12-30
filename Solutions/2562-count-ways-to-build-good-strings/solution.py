class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        cache = {}
        def backtrack(s):
            if s > high:
                return 0
            if s in cache:
                return cache[s]
            count = 0
            if s >= low and s <=high:
                count = 1
            cache[s] = count+ backtrack(s+zero) + backtrack(s+one)
            cache[s] = cache[s]%1000000007
            return cache[s]
        return backtrack(0)
            
            
