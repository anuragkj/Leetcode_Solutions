class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        biggest = 0
        second_biggest = 0
        smallest = inf
        second_smallest = inf
        
        for num in nums:
            if num > biggest:
                second_biggest = biggest
                biggest = num
            else:
                second_biggest = max(second_biggest, num)
                
            if num < smallest:
                second_smallest = smallest
                smallest = num
            else:
                second_smallest = min(second_smallest, num)
        
        return biggest * second_biggest - smallest * second_smallest
