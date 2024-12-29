class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subs = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    char = board[i][j]
                    subgrid = (i // 3) * 3 + (j // 3)
                    rows[i].add(char)
                    cols[j].add(char)
                    subs[subgrid].add(char)

        # if char in rows[i] or char in cols[j] or char in subs[subgrid]:
        #     return False
        # return True

        def backtrack(board, i, j):
            if i == 9:
                return True
            if j == 9:
                return backtrack(board, i + 1, 0)

            if board[i][j] != ".":
                return backtrack(board, i, j + 1)

            for k in range(1, 10):
                char = str(k)
                subgrid = (i // 3) * 3 + (j // 3)

                if char in rows[i] or char in cols[j] or char in subs[subgrid]:
                    continue

                board[i][j] = char
                rows[i].add(char)
                cols[j].add(char)
                subs[subgrid].add(char)

                if backtrack(board, i, j + 1):
                    return True

                rows[i].remove(char)
                cols[j].remove(char)
                subs[subgrid].remove(char)
                board[i][j] = "."

            return False

        backtrack(board, 0, 0)
