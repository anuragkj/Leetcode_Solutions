class Solution:
    def longestMonotonicSubarray(self, nums):
        if not nums:
            return 0

        max_length = 1
        inc, dec = 1, 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1

            max_length = max(max_length, max(inc, dec))

        return max_length
