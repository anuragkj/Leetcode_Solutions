class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        memo = [-1] * len(nums)
        return self.dfs(0, nums, memo)

    def isValid2(self, a, b) -> bool:
        return a == b

    def isValid(self, a, b, c) -> bool:
        return (a == b) and (b == c)

    def isConsecutive(self, a, b, c) -> bool:
        return (c-b == 1) and (b-a == 1)

    def dfs(self, idx, nums: List[int], memo: List[int]) -> bool:
        n = len(nums)
        if idx == n:
            return 1
        if n-idx < 2:
            return 0
        if memo[idx] != -1:
            return memo[idx]
        # take 2 equal
        take2 = self.isValid2(nums[idx], nums[idx+1]) and self.dfs(idx+2, nums, memo)
        if n-idx < 3:
            # we don't need to consider 3 length subarray.
            memo[idx] = take2
            return take2
        # take 3 equal or consecutive increasing
        take3 = (self.isValid(nums[idx], nums[idx+1], nums[idx+2]) or self.isConsecutive(nums[idx], nums[idx+1], nums[idx+2])) and self.dfs(idx+3, nums, memo)
        memo[idx] = (take2 or take3)
        return memo[idx]
