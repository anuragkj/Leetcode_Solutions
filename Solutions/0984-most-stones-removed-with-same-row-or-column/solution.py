class Solution:
    def removeStones(self, stones):
        n = len(stones)
        uf = self.UnionFind(n)

        # Populate uf by connecting stones that share the same row or column
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf._union(i, j)

        return n - uf.count

    # Union-Find data structure for tracking connected components
    class UnionFind:
        def __init__(self, n):
            self.parent = [-1] * n  # Initialize all nodes as their own parent
            self.count = (
                n  # Initially, each stone is its own connected component
            )

        # Find the root of a node with path compression
        def _find(self, node):
            if self.parent[node] == -1:
                return node
            self.parent[node] = self._find(self.parent[node])
            return self.parent[node]

        # Union two nodes, reducing the number of connected components
        def _union(self, n1, n2):
            root1 = self._find(n1)
            root2 = self._find(n2)

            if root1 == root2:
                return  # If they are already in the same component, do nothing

            # Merge the components and reduce the count of connected components
            self.count -= 1
            self.parent[root1] = root2
