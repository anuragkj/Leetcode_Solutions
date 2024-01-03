class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ret = 0
        last = -1

        for i in bank:
            curr = 0
            for j in i:
                curr += int(j)
            if last == -1:
                last = curr
                continue
            if curr != 0:
                ret += curr * last
                last = curr

        return ret
