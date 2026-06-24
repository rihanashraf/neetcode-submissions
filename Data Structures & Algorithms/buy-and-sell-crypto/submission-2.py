class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_value = float("INF")
        max_profit = 0
        for i in range(len(prices)):
            curr = prices[i]
            if curr <min_value:
                min_value = curr
            profit = curr - min_value
            if profit >max_profit:
                max_profit = profit
        return max_profit


        