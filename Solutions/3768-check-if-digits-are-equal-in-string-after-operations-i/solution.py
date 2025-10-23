class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(digits) for digits in s]  
        n = len(s)
        # let's calculate all the relevant binomial coefficients:
        binomial_coeff = [comb(n-2,i) for i in range(n-1)] 
        # calculating the final left and right digits
        left = sum([digit*coeff for digit, coeff in zip(s[:-1], binomial_coeff)]) % 10
        right = sum([digit*coeff for digit, coeff in zip(s[1:], binomial_coeff)]) % 10
        return left == right
