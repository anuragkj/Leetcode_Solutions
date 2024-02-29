# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        que = deque([root])
        while(que):
            node = que.popleft()
            if node.right is not None:
                que.append(node.right)
            if node.left is not None:
                que.append(node.left)
        return node.val
        
