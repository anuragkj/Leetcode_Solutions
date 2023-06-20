class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        divisor = 2*k + 1
        result = []
        window = nums[0:2*k+1]
        sum_window = sum(window)
        average = sum_window//divisor
        result.append(average)
        pop_val = 0
        for i in range(2*k+1, len(nums)):
            rem = window.pop(0)
            window.append(nums[i])
            sum_window = sum_window - rem + nums[i]
            result.append(sum_window//divisor)
        output = []
        for i in range(len(nums)):
            if i<k:
                output.append(-1)
            elif i>= k and i< len(nums) - k:
                    output.append(result[i-k])
            else:
                output.append(-1)
        return output



