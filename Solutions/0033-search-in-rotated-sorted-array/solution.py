class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        rot = bisect_left(nums, True, key=lambda n: n <= nums[-1])
        
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            real = (mid + rot) % n

            if nums[real] == target:
                return real
                
            if nums[real] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1
