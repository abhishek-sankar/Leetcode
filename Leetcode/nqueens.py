def isPlacementValid(placements: list) -> bool:
    # Intuition - I just need to check if the last placement breaks things
    rowId = len(placements) - 1
    for i in range(len(placements) - 1):
        diff = abs(placements[i] - placements[rowId])
        if diff == 0 or diff == rowId - i:
            return False

    return True


def backtrackNQueens(n: int, placements: list, currentRow: int, res: list):
    if len(placements) == n:
        res.append(placements.copy())
    else:
        for i in range(n):
            # print(placements)
            placements.append(i)
            if isPlacementValid(placements=placements):
                backtrackNQueens(
                    n, placements=placements, currentRow=currentRow + 1, res=res
                )
            placements.pop()


res = []


def isRotation(board1, board2):
    """Check if board2 is a rotation of board1."""
    return any(board1 == board2[i:] + board2[:i] for i in range(len(board2)))


unique_boards = []
backtrackNQueens(8, [], 0, res)

# Filter out rotations
for board in res:
    if not any(isRotation(board, unique_board) for unique_board in unique_boards):
        unique_boards.append(board)
print(len(res))
print(len(unique_boards))
