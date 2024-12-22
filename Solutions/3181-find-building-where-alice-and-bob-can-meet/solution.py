class Solution:
    def leftmostBuildingQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        stack = []
        n = len(nums)
        nextGreater = [-1]*n
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop()
            if stack:
                nextGreater[i]=stack[-1]
            stack.append(i)
        # @cache
        cache = {}
        def dfs(x,y,i):
            f = (max(nums[x],nums[y]),i)
            if f in cache:
                return cache[f]
            if i >=n:
                return -1
            if i == -1:
                return i
            if x!=i and y!=i and nums[i]>nums[x] and nums[i]>nums[y]:
                return i
            if x==i and y!=i and nums[i]>nums[y]:
                return i
            if y == i and x!=i and nums[i]>nums[x]:
                return i
            nextI = nextGreater[i]
            ret = dfs(x,y,nextI)
            cache[f]=ret
            return ret
        for qry in queries:
            i = min(qry[0],qry[1])
            j = max(qry[0],qry[1])
            if i == j:
                res.append(j)
            elif nums[i]<nums[j]:
                res.append(j)
            else:
                res.append(dfs(i, j, j))

        return res
