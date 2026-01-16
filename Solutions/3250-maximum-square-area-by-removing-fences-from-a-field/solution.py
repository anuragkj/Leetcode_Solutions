class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1,m])
        vFences.extend([1,n])
        hFences.sort()
        vFences.sort()
        h,v = len(hFences),len(vFences)
        seen_h=set()
        for i in range(h-1):
            for j in range(i+1,h):
                seen_h.add(hFences[j]-hFences[i])
        m=-1
        for i in range(v-1):
            for j in range(i+1,v):
                q = vFences[j]-vFences[i]
                if q in seen_h:
                    m = max(m,q)
        MOD = 10**9+7
        return m**2 % MOD if m>0 else -1

