# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        diff = float("inf")

        
        def DFS(node):
            nonlocal prev, diff
            if node == None:
                return
            DFS(node.left)
            if prev:
                diff = min(diff, node.val - prev.val)
            prev = node
            DFS(node.right)

        DFS(root)
        return diff
