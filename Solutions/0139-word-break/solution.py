class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dfs(i):
            if i == len(s):
                return True
            ret = False
            for word in wordDict:
                if s[i:].startswith(word):
                    ret = ret or dfs(i+len(word))
            return ret
        
        return dfs(0)
