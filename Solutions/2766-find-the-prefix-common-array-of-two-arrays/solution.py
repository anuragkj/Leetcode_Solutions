class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        aSet = set()
        bSet = set()
        l = len(A)
        count = 0
        out = []

        for i in range(l):
            elA = A[i]
            elB = B[i]

            if elA == elB:
                count += 1
            else:
                aSet.add(elA)
                bSet.add(elB)

                if elB in aSet:
                    count += 1
                if elA in bSet:
                    count += 1

            out.append(count)
        return out
