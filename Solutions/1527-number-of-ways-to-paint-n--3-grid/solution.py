class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 1000000007
        alternating_patterns, all_different_patterns = 6, 6
        
        for i in range(2, n + 1):
            new_alternating = (3 * alternating_patterns + 2 * all_different_patterns) % MOD
            new_all_different = (2 * alternating_patterns + 2 * all_different_patterns) % MOD
            alternating_patterns, all_different_patterns = new_alternating, new_all_different
        
        return (alternating_patterns + all_different_patterns) % MOD
