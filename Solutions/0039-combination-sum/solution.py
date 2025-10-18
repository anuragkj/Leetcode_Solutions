class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(ind, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or ind >= len(candidates):
                return

            curr.append(candidates[ind])
            dfs(ind, curr, total+candidates[ind])
            curr.pop()
            dfs(ind+1, curr, total)

            return
        dfs(0,[],0)
        return res

