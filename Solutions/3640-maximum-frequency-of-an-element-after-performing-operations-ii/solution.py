class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        freq = Counter(nums)
        line = []
        for num,f in freq.items():
            line.append((num - k, f))
            line.append((num, 0))
            line.append((num + k + 1, -f))
        line.sort()
        max_freq = 0
        overlaps = 0
        for e,d in line:
            overlaps += d
            max_freq = max(max_freq, min(numOperations, max(0, overlaps - freq[e])) + freq[e])
        return max_freq
