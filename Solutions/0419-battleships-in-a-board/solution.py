class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        rows = len(board)
        cols = len(board[0])

        def dfs(x, y):
            if x < 0 or x > rows - 1 or y <0 or y > cols -1 or board[x][y] == ".":
                return
            board[x][y] = "."
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            for xi, yi in dirs:
                x_new, y_new = x+xi, y+yi
                if x_new >=0 and x_new < rows and y_new >= 0 and y_new <cols and board[x_new][y_new] == "X":
                    dfs(x_new, y_new)
            return
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "X":
                    dfs(i,j)
                    count+=1
        
        return count
