class Solution:
    def __init__(self):
        self.dp = []
        self.OFFSET = 1000  # Offset to handle negative target values

    def solve(self, ind, nums, target):
        # Base cases
        if ind >= len(nums):
            return 1 if target == 0 else 0

        # Check if already computed
        if self.dp[ind][target + self.OFFSET] != -1:
            return self.dp[ind][target + self.OFFSET]

        # Recursively calculate the number of ways
        ans = 0
        ans += self.solve(ind + 1, nums, target - nums[ind])  # Subtract current number
        ans += self.solve(ind + 1, nums, target + nums[ind])  # Add current number

        # Store result in dp array
        self.dp[ind][target + self.OFFSET] = ans
        return ans

    def findTargetSumWays(self, nums, target):
        # Initialize dp array with -1
        self.dp = [[-1] * 3002 for _ in range(len(nums))]
        return self.solve(0, nums, target)  # Start recursion from index 0
