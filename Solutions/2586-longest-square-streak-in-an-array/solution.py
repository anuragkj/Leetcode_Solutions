class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        streak_lengths = {}

        nums.sort()

        for number in nums:
            root = int(number**0.5)
            if root * root == number and root in streak_lengths:
                streak_lengths[number] = streak_lengths[root] + 1
            else:
                streak_lengths[number] = 1

        longest_streak = max(streak_lengths.values(), default=0)

        return longest_streak if longest_streak > 1 else -1
