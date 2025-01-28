class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            additional = grid[r][c]
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            grid[r][c] = -1 # setting this to visited
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                    additional += dfs(nr, nc)
            return additional
        
        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total = max(total, dfs(i, j))
        
        return total