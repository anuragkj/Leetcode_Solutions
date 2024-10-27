class Solution:  
    def maximumSubarraySum(self, monthlyPrices: List[int], k: int) -> int:  
        start = 0  
        currentSum = 0  
        maxSum = 0  
        lastSeen = {}  
  
        for end in range(len(monthlyPrices)):  
            if monthlyPrices[end] in lastSeen and lastSeen[monthlyPrices[end]] >= start:  
                start = lastSeen[monthlyPrices[end]] + 1  # update start to repeat element + 1  
                currentSum = 0  
                for idx in range(start, end):  
                    currentSum += monthlyPrices[idx]  
            currentSum += monthlyPrices[end]  
            lastSeen[monthlyPrices[end]] = end  # update elements  
            if end - start + 1 == k:  
                maxSum = max(maxSum, currentSum)  
                currentSum -= monthlyPrices[start]  
                start += 1  
  
        return maxSum  
