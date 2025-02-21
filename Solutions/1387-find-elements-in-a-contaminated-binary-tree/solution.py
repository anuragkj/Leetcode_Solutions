class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = set() # holds all correct values for tree

        def dfs(node, contam_node):
            if not contam_node:
                return # no corresponding node in contaminated tree
            self.nodes.add(node) # contam node exists, add correct value to nodes
            dfs(2 * node + 1, contam_node.left) # check left
            dfs(2 * node + 2, contam_node.right) # check right

        dfs(root.val + 1, root) # build tree after correcting root value
        

    def find(self, target: int) -> bool:
        return target in self.nodes # check if target is in tree
