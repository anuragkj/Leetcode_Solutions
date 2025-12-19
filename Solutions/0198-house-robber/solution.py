class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i >= len(nums):
                return 0
            return max(dfs(i+1),nums[i]+dfs(i+2))
        return dfs(0)
        
