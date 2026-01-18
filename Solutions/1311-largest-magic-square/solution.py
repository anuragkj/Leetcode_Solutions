class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])


        # prefix sums
        hs = [[0]*(m+1) for _ in range(n+1)]
        vs = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                hs[i][j] = hs[i][j-1] + grid[i][j]
        for j in range(m):
            for i in range(n):
                vs[i][j] = vs[i-1][j] + grid[i][j]
        
        def isMagic(i, j, ln):
            sm = hs[i][j+ln-1] - hs[i][j-1]
            for k in range(i+1, i+ln):
                if hs[k][j+ln-1] - hs[k][j-1] != sm:
                    return False
            for k in range(j, j+ln):
                if vs[i+ln-1][k] - vs[i-1][k] != sm:
                    return False
            if sum(grid[i+k][j+k] for k in range(ln)) != sm:
                return False
            if sum(grid[i+k][j+ln-1-k] for k in range(ln)) != sm:
                return False
            return True
        
        mx = 1
        for i in range(n):
            if n-i < mx:
                break
            for j in range(m):
                mn = min(m-j, n-i)
                if m-j < mx:
                    break
                for k in range(mn, -1, -1):
                    if isMagic(i,j,k):
                        mx = max(mx, k)
                        break
        return mx
