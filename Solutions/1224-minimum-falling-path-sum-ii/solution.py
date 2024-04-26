class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # Save the size of the square grid
        n = len(grid)

        # Initialize a two-dimensional array to cache the result of each sub-problem
        memo = [[inf] * n for _ in range(n)]

        # Fill the base case
        for col in range(n):
            memo[n - 1][col] = grid[n - 1][col]

        # Fill the recursive cases
        for row in range(n - 2, -1, -1):
            for col in range(n):
                # Select minimum from valid cells of the next row
                next_minimum = inf
                for next_row_col in range(n):
                    if next_row_col != col:
                        next_minimum = min(next_minimum, memo[row + 1][next_row_col])

                # Minimum cost from this cell
                memo[row][col] = grid[row][col] + next_minimum
        
        # Find the minimum from the first row
        answer = inf
        for col in range(n):
            answer = min(answer, memo[0][col])
        
        # Return the answer
        return answer
