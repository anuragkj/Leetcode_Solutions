# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy = TreeNode()
        dummy.left = root
        q,level = deque([dummy]),0

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if level==depth-1:
                    newLeft = TreeNode(val)
                    newLeft.left,node.left = node.left,newLeft

                    newRight = TreeNode(val)
                    newRight.right,node.right = node.right,newRight

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
            if level==depth:
                break

        return dummy.left
                    
                    


