class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        c1 = False  # increasing
        c2 = False  # decreasing
        c3 = False  # increasing again

        for i in range(1, len(nums)):
            prev = nums[i - 1]
            curr = nums[i]

            # Phase 1: increasing
            if not c1:
                if curr > prev:
                    c1 = True
                else:
                    return False  # must increase in the start

            # Phase 2: decreasing
            elif c1 and not c2:
                if curr > prev:
                    continue  # still increasing (consider in phase1)
                elif curr < prev:
                    c2 = True  # decreasing started
                else:
                    return False  # no flat values allowed

            # Phase 3 start: increasing again
            elif c1 and c2 and not c3:
                if curr < prev:
                    continue  # still decreasing (consider in phase2)
                elif curr == prev:
                    return False  # no flat values allowed
                else:
                    c3 = True  # second increasing started

            # Phase 3 continuation: must strictly increase
            elif c1 and c2 and c3:
                if curr <= prev:
                    return False  # cannot go down or stay flat

        return c1 and c2 and c3
