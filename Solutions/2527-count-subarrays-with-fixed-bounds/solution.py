class Solution:
    def countSubarrays(self, nums, minK, maxK):
        n = len(nums)
        left_bound = -1  # Tracks the left boundary of valid subarrays
        last_minK = last_maxK = -1  # Last seen positions of minK and maxK
        count = 0
        
        for i in range(n):
            if not (minK <= nums[i] <= maxK):
                left_bound = i  # Reset when the number is out of bounds
            
            if nums[i] == minK:
                last_minK = i  # Update the position of minK
            if nums[i] == maxK:
                last_maxK = i  # Update the position of maxK
            
            # Count subarrays with both minK and maxK, valid from left_bound to the current index
            if last_minK != -1 and last_maxK != -1:
                count += max(0, min(last_minK, last_maxK) - left_bound)
        
        return count
