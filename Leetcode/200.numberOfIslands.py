class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            grid[r][c] = "-1"
            for dr, dc in directions:
                nr, nc = min(max(0, r + dr), m - 1) , min(max(c + dc, 0), n - 1)
                if grid[nr][nc] == "1":
                    dfs(nr, nc)
        count = 0
        for r in range(m):
            # print("test")
            for c in range(n):
                # print("world")
                if grid[r][c] == "1":
                    # print("hello")
                    count +=1
                    dfs(r, c)
        return count