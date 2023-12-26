class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        @cache
        def dfs(n, target):
            if target < n or target > n * k:
                return 0
                
            if n == 1 or target == n * k: 
                return 1

            total = 0
            for i in range(1, k + 1):
                total += dfs(n - 1, target - i) % mod
            print(total)
            return total % mod

        return dfs(n, target) % mod
