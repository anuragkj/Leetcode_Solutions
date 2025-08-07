from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []

        if not root:
            return ret
        queue = deque([root])

        while(queue):
            queue_length = len(queue)
            temp = []
            print(ret)
            for i in range(queue_length):
                ele = queue.popleft()
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
                temp+=[ele.val]
            ret.append(temp)
        return ret
        
