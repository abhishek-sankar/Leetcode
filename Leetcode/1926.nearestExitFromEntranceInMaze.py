class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        q = deque()
        visited = set()
        entry = tuple(entrance)
        q.append((entry[0], entry[1], 0))
        visited.add(entry)
        while q:
            r, c, distance = q.popleft()
            if (r, c) != entry and (
                r == 0 or r == len(maze) - 1 or c == 0 or c == len(maze[0]) - 1
            ):
                return distance
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < len(maze)
                    and 0 <= nc < len(maze[0])
                    and maze[nr][nc] == "."
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    q.append((nr, nc, distance + 1))

        return -1
