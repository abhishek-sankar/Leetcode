class Solution:
    def totalNQueens(self, n: int) -> int:
        res = set()
        def checkPosition(board):
            rowId = len(board) - 1
            if rowId == 0:
                return True
            for i in range(len(board) - 1):
                diff = abs(board[rowId] - board[i])
                if diff == 0 or diff == rowId - i:
                    return False
            return True

        def backtrack(board):
            if len(board) == n:
                res.add(tuple(board))
            for i in range(n):
                board.append(i)
                if checkPosition(board):
                    backtrack(board)
                board.pop()
        backtrack([])
        return len(res)