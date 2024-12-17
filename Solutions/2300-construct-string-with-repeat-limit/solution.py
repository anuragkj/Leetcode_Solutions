class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        s = Counter(s)
        chars = sorted(s.keys())
        output = ""
        while s:
            count = min(repeatLimit, s[chars[-1]])
            output += chars[-1]*count
            if count >= s[chars[-1]]:
                del s[chars[-1]]
                chars.pop()
            else:
                s[chars[-1]] -= count
                if len(s) == 1:
                    return output
                s[chars[-2]] -= 1
                output += chars[-2]
                if s[chars[-2]] == 0:
                    del s[chars[-2]]
                    chars.pop(-2)

        return output
            
