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

        count, maxCount = 0, 0
        l, r = 0, 0

        while(l < len(start)):
            if start[l] < end[r]:
                l += 1
                count += 1
            else:
                r += 1
                count -= 1
            maxCount = max(count, maxCount)
        return maxCount
