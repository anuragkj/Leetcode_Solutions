class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def is_possible(penalty):
            return sum((num-1)//penalty for num in nums) <= maxOperations

        l, r = 1, max(nums) + 1
        while l < r:
            m = (l + r) // 2
            if not is_possible(m):
                l = m + 1
            else:
                r = m
        return l
