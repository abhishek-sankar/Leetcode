class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_indices = [
            (r, c)
            for c in range(len(grid[0]))
            for r in range(len(grid))
            if grid[r][c] == 2
        ]
        gridInFinalState = all(
            [
                (grid[r][c] == 0 or grid[r][c] == 2)
                for c in range(len(grid[0]))
                for r in range(len(grid))
            ]
        )
        if gridInFinalState:
            return 0
        q = deque(rotten_indices)
        timestep = 0
        visited = set(rotten_indices)
        while q:
            count = len(q)
            timestep += 1
            for i in range(count):
                r, c = q.popleft()

                directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < len(grid)
                        and 0 <= nc < len(grid[0])
                        and grid[nr][nc] == 1
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))

        didAllOrangesRot = all(
            [
                (grid[r][c] == 0 or (r, c) in visited)
                for c in range(len(grid[0]))
                for r in range(len(grid))
            ]
        )

        return timestep - 1 if didAllOrangesRot else -1
