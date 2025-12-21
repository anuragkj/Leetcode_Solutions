class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(i,j,ptr,visited):
            if i >= rows or i < 0 or j>= cols or j <0 or board[i][j]!=word[ptr] or (i,j) in visited:
                return False 
            if ptr == len(word) - 1:
                return True
            dirs = ((0,1),(1,0),(-1,0),(0,-1))
            ret = False
            visited.add((i,j))
            for dx,dy in dirs:
                x = i+dx
                y = j+dy
                    
                ret = ret or dfs(x,y,ptr+1,visited)
            
            visited.remove((i,j))
            return ret
        visit = set()
        ret = False
        for i in range(rows):
            for j in range(cols):
                ret = ret or dfs(i,j,0,visit)
        return ret
