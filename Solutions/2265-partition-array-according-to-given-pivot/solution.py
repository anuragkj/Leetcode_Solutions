class Solution:
    def pivotArray(self, nums, pivot):
        lCount, pCount = 0, 0
        for num in nums:
            if num < pivot:
                lCount += 1
            elif num == pivot:
                pCount += 1

        res = [0] * len(nums)
        left, mid, right = 0, lCount, lCount + pCount

        for num in nums:
            if num < pivot:
                res[left] = num
                left += 1
            elif num > pivot:
                res[right] = num
                right += 1
            else:
                res[mid] = num
                mid += 1

        return res
