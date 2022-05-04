# -----------------------------------------------------------------------------
#  Attempt: #1                start of solution
# -----------------------------------------------------------------------------

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastAddedEnd = output[-1][1]
            if start <= lastAddedEnd:
                output[-1][1] = max(end, lastAddedEnd)
            else:
                output.append([start,end])
        return output