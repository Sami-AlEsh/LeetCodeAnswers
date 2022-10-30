class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        # sort the intervals on the start time
        intervals.sort(key = lambda x: x[0])

        mergedIntervals = []
        start = intervals[0][0]
        end = intervals[0][1]
        
        for interval in intervals[1:]:
            if end >= interval[0]:  # overlapping intervals
                end = max(end, interval[1])
            else:  # non-overlapping interval
                mergedIntervals.append([start, end])
                start, end = interval[0], interval[1]

        # add the last interval
        mergedIntervals.append([start, end])
        return mergedIntervals