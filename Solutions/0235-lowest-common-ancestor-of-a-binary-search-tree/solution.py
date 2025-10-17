# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def dfs(node):
            if node is None:
                return
            if node.val > p.val and node.val>q.val:
                return dfs(node.left)
            elif node.val < p.val and node.val<q.val:
                return dfs(node.right)
            else:
                return node
        
        return dfs(root)
