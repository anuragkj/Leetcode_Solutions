class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_minutes = 0  # Total minutes needed for garbage collection
        current_travel_time = 0  # Current travel time

        # Add the initial minutes required to collect garbage at the first house
        total_minutes += len(garbage[0])

        last_garbage_indices = [-1, -1, -1]  # Keep track of the last occurrence of each type of garbage

        # Iterate through each house starting from the second house
        for house_index in range(1, len(garbage)):
            # Add the minutes required to collect garbage at the current house
            total_minutes += len(garbage[house_index])

            # Update the indices of the last occurrence of each type of garbage
            if "M" in garbage[house_index]:
                last_garbage_indices[0] = house_index - 1
            if "P" in garbage[house_index]:
                last_garbage_indices[1] = house_index - 1
            if "G" in garbage[house_index]:
                last_garbage_indices[2] = house_index - 1

        # Iterate through each travel segment
        for travel_index in range(len(travel)):
            # Add the current travel time
            current_travel_time += travel[travel_index]

            # Add the minutes required to collect garbage if a garbage truck is at the corresponding house
            for truck_index in range(3):
                if last_garbage_indices[truck_index] == travel_index:
                    total_minutes += current_travel_time

        return total_minutes
