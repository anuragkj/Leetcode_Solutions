class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono = deque()

        ret = []

        for i in range(len(temperatures)-1,-1,-1):
            while mono and temperatures[i] >= mono[-1][0]:
                mono.pop()

            if len(mono)>0:
                ret.append(mono[-1][1]-i)
            else:
                ret.append(0)
            
            mono.append([temperatures[i],i])

        return ret[::-1]
