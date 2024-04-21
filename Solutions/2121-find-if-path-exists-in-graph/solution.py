class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for src, dest in edges:
            graph[src] = graph.get(src, []) + [dest]
            graph[dest] = graph.get(dest, []) + [src]
        visited = set()
        def dfs(node):
            if node == destination:
                return True
            ret = False
            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    ret = ret or dfs(i)
            return ret
        return dfs(source)
        
