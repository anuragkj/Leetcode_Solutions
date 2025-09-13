class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 3 decisions: buy, sell, wait

        n = len(prices)
        dp = {}
        def dfs(price, day, cooldown):
            if day >= n: return 0

            key = (price, day, cooldown)
            if key in dp: return dp[key]

            res = 0
            # buy
            # if i sold and cooldown is over i can buy
            if price == -1 and cooldown == 0:
                res = max(res, dfs(prices[day], day + 1, 0))
            
            # wait
            # I can wait whenever, price doesnt change just day, and the cooldown becomes 0
            res = max(res, dfs(price, day + 1, 0))

            # sell
            # i only want to sell if my next price is greater than other wise there is no point in selling at a loss. (since we are maximizing)
            if prices[day] > price and price != -1:
                res = max(res, (prices[day] - price) + dfs(-1, day + 1, 1))

            dp[key] = res

            return res


        return dfs(-1, 0, 0)
