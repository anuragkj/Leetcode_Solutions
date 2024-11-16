class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        if n==1 or k==1: return nums
        ans=[-1]*(n-k+1)
        Len=1
        for r in range(1, n):
            Len=Len+1 if nums[r]==nums[r-1]+1 else 1
            if Len>=k: ans[r-k+1]=nums[r]
        return ans
        
