class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def dfs(i,path):
            ret.append(path.copy())
            for j in range(i+1,len(nums)):
                if len(path)!=len(nums):
                    path.append(nums[j])
                    dfs(j,path)
                    path.pop()
        dfs(-1,[])
        return ret
