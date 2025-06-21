class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(Counter(word).values())
        freq.sort()
        n = len(freq)
        answer = float('inf')

        for i in range(n):
            min_freq = freq[i]
            deletions = 0
            for j in range(i):
                deletions += freq[j]  
            for j in range(i, n):
                if freq[j] > min_freq + k:
                    deletions += freq[j] - (min_freq + k)
            answer = min(answer, deletions)
        
        return answer
