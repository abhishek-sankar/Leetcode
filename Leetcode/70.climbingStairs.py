class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        if n < 3:
            return max(n, 1)        
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            for j in range(1,3):
                dp[i] += dp[i - j]
        
        return dp[n]