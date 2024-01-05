
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n)]
        return self.f(0, -1, nums, n, dp)

    def f(self, index, prevInd, nums, n, dp):
        if index == n:
            return 0
        if dp[index][prevInd + 1] != -1:
            return dp[index][prevInd + 1]
        length = 0 + self.f(index + 1, prevInd, nums, n, dp)
        if prevInd == -1 or nums[index] > nums[prevInd]:
            length = max(length, 1 + self.f(index + 1, index, nums, n, dp))
        dp[index][prevInd + 1] = length
        return length

