class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) in [0,1]:
            return 0
        
        res = 0

        for i in range(1, len(points)):
            x1,y1 = points[i]
            x0,y0 = points[i-1]

            dif_x = abs(x1-x0)
            dif_y = abs(y1-y0)

            min_dif = min(dif_x,dif_y)

            res += min_dif + dif_x-min_dif + dif_y-min_dif

        return res

