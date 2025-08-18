from typing import List
import math

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def backtrack(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < EPS

            n = len(nums)
            for i in range(n):
                for j in range(i + 1, n):
                    rest = [nums[k] for k in range(n) if k != i and k != j]
                    a, b = nums[i], nums[j]

                    candidates = []
                    candidates.append(a + b)
                    candidates.append(a * b)
                    candidates.append(a - b)
                    candidates.append(b - a)

                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)

                    for x in candidates:
                        if backtrack(rest + [x]):
                            return True
            return False

        return backtrack([float(x) for x in cards])
