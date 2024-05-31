class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        freq = defaultdict(int)  # number -> appear_number
        for n in nums:
            freq[n] += 1

        res: list[int] = []
        for num, f in freq.items():
            if f == 1:
                res.append(num)

        return res
