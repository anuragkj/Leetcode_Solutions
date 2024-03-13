class Solution:
    def pivotInteger(self, n: int) -> int:
        # Iterate through possible pivot values
        for i in range(1, n + 1):
            # Calculate the sum of elements on the left side of the pivot
            sum_left = sum(range(1, i + 1)) 
            # Calculate the sum of elements on the right side of the pivot
            sum_right = sum(range(i, n + 1)) 

            # Check if the sums on both sides are equal
            if sum_left == sum_right:
                return i  # Return the pivot value if found

        return -1  # Return -1 if no pivot is found
