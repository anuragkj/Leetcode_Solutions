class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2!=0:
            return []
        ret = []
        start = 2
        remain = finalSum
        #8 2 rem 6, start 4
        while(start<=finalSum):
            if remain-start == 0:
                ret.append(start)
                break
            if remain-start > start and remain - start <= finalSum:
                ret.append(start)
                remain -= start
            start+=2
        return ret
