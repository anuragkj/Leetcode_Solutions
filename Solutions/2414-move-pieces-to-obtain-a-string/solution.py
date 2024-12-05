class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Step 1: Remove underscores and check if the character sequence matches
        if start.replace('_', '') != target.replace('_', ''):
            return False

        n = len(start)
        i, j = 0, 0

        # Step 2: Use two pointers to check movement constraints
        while i < n and j < n:
            # Skip underscores in start
            while i < n and start[i] == '_':
                i += 1
            # Skip underscores in target
            while j < n and target[j] == '_':
                j += 1

            # If both pointers are out of bounds, we're done
            if i == n and j == n:
                return True
            # If one pointer is out of bounds but not the other, return False
            if i == n or j == n:
                return False

            # Check movement constraints for 'L' and 'R'
            if start[i] != target[j]:
                return False
            if start[i] == 'L' and i < j:  # 'L' cannot move to the right
                return False
            if start[i] == 'R' and i > j:  # 'R' cannot move to the left
                return False

            # Move both pointers
            i += 1
            j += 1

        return True
