import heapq
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(g) == 0 or len(s) == 0:
            return 0
        heapq._heapify_max(g) 
        heapq._heapify_max(s) 
        res = 0
        gpop = heapq._heappop_max(g)
        spop =  heapq._heappop_max(s)

        while (True):
            print(gpop, spop)
            if gpop <= spop:
                res += 1
                if (len(s) > 0):
                    spop =  heapq._heappop_max(s)
                else:
                    break
            if (len(g) > 0):
                gpop = heapq._heappop_max(g)
            else:
                break

        return res
