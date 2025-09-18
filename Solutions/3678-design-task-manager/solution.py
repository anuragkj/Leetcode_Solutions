import heapq

class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        self.maxHeap = []  # (-priority, -taskId) for max behavior
        self.taskMap = {}  # taskId -> (userId, priority)

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskMap[taskId] = (userId, priority)
        heapq.heappush(self.maxHeap, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.taskMap:
            userId, _ = self.taskMap[taskId]
            self.taskMap[taskId] = (userId, newPriority)
            heapq.heappush(self.maxHeap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.taskMap:
            del self.taskMap[taskId]  # lazy deletion

    def execTop(self) -> int:
        while self.maxHeap:
            priority, taskId = heapq.heappop(self.maxHeap)
            taskId = -taskId
            priority = -priority
            if taskId in self.taskMap and self.taskMap[taskId][1] == priority:
                userId, _ = self.taskMap[taskId]
                del self.taskMap[taskId]
                return userId
        return -1
