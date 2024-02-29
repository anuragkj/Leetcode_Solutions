# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        que = deque([root])
        level = 0
        while(que):
            if level % 2 == 0:
                last = float('-inf')
            else:
                last = float('inf')
            for i in range(len(que)):
                node = que.popleft()
                if ((level % 2) == (node.val % 2)) or (level % 2 == 1 and node.val >= last) or (level % 2 == 0 and node.val <= last):
                    return False
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
                last = node.val
            level += 1
        return True
