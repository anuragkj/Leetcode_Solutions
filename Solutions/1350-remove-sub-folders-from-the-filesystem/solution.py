class TrieNode():
    def __init__(self):
        self.is_word= False
        self.children={}

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        node = TrieNode()
        folder.sort()
        output=[]
        for i in folder:
            fol=i.split("/")
            root=node
            flag=0
            for x in fol:
                if x not in root.children:
                    root.children[x] = TrieNode()
                root= root.children[x]
                if root.is_word:
                    flag=1
                    break
            if flag==0:
                root.is_word= True
                output.append(i)
        return output                    
