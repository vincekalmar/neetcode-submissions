"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda i: i.start)

        maxEnd = 0
        for interval in intervals:
            
            if interval.start < maxEnd:
                return False
            maxEnd = max(interval.end, maxEnd)

        return True