class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        sartWordset=set()
        for i in  range(len(startWords)):
           sartWordset.add("".join(sorted(startWords[i])))
        
        for j in range(len(targetWords)):
            targetWords[j]="".join(sorted(targetWords[j]))

        cnt =0
        for word in targetWords:
            for bp in range(len(word)):
                newWord = word[:bp] + word[bp+1:]
                #print(newWord,word)
                if newWord in sartWordset:
                    cnt+=1
                    break
        return cnt

