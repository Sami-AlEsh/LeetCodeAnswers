class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        # sort the intervals on the start time
        intervals.sort(key = lambda x: x[0])

        mergedIntervals = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:  # overlapping intervals, adjust the 'end'
                end = max(interval[1], end)
            else:  # non-overlapping interval, add the previous internval and reset
                mergedIntervals.append([start, end])
                start = interval[0]
                end = interval[1]

        # add the last interval
        mergedIntervals.append([start, end])
        return mergedIntervals