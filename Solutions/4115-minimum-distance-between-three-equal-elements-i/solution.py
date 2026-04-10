mn = lambda x,y: x if x < y else y

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        res = inf
        d = defaultdict(list)

        for idx, key in enumerate(nums):
            d[key].append(idx)
            if len(d[key])  < 3: continue
            res = mn(res, d[key][-1] - d[key][-3])
            
        return -1 if res == inf else res + res
