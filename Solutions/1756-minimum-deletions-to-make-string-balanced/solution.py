class Solution:
    def minimumDeletions(self, s: str) -> int:
        cache = [[None]*2 for _ in range(len(s))]
        
        def dp(idx, b):
            if idx >= len(s):
                return 0
            if cache[idx][b] is None:
                if b:
                    if s[idx] == 'a':
                        res = 1 + dp(idx+1, b)
                    else:
                        res = dp(idx+1, b)
                else:
                    if s[idx] == 'b':
                        res = min(1 + dp(idx+1, b), dp(idx+1, 1))
                    else:
                        res = dp(idx+1, b)
                cache[idx][b] = res
            return cache[idx][b]
        
        return dp(0, 0)
