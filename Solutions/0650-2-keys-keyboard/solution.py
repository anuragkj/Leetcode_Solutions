class Solution:
    def minSteps(self, n: int) -> int:
        dp = [1000] * (n + 1)

        # Base case
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                # Copy All and Paste (i-j) / j times
                # for all valid j's
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)

        return dp[n]
