class Solution:
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        total = 0

        row = [0] * m
        col = [0] * n

        for i in range(m):
            for j in range(n):
                total += grid[i][j]
                row[i] += grid[i][j]
                col[j] += grid[i][j]

        if total % 2 != 0:
            return False

        target = total // 2

        curr = 0
        for i in range(m - 1):
            curr += row[i]
            if curr == target:
                return True

        curr = 0
        for j in range(n - 1):
            curr += col[j]
            if curr == target:
                return True

        return False
