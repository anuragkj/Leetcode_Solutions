class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        prev_c = colors[0]
        prev_time = neededTime[0]
        ans = 0
        for i in range(1,n):
            if colors[i] == prev_c:
                ans += min(neededTime[i],prev_time)
                prev_time = max(neededTime[i],prev_time)
            else:
                prev_time = neededTime[i]
                prev_c = colors[i]
        return ans
