class Solution:
    MOD = 10**9 + 7

    def idealArrays(self, n: int, maxValue: int) -> int:
        # 1) Sieve for smallest prime divisor
        mind = [0] * (maxValue + 1)
        for p in range(2, maxValue + 1):
            if mind[p] == 0:
                for i in range(p, maxValue + 1, p):
                    if mind[i] == 0:
                        mind[i] = p

        # 2) Precompute binomial coefficients C(n+i-1, i) for i up to log2(maxValue)
        maxPow = int(log2(maxValue)) + 1
        C = [1] * (maxPow + 1)
        for i in range(1, maxPow + 1):
            C[i] = comb(n + i - 1, i) % self.MOD

        # 3) For each value i, factorize via mind[] and multiply the counts of partitions
        ans = 0
        for i in range(1, maxValue + 1):
            x, prod = i, 1
            while x > 1:
                p, exp = mind[x], 0
                while x % p == 0:
                    x //= p
                    exp += 1
                prod = prod * C[exp] % self.MOD
            ans = (ans + prod) % self.MOD

        return ans
