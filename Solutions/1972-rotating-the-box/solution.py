class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        result = [["" for _ in range(m)] for _ in range(n)]

        # Create the transpose of the input grid in `result`
        for i in range(n):
            for j in range(m):
                result[i][j] = box[j][i]

        # Reverse each row in the transpose grid to complete the 90° rotation
        for i in range(n):
            result[i].reverse()

        # Apply gravity to let stones fall to the lowest possible empty cell in each column
        for j in range(m):
            lowest_row_with_empty_cell = n - 1
            # Process each cell in column `j` from bottom to top
            for i in range(n - 1, -1, -1):
                # Found a stone - let it fall to the lowest empty cell
                if result[i][j] == "#":
                    result[i][j] = "."
                    result[lowest_row_with_empty_cell][j] = "#"
                    lowest_row_with_empty_cell -= 1
                # Found an obstacle - reset `lowest_row_with_empty_cell` to the row directly above it
                if result[i][j] == "*":
                    lowest_row_with_empty_cell = i - 1

        return result
