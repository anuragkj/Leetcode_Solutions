class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        dp = [[dict() for _ in range(cols)] for _ in range(rows)]
        dp[0][0][0] = 0

        for r in range(rows):
            for c in range(cols):
                # For each possible way to (r, c) 
                # try to explore it further down and right
                for cost in dp[r][c]:
                    # go right
                    if c + 1 < cols:
                        costnew = cost + int(grid[r][c + 1] > 0)
                        if costnew <= k:
                            dp[r][c + 1][costnew] = max(
                                dp[r][c + 1].get(costnew, -1),
                                dp[r][c][cost] + grid[r][c + 1],
                            )

                    # go down
                    if r + 1 < rows:
                        costnew = cost + int(grid[r + 1][c] > 0)
                        if costnew <= k:
                            dp[r + 1][c][costnew] = max(
                                dp[r + 1][c].get(costnew, -1),
                                dp[r][c][cost] + grid[r + 1][c],
                            )

        scores = dp[-1][-1].values()
        return max(scores) if len(scores) > 0 else -1
