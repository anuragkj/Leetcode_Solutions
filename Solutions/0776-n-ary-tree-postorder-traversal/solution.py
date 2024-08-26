"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: "Node") -> List[int]:
        result = []
        if not root:
            return result
        self._traverse_postorder(root, result)
        return result

    def _traverse_postorder(
        self, current_node: "Node", postorder_list: List[int]
    ) -> None:
        if not current_node:
            return
        for child_node in current_node.children:
            self._traverse_postorder(child_node, postorder_list)
        postorder_list.append(current_node.val)
