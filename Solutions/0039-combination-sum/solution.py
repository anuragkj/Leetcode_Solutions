class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ret = []

        def dfs(i,tsum,path):
            nonlocal ret
            if tsum == target:
                ret.append(path.copy())
            if tsum > target:
                return
            
            for j in range(i, len(candidates)):
                if tsum + candidates[j] <= target:
                    path.append(candidates[j])
                    dfs(j,tsum+candidates[j],path)
                    path.pop()
            return
        dfs(0,0,[])
        return ret
            

