class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        seen = set()
        binCodes = 2 ** k

        l = 0
        r = k

        while r < len(s)+1:

            window = s[l:r]
            
            seen.add(window)

            l+=1
            r+=1


        return len(seen) == binCodes

        
        
