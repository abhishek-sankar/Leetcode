class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        pre = [0] * n
        suf = [0] * n
        pre[0] = grid[0][0]
        suf[n - 1] = grid[1][n - 1]
        for i in range(1, n):
            pre[i] = pre[i - 1] + grid[0][i]

        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] + grid[1][i]

        pivot = 0
        total = float("inf")
        for i in range(n):
            topRemaining = pre[-1] - pre[i]
            bottomRemaining = suf[0] - suf[i]

            secondRobotPoints = max(topRemaining, bottomRemaining)
            total = min(total, secondRobotPoints)

        return total
