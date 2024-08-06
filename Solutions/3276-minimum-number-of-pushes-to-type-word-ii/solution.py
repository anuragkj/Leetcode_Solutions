class Solution:
    def minimumPushes(self, word):
        arr = [0] * 26
        
        for char in word:
            arr[ord(char) - ord('a')] += 1
        
        arr.sort(reverse=True)
        
        res = 0
        for i in range(len(arr)):
            res += arr[i] * ((i // 8) + 1)
        
        return res

        
