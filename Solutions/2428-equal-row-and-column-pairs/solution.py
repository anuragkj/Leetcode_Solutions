class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        output = 0
        transpose = []
        for i in range(len(grid)):
            list = []
            for j in range(len(grid[0])):
                list.append(grid[j][i])
            transpose.append(list)
        for i in grid:
            for j in transpose:
                if i == j:
                    output+=1
        return output
