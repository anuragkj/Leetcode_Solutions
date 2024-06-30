class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n+1)]
        self.rank = [1]*(n+1)

    def find(self,node):
        while node!=self.par[node]:
            self.par[node]=self.par[self.par[node]]
            node = self.par[node]
        return node

    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)

        if p1==p2:
            return 1
        
        if self.rank[p1]>self.rank[p2]:
            self.rank[p1]+=self.rank[p2]
            self.par[p2]=p1
        else:
            self.rank[p2]+=self.rank[p1]
            self.par[p1]=p2

        return 0


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice,bob = UnionFind(n),UnionFind(n)
        count = 0

        for t,v1,v2 in edges:
            if t==3:
                count+=(alice.union(v1,v2)|bob.union(v1,v2))

        for t,v1,v2 in edges:
            if t==1:
                count+=alice.union(v1,v2)
            elif t==2:
                count+=bob.union(v1,v2)
   
        return -1 if max(alice.rank)!=n or max(bob.rank)!=n else count
