class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')
        min_penalty = penalty
        min_hour = 0
        for idx, char in enumerate(customers):
            if char == 'Y':
                penalty -= 1
            else:
                penalty += 1
            if penalty < min_penalty:
                min_penalty = penalty
                min_hour = idx + 1
            
        return min_hour
