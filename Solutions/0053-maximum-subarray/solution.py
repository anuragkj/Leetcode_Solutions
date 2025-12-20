class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = -float('inf')
        curr_sum = nums[0]
        for i in range(1,len(nums)):
            maxi = max(curr_sum, maxi)
            curr_sum = max(curr_sum+nums[i],nums[i])
        return max(curr_sum, maxi)
