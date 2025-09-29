from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_oranges = 0

        # 1. Initial scan to populate the queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c)) # Add all initial rotten oranges to the queue
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Edge case: If there are no fresh oranges, no time is needed.
        if fresh_oranges == 0:
            return 0

        minutes = 0
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # 2. Start the Multi-Source BFS
        while q and fresh_oranges > 0:
            # This loop processes one level (one minute) at a time
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc

                    # Check boundaries and if the neighbor is a fresh orange
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        # Rot the orange
                        grid[new_r][new_c] = 2
                        # Add it to the queue for the next level/minute
                        q.append((new_r, new_c))
                        # Decrement the count of fresh oranges
                        fresh_oranges -= 1
        
        # 3. Final Check: If fresh oranges remain, it's impossible.
        if fresh_oranges == 0:
            return minutes
        else:
            return -1
