class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def insert_in_tree(node, val):
            if not node:
                return TreeNode(val)
            else:
                node.size += 1
                if val < node.val:
                    node.left = insert_in_tree(node.left, val)
                else:
                    node.right = insert_in_tree(node.right, val)
                return node
        
        tree = None
        for num in nums:
            tree = insert_in_tree(tree, num)

        def interleave_count(l, r):
            ls, rs = l.size if l else 0, r.size if r else 0
            return comb(ls + rs, ls)

        def num_of_ways(node):
            if node is None:
                return 1
            return num_of_ways(node.left) * num_of_ways(node.right) * \
                interleave_count(node.left, node.right) % 1000000007
        
        return num_of_ways(tree) - 1
