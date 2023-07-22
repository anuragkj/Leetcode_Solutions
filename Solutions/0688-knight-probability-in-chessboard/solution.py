# class Solution:
#     def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
#         queue1 = []
#         queue2 = []
#         queue1.append((row, column))
#         movements = [(1,2), (-1,2), (1,-2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]
#         valid = 0
#         for _k in range(k):
#             while(len(queue1) != 0):
#                 row, column = queue1.pop(0)
#                 for i, j in movements:
#                     if ((row + i) >= 0 and (row + i) <= (n-1)) and ((column + j) >= 0 and (column + j) <= (n-1)):
#                         queue2.append((row+i, column+j))
#             queue1 = queue2.copy()
#             queue2.clear()
         
#         return len(queue1)/8**k

class Solution:
  def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
    # Possible moves of knight in (row, col) directions
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    # Create a 2D memo table to store the probabilities for the current move and the previous move
    # We only need to keep track of the probabilities for the current and previous moves
    memo = [[0] * n for _ in range(n)]
    # Initialize the memo table for the first move with all probabilities set to 1
    for i in range(n):
        for j in range(n):
            memo[i][j] = 1
    
    # For each move from 1 to k
    for m in range(1, k+1):
        # Create a new 2D memo table to store the probabilities for the current move
        new_memo = [[0] * n for _ in range(n)]
        # For each cell on the board
        for i in range(n):
            for j in range(n):
                prob = 0
                # Iterate over all possible moves from the previous cell
                for move in moves:
                    new_i = i + move[0]
                    new_j = j + move[1]
                    # If the move is still on the board
                    if 0 <= new_i < n and 0 <= new_j < n:
                        prob += memo[new_i][new_j]
                # Update the probability of the current cell for current moves
                new_memo[i][j] = prob / 8
        # Set the memo table for the previous move to the memo table for the current move
        memo = new_memo
    
    # Return the probability of the starting cell for k moves
    return memo[row][column]
