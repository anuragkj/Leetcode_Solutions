# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def _getlca(node, n1, n2):
            if node is None or node == n1 or node == n2:
                return node
            left = _getlca(node.left,n1,n2)
            right = _getlca(node.right,n1,n2)

            if left and right:
                return node
            return left or right

        def _getnode(node, value):
            if node is None or node.val == value:
                return node
            return _getnode(node.left, value) or _getnode(node.right, value)
        
        def _getdir(node, tonode):
            if node == tonode:
                return ''
            queue = deque()
            queue.append((node, ''))

            while queue:
                n, path = queue.popleft()
                if n == tonode:
                    return path
                if n.left:
                    queue.append((n.left, path+'L'))
                if n.right:
                    queue.append((n.right, path+'R'))
            
            return None           


        startnode = _getnode(root, startValue)
        endnode = _getnode(root, destValue)
        lca = _getlca(root, startnode, endnode)
        path_lca_to_start = _getdir(lca, startnode)
        path_lca_to_end = _getdir(lca, endnode)
        path_start_to_lca = 'U'*len(path_lca_to_start)
        return path_start_to_lca+path_lca_to_end


        
