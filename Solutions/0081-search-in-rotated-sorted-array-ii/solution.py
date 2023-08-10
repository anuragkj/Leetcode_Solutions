class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)  # size of the numsay
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            # if mid points to the target
            if nums[mid] == target:
                return True

            # Edge case:
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # if left part is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    # element exists
                    high = mid - 1
                else:
                    # element does not exist
                    low = mid + 1
            else:  # if right part is sorted
                if nums[mid] <= target <= nums[high]:
                    # element exists
                    low = mid + 1
                else:
                    # element does not exist
                    high = mid - 1

        return False
