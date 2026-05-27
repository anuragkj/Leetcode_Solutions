class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        A = [[False, False] for _ in range(27)]

        for ch in word:
            k = ord(ch)
            i = k & 31
            C = (k >> 5) & 1

            A[i][C] = not (C and A[i][0])

        res = 0
        for u, v in A:
            if u and v:
                res += 1

        return res
