class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        memo = {}
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(x,y):
            if (x,y) in memo:
                return memo[(x,y)]
            
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            maxi = 0
            for dx, dy in dirs:
                new_x, new_y = x+dx, y+dy
                if new_x >=0 and new_x < rows and new_y >= 0 and new_y < cols:
                    if matrix[new_x][new_y] > matrix[x][y]:
                        maxi = max(maxi, 1 + dfs(new_x, new_y))

            memo[(x,y)] = maxi
            return maxi
        
        ret = 0
        for i in range(rows):
            for j in range(cols):
                ret = max(ret, dfs(i,j))

        return ret+1


        
