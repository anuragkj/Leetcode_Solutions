class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        start = 0

        for i in range(len(s)):
            if s[i] == ' ' or i == len(s) - 1:
                end = i
                if i == len(s) - 1 and s[i] != ' ':
                    end += 1
                # Inline reverse logic
                while start < end:
                    s[start], s[end - 1] = s[end - 1], s[start]
                    start += 1
                    end -= 1
                start = i + 1

        return ''.join(s)
