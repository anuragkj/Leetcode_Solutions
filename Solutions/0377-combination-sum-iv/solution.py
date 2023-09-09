class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort() 
        memo = {}
        
        def helper(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < nums[0]:
                return 0
            
            count = 0
            for num in nums:
                if n - num < 0:
                    break 
                count += helper(n - num)
                
            memo[n] = count
            return count
        
        return helper(target)
        
