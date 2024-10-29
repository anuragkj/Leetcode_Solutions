class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row,col = len(grid), len(grid[0])
        cache = {}
        def solve(i,j,prev):
            if (i,j,prev) in cache:
                return cache[(i,j,prev)]
            if i >= row or j >= col or i<0:
                cache[(i,j,prev)] = 0
                return 0
            if grid[i][j] <= prev:
                cache[(i,j,prev)] = 0
                return 0

            prev = grid[i][j]
            cache[(i-1,j+1,prev)] = solve(i-1,j+1,prev)
            cache[(i,j+1,prev)] = solve(i,j+1,prev)
            cache[(i+1,j+1,prev)] = solve(i+1,j+1,prev)
            cache[(i,j,prev)] = 1 + max(cache[(i-1,j+1,prev)],cache[(i,j+1,prev)],
                                        cache[(i+1,j+1,prev)])
            return cache[(i,j,prev)]

        res = 0
        for i in range(len(grid)):
            res = max(res,solve(i,0,-1))
        
        return res-1
