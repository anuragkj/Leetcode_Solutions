class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        # Loop through the array up to the third-to-last element
        for i in range(len(arr) - 2):
            product = arr[i] * arr[i + 1] * arr[i + 2]
            # Check if the product is odd
            if product % 2 == 1:
                return True
        return False
