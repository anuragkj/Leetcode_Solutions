class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid]<=nums[r]:
                # right hald is sorted
                if target <= nums[r] and target >= nums[mid]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                # left half is sorted
                if target >= nums[l] and target <= nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
        return -1
