class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a memoization table to store computed results
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        
        # Call the recursive function to compute unique paths
        return self.uniquePathsRecursive(0, 0, m, n, memo)
    
    def uniquePathsRecursive(self, x: int, y: int, m: int, n: int, memo: List[List[int]]) -> int:
        # If we reach the destination (bottom-right corner), return 1
        if x == m - 1 and y == n - 1:
            return 1
        
        # If we have already computed the result for this cell, return it from the memo table
        if memo[x][y] != -1:
            return memo[x][y]
        
        # Calculate the number of unique paths by moving right and down
        rightPaths = 0
        downPaths = 0
        
        # Check if it's valid to move right
        if x < m - 1:
            rightPaths = self.uniquePathsRecursive(x + 1, y, m, n, memo)
        
        # Check if it's valid to move down
        if y < n - 1:
            downPaths = self.uniquePathsRecursive(x, y + 1, m, n, memo)
        
        # Store the result in the memo table and return it
        memo[x][y] = rightPaths + downPaths
        return memo[x][y]
