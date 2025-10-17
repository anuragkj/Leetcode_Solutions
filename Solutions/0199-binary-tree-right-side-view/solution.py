# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []

        if root is None:
            return ret
        
        q = deque([root])

        while q:
            lvl = -1
            for _ in range(len(q)):
                lvl = q.popleft()
                if lvl.left is not None:
                    q.append(lvl.left)
                if lvl.right is not None:
                    q.append(lvl.right)
            ret.append(lvl.val)
        return ret
