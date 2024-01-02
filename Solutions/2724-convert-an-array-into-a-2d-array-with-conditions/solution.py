class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hash_map = defaultdict(int)
        res = []
        for i in nums:
            k = hash_map[i]
            if k >= len(res):
                res.append([i])
            else:
                res[k].append(i)
            hash_map[i] += 1
        return res
