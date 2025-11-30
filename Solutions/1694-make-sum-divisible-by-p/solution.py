class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        extra = total % p
        if extra == 0:
            return 0

        prefix = 0
        ret = len(nums)
        seen = {0: 0}

        for i, x in enumerate(nums, 1):
            prefix = (prefix + x) % p
            needed = (prefix - extra) % p

            if needed in seen:
                ret = min(ret, i - seen[needed])

            seen[prefix] = i  # update after checking

        return ret if ret < len(nums) else -1

