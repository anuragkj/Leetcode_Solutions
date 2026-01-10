fmax = lambda a, b: a if a > b else b


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        dp = [0] * (n1 + 1)
        for i in range(n2):
            dp2 = [0] * (n1 + 1)
            for j in range(n1):
                dp2[j] = fmax(dp2[j - 1], dp[j])
                if s2[i] == s1[j]:
                    dp2[j] = fmax(dp2[j], ord(s1[j]) + dp[j - 1])
            dp = dp2
        return sum(ord(c) for c in s1) + sum(ord(c) for c in s2) - 2 * dp[-2]
