class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dirs = ((1,0),(0,1),(-1,0),(0,-1))
        visited = set()

        def dfs(x,y,visited):
            if x<0 or x>=rows or y<0 or y>=cols or grid[x][y]!="1" or ((x,y) in visited):
                return
            visited.add((x,y))
            for dx,dy in dirs:
                nx, ny = x+dx, y+dy
                dfs(nx,ny,visited)
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count+=1
                    dfs(r,c,visited)

        return count

