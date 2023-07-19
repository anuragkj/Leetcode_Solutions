class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda k: (k[1]))
        final_end = -float('inf')
        res = 0
        for i in range(len(intervals)):
            if intervals[i][0] >= final_end:
                final_end = intervals[i][1]
            else:
                res+=1
        return res


