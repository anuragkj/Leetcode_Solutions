import collections
from typing import List

class Solution:
    def canCross(self, row, col, cells, day):
        # Create a grid initialized to 0 (land)
        grid = [[0] * col for _ in range(row)]
        queue = collections.deque()

        # Mark water cells for the current day
        # cells coordinates are 1-based, so convert to 0-based
        for r, c in cells[:day]:
            grid[r-1][c-1] = 1

        # Add all starting land cells from the top row to the queue
        # Note: The logic effectively runs BFS starting from available top-row cells
        for i in range(col):
            if not grid[0][i]:
                queue.append((0, i))
                grid[0][i] = -1  # Mark as visited
                           
            while queue:
                r, c = queue.popleft()
                if r == row - 1:
                    return True
                
                for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                    new_row, new_col = r + dr, c + dc
                    if 0 <= new_row < row and 0 <= new_col < col and grid[new_row][new_col] == 0:
                        grid[new_row][new_col] = -1  # Mark as visited
                        queue.append((new_row, new_col))
            
        return False

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left, right = 1, row * col
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if self.canCross(row, col, cells, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
            
            
