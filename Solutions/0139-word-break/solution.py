# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:

#         def rec(suffix):
#             if suffix == "":
#                 return True
            
#             ret = False
#             for i in wordDict:
#                 if suffix.startswith(i):
#                     ret = ret or rec(suffix[len(i) : ])
#             return ret

#         return rec(s)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i):
            if i < 0: 
                return True

            for word in wordDict:
                if s[i - len(word) + 1:i + 1] == word and dp(i - len(word)):
                    return True
            
            return False
        
        return dp(len(s) - 1)
