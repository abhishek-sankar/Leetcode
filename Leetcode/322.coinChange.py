class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 1
        if amount == 0:
            return 0

        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for i in range(1, amount + 1):
            dp[i] = min([(dp[i - coin] + 1) for coin in coins if coin <= i] + [dp[i]])
        
        return dp[amount] if dp[amount] != float("inf") else -1