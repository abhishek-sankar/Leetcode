class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        if m == 0 or n == 0:
            return
        q = deque()
        for j in range(n):
            if board[0][j] == "O":
                q.append((0, j))
            if board[m - 1][j] == "O":
                q.append((m - 1, j))

        for i in range(m):
            if board[i][0] == "O":
                q.append((i, 0))
            if board[i][n - 1] == "O":
                q.append((i, n - 1))

        visited = set()

        def dfs(point):
            r, c = point
            if r < 0 or c < 0 or r >= m or c >= n or point in visited:
                return
            if board[r][c] == "O":
                visited.add(point)
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    dfs((r + dr, c + dc))

        while q:
            point = q.popleft()
            dfs(point)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if (i, j) not in visited:
                        board[i][j] = "X"
