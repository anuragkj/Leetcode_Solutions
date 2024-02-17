class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        pq = []
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if len(pq) < ladders:
                    heappush(pq, diff)
                else:
                    if not pq or pq[0] >= diff:
                        bricks -= diff
                    else:
                        poll = heappop(pq)
                        heappush(pq, diff)
                        bricks -= poll
                    if bricks < 0:
                        return i
        return n-1
