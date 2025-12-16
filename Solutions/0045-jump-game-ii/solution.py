class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def dfs(i):
            if i == len(nums) - 1:
                return 0
            ret = float('inf')
            for j in range(1,nums[i]+1):
                if i+j<= len(nums) - 1:
                    ret = min(ret, 1+dfs(i+j))
            return ret
        
        return dfs(0)
