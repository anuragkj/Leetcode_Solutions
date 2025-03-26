class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def isValidDivision(ranges):
            ranges.sort()

            cuts = 0
            current_max = ranges[0][1]

            for left, right in ranges:
                if current_max <= left:
                    cuts += 1
                current_max = max(current_max, right)

            return cuts >= 2

        horizontal_ranges = [[r[0], r[2]] for r in rectangles]
        vertical_ranges = [[r[1], r[3]] for r in rectangles]

        return isValidDivision(horizontal_ranges) or isValidDivision(vertical_ranges)
