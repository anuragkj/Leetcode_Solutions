class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows=len(heights)
        cols=len(heights[0])
        vis1=[[False]*cols for i in range(rows)]
        vis2=[[False]*cols for i in range(rows)]

        def bfs(i,j,vis):
            q=deque()
            q.append((i,j))
            vis[i][j]=True
            while q:
                x,y=q.popleft()
                for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]:
                    X=x+dx
                    Y=y+dy
                    if 0<=X<rows and 0<=Y<cols and not vis[X][Y] and heights[x][y]<=heights[X][Y]:
                        vis[X][Y]=True
                        q.append((X,Y)) 
        for i in range(rows):
            bfs(i,0,vis1)
        for i in range(cols):
            bfs(0,i,vis1)
        for i in range(rows):
            bfs(i,cols-1,vis2)
        for i in range(cols):
            bfs(rows-1,i,vis2)
        res=[]
        for i in range(rows):
            for j in range(cols):
                if vis1[i][j] and vis2[i][j]:
                    res.append([i,j])
        return res
