class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        event = []       # store (time, load/unload, value)

        for start, end, value in events:
            event += [(start, 1, value)]
            event += [(end + 1, -1, value)]

        # sort based on the time increasingly
        event = sorted(event)

        res = 0            # the maximum aggregation we can build so far
        max_value = 0      # the maximum value seen so far 

        for time, load, value in event:
            # see a new job, update the aggregation to 
            if load == 1:
                res = max(res, max_value + value)
                
            # otherwise, only update max_val seen so far
            else:
                max_value = max(max_value, value)

        return res
