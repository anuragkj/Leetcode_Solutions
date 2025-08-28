class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        end = float('-inf')
        count = 0
        for i in intervals:
            if i[0] < end:
                count += 1
            else:
                end = i[1]
        return count
