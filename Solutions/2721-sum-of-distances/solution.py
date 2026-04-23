class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        #finding the indexes who are duplicate value of that element
        d1={}
        for i in range (len(nums)):
            if nums[i] not in d1:
                d1[nums[i]]=[]
                d1[nums[i]].append(i)
            else:
                d1[nums[i]].append(i)
        # dictionary look like this {1:[0,2,3],3:[1],2:[4]}
        ans=[0]*(len(nums))
        #making ans of nth length
        for key,val in d1.items():
            suff=sum(val)#suffix sum
            pre=0#prefix sum
            s=len(val)#len(suffix)
            p=0#len(pre)
            for i in val:#iterate in the indexes value like [0,2,3]:
                pre+=i #pass1:pre=0
                p+=1#p=1
                suff-=i#suff=5-0=5
                s-=1#s=2
                ans[i]=(-pre+p*i-s*i+suff)#ans[0]=(-0+1*0-2*0+5)=5
        return ans
        
