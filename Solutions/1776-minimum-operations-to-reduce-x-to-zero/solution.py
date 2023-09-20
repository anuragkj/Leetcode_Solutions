class Solution:
    def minOperations(self, nums, targetSum) -> int:
        totalSum = sum(nums)
        target = totalSum - targetSum  # Calculate the target sum difference

        if target < 0:
            return -1  # Return -1 if target sum is not achievable

        if target == 0:
            return len(nums)  # Return the number of elements if target sum is 0

        n = len(nums)  # Number of elements in the list
        minOperations = float('inf')  # Minimum operations to achieve the target sum
        currentSum = 0  # Current sum of elements
        leftIndex = 0
        rightIndex = 0  # Pointers for the sliding window

        while rightIndex < n:
            currentSum += nums[rightIndex]
            rightIndex += 1

            while currentSum > target and leftIndex < n:
                currentSum -= nums[leftIndex]
                leftIndex += 1

            if currentSum == target:
                minOperations = min(minOperations, n - (rightIndex - leftIndex))

        return -1 if minOperations == float('inf') else minOperations  # Return the minimum operations or -1 if not possible
