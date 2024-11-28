class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        m, n = len(text1), len(text2)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        return dp[n][m]
                    
