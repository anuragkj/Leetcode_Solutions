class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(i, j):
            print(i,j)
            grid[i][j] = "0"
            dirs = [[0,1], [0,-1], [1,0],[-1,0]]

            for x,y in dirs:
                new_i = i+x
                new_j = j+y
                if new_i >= 0 and new_i < ROWS and new_j >=0 and new_j < COLS and grid[new_i][new_j] == "1":
                    dfs(new_i, new_j)



        
        res = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i,j)
                    res+=1
        return res


        
