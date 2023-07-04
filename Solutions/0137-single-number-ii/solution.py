class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        accepted_set = set()
        rejected_set = set()
        for i in nums:
            if i in accepted_set:
                accepted_set.remove(i)
                rejected_set.add(i)
            elif i not in rejected_set:
                accepted_set.add(i)

        for i in accepted_set:
            return i
