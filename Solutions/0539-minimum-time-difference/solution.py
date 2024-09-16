class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [False] * (24 * 60)
        for time in timePoints:
            h, m = map(int, time.split(":"))
            min_time = h * 60 + m
            if minutes[min_time]:
                return 0
            minutes[min_time] = True
        prevIndex = float("inf")
        firstIndex = float("inf")
        lastIndex = float("inf")
        ans = float("inf")

        # find differences between adjacent elements in sorted array
        for i in range(24 * 60):
            if minutes[i]:
                if prevIndex != float("inf"):
                    ans = min(ans, i - prevIndex)
                prevIndex = i
                if firstIndex == float("inf"):
                    firstIndex = i
                lastIndex = i

        return min(ans, 24 * 60 - lastIndex + firstIndex)
