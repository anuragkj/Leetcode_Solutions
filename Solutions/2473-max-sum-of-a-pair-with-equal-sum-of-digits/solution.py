
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        lookup = collections.defaultdict(list)
        for num in nums:
            curSumDigits = self.getSumDigits(num)
            if curSumDigits in lookup:
                res = max(res, num + lookup[curSumDigits][0] * -1)
            heapq.heappush(lookup[curSumDigits], num*-1)
        return res
        
    def getSumDigits(self, number: int):
        sumDigits = 0
        for char in str(number):
            sumDigits += int(char)
        return sumDigits
		
