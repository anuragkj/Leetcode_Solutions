import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        openChairs, timeHeap = [], []
        output, startTime = 0, 0
        
        # populate minHeap with all posible chairs open
        for i in range(len(times)):
            if i == targetFriend:
                startTime = times[i][0]
            heapq.heappush(openChairs, i)
        
        times.sort(key=lambda x : x[0]) # sort by arrival time
        
        for i, timeObj in enumerate(times):

            arrival, leaving = timeObj
            # if our new arrival time is greater than any previous leaving time, 
            # pop our timeHeap and push occupied chair # to openChairs
            while len(timeHeap) and arrival >= timeHeap[0][0]:
                oldTime, chair = heapq.heappop(timeHeap)
                heapq.heappush(openChairs, chair)
            
            if startTime == arrival:
                return heapq.heappop(openChairs) # return next open chair
            
            heapq.heappush(timeHeap, (leaving, heapq.heappop(openChairs)))
            
        return -1
