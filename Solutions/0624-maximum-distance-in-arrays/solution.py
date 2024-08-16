class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            # Calculate the distance using the current min and max with the current array
            max_distance = max(max_distance, abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0]))
            
            # Update the global min and max values
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        
        return max_distance
