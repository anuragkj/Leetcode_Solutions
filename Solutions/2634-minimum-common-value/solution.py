class Solution:
    def getCommon(self, nums1, nums2):
        nums1, nums2 = (
            (set(nums1), nums2)
            if len(nums1) < len(nums2)
            else (set(nums2), nums1)
        )

        for x in nums2:
            if x in nums1:
                return x

        return -1
