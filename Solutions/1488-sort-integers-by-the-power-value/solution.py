class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        def dfs(n):
            if n == 1:
                return 0
            
            if n in memo:
                return memo[n]
            
            if n%2 == 0:
                ret = 1+dfs(n/2)
            else:
                ret = 1+dfs(3*n+1)
            memo[n] = ret
            return ret
        
        res = []
        for i in range(lo, hi+1):
            heapq.heappush(res,(dfs(i),i))
        ret = -1
        for i in range(k):
            _,ret = heapq.heappop(res)

        return ret
        

