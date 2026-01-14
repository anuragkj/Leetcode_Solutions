from typing import List, Tuple


class SegmentTree:
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1
        self.covered_count = [0] * (4 * self.n)
        self.covered_width = [0] * (4 * self.n)

    def add(self, i: int, j: int, val: int):
        self._add(0, 0, self.n - 1, i, j, val)

    def get_covered_width(self) -> int:
        return self.covered_width[0]

    def _add(self, idx, lo, hi, i, j, val):
        if j <= self.xs[lo] or self.xs[hi + 1] <= i:
            return

        if i <= self.xs[lo] and self.xs[hi + 1] <= j:
            self.covered_count[idx] += val
        else:
            mid = (lo + hi) // 2
            self._add(2 * idx + 1, lo, mid, i, j, val)
            self._add(2 * idx + 2, mid + 1, hi, i, j, val)

        if self.covered_count[idx] > 0:
            self.covered_width[idx] = self.xs[hi + 1] - self.xs[lo]
        elif lo == hi:
            self.covered_width[idx] = 0
        else:
            self.covered_width[idx] = (
                self.covered_width[2 * idx + 1] +
                self.covered_width[2 * idx + 2]
            )


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = set()

        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs.add(x)
            xs.add(x + l)

        events.sort()
        xs = sorted(xs)

        half_area = self._get_area(events, xs) / 2

        tree = SegmentTree(xs)
        area = 0
        prev_y = 0

        for y, delta, xl, xr in events:
            width = tree.get_covered_width()
            area_gain = width * (y - prev_y)

            if area + area_gain >= half_area:
                return prev_y + (half_area - area) / width

            area += area_gain
            tree.add(xl, xr, delta)
            prev_y = y

    def _get_area(self, events, xs):
        tree = SegmentTree(xs)
        prev_y = 0
        total = 0

        for y, delta, xl, xr in events:
            total += tree.get_covered_width() * (y - prev_y)
            tree.add(xl, xr, delta)
            prev_y = y

        return total
