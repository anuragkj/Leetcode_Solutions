from bisect import bisect_left, bisect_right
class MyCalendar:

    def __init__(self):
        self.bookings = []
        self.len_book = 0
        

    def book(self, startTime: int, endTime: int) -> bool:
        left_add = bisect_left(self.bookings, startTime, key = lambda x: x[0])
        right_add = bisect_right(self.bookings, endTime, key = lambda x: x[1])
        if left_add == right_add:
            if (left_add == 0 or self.bookings[left_add-1][1] <= startTime) and (right_add == self.len_book or self.bookings[right_add][0] >= endTime):
                self.bookings.insert(left_add, [startTime, endTime])
                self.len_book += 1
                return True
        return False
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
