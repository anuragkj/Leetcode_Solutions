class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono = deque()
        ret = []

        for idx,i in enumerate(nums):
            while mono and mono[-1][0] < i:
                mono.pop()
            while mono and mono[0][1] <= idx-k:
                mono.popleft()
            
            mono.append([i,idx])
            if idx>=k-1:
                ret.append(mono[0][0])
        
        return ret
        
        
