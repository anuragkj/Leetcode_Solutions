from functools import cache

class Solution:
    def rotatedDigits(self, n: int) -> int:
        unchanged_digits = [0, 1, 8]
        changed_digits = [2, 5, 6, 9]

        digits = [int(i) for i in str(n)]

        # TC: O(d), where d = number of digits in n
        # SC: O(d), for the memoized recursion stack and DP states
        @cache
        def dp(index: int, tight: bool, started: bool, changed: bool) -> int:
            if index == len(digits):
                return int(started and changed)

            total = 0

            # Skip this position, only allowed before the number has started.
            if not started:
                total += dp(index + 1, False, False, changed)

            if not tight:
                # Use an unchanged digit: 0, 1, or 8.
                # If the number has not started, exclude leading 0.
                unchanged_count = len(unchanged_digits) - int(not started)
                total += unchanged_count * dp(index + 1, False, True, changed)

                # Use a changed digit: 2, 5, 6, or 9.
                total += len(changed_digits) * dp(index + 1, False, True, True)

                return total

            limit = digits[index]

            for digit in unchanged_digits:
                if digit == 0 and not started:
                    continue
                if digit > limit:
                    break

                total += dp(
                    index + 1,
                    tight and digit == limit,
                    True,
                    changed
                )

            for digit in changed_digits:
                if digit > limit:
                    break

                total += dp(
                    index + 1,
                    tight and digit == limit,
                    True,
                    True
                )

            return total

        return dp(0, True, False, False)
