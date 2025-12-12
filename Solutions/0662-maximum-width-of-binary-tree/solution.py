from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((0,root))
        ret = 1

        while(queue):
            l = len(queue)
            ret = max(ret, queue[-1][0]-queue[0][0]+1)
            for i in range(l):
                index, node = queue.popleft()
                if node.left:
                    queue.append((index*2, node.left))
                if node.right:
                    queue.append((index*2+1, node.right))

        return ret        
