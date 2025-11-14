class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]
        
        for r1, c1, r2, c2 in queries:
            for i in range(r1, r2 + 1):
                mat[i][c1] += 1
                if c2 + 1 < n:
                    mat[i][c2 + 1] -= 1
        
        for i in range(n):
            cur = 0
            for j in range(n):
                mat[i][j] += cur
                cur = mat[i][j]
        
        return mat
