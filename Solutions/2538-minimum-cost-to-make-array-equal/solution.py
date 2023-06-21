class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        pairs = [[i,j] for i,j in zip(nums,cost)]
        pairs.sort()
        size = 0
        for c in cost:
            size += c
        total = (size + 1) // 2
        i = 0
        while total - pairs[i][1] > 0 and i < len(pairs):
            total -= pairs[i][1]
            i += 1
        median = pairs[i][0]
        ans = 0
        for p in pairs:
            ans += abs(median - p[0]) * p[1]
        return ans
