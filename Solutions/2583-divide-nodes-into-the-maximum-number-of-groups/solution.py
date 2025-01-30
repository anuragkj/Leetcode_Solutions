class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for p1,p2 in edges:
            graph[p1].append(p2)
            graph[p2].append(p1)

        dist = [0] * (n+1)
        group_dict = {}
        group = 0
        MAX = 0

        for i in range(1,n+1):
            # group assignment
            if i not in group_dict:
                group = MAX +  1
                MAX = group
            else:
                group = group_dict[i]

            seen = set()
            seen.add(i)
            q = [i]
            level = 0

            # color used to check bipartite
            color = [0] * n
            color[i-1] = 1
            c_color = -1

            group_dict[i] = group

            while q:
                tmp = []
                for p in q:
                    for node in graph[p]:
                        if color[p-1] * color[node-1] > 0: # check if parent and child can be painted using differen color
                            return -1
                        if node not in seen:
                            seen.add(node)
                            tmp.append(node)

                            group_dict[node] = group # assign to connected component
                            color[node-1] = c_color # paint the node

                c_color *= -1 # alternate color
                level += 1
                q = tmp
            
            dist[group] = max(dist[group],level) # only corresponding group is updated
    
        return sum(dist)
            
            

                
