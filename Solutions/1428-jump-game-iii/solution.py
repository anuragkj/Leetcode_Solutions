class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        q = deque([start])
        vis = [False] * n

        vis[start] = True

        while q:

            i = q.popleft()

            if arr[i] == 0:
                return True

            forward = i + arr[i]
            backward = i - arr[i]

            if forward < n and not vis[forward]:
                vis[forward] = True
                q.append(forward)

            if backward >= 0 and not vis[backward]:
                vis[backward] = True
                q.append(backward)

        return False
