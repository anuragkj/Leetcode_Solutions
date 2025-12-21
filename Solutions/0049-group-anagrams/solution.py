class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def strtotuple(s):
            alp = [0]*26
            for i in s:
                alp[ord(i)-ord('a')] += 1
            return tuple(alp)
        
        dic = defaultdict(list)
        for st in strs:
            k = strtotuple(st)
            dic[k].append(st)
        return list(dic.values())
