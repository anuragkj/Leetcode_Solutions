class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
            
        def get_sum(l, r):
            return prefix_sum[r+1] - prefix_sum[l]

        # Identify monotonic intervals
        intervals = []
        i = 0
        while i < n - 1:
            j = i
            if nums[j+1] > nums[j]:
                while j < n - 1 and nums[j+1] > nums[j]: j += 1
                intervals.append((i, j, 1))
            elif nums[j+1] < nums[j]:
                while j < n - 1 and nums[j+1] < nums[j]: j += 1
                intervals.append((i, j, -1))
            else:
                while j < n - 1 and nums[j+1] == nums[j]: j += 1
                intervals.append((i, j, 0))
            i = j

        max_trionic_sum = -float('inf')
        
        for k in range(len(intervals) - 2):
            # Check pattern: Inc (1) -> Dec (-1) -> Inc (1)
            if intervals[k][2] == 1 and intervals[k+1][2] == -1 and intervals[k+2][2] == 1:
                l_limit, p = intervals[k][0], intervals[k][1]
                q, r_limit = intervals[k+1][1], intervals[k+2][1]
                
                # Optimize S1: Maximize suffix sum ending at p
                curr_l = l_limit
                best_s1_sum = get_sum(l_limit, p)
                curr_s1 = best_s1_sum
                while curr_l < p - 1:
                    curr_s1 -= nums[curr_l]
                    best_s1_sum = max(best_s1_sum, curr_s1)
                    curr_l += 1
                
                # Optimize S3: Maximize prefix sum starting at q
                curr_r = q + 1
                best_s3_sum = get_sum(q, q + 1)
                curr_s3 = best_s3_sum
                while curr_r < r_limit:
                    curr_r += 1
                    curr_s3 += nums[curr_r]
                    best_s3_sum = max(best_s3_sum, curr_s3)

                # Combine: S1[best_l...p] + S2[p+1...q-1] + S3[q...best_r]
                # To avoid double counting p and q:
                total = best_s1_sum + get_sum(p + 1, q - 1) + best_s3_sum
                max_trionic_sum = max(max_trionic_sum, total)
                
        return max_trionic_sum
