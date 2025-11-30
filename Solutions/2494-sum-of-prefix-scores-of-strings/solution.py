class TrieNode:
    def __init__(self, val = ''):
        self.value = val
        self.count = 0
        self.children = {}
        self.end = 'False'

class Trie:
    def __init__(self):
        self.root = TrieNode('')
    
    def insert(self, word):
        start = self.root
        for ch in word:
            if ch in start.children:
                start = start.children[ch]
                start.count+=1
            else:
                node_to_insert = TrieNode(ch)
                start.children[ch] = node_to_insert
                start = node_to_insert
                start.count+=1
        start.end = True

    def search(self, word):
        start = self.root
        ret = 0
        for ch in word:
            ret += start.count
            start = start.children[ch]
        ret+=start.count
        return ret

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for i in words:
            trie.insert(i)
        ret = []
        for i in words:
            ret.append(trie.search(i))
        return ret
