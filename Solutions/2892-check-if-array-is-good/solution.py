class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n, s = len(nums) - 1, set(nums)
        if n not in s:
            return False
        for i in range(1, n):
            if i not in s:
                return False
        return nums.index(n) != len(nums) - 1 - nums[::-1].index(n)
