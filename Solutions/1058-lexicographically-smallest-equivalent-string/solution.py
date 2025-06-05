class Solution:
    def dfs(self, node, adj, visited, group):
        visited[node] = True
        group.append(node)
        for nei in adj[node]:
            if not visited[nei]:
                self.dfs(nei, adj, visited, group)

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = [[] for _ in range(26)]

        # Step 1: Build graph
        for a, b in zip(s1, s2):
            u = ord(a) - ord('a')
            v = ord(b) - ord('a')
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * 26
        rep = [None] * 26

        # Step 2: Find connected components
        for i in range(26):
            if not visited[i]:
                group = []
                self.dfs(i, adj, visited, group)

                min_char = min(chr(idx + ord('a')) for idx in group)
                for idx in group:
                    rep[idx] = min_char

        # Step 3: Build result
        return ''.join(rep[ord(ch) - ord('a')] if rep[ord(ch) - ord('a')] else ch for ch in baseStr)
