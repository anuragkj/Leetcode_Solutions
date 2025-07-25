class Solution:
 def maxSum(_,N):return sum({i for i in N if i>0})or max(N)
