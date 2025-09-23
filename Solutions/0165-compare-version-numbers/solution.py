class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        index1, index2 = 0, 0
        length1, length2 = len(version1), len(version2)

        while index1 < length1 or index2 < length2:
            number1 = 0
            while index1 < length1 and version1[index1] != '.':
                number1 = number1 * 10 + int(version1[index1])
                index1 += 1
            index1 += 1  

            number2 = 0
            while index2 < length2 and version2[index2] != '.':
                number2 = number2 * 10 + int(version2[index2])
                index2 += 1
            index2 += 1  

            if number1 > number2:
                return 1
            elif number1 < number2:
                return -1

        return 0
