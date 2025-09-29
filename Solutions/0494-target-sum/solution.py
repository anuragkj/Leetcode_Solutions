class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            ways = 0
            ways += dfs(i+1, total + nums[i])
            ways += dfs(i+1, total - nums[i])
            return ways
        ret = dfs(0,0)
        return ret

