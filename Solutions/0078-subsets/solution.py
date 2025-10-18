class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        visisted = set()
        def dfs(i, path):
            if i >= len(nums):
                return
            res.append(path.copy())
            for j in range(i+1, len(nums)):
                path.append(nums[j])
                dfs(j, path)
                path.pop()
            return
        dfs(-1, [])
        return res
            

