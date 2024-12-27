class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        mp = {}
        
        def solve(i, taken):
            if taken >= 2:
                return 0
            
            if i >= len(values):
                return -math.inf
            
            key = (i, taken)
            if key in mp:
                return mp[key]
            
            pick, notPick = values[i] + solve(i + 1, taken + 1), solve(i + 1, taken)
            
            if taken == 1:
                pick -= i
            else:
                pick += i
            
            mp[key] = max(pick, notPick)
            return mp[key]
        
        return solve(0, 0)
        
