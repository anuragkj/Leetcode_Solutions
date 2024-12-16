class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int):
        n = len(nums)

        for _ in range(k):
            # Find the index of the smallest element in the array
            min_index = 0
            for i in range(n):
                if nums[i] < nums[min_index]:
                    min_index = i

            # Multiply the smallest element by the multiplier
            nums[min_index] *= multiplier

        return nums
