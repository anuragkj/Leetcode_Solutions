class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix = 0 
        suffix = sum(nums)
        ans = []
        for x in nums: 
            prefix += x
            ans.append(abs(prefix - suffix))
            suffix -= x
        return ans 
