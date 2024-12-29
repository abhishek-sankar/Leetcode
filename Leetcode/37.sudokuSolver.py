class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        counts = {x: [0] * 27 for x in range(1, 10)}
        print(counts)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if board[i][j] != ".":
                    counts[int(board[i][j])][int(i)] += 1
                    if counts[int(board[i][j])][int(i)] > 1:
                        return False

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    counts[board[i][j]][9 + i] += 1
                    if counts[board[i][j]][9 + i] > 1:
                        return False

                if board[j][i] != ".":
                    counts[board[j][i]][18 + i] += 1
                    if counts[board[j][i]][18 + i] > 1:
                        return False

        return True
