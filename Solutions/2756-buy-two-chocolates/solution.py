class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Assume minimum and second minimum
        minimum = min(prices[0], prices[1])
        second_minimum = max(prices[0], prices[1])

        # Iterate over the remaining elements
        for i in range(2, len(prices)):
            if prices[i] < minimum:
                second_minimum = minimum
                minimum = prices[i]
            elif prices[i] < second_minimum:
                second_minimum = prices[i]
            
        # Minimum Cost
        min_cost = minimum + second_minimum

        # We can buy chocolates only if we have enough money
        if min_cost <= money:
            # Return the Amount of Money Left
            return money - min_cost
        
        # We cannot buy chocolates. Return the initial amount of money
        return money
