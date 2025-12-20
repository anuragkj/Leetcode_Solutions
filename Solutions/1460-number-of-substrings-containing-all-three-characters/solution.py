class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic = defaultdict(int)
        l = 0
        ret = 0
        for r in range(len(s)):
            dic[s[r]] += 1
            while len(dic.keys()) == 3:
                ret += len(s) - r
                dic[s[l]] -= 1
                if dic[s[l]]==0:
                    del dic[s[l]]
                l+=1
        return ret
