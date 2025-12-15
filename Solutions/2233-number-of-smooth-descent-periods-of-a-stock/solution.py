class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        res = 1
        curr = 1
        for i in range(1, n):
            if prices[i - 1] - prices[i] == 1:
                curr += 1
            else:
                curr = 1
            res += curr
        return res
