class Solution:
#     def dfs(self, index, last_index, nums, dp):
#         if index == 0:
#             if last_index == -1 or nums[index] < nums[last_index]:
#                 dp[(index, last_index)] = 1
#                 return 1
#             else:
#                 dp[(index, last_index)] = 0
#                 return 0
        
#         if dp[(index, last_index)] != -1:
#             return dp[(index, last_index)]

#         l1 = 0 + self.dfs(index - 1, last_index, nums, dp)
#         l2 = -inf
#         if last_index == -1 or nums[index] < nums[last_index]:
#             l2 = 1 + self.dfs(index - 1, index, nums, dp)
#         dp[(index, last_index)] = max(l1, l2)
#         return dp[(index, last_index)]
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         dp = {}
#         for i in range(len(nums)):
#             for j in range(-1, len(nums)):
#                 dp[(i,j)] = -1
#         return self.dfs(len(nums) - 1, -1, nums, dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        total_number = len(nums)
        dp = [0 for _ in range(total_number)]
        for i in range(1, total_number):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) + 1
