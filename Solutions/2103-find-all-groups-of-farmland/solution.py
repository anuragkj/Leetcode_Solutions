class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        m,n = len(land),len(land[0])
        
        def dfs(i,j):
            if i==m or j==n or land[i][j]==0:
                return [0,0]
            land[i][j]=0
            a1 = dfs(i,j+1)
            a2 = dfs(i+1,j)
            return [max(i,a1[0],a2[0]),max(j,a1[1],a2[1])]

        for i in range(len(land)):
            j = 0
            while j<n:
                if land[i][j]==1:
                    arr = dfs(i,j)
                    ans.append([i,j]+arr)
                    j = arr[1]
                j+=1
        return ans
        
