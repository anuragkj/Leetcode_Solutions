class Solution:
    def canPartition(self, s: str, target: int) -> bool:
        if s == "" and target == 0:
            return True
        if target < 0:
            return False
        ans = False
        for i in range(len(s)):  # try all possible pivot points
            left = s[: i + 1]  # keep the left part
            right = s[i + 1 :]  # recurse for right part
            leftNum = int(left)

            isPossible = self.canPartition(right, target - leftNum)
            if isPossible:
                ans = True
                break
        return ans

    def punishmentNumber(self, n: int) -> int:
        sum_ = 0
        for num in range(1, n + 1):
            sqr = num * num
            if self.canPartition(str(sqr), num):
                sum_ += sqr
        return sum_
