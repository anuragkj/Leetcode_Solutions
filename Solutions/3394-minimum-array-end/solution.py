class Solution:
    def minEnd(self, n: int, x: int) -> int:
        pos = 0
        n -= 1
        while n > 0:
            bit = n & 1
            n = n >> 1
            while x & (1 << pos) > 0:
                pos += 1
            x = x ^ bit << pos
            pos += 1
        return x
