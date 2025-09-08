# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        count = 0
        def dfs(i, maxi):
            nonlocal count
            if not i:
                return
            if i.val >= maxi:
                count+=1
                maxi = i.val
            dfs(i.left, maxi)
            dfs(i.right, maxi)

        dfs(root, float('-inf'))
        return count
        
