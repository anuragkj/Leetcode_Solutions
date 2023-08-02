class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        final = []
        def rec(curr):
            if len(curr) == n:
                final.append(curr.copy())
                return 
            for i in nums:
                if i not in curr:
                    curr.append(i)
                    rec(curr)
                    curr.remove(i)
        rec([])
        return final
