class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        indegree = [0 for x in range(numCourses)]
        for i, j in prerequisites:
            indegree[i] += 1
            adj[j].append(i)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while(q):
            ele = q.popleft()
            for nei in adj[ele]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if sum(indegree) == 0:
            return True
        else:
            return False
        
