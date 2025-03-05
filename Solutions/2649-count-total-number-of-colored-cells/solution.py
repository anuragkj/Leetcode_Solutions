class Solution:
    def coloredCells(self, n: int) -> int:
        x=n-1
        res=1+4*(x*(x+1))/2
        return int(res)
