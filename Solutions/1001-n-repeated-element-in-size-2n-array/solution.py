class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return next((nums[i] for i in range(1, len(nums)) if nums[i] in nums[:i]), None)
