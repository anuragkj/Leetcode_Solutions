# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    # Create two lists to store the leaf values of each tree
    leaves1 = []
    leaves2 = []

    # Perform a depth-first search on each tree to get the leaf values
    self.dfs(root1, leaves1)
    self.dfs(root2, leaves2)

    # Compare the two lists of leaf values
    return leaves1 == leaves2

  def dfs(self, node: Optional[TreeNode], leaves: List[int]):
    # If the node is null, return
    if node is None:
      return

    # If the node is a leaf, add its value to the list of leaves
    if node.left is None and node.right is None:
      leaves.append(node.val)

    # Recursively traverse the left and right subtrees
    self.dfs(node.left, leaves)
    self.dfs(node.right, leaves)
