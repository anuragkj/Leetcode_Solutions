class Solution:
    def maxProfit(self, a: List[int], b: List[int], k: int) -> int:
        return max([*accumulate((u*v-p-o*w+o for u,v,p,o,w in zip(a,b,a[k//2:],a[k:],b[k:])),
            initial=sum(map(mul,a,k//2*[0]+k//2*[1]+b[k:]))),sum(map(mul,a,b))])
