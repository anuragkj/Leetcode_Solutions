class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        def solve(idx):
            if idx >= n:
                return 0
            if memo[idx] != -1:
                return memo[idx]  
            memo[idx] = max((unq[idx] * freq[unq[idx]]) + solve(next_indices[idx]), solve(idx + 1))
            return memo[idx]
        freq = Counter(power)
        unq = sorted(freq.keys())
        n = len(unq)
        memo = [-1] * n
        next_indices = [bisect_right(unq, unq[i] + 2) for i in range(n)]
        return solve(0)
