class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>0:
            q, r=divmod(n, 3)
            if r==2: return False
            n=q
        return True
