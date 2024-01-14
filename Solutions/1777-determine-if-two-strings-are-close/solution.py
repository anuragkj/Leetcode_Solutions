class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1lst = [0] * 26
        w2lst = [0] * 26

        if len(word1) != len(word2):
            return False
        
        for i in range(len(word1)):
            w1lst[ord(word1[i]) - ord('a')] += 1
            w2lst[ord(word2[i]) - ord('a')] += 1

        for i in range(26):
            if (w1lst[i] == 0 and w2lst[i] != 0) or (w1lst[i] != 0 and w2lst[i] == 0):
                return False

        return sorted(w1lst) == sorted(w2lst)
