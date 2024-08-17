class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        r, c=len(points), len(points[0])
        for i in range(1, r):
            left, right=[0]*c, [0]*c

            right[-1]=points[i-1][-1]
            for j in range(c-2, -1, -1):
                right[j]=max(right[j+1]-1, points[i-1][j])
            
            left[0]=points[i-1][0]
            points[i][0]=max(left[0], right[0])+points[i][0]
            for j in range(1, c):
                left[j]=max(left[j-1]-1, points[i-1][j])
                points[i][j]=max(left[j], right[j])+points[i][j]
                
        return max(points[-1])
