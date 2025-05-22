import heapq

class Solution:
    def maxRemoval(self, nums, queries):
        n = len(nums)
        m = len(queries)
        workload = [0] * (n + 1)

        queries.sort()
        available = []  # Max heap via negatives
        q_index = 0

        for time in range(n):
            if time > 0:
                workload[time] += workload[time - 1]

            while q_index < m and queries[q_index][0] == time:
                heapq.heappush(available, -queries[q_index][1])
                q_index += 1

            while workload[time] < nums[time]:
                if not available or -available[0] < time:
                    return -1

                workload[time] += 1
                end_time = -heapq.heappop(available)
                if end_time + 1 < len(workload):
                    workload[end_time + 1] -= 1

        return len(available)
