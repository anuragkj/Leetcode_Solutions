from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)

        while left < right:
            mid = (left + right) // 2
            if self.canRob(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        
        return left

    def canRob(self, nums: List[int], k: int, capability: int) -> bool:
        count, i = 0, 0
        while i < len(nums):
            if nums[i] <= capability:
                count += 1
                i += 2
            else:
                i += 1
            if count >= k:
                return True
        return count >= k
