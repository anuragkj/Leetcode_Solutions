class Solution:
    def calc(self, part1: int, part2: int, part3: int) -> int:
        return max(part1, part2, part3) - min(part1, part2, part3)

    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        total = 0
        for num in nums:
            total ^= num

        self.res = float("inf")

        def dfs2(node: int, parent: int, part1: int, root: int) -> int:
            sub_xor = nums[node]
            for nei in graph[node]:
                if nei == parent:
                    continue
                sub_xor ^= dfs2(nei, node, part1, root)
            if node != root:
                self.res = min(
                    self.res, self.calc(part1, sub_xor, part1 ^ sub_xor ^ total)
                )
            return sub_xor

        def dfs(node: int, parent: int) -> int:
            sub_xor = nums[node]
            for nei in graph[node]:
                if nei == parent:
                    continue
                sub_xor ^= dfs(nei, node)
            if node != 0:
                dfs2(parent, node, sub_xor, parent)
            return sub_xor

        dfs(0, -1)
        return self.res
