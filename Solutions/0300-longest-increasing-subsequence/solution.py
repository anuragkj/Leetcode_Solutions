class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        ahead=[0]*(n+1)
        curr=[0]*(n+1)
        for ind in range(n-1,-1,-1):
            for prev in range(ind-1,-2,-1):
                not_take=0+ahead[prev+1]
                take=0
                if prev==-1 or nums[ind]>nums[prev]:
                    take=1+ahead[ind+1]
                curr[prev+1]=max(take,not_take)
            ahead=curr[:]
        return curr[0]
