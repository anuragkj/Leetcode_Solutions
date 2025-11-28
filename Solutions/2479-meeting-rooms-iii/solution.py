class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x: x[0])
        current_meets = [] #(end_time, room_num)
        free_rooms = [i for i in range(n)]
        heapq.heapify(free_rooms)

        count = [0]*n

        for arrival, end in meetings:
            while current_meets and current_meets[0][0] <= arrival:
                _, freed_room = heapq.heappop(current_meets)
                heapq.heappush(free_rooms, freed_room)

            if free_rooms:
                available_room = heapq.heappop(free_rooms)
                heapq.heappush(current_meets,(end,available_room))
                count[available_room] += 1
            else:
                first_free_time, first_avail_room = heapq.heappop(current_meets)
                heapq.heappush(current_meets,(first_free_time + (end - arrival),first_avail_room))
                count[first_avail_room] += 1

        max_count = max(count)
        ret = count.index(max_count)
        return ret



        
