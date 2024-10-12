class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        endptr, res = 0, 0
        
        for start in starts :
            if start > ends[endptr] :
                endptr +=1
            else :
                res+=1
        return res
