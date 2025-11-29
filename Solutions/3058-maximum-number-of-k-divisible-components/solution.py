class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        self.components = 0

        adj_list = defaultdict(list)
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        def dfs(root, parent):
            
            if root is None:
                return 0
            total_sum = 0
            for nei in adj_list[root]:
                if nei!=parent:
                    total_sum += dfs(nei, root)
            total_sum += values[root]
            if total_sum%k == 0:
                self.components+=1
            
            return total_sum

        dfs(0,-1)
        return self.components
        
