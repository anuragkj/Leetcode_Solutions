class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        right = 0
        false_vals = 0 
        true_vals = 0
        ret = -float('inf')
        for right in range(len(answerKey)):
            if answerKey[right] == 'T':
                true_vals += 1
            else:
                false_vals += 1

            if true_vals <= k or false_vals <= k:
                ret = max(ret, right - left + 1)
            else:
                while(true_vals > k and false_vals > k):
                    if answerKey[left] == 'T':
                        true_vals -= 1
                    else:
                        false_vals -= 1
                    left += 1

        return ret
