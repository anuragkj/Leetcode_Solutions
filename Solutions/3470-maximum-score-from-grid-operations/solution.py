class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        r0, r1, pref = range(n), range(n+1), []
        curr = [[0, 0] for _ in r1]

        pref = [list(accumulate(col, initial = 0))
                                    for col in zip(*grid)]
        
        for i in reversed(r0):
            prev, curr = curr, [[0, 0] for _ in r1]

            for j, k, option in product(r1, r1, (0,1)):

                if  k > j and i != 0 and option == 1:
                    curr[j][1] = max(curr[j][1], 
                             pref[i - 1][k] - pref[i - 1][j] + prev[k][1])
                             
                elif j > k:
                    curr[j][option] = max(curr[j][option],
                            pref[i][j] - pref[i][k] + prev[k][0])

                else:
                    curr[j][option] = max(curr[j][0], prev[k][1])

        return max(*curr[0])
