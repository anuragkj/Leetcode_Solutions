class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        
		# UNION FIND
        par = {i: i for i in range(n)}
        rank = {i: 1 for i in range(n)}
        
        def find(n1):
            while n1 != par[n1]:
                par[n1] = par[par[n1]]
                n1 = par[n1]
            return n1
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] < rank[p2]:
                p1, p2 = p2, p1
            par[p2] = p1
            rank[p1] += rank[p2]
            return 1
        
		# TO FIND PRIME FACTORS
        def getPrimeDivs(n):
            if n < 0: return []
            res = set()

            for i in range(2, isqrt(n) + 1):
                while n % i == 0:
                    res.add(i)
                    n //= i

            if n > 1: res.add(n)
            return res
        
        primes = defaultdict(list) # Stores the indices of elements having key as a prime factor
        for idx, i in enumerate(nums):
            primeDivs = getPrimeDivs(i)
            
            for p in primeDivs:
                primes[p].append(idx)
        
		# UNITE INDICES HAVING SAME PRIME FACTORS
        for p in primes:
            for i in primes[p]:
                union(i, primes[p][0])
        
		# CHECK IF THE GRAPH IS CONNECTED
        return sum(i == find(i) for i in range(n)) == 1
