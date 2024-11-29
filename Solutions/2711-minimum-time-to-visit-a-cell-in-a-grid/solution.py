from heapq import heappush, heappop
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1: 
            return -1
        heap = [(0,0,0)]
        visited = set()
        while heap:
            d, i, j = heappop(heap)
            if (i, j) in visited: continue
            visited.add((i,j))
            if (i, j) == (m-1, n-1): return d
            for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
                if 0 <= i + di < m and 0 <= j + dj < n and (i + di, j + dj) not in visited:
                    t = grid[i+di][j+dj]
                    gap = max(t-(d+1), 0)
                    heappush(heap, (d + 1 + gap + (gap%2), i + di, j + dj))
