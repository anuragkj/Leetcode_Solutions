class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        block_queue = deque()
        num_whites = 0

        # Initiate queue with first k values
        for i in range(k):
            current_char = blocks[i]
            if current_char == "W":
                num_whites += 1
            block_queue.append(current_char)

        # Set initial minimum
        num_recolors = num_whites

        for i in range(k, len(blocks)):

            # Remove front element from queue and update current number of white blocks
            if block_queue.popleft() == "W":
                num_whites -= 1

            # Add current element to queue and update current number of white blocks
            current_char = blocks[i]
            if current_char == "W":
                num_whites += 1
            block_queue.append(current_char)

            # Update minimum
            num_recolors = min(num_recolors, num_whites)

        return num_recolors
