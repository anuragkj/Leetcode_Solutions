class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # Solution 2: 
        freq, even_nums = [0] * 10, []
        for d in digits:
            freq[d] += 1       
        for a in range(1, 10):          # hundreds digit: 1–9
            if freq[a] == 0: continue
            freq[a] -= 1
            for b in range(10):         # tens digit: 0–9
                if freq[b] == 0: continue
                freq[b] -= 1
                for c in (0,2,4,6,8):   # ones digit: even only
                    if freq[c] > 0:
                        even_nums.append(100 * a + 10 * b + c)
                freq[b] += 1
            freq[a] += 1
        return sorted(even_nums)
