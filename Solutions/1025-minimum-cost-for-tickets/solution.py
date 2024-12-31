class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        travel_days_set = set(days)

        @cache
        def dp(i):
            if i <= 0:
                return 0

            if i not in travel_days_set:
                return dp(i - 1)

            return min(
                dp(i - 1) + costs[0],
                dp(i - 7) + costs[1],
                dp(i - 30) + costs[2]
            )

        return dp(last_day)
