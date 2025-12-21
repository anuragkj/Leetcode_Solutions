class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visitp = set()
        visita = set()
        rows = len(heights)
        cols = len(heights[0])
        dirs = ((1,0),(-1,0),(0,1),(0,-1))

        def dfs(x,y,visited):
            if x<0 or x>=rows or y<0 or y>=cols or (x,y) in visited:
                return
            visited.add((x,y))
            for dx,dy in dirs:
                nx, ny = x+dx, y+dy
                if nx >=0 and nx<rows and ny>=0 and ny<cols and (nx,ny) not in visited and heights[nx][ny]>=heights[x][y]:
                    dfs(nx,ny,visited)
        
        for r in range(rows):
            dfs(r,0,visitp)
            dfs(r,cols-1,visita)


        for c in range(cols):
            dfs(0,c,visitp)
            dfs(rows-1,c,visita)

        ret = []
        for i in visita:
            if i in visitp:
                ret.append(i)
        

        return(ret)
