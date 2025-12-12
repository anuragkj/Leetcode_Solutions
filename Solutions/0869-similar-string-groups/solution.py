class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0]*n
        self.components = n

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        parx, pary = self.find(x), self.find(y)
        if parx==pary:
            return
        if self.rank[parx] < self.rank[pary]:
            self.parents[parx] = pary
        elif self.rank[parx] > self.rank[pary]:
            self.parents[pary] = parx
        else:
            self.parents[pary] = parx
            self.rank[parx] += 1
        self.components -= 1

class Solution:
    def strmatch(self,x,y):
        out_of_place = 0 
        for i in range(len(x)):
            if x[i]!=y[i]:
                out_of_place+=1
        if out_of_place <=2:
            return True
        return False
    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = UnionFind(len(strs))
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if self.strmatch(strs[i], strs[j]):
                    uf.union(i,j)

        return uf.components

        
