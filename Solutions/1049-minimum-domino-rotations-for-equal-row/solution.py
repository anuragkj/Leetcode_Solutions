class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        total = len(tops)
        top_fr, bot_fr, val_total = [0]*7, [0]*7, [total]*7
        for top, bot in zip(tops, bottoms):
            if top == bot:
                val_total[top] -= 1
            else:
                top_fr[top] += 1
                bot_fr[bot] += 1
                
        for val in range(1, 7):
            if (val_total[val] - top_fr[val]) == bot_fr[val]:
                return min(top_fr[val], bot_fr[val])
            
        return -1
