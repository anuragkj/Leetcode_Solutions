class Solution:
    def separateSquares(self, a: List[List[int]]) -> float:
        h,w,q,tq = 0,0,0,sum(l*l for _,_,l in a)
        for y,l in sorted(e for _,y,l in a for e in ((y,l),(y+l,-l))):
            if (q:=q+w*(y-h))*2 >= tq: return y-(q-tq/2)/w
            h,w = y,w+l
