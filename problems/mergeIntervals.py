# 56
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda interval: interval.start)
        merged = list()
        merged.append(intervals[0])

        for interval in intervals[1:]:
            if merged[-1].end >= interval.start:
                merged[-1].end = max(merged[-1].end, interval.end)
            else:
                merged.append(interval)
        return merged
