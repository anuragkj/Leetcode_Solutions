class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        kval = 0
        maxi = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                kval+=1
            while kval > k:
                if nums[l] == 0:
                    kval -= 1
                l+=1
            maxi = max(maxi,r-l+1)
        return maxi
