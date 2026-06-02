from typing import List

class Solution:
    def earliestFinishTime(self,landStartTime: List[int],landDuration: List[int],waterStartTime: List[int],waterDuration: List[int]) -> int:
        res = float('inf')
        n, m = len(landStartTime), len(waterStartTime)

        for i in range(n):  # loop over all land rides
            a, d = landStartTime[i], landDuration[i]  # a = start, d = duration of land ride
            for j in range(m):  # loop over all water rides
                b, e = waterStartTime[j], waterDuration[j]  # b = start, e = duration of water ride

                # Land → Water
                land_end = a + d
                start_water = max(land_end, b)
                finish1 = start_water + e

                # Water → Land
                water_end = b + e
                start_land = max(water_end, a)
                finish2 = start_land + d

                # Take the minimum of all finish times
                res = min(res, finish1, finish2)

        return res
