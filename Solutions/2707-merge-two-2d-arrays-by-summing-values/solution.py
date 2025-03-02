class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d={}
        for i in nums1:
                d[i[0]]=i[1]
        for i in nums2:
            if i[0] not in d.keys():
                d[i[0]]=i[1]
            else :
                d[i[0]]=i[1]+d[i[0]]
        l=[]
        for i in sorted(d.keys()):
            l.append([i,d[i]])
        return l
