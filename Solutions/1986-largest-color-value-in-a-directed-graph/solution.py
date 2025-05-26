class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        hashmap = collections.defaultdict(list)

        for u, v in edges:
            if u == v:
                return -1
            hashmap[u].append(v)

        visited = set()
        
        @cache
        def dfs(curr, target):
            result = 0
            for adj in hashmap[curr]:
                if adj in visited:
                    return float('inf')
                visited.add(adj)
                result = max(result, dfs(adj, target))
                visited.remove(adj)

            return result + 1 if colors[curr] == target else result

        max_path_value = 0
        for i in range(len(colors)):
            max_path_value = max(max_path_value, dfs(i, colors[i]))

        return -1 if max_path_value == float('inf') else max_path_value
