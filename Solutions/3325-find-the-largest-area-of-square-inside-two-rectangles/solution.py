class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        result = 0
        n = len(bottomLeft)
        for i in range(n-1):
            for j in range(i+1,n):
                left = max(bottomLeft[i][0],bottomLeft[j][0])
                right = min(topRight[i][0],topRight[j][0])
                top = min(topRight[i][1],topRight[j][1])
                bottom = max(bottomLeft[i][1],bottomLeft[j][1])
                width = right - left
                heigh = top - bottom
                if width > 0  and heigh > 0:
                    res = min(width,heigh)
                    result = max(result , res*res)
        return result
