class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq = [0] * 100      
        total = 0 

        for a, b in dominoes:
            key = a * 10 + b if a <= b else b * 10 + a
            total += freq[key]
            freq[key] += 1

        return total
