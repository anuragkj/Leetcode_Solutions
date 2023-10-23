class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        mask = 0x55555555
        return n > 0 and (n & (n - 1)) == 0 and (n & mask) == n
