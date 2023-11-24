class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        queue = deque(piles)
        ans = 0
        while queue:
            queue.pop() # alice
            ans += queue.pop() # us
            queue.popleft() # bob

        return ans
