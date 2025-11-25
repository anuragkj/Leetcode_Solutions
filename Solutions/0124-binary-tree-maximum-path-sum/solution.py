# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_path_sum = root.val
        def dfs(node):
            nonlocal max_path_sum
            if node is None:
                return 0
            
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            max_path_sum = max(max_path_sum, node.val+left+right)
            return max(node.val, node.val+left, node.val+right)

        dfs(root)
        return max_path_sum
        
