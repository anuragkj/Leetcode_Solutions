from collections import defaultdict, deque

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(deque)
        for word in words:
            buckets[word[0]].append((word, 0))

        count = 0
        for c in s:
            queue = buckets[c]
            for _ in range(len(queue)):
                word, i = queue.popleft()
                i += 1
                if i == len(word):
                    count += 1
                else:
                    buckets[word[i]].append((word, i))
        return count
