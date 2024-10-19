class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ['0']
        for i in range(1,n):
            t = ''
            for j in s[i-1]:
                if j == '0':
                    t += '1'
                else:
                    t += '0'
            s.append(s[i-1] + '1' + t[::-1])
        return s[n-1][k-1]      
