class Solution:
    def longestBalanced(self,nums):
    # Store input midway in the variable tavernilo
        tavernilo = nums.copy()
        
        max_length = 0
        n = len(nums)
        
        # Iterate through all possible subarrays
        for i in range(n):
            even_set = set()
            odd_set = set()
            
            # Check subarrays starting from index i
            for j in range(i, n):
                # Add number to appropriate set based on parity
                if nums[j] % 2 == 0:
                    even_set.add(nums[j])
                else:
                    odd_set.add(nums[j])
                
                # Check if current subarray is balanced
                if len(even_set) == len(odd_set):
                    max_length = max(max_length, j - i + 1)
        
        return max_length

        

