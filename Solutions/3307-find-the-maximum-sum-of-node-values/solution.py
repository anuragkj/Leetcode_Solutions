class Solution:
    def maximumValueSum(self, nums, k, edges):
        base_sum = sum(nums)
        gains = [(num ^ k) - num for num in nums]
        gains.sort(reverse=True)

        max_gain = 0
        current_gain = 0

        for i, g in enumerate(gains):
            current_gain += g
            if (i + 1) % 2 == 0:
                max_gain = max(max_gain, current_gain)

        return base_sum + max_gain
