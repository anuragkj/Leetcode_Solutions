class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = [0] * len(nums)
        res = []
        
        for num in nums:
            freq[num] += 1
        
        for i in range(len(freq)):
            if freq[i] == 2:
                res.append(i)
        
        return res
