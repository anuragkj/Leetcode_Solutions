class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        w1 = self._total_waviness_upto(num1 - 1)
        w2 = self._total_waviness_upto(num2)
        return w2 - w1

    def _total_waviness_upto(self, num: int) -> int:
        digits = [int(c) for c in str(num)]
        length = len(digits)

        # Returns: (total_waviness, total_count) from the current state.
        @lru_cache(None)
        def dfs(
            pos: int,
            p1: Optional[int],
            p2: Optional[int],
            tight: bool,
            has_started: bool,
        ) -> Tuple[int, int]:

            if pos == length:
                return 0, 1  # no more waviness, exactly 1 number formed

            max_d = digits[pos] if tight else 9
            total_waviness = 0
            total_count = 0

            for d in range(max_d + 1):
                next_tight = tight and (d == digits[pos])
                next_started = has_started or (d != 0)

                # Update last two real digits
                if not next_started:
                    nd1, nd2 = None, None
                elif not has_started:
                    nd1, nd2 = d, None
                else:
                    nd1, nd2 = d, p1

                sub_waviness, sub_count = dfs(
                    pos + 1, nd1, nd2, next_tight, next_started
                )

                # Always add downstream waviness
                total_waviness += sub_waviness
                total_count += sub_count

                # If we have enough digits to form a triple, check peak/valley
                if has_started and next_started and p1 is not None and p2 is not None:
                    if (p2 < p1 > d) or (p2 > p1 < d):
                        total_waviness += (
                            sub_count  # this peak/valley applies to all completions
                        )

            return total_waviness, total_count

        return dfs(0, None, None, True, False)[0]
