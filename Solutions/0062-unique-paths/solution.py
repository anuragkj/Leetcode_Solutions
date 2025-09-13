class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(x,y):
            if x == m or y == n:
                return 0
            if x==m-1 and y == n-1:
                return 1
            if (x,y) in memo:
                return memo[(x,y)]
            ways = 0
            ways+= dfs(x+1, y)
            ways += dfs(x, y+1)

            memo[(x,y)] = ways

            return ways
        return dfs(0,0)
        
