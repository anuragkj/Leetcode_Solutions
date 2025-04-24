class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans, left, k = 0, 0, len(set(nums))
        cnt = [0] * (max(nums)+1)
        for n in nums:
            if cnt[n] == 0:
                k -= 1
            cnt[n] += 1
            while k <= 0:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    k += 1
                left += 1
            ans += left  
        return ans
