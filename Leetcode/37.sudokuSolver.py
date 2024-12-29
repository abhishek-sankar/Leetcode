class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def validSudoku(board):
            rows = [set() for _ in range(9)]
            cols = [set() for _ in range(9)]
            subs = [set() for _ in range(9)]
