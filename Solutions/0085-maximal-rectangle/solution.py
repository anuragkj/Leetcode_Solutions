class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                matrix[i][j] = int(matrix[i][j])

        for i in range(1, row):
            for j in range(col):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]

        def calculate(h):
            stack = []
            n = len(h)
            maxArea = 0
            for i in range(n):
                length = i
                while stack and stack[-1][0] > h[i]:
                    val, idx = stack.pop()
                    maxArea = max(maxArea, val * (i - idx))
                    length = idx
                stack.append((h[i], length))
            
            while stack:
                val, idx = stack.pop()
                maxArea = max(maxArea, val * (n - idx))

            return maxArea

        maxArea = 0
        for i in range(row):
            maxArea = max(maxArea, calculate(matrix[i]))

        return maxArea
