class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        arrows = 1
        points.sort(key=lambda x: x[1])
        start, end = points[0]

        for left, right in points[1:]:
            if left > end:
                arrows += 1
                end = right

        return arrows


# class Solution:
#     def findMinArrowShots(self, points: List[List[int]]) -> int:
#         overlaps = 0
#         points.sort(key=lambda x: x[0])
#         start, end = points[0]
#         # check for just one balloon

#         for i in range(1, len(points)):
#             left, right = points[i]
#             if end >= left:
#                 start = max(start, left)
#                 end = min(end, right)
#                 overlaps += 1
#             else:
#                 start = left
#                 end = right

#         return len(points) - overlaps
