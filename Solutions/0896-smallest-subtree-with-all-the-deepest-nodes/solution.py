# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        hashMap={}
        ans=[]
        output=[]
        if not root:
            return []
        if root and(not root.right and not root.left):
            return root
        q=deque()
        q.append(root)
        parent=None
        while q:
            size=len(q)
            output=[]
            for _ in range(size):
                node=q.popleft()
                output.append(node)
                if node.left:
                    hashMap[node.left]=node
                    q.append(node.left)
                    
                if node.right:
                    hashMap[node.right]=node
                    q.append(node.right)
        while len(output)>1:
            temp=set()
            for i in output:
                parent=hashMap[i]
                temp.add(parent)
            output=list(temp)
        return output[0]
        
       
