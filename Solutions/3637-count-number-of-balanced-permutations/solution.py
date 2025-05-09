
class Solution:
    def countBalancedPermutations(self, num: str) -> int:

        @lru_cache(8000)
        def dp(odd_digits, evn_digits, odd_sum, digit, res = 0):

            if digit > 9: return (odd_sum, odd_digits) == (odd_target, odd_cnt)

            for odd_add in range(ctr[digit] + 1):
                evn_add = ctr[digit] - odd_add

                if (digit * odd_add + odd_sum > odd_target or
                    odd_digits + odd_add > odd_cnt or 
                    evn_digits + evn_add > evn_cnt): continue

                res+= (dp(odd_digits + odd_add,
                          evn_digits + evn_add,
                          odd_sum + digit * odd_add,
                          digit + 1) %mod_ *

                       comb(odd_cnt - odd_digits, odd_add) %mod_ *
                       comb(evn_cnt - evn_digits, evn_add) %mod_)

            return res %mod_


        mod_ = 1_000_000_007

        sm = sum([int(ch) for ch in num])
        if sm % 2: return 0

        ctr = [0] * 10
        for ch in num: ctr[int(ch)]+= 1

        odd_cnt, evn_cnt, odd_target = len(num)//2, (len(num)+1)//2, sm//2
        
        return dp(0,0,0,0) %mod_
