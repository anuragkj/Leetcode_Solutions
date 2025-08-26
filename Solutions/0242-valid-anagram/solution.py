class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for i in s:
            sdict[i] = sdict.get(i, 0) + 1
        for i in t:
            tdict[i] = tdict.get(i, 0) + 1
        return sdict == tdict
