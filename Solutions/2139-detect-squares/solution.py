from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.squares = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.squares[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        result = 0
        px, py = point
        for (x, y), cnt in self.squares.items():
            if abs(py - y) == abs(px - x) and (py != y and px != x):
                result += cnt * self.squares.get((x, py), 0) * self.squares.get((px, y), 0)
        return result
