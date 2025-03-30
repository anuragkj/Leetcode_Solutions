class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        P = [-1] * 26
        for i, c in enumerate(s):
            x = ord(c) - 97
            P[x] = i
        pLen = []
        start, end = 0, -1
        for i, c in enumerate(s):
            x = ord(c) - 97
            end = max(end, P[x])
            if i == end:
                pLen.append(end - start + 1)
                start = i + 1
        return pLen

        
