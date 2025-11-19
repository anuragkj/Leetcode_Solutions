from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        # A quick optimization: if k is large enough, we can treat it as a simple BFS
        # without obstacles. The longest possible shortest path is rows + cols - 2.
        if k >= rows + cols - 2:
            return rows + cols - 2

        # State in queue: (row, col, steps, remaining_k)
        queue = deque([(0, 0, 0, k)])
        
        # visited[r][c] = stores the maximum k we had when we visited this cell.
        # Initialize with -1 to indicate not visited yet.
        visited = [[-1] * cols for _ in range(rows)]
        visited[0][0] = k
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c, steps, remaining_k = queue.popleft()

            if r == rows - 1 and c == cols - 1:
                return steps

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < rows and 0 <= new_c < cols:
                    # Case 1: The new cell is an empty cell (0)
                    if grid[new_r][new_c] == 0:
                        # If we can visit this cell with a better or equal k, explore it
                        if remaining_k > visited[new_r][new_c]:
                            visited[new_r][new_c] = remaining_k
                            queue.append((new_r, new_c, steps + 1, remaining_k))
                    
                    # Case 2: The new cell is an obstacle (1)
                    else:
                        # If we have eliminations left and can visit with a better k
                        if remaining_k > 0 and remaining_k - 1 > visited[new_r][new_c]:
                            visited[new_r][new_c] = remaining_k - 1
                            queue.append((new_r, new_c, steps + 1, remaining_k - 1))
        
        return -1
