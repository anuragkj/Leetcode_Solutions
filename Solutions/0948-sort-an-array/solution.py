class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        counting: list[int] = [0 for _ in range(2 * 5 * 10**4 + 1)]
        for num in nums:
            # we add 5 * 10^4 because for smallest possible element -5 * 10^4 index must be 0
            counting[num + 5 * 10**4] += 1
        write_ind: int = 0
        for number_ind, freq in enumerate(counting):
            while freq != 0:
                nums[write_ind] = number_ind - 5 * 10**4
                write_ind += 1
                freq -= 1

        return nums
