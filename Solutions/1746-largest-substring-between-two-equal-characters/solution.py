class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hash_map = {}
        res = -1
        for i in range(len(s)):
            if s[i] in hash_map:
                res = max(res, i - hash_map[s[i]])
            else:
                hash_map[s[i]] = i
        return -1 if res == -1 else res - 1
