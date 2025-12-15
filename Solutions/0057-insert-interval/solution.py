class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort(intervals, newInterval)
        ret = []
        to_add = intervals[0]
        for i in range(1, len(intervals)):
            new = intervals[i]
            if new[0] > to_add[1]:
                ret.append(to_add)
                to_add = new
            else:
                to_add = [min(to_add[0],new[0]), max(to_add[1],new[1])]
        ret.append(to_add)
        return ret
