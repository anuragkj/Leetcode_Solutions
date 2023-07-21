# class Solution:
    # def __init__(self):
    #     self.max_len = -inf
    #     self.result = 0
    # def dfs(self, index, last_index, nums, dp):
    #     if index == 0:
    #         if nums[index] < nums[last_index]:
    #             dp[(index, last_index)] = 1
    #             return 1
    #         else:
    #             dp[(index, last_index)] = 0
    #             return 0
        
    #     if dp[(index, last_index)] != -1:
    #         return dp[(index, last_index)]

    #     l1 = 0 + self.dfs(index - 1, last_index, nums, dp)
    #     l2 = -inf
    #     if nums[index] < nums[last_index]:
    #         l2 = 1 + self.dfs(index - 1, index, nums, dp)
    #     dp[(index, last_index)] = max(l1, l2)
    #     if dp[(index, last_index)] > self.max_len:
    #         self.max_len = dp[(index, last_index)]
    #         self.result = 1
    #     elif dp[(index, last_index)] == self.max_len:
    #         self.result += 1
    #     return dp[(index, last_index)]
    # def findNumberOfLIS(self, nums: List[int]) -> int:
    #     dp = {}
    #     for i in range(len(nums)):
    #         for j in range(-1, len(nums)):
    #             dp[(i,j)] = -1
    #     _ = self.dfs(len(nums) - 1, -1, nums, dp)
    #     return self.result
class Solution:
    def findNumberOfLIS(self, nums):
        n = len(nums)
        length = [0] * n
        count = [0] * n

        def calculate_dp(i):
            if length[i] != 0:
                return

            length[i] = 1
            count[i] = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    calculate_dp(j)
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_length = 0
        result = 0
        for i in range(n):
            calculate_dp(i)
            max_length = max(max_length, length[i])

        for i in range(n):
            if length[i] == max_length:
                result += count[i]

        return result
