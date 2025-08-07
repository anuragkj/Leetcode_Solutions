# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        ans = 0
        def dfs(root):
            nonlocal ans
            nonlocal counter
            if root is None:
                return
            dfs(root.left)
            counter += 1
            if counter == k:
                ans = root.val
                return
            dfs(root.right)
        dfs(root)
        return ans
