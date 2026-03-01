class Solution:
    def minPartitions(self, n: str) -> int:
        ret = 0
        for i in n:
            if int(i) > ret:
                ret = int(i)
        return ret
