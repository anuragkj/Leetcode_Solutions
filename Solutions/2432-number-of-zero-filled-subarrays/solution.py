class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        s=0
        for i in range(n):
            if nums[i]==0:
                c+=1
            else:
                s+=(c*(c+1))//2
                c=0
        s+=(c*(c+1))//2
        return s
