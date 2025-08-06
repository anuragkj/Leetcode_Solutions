# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check_equivalence(root, sub_root):
            if not root and not sub_root:
                return True
            if not root or not sub_root or (root.val != sub_root.val):
                return False

            left_check = check_equivalence(root.left, sub_root.left)
            right_check = check_equivalence(root.right, sub_root.right)
            return left_check and right_check

        def root_dfs(root):
            if root is None:
                return False

            equivalence = False
            if root.val == subRoot.val:
                equivalence = check_equivalence(root, subRoot)
            
            return equivalence or root_dfs(root.left) or root_dfs(root.right)
        
        return root_dfs(root)
        
