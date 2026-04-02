class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])

        profits = [[[-inf, -inf, -inf] for _ in range(n + 1)] for _ in range(m + 1)]
        profits[0][1] = [0, 0, 0]

        for i in range(m):
            for j in range(n):
                top = profits[i][j + 1]
                left = profits[i + 1][j]

                profit = coins[i][j]
                profits[i + 1][j + 1] = [
                    max(top[0], left[0]) + profit,
                    max(
                        max(top[0], left[0]),
                        max(top[1], left[1]) + profit
                    ),
                    max(
                        max(top[1], left[1]),
                        max(top[2], left[2]) + profit
                    ),
                ]
        return max(profits[m][n])
