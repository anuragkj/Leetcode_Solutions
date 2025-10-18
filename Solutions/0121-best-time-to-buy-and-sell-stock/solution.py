class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = [-1]*len(prices)
        ind = len(prices) - 1
        max_val = -1
        for i in prices[::-1]:
            print(i)
            if max_val < i:
                max_val = i
            print(ind)
            maxi[ind] = max_val
            ind -= 1
        ret = -1
        for i in range(len(prices)):
            ret = max(ret, maxi[i] - prices[i])
        return ret

