class Solution:
    def numDecodings(self, s: str) -> int:
        # memo[i] will store the number of ways to decode s[i:]
        memo = {} 

        def dfs(i):
            # If we've already computed this subproblem, return the stored result
            if i in memo:
                return memo[i]

            # Base Case 1: If we've reached the end of the string, we've found one valid way.
            if i == len(s):
                return 1

            # Base Case 2: A code cannot start with '0'. This is an invalid path.
            if s[i] == "0":
                return 0

            # --- Recursive Step ---

            # Option 1: Decode the current single digit (s[i])
            # The number of ways for this option is the number of ways to decode the rest of the string.
            res = dfs(i + 1)

            # Option 2: Decode the current two digits (s[i:i+2])
            # This is only possible if we have at least 2 digits left AND the number is <= 26.
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                res += dfs(i + 2)
            
            # Store the result for this subproblem before returning
            memo[i] = res
            return res
        
        return dfs(0)
