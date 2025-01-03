class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        low, high = intervals[0][0], intervals[0][1]
        l = 0
        res = []
        for r in range(len(intervals)):
            if intervals[r][0] <= high:
                low = min(low, intervals[r][0])
                high = max(intervals[r][1], high)
            else:
                res.append([low, high])
                low = intervals[r][0]
                high = intervals[r][1]
                l = r
        
        res.append([low, high])
        return res
            