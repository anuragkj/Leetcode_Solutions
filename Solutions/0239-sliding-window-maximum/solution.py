class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums = [(-num, i) for i, num in enumerate(nums)]
        pq = nums[:k]
        heapify(pq)
        res = [-pq[0][0]]
        
        for num, i in nums[k:]:
            heappush(pq, (num, i))

            while i - pq[0][1] >= k:
                heappop(pq)

            res.append(-pq[0][0]) 
        
        return res
