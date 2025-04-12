class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # Find factorial of each number when it is required
        fact = {0:1}
        def findFac(n):
            if n not in fact:
                fact[n] = n*findFac(n-1)
            return fact[n]

        # Store the integers we have encountered inorder to not could again
        # For example we don't have to count '8448' again if we have considered rearrangements of '4884'    
        found = set()
        def posRearr(s):
            s = ''.join(sorted(s))              # We just need the count of each digit. Order does not matter
            if s in found:
                return 0                        # Add 0 to answer if already encountered
            digs = [0]*10
            for c in s:
                digs[int(c)] += 1               # Store the count of each digit in the number
            # We are going to use the P&C formula for permutations with repetitions
            # https://brilliant.org/wiki/permutations-with-repetition/
            tot = sum(digs)
            num = (tot-digs[0])*findFac(tot-1)  # Ignore all the numbers that start with 0 
            den = 1
            for d in digs:
                den *= findFac(d)                       
            found.add(s)                        # Add it to found so that we don't check any rearrangement of this
            return num//den

        ans = 0
        # When n is odd, we take n//2+1 digits as first half and append the reverse of this excluding the last digit.
        # For eg, n = 7 | we check all numbers from 1000 to 9999 | eg: we convert 3567 to '3567' + '653'
        # When n is even we take n//2 digits as first half and append the reverse of this.
        # For eg, n = 6 | we check all numbers from 100 to 999 | eg: we convert 748 to '748' + '847'
        for i in range(10**((n-1)//2), 10**((n+1)//2)):
            x = str(i) + str(i)[-1-n%2::-1]
            if int(x)%k==0:                     # Check divisibility by k as it is a necessary condition
                ans += posRearr(x)
        return ans
