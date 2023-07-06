class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, win_sum = 0, 0, 0
        ret = float('inf')

        for right in range(len(nums)):
            win_sum += nums[right]

            while(win_sum >= target):
                ret = min(ret, right - left + 1)
                win_sum -= nums[left]
                left += 1

        if ret == float('inf'):
            return 0
        else:
            return ret
        

