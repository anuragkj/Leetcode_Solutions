class Solution:
    def pow(self, x, n):
        if n == 0: return 1
        if n % 2 == 1:
            ret = self.pow(x, n - 1)
            return x * ret
        else:
            ret = self.pow(x, n//2)
            return ret * ret
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return pow(1/x, abs(n))
        else:
            return pow(x, abs(n))
