class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        ret = 0
        curr = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < curr[1]:
                ret+=1
            else:
                curr = intervals[i]
        return ret

