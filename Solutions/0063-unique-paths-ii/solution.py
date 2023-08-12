class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo={}
        def uniquePathsWithObstacleHelper(i,j,obstacleGrid):
            if i==len(obstacleGrid)-1 and j==len(obstacleGrid[0])-1 and obstacleGrid[i][j]==1:
                return 0
            if i==len(obstacleGrid)-1 and j==len(obstacleGrid[0])-1:
                return 1
            if i>len(obstacleGrid)-1 or j>len(obstacleGrid[0])-1 or obstacleGrid[i][j]==1:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)]=uniquePathsWithObstacleHelper(i+1,j,obstacleGrid)+uniquePathsWithObstacleHelper(i,j+1,obstacleGrid)
            return memo[(i,j)]
        return uniquePathsWithObstacleHelper(0,0,obstacleGrid)
