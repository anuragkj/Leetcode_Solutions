class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dxz = abs(x - z)
        dyz = abs(y - z)
        if dxz < dyz:
            return 1
        elif dxz > dyz:
            return 2
        else:
            return 0
