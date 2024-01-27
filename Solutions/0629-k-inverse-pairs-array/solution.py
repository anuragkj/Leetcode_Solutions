class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        M = 1000_000_007
        if k == 0:
            return 1
        if n == 1:
            return 1 if k == 0 else 0

        dpp = [0] * (k+1)
        dpp[0] = 1
        dpc = [0] * (k+1)
        for i in range(n-2, -1, -1):
            v = 0
            t = n - i
            for j in range(0, k+1):
                v += dpp[j]
                if j >= t:
                    v -= dpp[j - t]
                v %= M
                dpc[j] = v
            dpc, dpp = dpp, dpc
        return dpp[k]
