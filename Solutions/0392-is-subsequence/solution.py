class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        if s == "":
            return True
        for i in range(len(t)):
            if s[j] == t[i]:
                j += 1
            if j == len(s):
                return True

        return False 
