class DSU:
    def __init__(self):
        self.king = {} # king = {location:location_of_king}
        self.size = {} # size[location] = size of territory under the king
    
    # initially, every islander is king
    # and territory size is 1
    def make_king(self, u):
        self.king[u] = u
        self.size[u] = 1
	
	# returns the king of a particular islander
    def find_king(self, u):
        if self.king[u] == u:
            return u
        self.king[u] = self.find_king(self.king[u]) # path compression, check references
        return self.king[u]
    
	# kings battle it out. first we find the rulers of lands u and v
    def unite_kings(self, u, v):
        u = self.find_king(u)
        v = self.find_king(v)
        
        if u == v: return
        if not self.size[u] > self.size[v]: u, v = v, u    
        # u gets the territory
        self.size[u] += self.size[v]
        self.king[v] = self.king[u] # v is now ruled by u

    
class Solution:
	# returns valid neighbours of graph with a particular value
	# if val is None, return both 0s and 1s containing neighbours
    def get_neighbours(self, u, val=None):
        r, c = u
        ans = []
        for dr, dc in zip([-1, 1, 0, 0], [0, 0, 1, -1]):
            nr, nc = r+dr, c+dc
            if 0 <= nr < self.n and 0 <= nc < self.n: # if in the valid range
                if val == 0 and self.grid[nr][nc] == 0: ans.append((nr, nc))
                if val == 1 and self.grid[nr][nc] == 1: ans.append((nr, nc))
                if val is None: ans.append((nr, nc))
        return ans

    def largestIsland(self, grid: List[List[int]]) -> int:
        dsu = DSU()
        self.grid = grid
        self.n = len(grid)
        
        for r in range(self.n):
            for c in range(self.n):
                if grid[r][c]:
                    dsu.make_king((r, c)) # each islander is made king initially
        
        for r in range(self.n):
            for c in range(self.n):
                if grid[r][c]:
                    for neighbour in self.get_neighbours((r, c), val=1):
                        dsu.unite_kings(neighbour, (r, c)) # the kings battle it out

        ans = -inf
        for r in range(self.n):
            for c in range(self.n):
                if not grid[r][c]:
				# finding the unique kings surrounding the current location
                    kings = list(set([dsu.find_king(neighbour) for neighbour in self.get_neighbours((r, c), val=1)]))
					# getting the sum of all of their sizes
					# +1 because the current cell is also becoming 1 from a 0
                    ans = max(ans, 1+sum([dsu.size[king] for king in kings]))

		# if no cell is accessed, all are 1s.
        if ans == -inf: ans = self.n*self.n
        return ans
