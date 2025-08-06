# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_level = 1
        def dfs(root, level):
            nonlocal max_level
            if root is None:
                return
            max_level = max(max_level, level)
            dfs(root.left, level+1)
            dfs(root.right, level+1)

        if root is None:
            return 0
        dfs(root, 1)
        return max_level
        
