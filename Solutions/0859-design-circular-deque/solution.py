class MyCircularDeque:
    def __init__(self, k: int):
        self.maxSize = k
        self.dq = deque()

    def insertFront(self, value: int) -> bool:
        if len(self.dq) < self.maxSize:
            self.dq.appendleft(value)
            return True

    def insertLast(self, value: int) -> bool:
        if len(self.dq) < self.maxSize:
            self.dq.append(value)
            return True

    def deleteFront(self) -> bool:
        if self.dq:
            self.dq.popleft()
            return True

    def deleteLast(self) -> bool:
        if self.dq:
            self.dq.pop()
            return True

    def getFront(self) -> int:
        if self.dq:
            return self.dq[0]
        return -1

    def getRear(self) -> int:
        if self.dq:
            return self.dq[-1]
        return -1

    def isEmpty(self) -> bool:
        return not self.dq

    def isFull(self) -> bool:
        return len(self.dq) == self.maxSize
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
