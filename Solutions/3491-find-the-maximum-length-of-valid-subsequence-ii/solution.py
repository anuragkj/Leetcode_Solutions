class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # dp[i][t] := longest valid subsequence of nums by the end of index i and remonder of t s.t. t = 0, ..., k - 1
        dp = [[0 for _ in range(k)] for _ in range(n)]

        # possible sequence:
        # (0, 0, 0 ...) or (0, 1, 0, ...) or (0, 2, 0, ...) or (0, k - 1, 0, k - 1, ..)
        # (1, 0, 1 ...) or (1, 1, 1, ...) or (1, 2, 1, ...) or (1, k - 1, 1, k - 1, ..)
        # ...

        res = 0

        # fix the tail in dp
        for j in range(n):
            # search for the head to check nums[i:j]
            for i in range(j):
                # get remainder
                t = (nums[i] + nums[j])%k
                
                # jump from i to j 
                dp[j][t] = dp[i][t] + 1

                # update res
                res = max(res, dp[j][t])

        return res + 1
