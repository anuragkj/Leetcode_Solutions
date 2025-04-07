from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def sum_of(nums: List[int]) -> int:
            return sum(nums)

        def rec(i: int, nums: List[int], n: int, target: int, dp: List[List[int]]) -> bool:
            if target == 0:
                return True
            if target < 0 or i >= n:
                return False
            if dp[i][target] != -1:
                return dp[i][target] == 1

            dont = rec(i + 1, nums, n, target, dp)
            pick = rec(i + 1, nums, n, target - nums[i], dp) if nums[i] <= target else False
            
            dp[i][target] = 1 if pick or dont else 0
            return pick or dont

        n = len(nums)
        total_sum = sum_of(nums)
        if total_sum % 2 == 1:
            return False
        target = total_sum // 2

        dp = [[-1] * (target + 1) for _ in range(n)]
        return rec(0, nums, n, target, dp)
