class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_2digits = [0] * 101
        for i in range(1, 101):
            sum_2digits[i] = i // 10 + i % 10
        groups = [0] * 37
        for i in range(1, n+1):
            groups[sum_2digits[i // 100] + sum_2digits[i % 100]] += 1
        return groups.count(max(groups))
