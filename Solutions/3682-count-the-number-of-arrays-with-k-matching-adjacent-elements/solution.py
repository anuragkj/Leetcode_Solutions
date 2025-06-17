MOD = 1_000_000_007

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        if k < 0 or k >= n:          # impossible cases
            return 0

        runs = n - k                 # number of value segments

        # factorials mod MOD
        fact = [1] * n
        for x in range(1, n):
            fact[x] = fact[x - 1] * x % MOD

        # inverse factorials mod MOD  (using Fermat’s little theorem)
        inv_fact = [1] * n
        inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
        for x in range(n - 2, -1, -1):
            inv_fact[x] = inv_fact[x + 1] * (x + 1) % MOD

        # nCk  = fact[n-1] / (fact[k] * fact[n-1-k])
        choose = fact[n - 1] * inv_fact[k] % MOD * inv_fact[n - 1 - k] % MOD

        answer = (
            m                                   # first block
            * choose % MOD                      # choose equal positions
            * pow(m - 1, runs - 1, MOD) % MOD   # choices for the rest
        )
        return answer
