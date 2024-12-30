class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1
        MOD = 1000000007

        for i in range(high + 1):
            if i + zero < high + 1:
                dp[i + zero] = (dp[i + zero] + dp[i]) % MOD
            if i + one < high + 1:
                dp[i + one] = (dp[i + one] + dp[i]) % MOD

        return sum(dp[low : high + 1]) % MOD
