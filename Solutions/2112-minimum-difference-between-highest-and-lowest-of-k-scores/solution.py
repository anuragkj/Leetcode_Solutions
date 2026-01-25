class Solution:
    def minimumDifference(self, a: List[int], k: int) -> int:
        return min(map(sub,(b:=sorted(a))[k-1:],b))
