class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        self.dict = {}
        

    def get(self, key: int) -> int:
        if key in self.queue:
            ind = self.queue.index(key)
            self.queue.pop(ind)
            self.queue.append(key)
            return self.dict[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.queue:
            ind = self.queue.index(key)
            self.queue.pop(ind)
            self.queue.append(key)
            self.dict[key] = value
            return
        if len(self.queue) == self.capacity:
            removed_key = self.queue.pop(0)
        self.queue.append(key)
        self.dict[key] = value
             


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
