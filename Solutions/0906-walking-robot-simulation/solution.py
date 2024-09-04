class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        direction_index = 0
        
        max_distance_squared = 0
        
        for command in commands:
            if command == -2:
                direction_index = (direction_index - 1) % 4
            elif command == -1:
                direction_index = (direction_index + 1) % 4
            else:
                for _ in range(command):
                    next_x = x + directions[direction_index][0]
                    next_y = y + directions[direction_index][1]
                    if (next_x, next_y) in obstacle_set:
                        break
                    x, y = next_x, next_y
                    max_distance_squared = max(max_distance_squared, x * x + y * y)
        
        return max_distance_squared
