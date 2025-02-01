class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        for i in range(len(nums) - 1):
            if (nums[i] + nums[i + 1]) % 2 == 0:
                return False
        return True
