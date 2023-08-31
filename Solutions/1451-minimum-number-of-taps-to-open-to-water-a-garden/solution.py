class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = [(max(center - radius, 0), center + radius) for center, radius in enumerate(ranges)]
        prev = -1
        curr = 0
        ans = 0
        for l, r in sorted(intervals):
            if curr >= n or l > curr:  # reached or cannot cover
                break
            elif prev < l <= curr:
                ans += 1
                prev = curr
            curr = max(curr, r)
        return ans if curr >= n else -1
