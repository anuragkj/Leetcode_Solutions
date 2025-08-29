class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ret = 0
        l = 0
        dic = defaultdict(int)

        for r in range(len(s)):
            dic[s[r]] += 1

            while((r-l+1) - max(dic.values()) > k):
                dic[s[l]] -= 1
                l+=1
            ret = max(ret, r-l+1)
        return ret
