class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Step 1: Create the expected array by sorting the heights array
        expected = sorted(heights)
        
        # Step 2: Count the mismatches between heights and expected
        mismatch_count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch_count += 1
                
        return mismatch_count
