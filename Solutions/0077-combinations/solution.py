class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        l1 = []
        for i in range(1, n+1):
            l1.append([i])
        if k == 1:
            return l1

        for j in range(2, k+1):
            for ele in l1:
                for i in range(ele[-1] + 1, n + 1):
                    res.append(ele+[i])
            l1.clear()
            l1 = res.copy()
            res.clear()
        
        return l1
                

