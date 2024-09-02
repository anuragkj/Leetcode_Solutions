class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)

        prefix_sum = [0] * n
        prefix_sum[0] = chalk[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + chalk[i]

        sum_chalk = prefix_sum[n - 1]
        remaining_chalk = k % sum_chalk

        return self.__binary_search(prefix_sum, remaining_chalk)

    def __binary_search(self, arr, tar):
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = low + (high - low) // 2

            if arr[mid] <= tar:
                low = mid + 1
            else:
                high = mid

        return high
