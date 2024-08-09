class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m < 3 or n < 3:
            return 0 
        count = 0
        
        for i in range(m - 2):
            for j in range(n - 2):
                d = set()
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        d.add(grid[k][l])
                
                if d == set(range(1, 10)):
                    if (grid[i][j] + grid[i][j+1] + grid[i][j+2] == 
                        grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] ==
                        grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] ==
                        grid[i][j] + grid[i+1][j] + grid[i+2][j] ==
                        grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] ==
                        grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] ==
                        grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] ==
                        grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]):
                        count += 1
                
        return count
