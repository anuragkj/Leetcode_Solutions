class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countDict = Counter(tasks)
        readyHeap = [-count for count in countDict.values()]
        heapq.heapify(readyHeap)
        waitingQueue = deque()
        currTime = 0
        
        while waitingQueue or readyHeap:
            currTime += 1

            if readyHeap:
                currItem = heapq.heappop(readyHeap) + 1
                if currItem != 0:
                    waitingQueue.append((currItem,currTime + n))

            if waitingQueue and waitingQueue[0][1] == currTime:
                heapq.heappush(readyHeap,waitingQueue.popleft()[0])

        return currTime
