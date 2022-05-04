# -----------------------------------------------------------------------------
#  Attempt: #1                start of solution
# -----------------------------------------------------------------------------

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        counter = 0
        
        recentEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < recentEnd:
                counter += 1
                recentEnd = min(recentEnd, end)
            else:
                recentEnd = end
            
        return counter