class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == 0 or len(nums)==1: return 0
        check = 1 if nums[0]==0 else 0
        maxi = 1
        l = 0
        for r in range(1, len(nums)):
            if nums[r] == 0:
                check += 1
            while check > 1:
                if nums[l] == 0:
                    check -= 1
                l+=1
            maxi = max(maxi, r-l)
        return maxi
