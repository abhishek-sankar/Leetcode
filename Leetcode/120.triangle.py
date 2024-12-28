class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        count = len(triangle)
        if count == 1:
            return min(triangle[0])
        for i in range(len(triangle) - 2, -1, -1):
            count -= 1
            for j in range(count):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]
