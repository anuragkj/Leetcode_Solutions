class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        l, r, res = 0, 0, 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] + nums[i - 1] < lower:
                break
            if nums[i] + nums[l] > upper:
                continue
            while r < i and nums[r] + nums[i] <= upper:
                r += 1
            if r == i or nums[r] + nums[i] > upper:
                r -= 1
            while l <= r and nums[l] + nums[i] < lower:
                l += 1
            if l <= r:
                res += r - l + 1
        return res
