class Solution:
    def numDecodings(self, s: str) -> int:
        letters_array = []
        for i in range(1, 27):
            letters_array.append(str(i))
        @cache
        def dfs(i, curr):
            new_curr = s[i] + curr
            if i == 0:
                if (new_curr) in letters_array:
                    return 1 
                else:
                    return 0
            if int(new_curr) > 26:
                return 0
            take, no_take = 0, 0
            if new_curr in letters_array:
                take = dfs(i-1, '')
            no_take = dfs(i-1, new_curr)

            return take + no_take

        return dfs(len(s) - 1, '')

