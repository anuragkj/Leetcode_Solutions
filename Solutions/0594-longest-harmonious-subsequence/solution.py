class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Solution 3: One-liner
        return (lambda c: max((c[x]+c[x+1] for x in c if x+1 in c), default=0))(Counter(nums))

        # Solution 1: First solution
        cnt, res = Counter(nums), 0
        for x in cnt:
            if x + 1 in cnt:
                res = max(res, cnt[x] + cnt[x + 1])
        return res

        # Solution 2: Two-liner
        c = Counter(nums)
        return max((c[k] + c[k+1] for k in c if k+1 in c), default=0)

        # Solution 4: Sort + Sliding Window
        nums.sort()
        i = res = 0
        for j in range(len(nums)):
            while nums[j] - nums[i] > 1:
                i += 1
            if nums[j] - nums[i] == 1:
                res = max(res, j - i + 1)
        return res
