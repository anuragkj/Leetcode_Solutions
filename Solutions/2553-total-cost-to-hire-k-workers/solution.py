from heapq import *
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left = costs[:candidates]
        right = costs[max(len(costs)-candidates,candidates):]
        heapify(left)
        heapify(right)
        i, j = candidates, max(len(costs)-candidates,candidates)-1
        ans = 0
        for _ in range(k):
            if left and right:
                if left[0] <= right[0]:
                    ans += heappop(left)
                    if i<=j:
                        heappush(left,costs[i])
                        i += 1
                else:
                    ans += heappop(right)
                    if i<=j:
                        heappush(right,costs[j])
                        j -= 1
            elif left:
                ans += heappop(left)
            else:
                ans += heappop(right)
                
        return ans
