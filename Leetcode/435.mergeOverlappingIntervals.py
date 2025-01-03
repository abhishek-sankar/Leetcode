class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        count = 0
        low, high = intervals[0][0], intervals[0][1]
        l = 0
        print(intervals)
        for r in range(1, len(intervals)):
            if high > intervals[r][0]:
                count += 1
                high = min(high, intervals[r][1])
            else:
                high = max(high, intervals[r][1])
        return count