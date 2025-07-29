class Solution:
    def is_set(self, num, pos):
        return (num & (1 << pos)) != 0

    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        suf = [0] * n

        # suffix OR
        suf[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] | nums[i]

        l = r = 0
        cur = nums[0]
        freq = [0] * 32

        for j in range(32):
            if self.is_set(nums[0], j):
                freq[j] += 1

        while l < n:
            while r + 1 < n and cur != suf[l]:
                r += 1
                cur |= nums[r]
                for j in range(32):
                    if self.is_set(nums[r], j):
                        freq[j] += 1

            res[l] = max(1, r - l + 1)

            for j in range(32):
                if self.is_set(nums[l], j):
                    freq[j] -= 1
                    if freq[j] == 0:
                        cur &= ~(1 << j)

            l += 1

        return res
