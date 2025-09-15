class Solution:
    def canBeTypedWords(self, text: str, broken: str) -> int:
        mask = 0
        for ch in broken:
            mask |= 1 << (ord(ch) - 97)
        
        count = 0
        brokenWord = False
        n = len(text)
        for i in range(n + 1):
            if i < n and 'a' <= text[i] <= 'z' and (mask & (1 << (ord(text[i]) - 97))):
                brokenWord = True
            if i == n or text[i] == ' ':
                if not brokenWord:
                    count += 1
                brokenWord = False
        return count
