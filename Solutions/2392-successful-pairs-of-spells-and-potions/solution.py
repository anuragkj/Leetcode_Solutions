class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()  # Sort potions for binary search
        n = len(potions)  # Cache the length
        res = []  # Store results for each spell
        
        for i in range(len(spells)):  # Process each spell
            l, r = 0, n - 1  # Initialize binary search pointers
            
            while l <= r:  # Binary search for first successful potion
                m = (l + r) // 2  # Find middle potion
                if potions[m] * spells[i] < success:
                    l = m + 1  # Product too small, search right half
                else:
                    r = m - 1  # Product works, search left for earlier successes
            
            res.append(n - l)  # Count successful pairs from index l onwards
        
        return res  # Return all counts
