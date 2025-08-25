class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [nums[0]] + [-1]*(len(nums)-1)
        dp_min =[nums[0]] + [-1]*(len(nums)-1)

        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i])
            dp_min[i] = min(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i])

        return max(dp_max)
            
        
