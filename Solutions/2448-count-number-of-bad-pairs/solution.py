class Solution:
    def countBadPairs(self, nums):
        freq = {}
        good = 0
        
        for i in range(len(nums)):
            key = nums[i] - i
            good += freq.get(key, 0)  # Get the count of good pairs for this key
            freq[key] = freq.get(key, 0) + 1  # Increment the count for this key
        
        total_pairs = len(nums) * (len(nums) - 1) // 2  # Total pairs (i, j) with i < j
        return total_pairs - good  # Bad pairs = Total pairs - Good pairs
