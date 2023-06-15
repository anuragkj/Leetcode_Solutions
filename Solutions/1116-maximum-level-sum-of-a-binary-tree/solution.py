# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        k = 1
        q1 = [root]
        q2 = []
        max_val = root.val
        output = 1
        level = 1
        while(True):
            if k==1:
                for i in q1:
                    if i is not None:
                        q2.append(i.left)
                        q2.append(i.right)
                sum = 0
                flag = 0
                for i in q2:
                    if i is not None:
                        sum+=i.val
                        flag = 1
                if flag == 0:
                    break
                if sum>max_val:
                    max_val = sum
                    output = level + 1
                q1.clear()
                k = 0
            else:
                for i in q2:
                    if i is not None:
                        q1.append(i.left)
                        q1.append(i.right)
                sum = 0
                flag = 0
                for i in q1:
                    if i is not None:
                        sum+=i.val
                        flag = 1
                if flag == 0:
                    break
                if sum>max_val:
                    max_val = sum
                    output = level + 1
                q2.clear()
                k = 1
            level+=1
        return output






