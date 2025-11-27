class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sel = nums[0]
        max_glo = nums[0]

        for i in range(1, len(nums)):
            max_sel =  max(max_sel + nums[i], nums[i])
            max_glo = max(max_sel, max_glo)

        return max_glo
