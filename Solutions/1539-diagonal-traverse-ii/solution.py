class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        queue = deque([(0, 0)])
        ans = []
        
        while queue:
            row, col = queue.popleft()
            ans.append(nums[row][col])
            
            if col == 0 and row + 1 < len(nums):
                queue.append((row + 1, col))
                
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))
        
        return ans
