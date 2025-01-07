class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, profit = -prices[0], 0

        for i in range(1, len(prices)):
            cash = max(cash, profit - prices[i])
            profit = max(profit, cash + prices[i] - fee)

        return profit
