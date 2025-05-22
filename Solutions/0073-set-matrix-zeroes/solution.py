class Solution:
    def setZeroes(self, g: List[List[int]]) -> None:
        r, c = [*map(all,g)], [*map(all,zip(*g))]
        for i,j in product(range(len(g)),range(len(g[0]))):
            g[i][j] *= r[i]&c[j]
