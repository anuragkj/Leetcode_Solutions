class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = int(1e9 + 7)

        @cache
        def ternary(n, m):
            if n == 0:
                return [0] * m
            nums = []
            while n:
                n, r = divmod(n, 3)
                nums.append(r)
            return nums + [0] * (m - len(nums))

        dp = defaultdict(int)
        for i in range(3**m):
            x = ternary(i, m)
            if all(x[j] != x[j + 1] for j in range(len(x) - 1)):
                dp[i] = 1
        temp = dp.keys()
        states = defaultdict(list)
        for j in temp:
            x = ternary(j, m)
            for k in temp:
                y = ternary(k, m)
                if all(xi != yi for xi, yi in zip(x, y)):
                    states[j].append(k)
        for i in range(n - 1):
            new = defaultdict(int)
            for j in states:
                for k in states[j]:
                    new[j] = (new[j] + dp[k]) % mod
            dp = new
        return sum(dp.values()) % mod
