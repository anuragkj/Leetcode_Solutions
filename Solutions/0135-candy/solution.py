class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        c = [1] * n
        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                c[i] = c[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                c[i] = max(c[i], c[i+1] + 1)


        return sum(c)
