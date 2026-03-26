class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])
        totalSum = 0
        valToCount = collections.defaultdict(int)
        for idx in range(M):
            for jdx in range(N):
                val = grid[idx][jdx]
                totalSum += val
                valToCount[val] += 1
        
        # Sweep down
        topSum = 0
        bottomSum = totalSum
        topElements = collections.defaultdict(int)
        botElements = valToCount.copy()
        for idx in range(M-1):
            curRow = 0
            for jdx in range(N):
                val = grid[idx][jdx]
                curRow += val
                topElements[val] += 1
                botElements[val] -= 1
                if botElements[val] == 0:
                    del botElements[val]
        
            topSum += curRow
            bottomSum -= curRow
            if topSum == bottomSum:
                return True
            # Discount one
            elif topSum > bottomSum:
                diff = topSum - bottomSum
                if diff in topElements:
                    # Check to see if this top half is just the top row and whether we have an element to remove on the corners
                    if idx == 0:
                        if diff != grid[0][0] and diff != grid[0][N-1]:
                            continue
                    
                    if N == 1:
                        # Instead of checking top row corners, we can only remove from top and bottom of the top half
                        if diff != grid[0][0] and diff != grid[idx][0]:
                            continue

                    return True
            else:
                diff = bottomSum - topSum
                if diff in botElements:
                    # Check to see if this bottom is just the last row and whether we have an element to remove on the corners
                    if idx == M-2:
                        if diff != grid[M-1][0] and diff != grid[M-1][N-1]:
                            # Must remove a middle piece, which breaks continuity
                            continue

                    if N == 1:
                        # Instead of checking last row corners, we can only remove from top and bottom of the bottom half
                        if diff != grid[idx+1][0] and diff != grid[M-1][0]:
                            continue

                    return True
            

        # Sweep right
        leftSum = 0
        rightSum = totalSum
        leftElements = collections.defaultdict(int)
        rightElements = valToCount.copy()
        for jdx in range(N-1):
            curCol = 0
            for idx in range(M):
                val = grid[idx][jdx]
                curCol += val
                leftElements[val] += 1
                rightElements[val] -= 1
                if rightElements[val] == 0:
                    del rightElements[val]
                
            leftSum += curCol
            rightSum -= curCol
            if leftSum == rightSum:
                return True
            # Discount one
            elif leftSum > rightSum:
                diff = leftSum - rightSum
                if diff in leftElements:
                    # Check to see if this left half is just the leftmost row and whether we have an element to remove on the corners
                    if jdx == 0:
                        if diff != grid[0][0] and diff != grid[M-1][0]:
                            continue

                    if M == 1:
                        # Instead of checking left col corners, we can only remove from left or right end of the left half
                        if diff != grid[0][0] and diff != grid[0][jdx]:
                            continue

                    return True
            else:
                diff = rightSum - leftSum
                if diff in rightElements:
                    # Check to see if this right is just the last col and whether we have an element to remove on the corners
                    if jdx == N-2:
                        if diff != grid[0][N-1] and diff != grid[M-1][N-1]:
                            # Must remove a middle piece, which breaks continuity
                            continue
                    
                    if M == 1:
                        # Instead of checking last col corners, we can only remove from left or right end of the right half
                        if diff != grid[0][jdx+1] and diff != grid[0][N-1]:
                            continue

                    return True

        return False
