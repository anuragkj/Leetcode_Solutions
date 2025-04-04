# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return (0, None) # (depth, lca)
            l, l_lca = dfs(node.left)
            r, r_lca = dfs(node.right)
            if l == r: return (l + 1, node)
            return (l + 1, l_lca) if l > r else (r + 1, r_lca)
        return dfs(root)[1]
