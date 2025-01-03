from collections import Counter

"""
[[".",".","4",".",".",".","6","3","."],
 [".",".",".",".",".",".",".",".","."],
 ["5",".",".",".",".",".",".","9","."],
 [".",".",".","5","6",".",".",".","."],
 ["4",".","3",".",".",".",".",".","1"],
 [".",".",".","7",".",".",".",".","."],
 [".",".",".","5",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."]]
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subgrids = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    char = board[i][j]
                    subgrid = (i // 3) * 3 + (j // 3)
                    if char in rows[i] or char in cols[j] or char in subgrids[subgrid]:
                        return False

                    rows[i].add(char)
                    cols[j].add(char)
                    subgrids[subgrid].add(char)

        return True


# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for i in range(9):
#             row_counter = Counter(board[i])
#             col_counter = Counter([row[i] for row in board])
#             del row_counter["."]
#             del col_counter["."]
#             if row_counter.keys() and max(row_counter.values()) > 1:
#                 return False
#             # print(col_counter.values())
#             if col_counter.keys() and max(col_counter.values()) > 1:
#                 return False

#         for i in range(0, 9, 3):
#             for j in range(0, 9, 3):
#                 _board = [row[j:j+3] for row in board[i:i+3]]
#                 _board_counts = Counter(_board[0] + _board[1] + _board[2])
#                 del _board_counts["."]
#                 if _board_counts.keys() and max(_board_counts.values()) > 1:
#                     return False

#         return True
