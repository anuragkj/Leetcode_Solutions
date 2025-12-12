from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        len_dict = defaultdict(list)
        for word in words:
            len_dict[len(word)].append(word)

        memo = {}

        def chain(w1, w2):
            l1 = 0
            l2 = 0
            diff = 0
            while l1<len(w1) and l2<len(w2):
                if w1[l1] == w2[l2]:
                    l1+=1
                    l2+=1
                elif diff < 1:
                    l2+=1
                    diff+=1
                else:
                    return False

            return True

        def dfs(word):
            max_word_len = 1
            if word in memo:
                return memo[word]
            
            for next_word in len_dict[len(word)+1]:
                if chain(word, next_word):
                    max_word_len = max(max_word_len, 1+dfs(next_word))

            memo[word] = max_word_len
            return max_word_len

        words.sort(key = lambda x: len(x))
        ret = 0
        for word in words:
            ret = max(ret, dfs(word))
        return ret
