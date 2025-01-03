class Solution:
    def maximalSquare(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        cache = {}

        def checkSquare(i, j):
            if i >= m or j >= n:
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if board[i][j] == "0":
                cache[(i, j)] = 0
                return cache[(i, j)]
            else:
                cache[(i, j)] = 1 + min(
                    checkSquare(i + 1, j),
                    checkSquare(i, j + 1),
                    checkSquare(i + 1, j + 1),
                )
                return cache[(i, j)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == "1":
                    checkSquare(i, j)

        return max(cache.values()) * max(cache.values()) if len(cache) else 0
