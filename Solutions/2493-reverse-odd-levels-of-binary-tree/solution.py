# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        if not root:
            return None  # Return None if the tree is empty.

        queue = [root]  # Start BFS with the root node.
        level = 0

        while queue:
            size = len(queue)
            current_level_nodes = []

            # Process all nodes at the current level.
            for _ in range(size):
                node = queue.pop(0)
                current_level_nodes.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse node values if the current level is odd.
            if level % 2 == 1:
                left, right = 0, len(current_level_nodes) - 1
                while left < right:
                    tmp = current_level_nodes[left].val
                    current_level_nodes[left].val = current_level_nodes[
                        right
                    ].val
                    current_level_nodes[right].val = tmp
                    left += 1
                    right -= 1

            level += 1

        return root  # Return the modified tree root.
