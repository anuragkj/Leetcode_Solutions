class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1
        mini, maxi = 1, max(dist)
        tmp = hour - len(dist) + 1
        if tmp < 1:
            maxi = max(maxi, ceil(dist[-1]/tmp))
        d1, d2 = dist[:-1], dist[-1]
        res = -1
        while mini <= maxi:
            if mini == maxi:
                return mini
            speed = (mini+maxi)//2
            time = 0
            for d in d1:
                time += ceil(d/speed)
            time += (d2/speed)
            if time <= hour:
                res = speed
                maxi = speed
            else:
                mini = speed + 1
        return res
