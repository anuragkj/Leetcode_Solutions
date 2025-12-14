class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        

    def addNum(self, num: int) -> None:
        #0...5(max heap)(always equal or one more num)  7...10(min heap)
        if len(self.left_heap)==0 or num <= -self.left_heap[0]:
            heapq.heappush(self.left_heap, -num)
            if len(self.left_heap) - len(self.right_heap) > 1:
                ele = -1*heapq.heappop(self.left_heap)
                heapq.heappush(self.right_heap, ele)  
        else:
            heapq.heappush(self.right_heap, num)
            if len(self.right_heap) - len(self.left_heap) > 0:
                ele = heapq.heappop(self.right_heap)
                heapq.heappush(self.left_heap, -ele)  

    def findMedian(self) -> float:
        if len(self.left_heap)>len(self.right_heap):
            return -self.left_heap[0]
        else:
            return (-self.left_heap[0] + self.right_heap[0])/2        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
