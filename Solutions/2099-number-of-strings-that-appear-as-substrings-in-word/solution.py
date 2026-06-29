class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        for s in patterns:
            if word.find(s) != -1: # return -1 when not found
                count += 1
        return count
