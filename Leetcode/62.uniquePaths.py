class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]

        dp[m-1][n-1] = 1
        def dfs(r, c):
            if r < m and c < n and dp[r][c] != -1:
                return dp[r][c]
            if r == m-1 and c == n-1:
                return 1
            elif r > m - 1 or c > n - 1 or r < 0 or c < 0:
                return 0
            else:
                dp[r][c] = dfs(r+1, c) + dfs(r, c+1)
                return dp[r][c]
        return dfs(0, 0)