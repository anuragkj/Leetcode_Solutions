class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(c0[1] - c1[1]), abs(c0[0] - c1[0])) for c0,c1 in pairwise(points))
