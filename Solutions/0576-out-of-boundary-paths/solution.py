class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        moves=[(1, 0), (-1,0), (0, 1), (0,-1)]
        @cache
        def f(i, j, moveLeft):
            if i<0 or i==m or j<0 or j==n: return 1
            if moveLeft==0: return 0
            ans=0
            for a, b in moves:
                ans=(ans+f(i+a, j+b, moveLeft-1))%(10**9+7)
            return ans
        return f(startRow, startColumn, maxMove)

        
