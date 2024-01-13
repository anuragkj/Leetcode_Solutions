class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = {}
        counter_t = {}
        
        diff = 0
        
        for i in s:
            counter_s[i] = counter_s.get(i, 0) + 1
        for j in t:
            counter_t[j] = counter_t.get(j, 0) + 1
        
        for i in counter_s.keys():
            diff += (counter_s[i] - counter_t.get(i, 0)) if (counter_s[i] - counter_t.get(i, 0)) > 0 else 0
        
        return diff
