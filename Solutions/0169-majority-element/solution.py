class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        n = len(nums) // 2

        for num in nums:
            counts[num] += 1

        for num, count in counts.items():
            if count > n:
                return num


