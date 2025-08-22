class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(nums, i, n):
            nonlocal dp
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            steal = nums[i] + solve(nums, i + 2, n)
            skip = solve(nums, i + 1, n)
            dp[i] = max(steal,skip)
            return dp[i]

        n = len(nums)
        dp = [-1] * 101
        return solve(nums,0,n)
