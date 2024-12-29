class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def validSudoku(board):
            rows = [set() for _ in range(9)]
            cols = [set() for _ in range(9)]
            subs = [set() for _ in range(9)]

            for i in range(9):
                for j in range(9):

                    if board[i][j] != ".":
                        char = board[i][j]
