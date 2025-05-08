class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])

        # dist[r][c] = best known arrival time at (r,c)
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0  # start at (0,0) at t=0

        # min-heap of (arrival_time, r, c)
        pq = [(0, 0, 0)]

        # Directions: right, left, down, up
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]

        while pq:
            t, r, c = heapq.heappop(pq)
            if t > dist[r][c]:
                continue
            if r == n-1 and c == m-1:
                return t

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    # wait until neighbor unlocks, then move
                    depart = max(t, moveTime[nr][nc])
                    arrive = depart + 1
                    if arrive < dist[nr][nc]:
                        dist[nr][nc] = arrive
                        heapq.heappush(pq, (arrive, nr, nc))

        return -1  # unreachable per problem constraints
