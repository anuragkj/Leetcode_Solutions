class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ans = 0
        L = len(nums)
        # c < (a+b)
        for i in range(L-1,1,-1):
            c = nums[i]
            start = 0
            end = i-1
            while start < end:
                if nums[start] + nums[end] > c:
                    ans += end - start
                    end -= 1
                elif nums[start] + nums[end] <= c:
                    start += 1
        return ans
                
        
        
