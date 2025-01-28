class Solution:
    def dfs(self, grid, visited, row, col):
        n = len(grid)
        m = len(grid[0])

        # Boundary checks and already visited or water cell checks
        if row < 0 or col < 0 or row >= n or col >= m or grid[row][col] == 0 or visited[row][col]:
            return 0

        # Mark the cell as visited
        visited[row][col] = True

        # Collect fish from the current cell
        total_fishes = grid[row][col]

        # Perform DFS in all 4 directions
        total_fishes += self.dfs(grid, visited, row + 1, col)  # Down
        total_fishes += self.dfs(grid, visited, row - 1, col)  # Up
        total_fishes += self.dfs(grid, visited, row, col + 1)  # Right
        total_fishes += self.dfs(grid, visited, row, col - 1)  # Left

        return total_fishes

    def findMaxFish(self, grid):
        n = len(grid)
        m = len(grid[0])
        max_fish = 0

        # Visited matrix to track which cells have been processed
        visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                # Start a DFS for each unvisited cell containing fish
                if grid[i][j] > 0 and not visited[i][j]:
                    max_fish = max(max_fish, self.dfs(grid, visited, i, j))

        return max_fish
