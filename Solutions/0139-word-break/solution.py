class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            
            ret = False
            for word in wordDict:
                wordlen = len(word)
                if i + wordlen <= len(s) and s[i:i+wordlen] == word:
                    ret = ret or dfs(i+wordlen)

            memo[i] = ret
            return ret
        
        return dfs(0)
