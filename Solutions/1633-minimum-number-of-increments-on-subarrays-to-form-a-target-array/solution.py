class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ct=target[0]
        for i in range(1,len(target)):
            if target[i]>target[i-1]:
                ct+=(target[i]-target[i-1])
        return ct
