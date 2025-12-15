class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        curr = intervals[0]
        ret = []
        for interval in intervals:
            start, end = interval
            if curr[1] < start:
                ret.append(curr)
                curr = interval
            else:
                curr = [min(curr[0], start),max(curr[1], end)]
        
        ret.append(curr)
        return ret
