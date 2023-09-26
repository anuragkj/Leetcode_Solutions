class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = collections.Counter(s)
        result = []
        visited = set()
        
        for c in s:
            count[c] -= 1
            if c in visited:
                continue
            while result and c < result[-1] and count[result[-1]] > 0:
                visited.remove(result.pop())
            visited.add(c)
            result.append(c)
            
        return ''.join(result)
