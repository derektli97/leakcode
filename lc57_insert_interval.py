# -----------------------------------------------------------------------------
#  Attempt: #1                start of solution
# -----------------------------------------------------------------------------

# for interval in intervals, check the 3 cases:

# 1. if the new interval’s end comes before current interval’s start
# 2. if the new interval’s start comes after the current interval’s end
# 3. if the new interval’s start comes before the current’s end or if the new interval’s end comes after the current’s start, then it will overlap.


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         sorting already done
        output = []
        
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                output.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                output.append(newInterval)
                return output + intervals[i:]
            else:
                tempMin = min(intervals[i][0], newInterval[0])
                tempMax = max(intervals[i][1], newInterval[1])
                newInterval = [tempMin, max(newInterval[1], intervals[i][1])]
        output.append(newInterval)
        return output
```