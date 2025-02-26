class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_prefix = 0  # Tracks the smallest prefix sum
        max_prefix = 0  # Tracks the largest prefix sum
        max_abs_sum = 0

        for num in nums:
            prefix_sum += num
            max_abs_sum = max(max_abs_sum, abs(prefix_sum - min_prefix), abs(prefix_sum - max_prefix))
            min_prefix = min(min_prefix, prefix_sum)
            max_prefix = max(max_prefix, prefix_sum)

        return max_abs_sum
