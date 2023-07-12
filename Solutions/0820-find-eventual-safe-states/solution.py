class Solution:
    def isSafe(self, s, graph, visited, checkCycle):
        if visited[s] == 1:
            return True  # Node is already visited and safe
        if visited[s] == -1:
            return False  # Node is visited and part of a cycle

        visited[s] = -1  # Mark the current node as visited and part of a cycle
        for it in graph[s]:
            if not self.isSafe(it, graph, visited, checkCycle):
                return False  # If any adjacent node is not safe, the current node is not safe

        visited[s] = 1  # Mark the current node as visited and safe
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v = len(graph)
        visited = [0] * v
        checkCycle = []
        for i in range(v):
            if self.isSafe(i, graph, visited, checkCycle):
                checkCycle.append(i)  # Add the nodes that are safe (eventual safe nodes) to the result
        return checkCycle
