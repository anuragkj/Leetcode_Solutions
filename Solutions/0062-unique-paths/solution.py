class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return 1
            if i < 0 or i >= m or j <0 or j >= n:
                return 0
            dirs = [(1,0),(0,1)]
            val = 0
            for dx,dy in dirs:
                new_x = i+dx
                new_y = j+dy
                if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n:
                    val+=dfs(new_x,new_y)
            return val
        return dfs(0,0)
        
