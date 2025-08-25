class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(sumi):
            if sumi in memo:
                return memo[sumi]
            if sumi > amount: 
                return float('inf')
            if sumi == amount:
                return 0
            ret = float('inf')
            for i in coins:
                ret = min(ret, 1 + dfs(i+sumi)) 
            memo[sumi]=ret
            return ret
        result = dfs(0)
        return result if result != float('inf') else -1      
