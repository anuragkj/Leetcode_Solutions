from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        dic = Counter(nums)
        lst = list((-dic[k],k) for k in dic.keys())
        heapq.heapify(lst)
        ret = []
        for i in range(k):
            ele = heapq.heappop(lst)
            ret.append(ele[1])
        return ret
