class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        a="zyxwvutsrqponmlkjihgfedcba"
        b=""
        for i in words:
            c=0
            for j in i:
                c+=weights[ord(j)-97]
            b+=a[c%26]
        return b
