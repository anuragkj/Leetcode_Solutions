class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_suffix = [0] * n  # max value from index i to the end
        max_k = 0

        # Precompute max suffix values for nums[k]
        for i in range(n - 1, 1, -1):
            max_k = max(max_k, nums[i])
            max_suffix[i - 1] = max_k

        max_i = nums[0]
        result = 0

        for j in range(1, n - 1):
            triplet_value = (max_i - nums[j]) * max_suffix[j]
            result = max(result, triplet_value)
            max_i = max(max_i, nums[j])  # update max_i for next j

        return result
