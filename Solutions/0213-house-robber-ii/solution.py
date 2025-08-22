class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dfs(i, first_taken):
            if i >= n:
                return 0

            not_take = dfs(i+1, first_taken)
            if i == 0:
                take = nums[i] + dfs(i+2, 1)
            elif i==n-1 and first_taken == 1:
                take = -float('inf')
            else:
                take = nums[i] + dfs(i+2, first_taken)

            return max(take, not_take)
        
        return dfs(0,0)
