class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
        result = [["" for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                result[i][j] = box[j][i]
        for i in range(n):
            result[i].reverse()
        for j in range(m):
            lowest_row_with_empty_cell = n - 1
            for i in range(n - 1, -1, -1):
                if result[i][j] == "#":
                    result[i][j] = "."
                    result[lowest_row_with_empty_cell][j] = "#"
                    lowest_row_with_empty_cell -= 1
                if result[i][j] == "*":
                    lowest_row_with_empty_cell = i - 1

        return result
