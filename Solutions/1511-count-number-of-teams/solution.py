class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0
        increasing_cache = [[-1] * 4 for _ in range(n)]
        decreasing_cache = [[-1] * 4 for _ in range(n)]

        # Calculate total teams by considering each soldier as a starting point
        for start_index in range(n):
            teams += self._count_increasing_teams(
                rating, start_index, 1, increasing_cache
            ) + self._count_decreasing_teams(
                rating, start_index, 1, decreasing_cache
            )

        return teams

    def _count_increasing_teams(
        self,
        rating: List[int],
        current_index: int,
        team_size: int,
        increasing_cache: List[List[int]],
    ) -> int:
        n = len(rating)

        # Base case: reached end of array
        if current_index == n:
            return 0

        # Base case: found a valid team of size 3
        if team_size == 3:
            return 1

        # Return cached result if available
        if increasing_cache[current_index][team_size] != -1:
            return increasing_cache[current_index][team_size]

        valid_teams = 0

        # Recursively count teams with increasing ratings
        for next_index in range(current_index + 1, n):
            if rating[next_index] > rating[current_index]:
                valid_teams += self._count_increasing_teams(
                    rating, next_index, team_size + 1, increasing_cache
                )

        # Cache and return the result
        increasing_cache[current_index][team_size] = valid_teams
        return valid_teams

    def _count_decreasing_teams(
        self,
        rating: List[int],
        current_index: int,
        team_size: int,
        decreasing_cache: List[List[int]],
    ) -> int:
        n = len(rating)

        # Base case: reached end of array
        if current_index == n:
            return 0

        # Base case: found a valid team of size 3
        if team_size == 3:
            return 1

        # Return cached result if available
        if decreasing_cache[current_index][team_size] != -1:
            return decreasing_cache[current_index][team_size]

        valid_teams = 0

        # Recursively count teams with decreasing ratings
        for next_index in range(current_index + 1, n):
            if rating[next_index] < rating[current_index]:
                valid_teams += self._count_decreasing_teams(
                    rating, next_index, team_size + 1, decreasing_cache
                )

        # Cache and return the result
        decreasing_cache[current_index][team_size] = valid_teams
        return valid_teams
