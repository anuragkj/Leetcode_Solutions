class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        heap = [(0, 0, 0)]
        visit = set()
        visit.add((0, 0))

        while heap:
            cost, r, c = heapq.heappop(heap)
            if r == ROWS - 1 and c == COLS - 1:
                return cost
            
            for dr, dc in directions:
                if min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS or (r + dr, c + dc) in visit:
                    continue
                visit.add((r + dr, c + dc))
                if grid[r + dr][c + dc] == 1:
                    heapq.heappush(heap, (cost + 1, r + dr, c + dc))
                else:
                    heapq.heappush(heap, (cost, r + dr, c + dc))
