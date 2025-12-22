class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = {}
        n = numCourses
        for i in range(n):
            indegree[i] = 0

        for i,j in prerequisites:
            adj[j].append(i)
            indegree[i]+=1
        
        q=deque()

        for i in indegree:
            if indegree[i] == 0:
                q.append(i)

        ret = []

        while q:
            sub = q.popleft()
            ret.append(sub)

            for nei in adj[sub]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return ret if len(ret)==n else []
