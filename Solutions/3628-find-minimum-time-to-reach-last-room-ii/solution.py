class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        min_time = [[inf]*n for _ in range(m)]
        min_time[0][0] = 0
        heap = [(0, 1, 0, 0)] 
        while heap:
            t, s, i, j = heappop(heap)
            if i == m-1 and j == n-1:
                return t
            if t == min_time[i][j]:
                ss = 3 - s
                for ii, jj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if 0 <= ii < m and 0 <= jj < n:
                        tt = max(t, moveTime[ii][jj]) + s
                        if min_time[ii][jj] > tt:
                            min_time[ii][jj] = tt
                            heappush(heap, (tt, ss, ii, jj))
