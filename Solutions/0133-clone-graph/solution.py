"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return node

        q = deque([node])
        cloned = {node.val:Node(node.val, [])}

        while(q):
            cur = q.popleft()
            cur_clone = cloned[cur.val]
            for ngbr in cur.neighbors:
                if ngbr.val not in cloned:
                    cloned[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                cur_clone.neighbors.append(cloned[ngbr.val])

        return cloned[node.val]

        
