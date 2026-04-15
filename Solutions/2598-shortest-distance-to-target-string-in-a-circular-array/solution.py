class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)

        left = startIndex
        right = startIndex
        steps = 0

        while steps <= n // 2:
            if words[left] == target or words[right] == target:
                return steps

            left = (left - 1 + n) % n
            right = (right + 1) % n
            steps += 1

            if left == right:
                if words[left] == target:
                    return steps
                break

        return -1
