class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        hs = defaultdict(int)

        print(hs)
        cnt = 0

        for i in range(len(answers)):
            if answers[i] in hs:
                if hs[answers[i]] == answers[i] + 1:
                    cnt += (answers[i] + 1)
                    hs[answers[i]] = 1
                else:
                    hs[answers[i]] += 1
            else:
                hs[answers[i]] += 1

        for e in hs:
            cnt += ((e + 1) if e != 0 else hs[e])
            print(cnt, e)
        
        return (cnt)
