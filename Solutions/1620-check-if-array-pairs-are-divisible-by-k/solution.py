class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dic = {}

        for i in arr:
            i %= k
            dic[i] = dic.get(i, 0) + 1
        
        for i in arr:
            i %= k
            if dic.get(i, 0) > 0:
                dic[i] -= 1
                p = (k-i)%k
                if dic.get(p, 0) > 0: 
                    dic[p] -= 1
                else:
                    return False

        return True
