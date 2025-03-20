class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.component_and = [-1] * size  # Initialize with all bits set to 1 (equiv. to -1 in two's complement)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y, w):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            # Nodes are already connected: update component AND with the current edge's weight
            self.component_and[root_x] &= w
            return

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        # Merge component AND values and include the current edge's weight
        self.component_and[root_x] &= (self.component_and[root_y] & w)
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v, w)

        result = []
        for s, e in queries:
            root_s = uf.find(s)
            root_e = uf.find(e)
            if root_s == root_e:
                result.append(uf.component_and[root_s])
            else:
                result.append(-1)
        return result
