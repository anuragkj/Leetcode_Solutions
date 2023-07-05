class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 0
        previousGroup = 0
        currentGroup = 0
        foundZero = False
        
        for i in range(n+1):
            if i < n and nums[i] == 0:
                foundZero = True
            if i < n and nums[i] == 1:
                currentGroup += 1
            else:
                longest = max(longest, previousGroup + currentGroup)
                previousGroup = currentGroup
                currentGroup = 0
        
        if not foundZero:
            return n - 1
        return longest
