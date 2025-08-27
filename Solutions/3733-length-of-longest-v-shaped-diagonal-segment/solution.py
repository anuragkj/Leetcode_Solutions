class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:

        
        @cache
        def dp(i, j, l, d, b):

            # print("here")

            if i < 0 or i >= len(grid):
                return 0
            
            if j < 0 or j >= len(grid[0]):
                return 0

            ans = 0
            # print("here")
            if d == 0:
                if (i - 1 >= 0 and i - 1 < len(grid)) and (j - 1 >= 0 and j - 1 < len(grid[0])):
                    if grid[i - 1][j - 1] != 1: 
                        if b == 1:
                            if grid[i - 1][j - 1] == 2:
                                ans = max(ans, 1 + dp(i - 1, j - 1, l, d, grid[i - 1][j - 1]))
                        elif b == 2:
                            if grid[i - 1][j - 1] == 0:
                                ans = max(ans, 1 + dp(i - 1, j - 1, l, d, grid[i - 1][j - 1]))
                        elif b == 0:
                            if grid[i - 1][j - 1] == 2:
                                ans = max(ans, 1 + dp(i - 1, j - 1, l, d, grid[i - 1][j - 1]))

            elif d == 1:
                
                if (i - 1 >= 0 and i - 1 < len(grid)) and (j + 1 >= 0 and j + 1 < len(grid[0])):
                    if grid[i - 1][j + 1] != 1:
                        if b == 1:
                            if grid[i - 1][j + 1] == 2:
                                ans = max(ans, 1 + dp(i - 1, j + 1, l, d, grid[i - 1][j + 1]))
                        elif b == 2:
                            if grid[i - 1][j + 1] == 0:
                                ans = max(ans, 1 + dp(i - 1, j + 1, l, d, grid[i - 1][j + 1]))
                        elif b == 0:
                            if grid[i - 1][j + 1] == 2:
                                ans = max(ans, 1 + dp(i - 1, j + 1, l, d, grid[i - 1][j + 1]))
                        
            elif d == 2:

                if (i + 1 >= 0 and i + 1 < len(grid)) and (j + 1 >= 0 and j + 1 < len(grid[0])):
                    if grid[i + 1][j + 1] != 1:
                        if b == 1:
                            if grid[i + 1][j + 1] == 2:
                                ans = max(ans, 1 + dp(i + 1, j + 1, l, d, grid[i + 1][j + 1]))
                        elif b == 2:
                            if grid[i + 1][j + 1] == 0:
                                ans = max(ans, 1 + dp(i + 1, j + 1, l, d, grid[i + 1][j + 1]))
                        elif b == 0:
                            if grid[i + 1][j + 1] == 2:
                                ans = max(ans, 1 + dp(i + 1, j + 1, l, d, grid[i + 1][j + 1]))   

            elif d == 3:
                # print("here")
                if (i + 1 >= 0 and i + 1 < len(grid)) and (j - 1 >= 0 and j - 1 < len(grid[0])):
                    if grid[i + 1][j - 1] != 1:
                        if b == 1:
                            if grid[i + 1][j - 1] == 2:
                                ans = max(ans, 1 + dp(i + 1, j - 1, l, d, grid[i + 1][j - 1]))
                        elif b == 2:
                            if grid[i + 1][j - 1] == 0:
                                ans = max(ans, 1 + dp(i + 1, j - 1, l, d, grid[i + 1][j - 1]))
                        elif b == 0:
                            if grid[i + 1][j - 1] == 2:
                                ans = max(ans, 1 + dp(i + 1, j - 1, l, d, grid[i + 1][j - 1]))
                        

            if l != 0:
                for v, w in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
                    if (v, w) == (-1, -1):
                        if (i + v >= 0 and i + v < len(grid)) and (j + w >= 0 and j + w < len(grid[0])):
                            if grid[i + v][j + w] != 1:
                                if b == 1:
                                    if grid[i + v][j + w] == 2:
                                        if d != 2 and d != 0 and d != 4: 
                                            ans = max(ans, 1 + dp(i + v, j + w, 0, 0, grid[i +v][j + w]))
                                elif b == 2:
                                    if grid[i + v][j + w] == 0:
                                        if d != 2 and d != 0 and d != 1: 
                                            ans = max(ans, 1 + dp(i + v, j + w, 0, 0, grid[i +v][j + w]))
                                elif b == 0:
                                    if grid[i + v][j + w] == 2:
                                        if d != 2 and d != 0 and d != 1: 
                                            ans = max(ans, 1 + dp(i + v, j + w, 0, 0, grid[i +v][j + w]))
                                
                    elif (v, w) == (-1, 1):
                        if (i + v >= 0 and i + v < len(grid)) and (j + w >= 0 and j + w < len(grid[0])):
                            if grid[i + v][j + w] != 1:
                                if b == 1:
                                    if  grid[i + v][j + w] == 2:
                                        if d != 3 and d != 1 and d != 2: 
                                            ans = max(ans, 1 + dp(i + v, j + w, 0, 1, grid[i +v][j + w]))
                                elif b == 2:
                                    if  grid[i + v][j + w] == 0:
                                        if d != 3 and d != 1 and d != 2: 
                                            ans = max(ans, 1 + dp(i + v, j + w, 0, 1, grid[i +v][j + w]))
                                elif b == 0:
                                    if grid[i + v][j + w] == 2:
                                        if d != 3 and d != 1 and d != 2: 
                                            ans = max(ans, 1 + dp(i + v, j + w, 0, 1, grid[i +v][j + w]))
                                
                    elif (v, w) == (1, 1):
                        if (i + v >= 0 and i + v < len(grid)) and (j + w >= 0 and j + w < len(grid[0])):
                            if grid[i + v][j + w] != 1:
                                if b == 1:
                                    if grid[i + v][j + w] == 2:
                                        if d != 2 and d != 0 and d != 3: 
                                            ans = max(ans, 1 + dp(i + v, j + w, 0, 2, grid[i +v][j + w]))
                                elif b == 2:
                                    if grid[i + v][j + w] == 0:
                                        if d != 2 and d != 0 and d != 3: 
                                            ans = max(ans, 1 + dp(i + v, j + w, 0, 2, grid[i +v][j + w]))
                                elif b == 0:
                                    if grid[i + v][j + w] == 2:
                                        if d != 2 and d != 0 and d != 3: 
                                            ans = max(ans, 1 + dp(i + v, j + w, 0, 2, grid[i +v][j + w]))
                    elif (v, w) == (1, -1):
                        if (i + v >= 0 and i + v < len(grid)) and (j + w >= 0 and j + w < len(grid[0])):
                            if grid[i + v][j + w] != 1:
                                if b == 1:
                                    if grid[i +v][j + w] == 2:
                                        if d != 1 and d != 3 and d != 0: 
                                            ans = max(ans, 1 + dp(i + v, j + w, 0, 3, grid[i +v][j + w]))
                                elif b == 2:
                                    if grid[i +v][j + w] == 0:
                                        if d != 1 and d != 3 and d != 0: 
                                            ans = max(ans, 1 + dp(i + v, j + w, 0, 3, grid[i +v][j + w]))
                                elif b == 0:
                                    if grid[i +v][j + w] == 2:
                                        if d != 1 and d != 3 and d != 0: 
                                            ans = max(ans, 1 + dp(i + v, j + w, 0, 3, grid[i +v][j + w]))
                    
            return ans

        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # print("here")
                    cnt = max(cnt, 1 + dp(i, j, 1, 0, 1))
                    cnt = max(cnt, 1 + dp(i, j, 1, 1, 1))
                    cnt = max(cnt, 1 + dp(i, j, 1, 2, 1))
                    cnt = max(cnt, 1 + dp(i, j, 1, 3, 1))

        return (cnt)
                
