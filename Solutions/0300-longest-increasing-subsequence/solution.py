class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if len(res) == 0 or res[-1] < i:
                res.append(i)
            else:
                pos = bisect.bisect_left(res,i)
                res[pos] = i
        return len(res)
