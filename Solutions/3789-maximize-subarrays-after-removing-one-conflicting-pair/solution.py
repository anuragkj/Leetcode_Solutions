import heapq
from collections import defaultdict

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: list[list[int]]) -> int:
        startAt = [[] for _ in range(n + 1)]
        for idx, (p1, p2) in enumerate(conflictingPairs):
            x, y = (p1, p2) if p1 < p2 else (p2, p1)
            startAt[x].append((y, idx))
        
        firstBlockingPos = [n] * (n + 2)
        secondBlockingPos = [n] * (n + 2)
        idxBlocking = [-1] * (n + 2)
        queue = []
        for i in range(n, 0, -1):
            for y, idx in startAt[i]:
                heapq.heappush(queue, (y, idx))
            if queue:
                y1, idx1 = queue[0]
                heapq.heappop(queue)
                y2 = queue[0][0] if queue else n + 1
                heapq.heappush(queue, (y1, idx1))
                firstBlockingPos[i] = y1 - 1
                secondBlockingPos[i] = y2 - 1 if y2 <= n else n
                idxBlocking[i] = idx1
            if firstBlockingPos[i] > firstBlockingPos[i + 1]:
                firstBlockingPos[i] = firstBlockingPos[i + 1]
                secondBlockingPos[i] = min(secondBlockingPos[i], secondBlockingPos[i + 1])
                idxBlocking[i] = idxBlocking[i + 1]
        validCnt = 0
        cand = defaultdict(int)
        for i in range(1, n + 1):
            validCnt += firstBlockingPos[i] - i + 1
            if idxBlocking[i] != -1 and secondBlockingPos[i] > firstBlockingPos[i]:
                cand[idxBlocking[i]] += secondBlockingPos[i] - firstBlockingPos[i]
        best = validCnt + max(cand.values(), default=0)
        return best
