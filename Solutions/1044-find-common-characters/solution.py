class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        dic = defaultdict(list)
        for i in range(len(words)):
            dic[i] = Counter(words[i])

        for ch in words[0]:
            same = True
            for i in range(len(words)):
                if dic[i][ch] <= 0:
                    same = False
                    break
                dic[i][ch] -= 1
            if same:
                res.append(ch)
        return res
