class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0  # Count of Good Squads
        n = len(nums)

        # Check each group of 3 consecutive soldiers
        for i in range(n - 2):
            first = nums[i]
            middle = nums[i + 1]
            third = nums[i + 2]

            # Check if the squad is a Good Squad
            if (first + third) * 2 == middle:
                count += 1  # Good Squad!

        return count  # Return total Good Squads count
