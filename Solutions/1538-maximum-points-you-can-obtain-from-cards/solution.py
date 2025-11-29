class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum=rsum=0
        for i in range(k):
            lsum+=cardPoints[i]
        max_score=lsum
        rightIndex = len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rightIndex]
            rightIndex-=1
            max_score = max(max_score,lsum+rsum)
        return max_score
