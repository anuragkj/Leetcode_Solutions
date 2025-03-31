class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights) == k or k == 1:
            return 0

        # Compute the sum of adjacent pairs
        wt_sum = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        wt_sum.sort()

        # Calculate the difference between the maximum and minimum sums
        return sum(wt_sum[-(k - 1):]) - sum(wt_sum[:k - 1])
