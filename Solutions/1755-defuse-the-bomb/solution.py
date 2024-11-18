class Solution:
    def decrypt(self, A: List[int], k: int) -> List[int]:
        n = len(A)
        A  = A + A
        pref = list(accumulate([0] + A))
        
        if k == 0: return [0] * n
        elif k > 0: return [pref[i + k + 1] - pref[i + 1] for i in range(n)]
        else: return [pref[i + n] - pref[i + n + k] for i in range(n)]
