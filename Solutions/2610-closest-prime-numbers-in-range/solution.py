class Solution:
    def __init__(self):
        self.N = 10**6 + 2
        self.prime = [1] * self.N
        self.seive()

    def seive(self):
        self.prime[0] = self.prime[1] = 0
        for i in range(2, int(self.N**0.5) + 1):
            if self.prime[i]:
                for j in range(i * i, self.N, i):
                    self.prime[j] = 0

    def closestPrimes(self, left: int, right: int):
        prev, diff = -1, float('inf')
        ans = [-1, -1]

        for i in range(left, right + 1):
            if self.prime[i]:
                if prev != -1 and i - prev < diff:
                    ans = [prev, i]
                    diff = i - prev
                prev = i
        return ans
