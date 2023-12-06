class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        complete_week = n // 7
        remaining_days = n % 7

        total += (28 * complete_week) + (7 * (complete_week - 1) * complete_week // 2) 

        total += (complete_week + 1 + complete_week + remaining_days) * remaining_days // 2

        return total
