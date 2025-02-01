class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        topSum = sum(grid[0])
        botSum = 0
        min2 = float('inf')
        for col in range(len(grid[0])):
            topSum -= grid[0][col]
            min2 = min(min2, max(topSum, botSum))
            botSum += grid[1][col]
        return min2
