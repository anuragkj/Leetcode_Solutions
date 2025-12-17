class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        N = len(prices)

        @cache
        # Don't have any pending transactions, free to do anything (normal, short, nothing) today
        def free(index, k):
            if index == N:
                return 0
            
            max_profit = 0
            if k > 0:
                # Normal: buy today, sell later
                max_profit = max(max_profit, can_sell(index+1, k-1) - prices[index])

                # Short: sell today, buy later
                max_profit = max(max_profit, can_buy(index+1, k-1) + prices[index])

            # Do nothing for today
            max_profit = max(max_profit, free(index+1, k))
            return max_profit
        
        @cache
        # If you shorted a stock, use this function to buy back the stock
        def can_buy(index, k):
            if index == N:
                # We aren't able to buy back this stock, so invalid choice
                return -inf
            
            # Buy today
            max_profit = free(index+1, k) - prices[index]
            # Don't buy yet
            max_profit = max(max_profit, can_buy(index+1, k))
            return max_profit
        
        @cache
        # If you bought a stock (in a normal transaction), use this function to sell back the stock
        def can_sell(index, k):
            if index == N:
                # We aren't able to sell back this stock, so invalid choice since we wasted money buying it
                return -inf
            
            # Sell today
            max_profit = free(index+1, k) + prices[index]
            # Don't sell yet
            max_profit = max(max_profit, can_sell(index+1, k))
            return max_profit
        
        max_profit = free(0, k)

        # Clear cache for subsequent calls to LC test cases
        can_sell.cache_clear()
        can_buy.cache_clear()
        free.cache_clear()
        
        return max_profit
