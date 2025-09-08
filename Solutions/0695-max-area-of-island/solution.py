class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            
            area = 1
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            
            return area

        ret = 0    
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 0:
                    ret = max(ret, dfs(i,j))
        return ret
        
