from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_val = 0
        mp = defaultdict(int)

        for num in nums:
            sum_val += num

            if sum_val == k:
                count += 1

            if sum_val - k in mp:
                count += mp[sum_val - k]

            mp[sum_val] += 1

        return count

    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        count = 0

        for i in range(len(matrix)):
            sum_val = [0] * len(matrix[0])

            for j in range(i, len(matrix)):
                for k in range(len(matrix[0])):
                    sum_val[k] += matrix[j][k]

                count += self.subarraySum(sum_val, target)

        return count

