
class Solution:
    def kWeakestRows(self, matrix, k) -> list[int]:
        min_heap = []  # Min heap to store (soldier_count, row_index) pairs

        # Calculate the sum of soldiers for each row and store in the min heap
        for row in range(len(matrix)):
            soldier_count = sum(matrix[row])
            heapq.heappush(min_heap, (soldier_count, row))

        # Extract the k weakest row indices from the min heap
        weakest_rows = [heapq.heappop(min_heap)[1] for _ in range(k)]

        return weakest_rows
