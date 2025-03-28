class Solution:
	def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
		#It is a simple questions based on the concept of graph
		#As we all know we can represent a matrix/grid into a graph
		#Then we can use the heap(min Heap) to get a perfect path.
		#Then we are using maxYet(means max till that index).
		m = len(grid)
		n = len(grid[0])
		heap = [(grid[0][0], 0, 0)]
		v = {(0, 0)}
		order = []
		while len(heap) > 0:
			curr, i, j = heapq.heappop(heap)
			order.append(curr)
			for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
				if 0 <= x < m and 0 <= y < n and (x, y) not in v:
					v.add((x, y))
					heapq.heappush(heap, (grid[x][y], x, y))
		maxYet = -1
		for i in range(len(order)):
			maxYet = max(maxYet, order[i])
			order[i] = maxYet
		res = []
		for q in queries:
			res.append(bisect.bisect_left(order, q))
		return res
