# -----------------------------------------------------------------------------
#  Attempt: #1                start of solution                    By: Derek Li
# -----------------------------------------------------------------------------

from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        start_p, end_p = 0,0

        counter = 0
        result = 0

        while start_p < len(intervals):
            if start[start_p] < end[end_p]:
                counter += 1
                start_p +=1
            else:
                counter -= 1
                end_p += 1
            result = max(result, counter)

        return result