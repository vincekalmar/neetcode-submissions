class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        newStart = intervals[0][0]
        newEnd = intervals[0][1]

        res = []

        for interval in intervals:
            if newEnd < interval[0]:
                res.append([newStart, newEnd])
                newStart = interval[0]
                newEnd = interval[1]
            else:
                newStart = min(newStart, interval[0]) 
                newEnd = max(newEnd, interval[1])

        if not res or res[-1][1] != newEnd:
            res.append([newStart, newEnd])
        
        return res