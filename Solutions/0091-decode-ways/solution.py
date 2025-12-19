class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i,pick):
            if i == len(s):
                return 0
            if i == len(s) - 1 and int(pick)*10 + int(s[i]) in range(1,27):
                return 1
            total = 0
            #commit/carry
            if int(pick)*10 + int(s[i]) in range(1,27):
                print(int(pick)*10 + int(s[i]))
                total += dfs(i+1, 0)
            if int(pick)==0 and int(s[i])!=0:
                total += dfs(i+1, s[i])
            return total
        
        return dfs(0,0)

