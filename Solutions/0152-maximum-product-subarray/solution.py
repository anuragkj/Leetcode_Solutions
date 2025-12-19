class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.memo = {}
        def dfs(i, currentProduct):
            key = (i, currentProduct)
            if (key in self.memo):
                return self.memo[key]
            if (i >= len(nums)):
                return currentProduct
			# 3 choices, Include the current number in the product, start a new product, or end the product
            ans = max(dfs(i + 1, currentProduct * nums[i]), dfs(i + 1, nums[i]), currentProduct)
            self.memo[key] = ans
            return ans
        return dfs(1, nums[0])
