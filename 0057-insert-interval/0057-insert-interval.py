class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [newInterval]
        
        # 1.Skip all intervals that come before the 'newInterval'
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            i += 1
        merged = intervals[:i]

        # 2.Merge all intervals that overlap with 'newInterval'
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        merged.append(newInterval)

        # 3.Add all the remaining intervals to the output
        merged.extend(intervals[i:])
        
        return merged
        