class SnapshotArray:

    def __init__(self, length: int):
        self.array_dict = defaultdict(list)
        self.snap_id = 0
        for i in range(length):
            self.array_dict[i].append([self.snap_id,0])
        return None        

    def set(self, index: int, val: int) -> None:
        if self.array_dict[index][-1][0] == self.snap_id:
            self.array_dict[index][-1][1] = val
        else:
            self.array_dict[index].append([self.snap_id,val])
        return None        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id -1        

    def get(self, index: int, snap_id: int) -> int:
        ele = bisect.bisect(self.array_dict[index], snap_id, key = lambda x:x[0])
        return self.array_dict[index][ele-1][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
