class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        # If the intervals vector is empty, return a vector containing the newInterval
        if not intervals:
            return [newInterval]

        n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1

        # Binary search to find the position to insert newInterval
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Insert newInterval at the found position
        intervals.insert(left, newInterval)

        # Merge overlapping intervals
        res = []
        for interval in intervals:
            # If res is empty or there is no overlap, add the interval to the result
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            # If there is an overlap, merge the intervals by updating the end of the last interval in res
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
