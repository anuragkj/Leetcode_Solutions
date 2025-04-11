class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c=0
        for i in range(low,high+1):
            n=str(i)
            x=len(n)
            if x%2==0:
                left=int(x/2)
                l=[]
                for j in n:
                    l.append(int(j))
                if sum(l[:left])==sum(l[left:]):
                    c=c+1
        return c
        
