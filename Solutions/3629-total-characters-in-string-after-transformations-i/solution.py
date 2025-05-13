from string import ascii_lowercase as alpha
mod = 1_000_000_007

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        d = {ch: i for i, ch in enumerate(alpha)}       # <- 1

        queue = deque([0] * 26)                         # <- 2
        for ch in s: queue[d[ch]] += 1

        for i in range(t):                              # <- 3
            queue[0]+= queue[25]
            queue.appendleft(queue.pop())
            
        return sum(queue) %mod                          # <- 4
