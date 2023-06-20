class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median_indices = []
        median_values = []
        total_len = (len(nums1) + len(nums2))
        if total_len % 2 == 0:
            median_indices.append(total_len//2 - 1)
            median_indices.append(total_len//2)
        else:
            median_indices.append(total_len//2)
        
        i = 0
        j = 0
        k = -1
        sto = -1

        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]<=nums2[j]:
                sto = nums1[i]
                i += 1
                k += 1
            else:
                sto = nums2[j]
                j += 1
                k += 1

            if k in median_indices:
                median_values.append(sto)

        while(i<len(nums1)):
            sto = nums1[i]
            i += 1
            k += 1

            if k in median_indices:
                median_values.append(sto)

        while(j<len(nums2)):
            sto = nums2[j]
            j += 1
            k += 1

            if k in median_indices:
                median_values.append(sto)

        return sum(median_values)/len(median_values)
