class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = float('-inf')
        ret = 0
        for i in prices[::-1]:
            ret = max(ret, maxi-i)
            maxi = max(maxi, i)
            print(ret, maxi)
        return ret
