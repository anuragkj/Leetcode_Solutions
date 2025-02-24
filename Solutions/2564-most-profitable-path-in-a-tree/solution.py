from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        bob_path = [-1] * len(amount)
        path = []
        self.fill_bob_path(bob, -1, path, graph)

        for i, node in enumerate(path):
            bob_path[node] = i

        return self.get_alice_max_score(0, -1, 0, bob_path, graph, 0, amount)

    def fill_bob_path(self, node, parent, path, graph):
        if node == 0:
            return True
        for neighbor in graph[node]:
            if neighbor != parent:
                path.append(node)
                if self.fill_bob_path(neighbor, node, path, graph):
                    return True
                path.pop()
        return False

    def get_alice_max_score(self, node, parent, curr_score, bob_path, graph, timestamp, amount):
        if bob_path[node] == -1 or bob_path[node] > timestamp:
            curr_score += amount[node]
        elif bob_path[node] == timestamp:
            curr_score += amount[node] // 2

        if len(graph[node]) == 1 and node != 0:
            return curr_score

        max_score = float('-inf')
        for neighbor in graph[node]:
            if neighbor != parent:
                max_score = max(max_score, self.get_alice_max_score(neighbor, node, curr_score, bob_path, graph, timestamp + 1, amount))
        return max_score
