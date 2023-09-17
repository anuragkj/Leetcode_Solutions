from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # Calculate the number of vertices in the graph.
        V = len(graph)
        
        # Initialize a deque for BFS, initially visiting all vertices one by one.
        curr_level = deque([(u, 1 << u) for u in range(V)])  # BFS Queue
        
        # Calculate a bitmask where all vertices are visited.
        all_visited = (1 << V) - 1  # Bitmask for when all vertices are visited
        
        # Initialize a 2D array to track visited nodes.
        visited = [[False for bit_mask in range(0, all_visited + 1)] for _ in range(V)]
        
        # Mark the initial states of the BFS by setting corresponding cells in the visited array to True.
        for u in range(V):
            visited[u][1 << u] = True
            
        # Initialize the shortest path length.
        path_length = 0
        
        # Start a BFS loop.
        while curr_level:
            n = len(curr_level)
            while n:
                # Dequeue the current node and its bitmask.
                u, bit_mask = curr_level.popleft()
                
                # Check if all nodes are visited in this BFS level.
                if bit_mask == all_visited:
                    return path_length 
                
                # Iterate through neighbors of the current node.
                for v in graph[u]:
                    # Calculate the bitmask after moving from u to v.
                    next_bit_mask = bit_mask | (1 << v)
                    
                    # If v with the next bitmask has already been visited, skip to the next neighbor.
                    if visited[v][next_bit_mask]:
                        continue 
                    
                    # If all nodes are visited with the next bitmask, return the shortest path length.
                    if next_bit_mask == all_visited: 
                        return path_length + 1
                    
                    # Enqueue the neighbor v with the next bitmask for further exploration.
                    curr_level.append((v, next_bit_mask))
                    
                    # Mark v as visited with the next bitmask.
                    visited[v][next_bit_mask] = True 
                
                n -= 1
            
            # Increment the path length for the next level of BFS.
            path_length += 1
        
        # If no valid path is found, return -1.
        return -1

