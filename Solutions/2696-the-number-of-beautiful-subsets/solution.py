class Solution:
    def beautifulSubsets(self, nums, k):
        return self._count_beautiful_subsets(nums, k, 0, 0)

    def _count_beautiful_subsets(self, nums, difference, index, mask):
        # Base case: Return 1 if mask is greater than 0 (non-empty subset)
        if index == len(nums):
            return 1 if mask > 0 else 0

        # Flag to check if the current subset is beautiful
        is_beautiful = True

        # Check if the current number forms a beautiful pair with any 
        # previous number in the subset
        for j in range(index):
            if ((1 << j) & mask) == 0 or \
               abs(nums[j] - nums[index]) != difference:
                continue
            else:
                is_beautiful = False
                break

        # Recursively calculate beautiful subsets including and excluding 
        # the current number
        skip = self._count_beautiful_subsets(nums, difference, index + 1, mask)
        take = (
            self._count_beautiful_subsets(
                nums, difference, index + 1, mask + (1 << index)
            )
            if is_beautiful
            else 0
        )

        return skip + take
