class Solution:
    def makeFancyString(self, s: str) -> str:
        last_term = ''
        max_len = 0
        ans = ''
        for i in s:
            if i != last_term:
                if max_len > 1:
                    ans += 2*last_term
                else:
                    ans += last_term
                max_len = 1
                last_term = i
            else:
                max_len += 1
        if max_len > 1:
            ans += 2*last_term
        else:
            ans += last_term
        return ans
