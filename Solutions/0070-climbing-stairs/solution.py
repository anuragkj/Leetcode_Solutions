class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(i):
            if i == 0:
                return 1
            
            one_stair = dfs(i-1)
            two_stair = 0
            if i >=2:
                two_stair = dfs(i-2)
            return one_stair + two_stair
        return dfs(n)
        
