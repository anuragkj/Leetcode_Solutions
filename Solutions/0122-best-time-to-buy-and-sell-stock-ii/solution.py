class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        held = prices[0]
        for i in range(len(prices)):
            if prices[i] >= held:
                profit += prices[i] - held
            held = prices[i]

        return profit
