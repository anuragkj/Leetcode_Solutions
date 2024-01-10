# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        tree_map: Dict[int, Set[int]] = {}
        self.convert(root, 0, tree_map)
        queue = deque([start])
        minute = 0
        visited = {start}

        while queue:
            level_size = len(queue)
            while level_size > 0:
                current = queue.popleft()
                for num in tree_map[current]:
                    if num not in visited:
                        visited.add(num)
                        queue.append(num)
                level_size -= 1
            minute += 1

        return minute - 1

    def convert(self, current: TreeNode, parent: int, tree_map: Dict[int, Set[int]]):
        if current is None:
            return
        if current.val not in tree_map:
            tree_map[current.val] = set()
        adjacent_list = tree_map[current.val]
        if parent != 0:
            adjacent_list.add(parent)
        if current.left:
            adjacent_list.add(current.left.val)
        if current.right:
            adjacent_list.add(current.right.val)
        self.convert(current.left, current.val, tree_map)
        self.convert(current.right, current.val, tree_map)
