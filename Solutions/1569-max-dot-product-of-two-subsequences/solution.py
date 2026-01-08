class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)
        if M > N:
            nums1, nums2 = nums2, nums1
            N, M = M, N

        curr = [-inf] * (M+1)
        for n in nums1:
            prev = 0
            for j in range(M):
                v = n * nums2[j]
                curr[j], prev = max(prev + v, v, curr[j-1], curr[j]), curr[j]
        return curr[-2]
