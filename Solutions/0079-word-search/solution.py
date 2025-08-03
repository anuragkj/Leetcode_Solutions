class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i, j, word_so_far, visited):
            if (i, j) in visited:
                return False
            if not (0 <= i < rows and 0 <= j < cols):
                return False
            if board[i][j] != word[len(word_so_far)]:
                return False

            word_so_far += board[i][j]
            if word_so_far == word:
                return True

            visited.add((i, j))
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dir_x, dir_y in dirs:
                new_i, new_j = i + dir_x, j + dir_y
                if dfs(new_i, new_j, word_so_far, visited):
                    return True
            visited.remove((i, j))  # backtrack

            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # start DFS only from matching first char
                    if dfs(i, j, "", set()):
                        return True
        return False

