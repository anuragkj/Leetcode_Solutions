class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        min_rank, max_rank = ranks[0], ranks[0]

        # Find min and max rank dynamically
        for rank in ranks:
            min_rank = min(min_rank, rank)
            max_rank = max(max_rank, rank)

        # Frequency list to count mechanics with each rank
        freq = [0] * (max_rank + 1)
        for rank in ranks:
            min_rank = min(min_rank, rank)
            freq[rank] += 1

        # Minimum possible time, Maximum possible time
        low = 1
        high = min_rank * cars * cars

        # Perform binary search to find the minimum time required
        while low < high:
            mid = (low + high) // 2
            cars_repaired = 0

            # Calculate the total number of cars that can be repaired in 'mid' time
            for rank in range(1, max_rank + 1):
                cars_repaired += freq[rank] * int(math.sqrt(mid // rank))

            # Adjust the search boundaries based on the number of cars repaired
            if cars_repaired >= cars:
                high = mid  # Try to find a smaller time
            else:
                low = mid + 1  # Need more time

        return low
