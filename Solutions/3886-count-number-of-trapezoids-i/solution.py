class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        cnt = Counter([y for _, y in points])  # counts the number of points with a given y value
        MOD = 1000000007
        ans = 0
        pairs_up_to_now = 0
        for k, v in cnt.items():
            if v < 2:  # if we can't form a pair / an edge, skip
                continue
            new_pairs = v * (v-1) // 2
            ans = (ans + new_pairs * pairs_up_to_now) % MOD
            pairs_up_to_now += new_pairs
        return ans
