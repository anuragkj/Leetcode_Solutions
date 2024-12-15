class Solution:
    def maxAverageRatio(self, cls: List[List[int]], extra: int) -> float:
        cls = [(p/t - (p+1)/(t+1), p, t) for p, t in cls]
        heapify(cls)

        if cls[0][0] == 0:
            return 1

        for _ in range(extra):
            _, p, t = heappop(cls)
            heappush(cls, ((p+1)/(t+1) - (p+2)/(t+2), p+1, t+1))

        return sum(p/t for _, p, t in cls) / len(cls)
