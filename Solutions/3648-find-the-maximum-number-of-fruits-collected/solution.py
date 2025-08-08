class Solution:
    def maxCollectedFruits(self, mat: List[List[int]]) -> int:
        self.n = len(mat)
        self.memo = [[-1] * self.n for _ in range(self.n)]

        def dfs3(row, col):
            if row < 0 or col < 0 or row >= self.n or col >= self.n:
                return 0

            if self.memo[row][col] != -1:
                return self.memo[row][col]

            val = mat[row][col]
            res = 0

            # row = i, col = j
            if row == col:
                res = max(res, dfs3(row + 1, col + 1))
            elif row - 1 == col:
                res = max(res,
                          dfs3(row + 1, col + 1),
                          dfs3(row, col + 1))
            else:
                res = max(res,
                          dfs3(row + 1, col + 1),
                          dfs3(row, col + 1),
                          dfs3(row - 1, col + 1))

            self.memo[row][col] = val + res
            return self.memo[row][col]

        def dfs2(row, col):
            if row < 0 or col < 0 or row >= self.n or col >= self.n:
                return 0

            if self.memo[row][col] != -1:
                return self.memo[row][col]

            val = mat[row][col]
            res = 0

            if row == col:
                res = max(res, dfs2(row + 1, col + 1))
            elif row == col - 1:
                res = max(res,
                          dfs2(row + 1, col + 1),
                          dfs2(row + 1, col))
            else:
                res = max(res,
                          dfs2(row + 1, col + 1),
                          dfs2(row + 1, col),
                          dfs2(row + 1, col - 1))

            self.memo[row][col] = val + res
            return self.memo[row][col]

        total = 0

        # child - 1
        # he will eat all diagonal fruits, so set them to 0 
        for i in range(self.n):
            total += mat[i][i]
            mat[i][i] = 0

        # child - 2
        total += dfs3(self.n - 1, 0)
        # child - 3
        total += dfs2(0, self.n - 1)

        return total
