from heapq import heappush, heappop

class Solution:
    def findScore(self, nums):
        n = len(nums)
        pq = []
        for i, val in enumerate(nums):
            heappush(pq, (val, i))
        
        sum_ = 0
        vis = [False] * n
        while pq:
            val, ind = heappop(pq)
            if vis[ind]:
                continue
            sum_ += val
            vis[ind] = True
            if ind - 1 >= 0:
                vis[ind - 1] = True
            if ind + 1 < n:
                vis[ind + 1] = True
        return sum_
