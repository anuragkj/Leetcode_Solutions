class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            if nums[i] == 1:                  
                for j in range(1, k + 1):
                    if i + j < len(nums):    
                        if nums[i + j] == 1:  
                            return False
        return True
