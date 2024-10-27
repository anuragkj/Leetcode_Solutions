class Solution:
    def solve(self, i, j, grid, dp):
        # If the cell lies outside the grid, return 0.
        if i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j] == 0:
            return 0
        # If we have already visited this cell, return the memoized value.
        if dp[i][j] != -1:
            return dp[i][j]
        # Find the answer for the cell to the right of the current cell.
        right = self.solve(i, j + 1, grid, dp)
        # Find the answer for the cell to the diagonal of the current cell.
        diagonal = self.solve(i + 1, j + 1, grid, dp)
        # Find the answer for the cell below the current cell.
        below = self.solve(i + 1, j, grid, dp)
        dp[i][j] = 1 + min(right, min(diagonal, below))
        return dp[i][j]

    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans += self.solve(i, j, matrix, dp)
        return ans
