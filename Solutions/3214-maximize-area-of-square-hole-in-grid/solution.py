class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        v, h = 1, 1
        hBars.sort()
        vBars.sort()
        cur = 1
        for i in range(1, len(hBars)):
            if hBars[i] - hBars[i-1] == 1: cur += 1
            else: cur = 1
            h = max(h, cur)

        cur = 1
        for i in range(1, len(vBars)):
            if vBars[i] - vBars[i-1] == 1: cur += 1
            else: cur = 1
            v = max(v, cur)

        sq = min(h, v)
        return (sq + 1) ** 2
