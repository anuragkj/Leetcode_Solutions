class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        d={}
        ans=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        
        maxval=max(d.values())
        maxkey=max(d,key=d.get)
        leftcnt=0
        rightcnt=maxval
        n=len(nums)
        for i in range(n):
            if nums[i]==maxkey:
                leftcnt+=1
                rightcnt-=1
            if leftcnt*2>(i+1) and rightcnt*2>(n-(i+1)):
                return i
        return -1




        
