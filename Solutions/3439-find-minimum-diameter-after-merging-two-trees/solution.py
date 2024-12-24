class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        g = []
        neighborCount = []
        leaves0 = []
        leaves1 = []
        def getTreeDiameter(edges):
            nonlocal g, neighborCount, leaves0, leaves1
            n = len(edges) + 1
            g.clear()
            neighborCount.clear()
            for _ in range(n):
                g.append([])
                neighborCount.append(0)
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
                neighborCount[u] += 1
                neighborCount[v] += 1

            leaves0.clear()
            leaves1.clear()
            for u, neighCnt in enumerate(neighborCount):
                if neighCnt == 1:
                    leaves0.append(u)
            result = 0
            while len(leaves0) > 1:
                result += 2
                for u in leaves0:
                    for v in g[u]:
                        neighborCount[v] -= 1
                        if neighborCount[v] == 1:
                            leaves1.append(v)
                leaves0, leaves1 = leaves1, leaves0
                leaves1.clear()
            return result - (1 - len(leaves0))
        d1 = getTreeDiameter(edges1)
        d1h = (d1 + 1) >> 1
        d2 = getTreeDiameter(edges2)
        d2h = (d2 + 1) >> 1

        return max(d1, d2, 1 + d1h + d2h)
