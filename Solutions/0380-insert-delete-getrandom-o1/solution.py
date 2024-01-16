class RandomizedSet:
    def __init__(self):
        self.stack = []
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        # dictionary is on average O(1) where as
        # checking the array is on average O(n)
        if val in self.dict:
            return False

        self.dict[val] = len(self.stack)
        self.stack.append(val)
        return True
        
    def remove(self, val: int) -> bool:
	    # dictionary is on average O(1) where as
        # checking the array is on average O(n)
        if val not in self.dict:
            return False        
        last = self.stack[-1]
        ind = self.dict[val] 
        
        self.dict[last] = ind
        self.stack[ind] = last
        
        self.stack.pop()
        
        self.dict.pop(val)
        
        
        return True        

    def getRandom(self) -> int:
        return random.choice(self.stack)
