class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_set = [tuple(row) for row in grid]
        col_set = [
            tuple([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))
        ]
        count = 0
        for row in row_set:
            if row in col_set:
                count += col_set.count(row)

        # print(row_set, col_set)
        return count
