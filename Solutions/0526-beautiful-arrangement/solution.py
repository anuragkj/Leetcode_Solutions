from functools import lru_cache

class Solution:  
    def countArrangement(self, n: int) -> int:  
        @lru_cache(None)
        def count_beautiful(pos, mask):
            # Base case: all numbers have been placed
            if pos > n:
                return 1
            
            count = 0
            for num in range(1, n + 1):
                # Check if the number is not used (bitmask) and satisfies the conditions
                if not (mask & (1 << num)) and (num % pos == 0 or pos % num == 0):
                    # Mark the number as used by updating the bitmask
                    count += count_beautiful(pos + 1, mask | (1 << num))
            
            return count
        
        # Start with position 1 and an empty bitmask (0)
        return count_beautiful(1, 0)
