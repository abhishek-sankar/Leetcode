class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        def dfs(r, c, reachable):
            reachable.add((r, c))

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c] and (nr, nc) not in reachable:
                    dfs(nr, nc, reachable)

        
        reachable_p = set()
        reachable_a = set()
        for i in range(m):
            dfs(i, 0, reachable_p)
        for j in range(n):
            dfs(0, j, reachable_p)

        for i in range(m):
            dfs(i, n-1, reachable_a)
        for j in range(n):
            dfs(m-1, j, reachable_a)

        res = list(reachable_a & reachable_p)

        return [(x, y) for x, y in res]