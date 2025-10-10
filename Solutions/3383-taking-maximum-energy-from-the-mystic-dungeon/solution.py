class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        dp = [0] * len(energy)
        
        for i in range(len(energy)-1, len(energy)-k-1, -1):
            dp[i] = energy[i]

        for i in range(len(energy)-k-1, -1, -1):
            dp[i] = energy[i] + dp[i+k]
        
        return max(dp)

        
