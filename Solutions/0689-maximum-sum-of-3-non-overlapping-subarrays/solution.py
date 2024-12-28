class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Number of possible subarray starting positions
        n = len(nums) - k + 1

        # Calculate sum of all possible k-length subarrays
        sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            sums.append(sums[-1] - nums[i - k] + nums[i])

        # memo[i][j]: max sum possible starting from index i with j subarrays remaining
        memo = [[-1] * 4 for _ in range(n)]
        indices = []

        # First find optimal sum using DP
        self._dp(sums, k, 0, 3, memo)

        # Then reconstruct the path to find indices
        self._dfs(sums, k, 0, 3, memo, indices)

        return indices

    def _dp(self, sums, k, idx, rem, memo):
        if rem == 0:
            return 0
        if idx >= len(sums):
            return float("-inf") if rem > 0 else 0

        if memo[idx][rem] != -1:
            return memo[idx][rem]

        # Try taking current subarray vs skipping it
        with_current = sums[idx] + self._dp(sums, k, idx + k, rem - 1, memo)
        skip_current = self._dp(sums, k, idx + 1, rem, memo)

        memo[idx][rem] = max(with_current, skip_current)
        return memo[idx][rem]

    def _dfs(self, sums, k, idx, rem, memo, indices):
        if rem == 0 or idx >= len(sums):
            return

        with_current = sums[idx] + self._dp(sums, k, idx + k, rem - 1, memo)
        skip_current = self._dp(sums, k, idx + 1, rem, memo)

        # Choose path that gave optimal result in DP
        if with_current >= skip_current:  # Take current subarray
            indices.append(idx)
            self._dfs(sums, k, idx + k, rem - 1, memo, indices)
        else:  # Skip current subarray
            self._dfs(sums, k, idx + 1, rem, memo, indices)
