class Solution:
    def minWindow(self, s: str, t: str) -> str:
        a, c, d, r = 0, Counter(), Counter(t), [inf, '']
        for b in range(len(s)):
            c[s[b]] += 1
            while c >= d:
                r = min(r, [b-a+1, s[a:b+1]])
                c[s[a]] -= 1
                a += 1
        
        return r[1]
