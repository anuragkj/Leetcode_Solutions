class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        R = L = _ = 0
        for m in moves:
            if m == "L":
                L += 1
            elif m == "R":
                R += 1
            else:
                _ += 1
        return _ + abs(L - R)
