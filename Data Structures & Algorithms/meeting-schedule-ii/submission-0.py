"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        minheap = []
        intervals.sort(key=lambda i : i.start)
        heapq.heapify(minheap)

        for interval in intervals:
            if minheap and interval.start >= minheap[0]:
                heapq.heappop(minheap)

            heapq.heappush(minheap, interval.end)

        return len(minheap)

        
        