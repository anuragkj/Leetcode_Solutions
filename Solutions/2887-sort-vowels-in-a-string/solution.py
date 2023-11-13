import heapq
class Solution:
    def sortVowels(self, s: str) -> str:
        l = list(s)
        res = []
        heapq.heapify(res)
        for i in l:
            if i in 'aeiouAEIOU':
                heapq.heappush(res, i)
        
        for i in range(len(l)):
            if l[i] in 'aeiouAEIOU':
                l[i] = heapq.heappop(res)
        return ''.join(l)
