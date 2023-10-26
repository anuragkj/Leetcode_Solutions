
MOD = 10**9 + 7
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # Step 1: Sort the input array.
        arr.sort()
        
        # Step 2: Create a set to store unique numbers in the array.
        unique_numbers = set(arr)
        
        # Step 3: Initialize a dynamic programming dictionary.
        dp = {x: 1 for x in arr}
        
        # Step 4: Dynamic Programming
        for i in arr:
            for j in arr:
                # If j is larger than the square root of i, break the loop because further j values won't be factors.
                if j > i**0.5:
                    break
                
                # Check if j is a factor of i and if i/j is in the set of unique numbers.
                if i % j == 0 and i // j in unique_numbers:
                    if i // j == j:
                        # If j and i/j are the same, update dp[i] accordingly.
                        dp[i] += dp[j] * dp[j]
                    else:
                        # If j and i/j are different, update dp[i] accordingly.
                        dp[i] += dp[j] * dp[i // j] * 2
                    dp[i] %= MOD
        
        # Step 5: Calculate the final result.
        result = sum(dp.values()) % MOD
        return result
