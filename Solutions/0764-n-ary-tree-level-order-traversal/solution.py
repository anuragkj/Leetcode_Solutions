"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        ret = []
        q = deque()
        q.append(root)
        while(q):
            app = []
            for i in range(len(q)):
                node = q.popleft()
                app.append(node.val)
                for nei in node.children:
                    q.append(nei)
            ret.append(app)
        return ret

        
