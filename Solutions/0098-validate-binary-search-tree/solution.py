# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, maxi, mini):
            if node is None:
                return True
            if node.val <= mini or node.val >= maxi:
                return False
            return dfs(node.left, node.val, mini) and dfs(node.right, maxi, node.val)
        return dfs(root, float('inf'), -float('inf'))
        
