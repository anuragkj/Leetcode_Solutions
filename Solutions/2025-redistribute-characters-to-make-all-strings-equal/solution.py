class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hash_map = defaultdict(int)
        l = len(words)
        for word in words:
            for letter in word:
                hash_map[letter] += 1
        for i in hash_map.values():
            if i % l != 0:
                return False
        return True
