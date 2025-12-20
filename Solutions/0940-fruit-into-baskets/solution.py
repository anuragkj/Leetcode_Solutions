class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = defaultdict(int)
        l = 0
        maxi = 0
        for r in range(len(fruits)):
            baskets[fruits[r]] += 1
            while len(baskets.keys()) > 2:
                baskets[fruits[l]] -= 1
                if baskets[fruits[l]] == 0:
                    del baskets[fruits[l]]
                l+=1
            maxi = max(maxi, r-l+1)
        return maxi
