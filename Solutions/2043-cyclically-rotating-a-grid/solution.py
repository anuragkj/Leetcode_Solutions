class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for l in range(layers):
            vals = []
            top, left = l, l
            bottom, right = m - l - 1, n - l - 1

            # top row
            for j in range(left, right):
                vals.append(grid[top][j])
            # right col
            for i in range(top, bottom):
                vals.append(grid[i][right])
            # bottom row
            for j in range(right, left, -1):
                vals.append(grid[bottom][j])
            # left col
            for i in range(bottom, top, -1):
                vals.append(grid[i][left])

            length = len(vals)
            shift = k % length
            vals = vals[shift:] + vals[:shift]

            idx = 0
            # put back
            for j in range(left, right):
                grid[top][j] = vals[idx]; idx += 1
            for i in range(top, bottom):
                grid[i][right] = vals[idx]; idx += 1
            for j in range(right, left, -1):
                grid[bottom][j] = vals[idx]; idx += 1
            for i in range(bottom, top, -1):
                grid[i][left] = vals[idx]; idx += 1

        return grid
