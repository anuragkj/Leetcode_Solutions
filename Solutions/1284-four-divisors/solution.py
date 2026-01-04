n = 100001
all_divisors = [[] for _ in range(n)]
for k in range(2, n//2+1):
    if not all_divisors[k]:
        for kk in range(k+k, n, k):
            all_divisors[kk].append(k)

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            divisors = all_divisors[num]
            if len(divisors) == 2 and mul(*divisors) == num:
                ans += 1 + sum(divisors) + num
            elif len(divisors) == 1 and divisors[0] ** 3 == num:
                ans += 1 + divisors[0] * (divisors[0] + 1) + num
        return ans
