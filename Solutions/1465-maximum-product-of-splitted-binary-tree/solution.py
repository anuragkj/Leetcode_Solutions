# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 1000000007
        def s(root):
            if not root:
                return 0
            return root.val + s(root.left) + s(root.right)
        total = s(root)
        ans = 1
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            ans = max(ans, (total - l) * l)
            ans = max(ans, (total - r) * r)
            return l + r + root.val
        dfs(root)
        return ans % mod
