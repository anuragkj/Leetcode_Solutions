class Solution:
    def bstToGst(self, root):
        node_sum = [0]  # Using a list to emulate a mutable integer reference
        self.bst_to_gst_helper(root, node_sum)
        return root

    def bst_to_gst_helper(self, root, node_sum):
        # If root is null, make no changes.
        if root is None:
            return

        self.bst_to_gst_helper(root.right, node_sum)
        node_sum[0] += root.val
        # Update the value of root.
        root.val = node_sum[0]
        self.bst_to_gst_helper(root.left, node_sum)
