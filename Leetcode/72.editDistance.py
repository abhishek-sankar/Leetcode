class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for r in range(m + 1):
            dp[r][0] = r

        for c in range(n + 1):
            dp[0][c] = c

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1

        return dp[m][n]
